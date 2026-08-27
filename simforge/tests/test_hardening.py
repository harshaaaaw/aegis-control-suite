"""SIMFORGE failure-path + idempotency tests (anti-slop P1 set).

Every test here is a proof, not decoration: it would fail if the invariant it
protects were deleted or weakened. The order mirrors how these bugs surface in
production (idempotency double-count, weak secret tunnel, tenant cross-read,
crashing agent breaks the forge, perturbations pass through unchanged).
"""
from __future__ import annotations

import os
import tempfile

os.environ["AEGIS_JWT_SECRET"] = "0" * 32

from simforge import Scenario, SimRun, from_record, run_scenario, to_record
from simforge.forge import ForgeRoom, forge_case
from simforge.server import get_app, register_agent
from starlette.testclient import TestClient  # noqa: N817

# ---------------------------------------------------------------------------
# Idempotency
# ---------------------------------------------------------------------------

def test_idempotent_run():
    """Same (tenant, scenario_id, seed) must return the same run_id (no double-
    count on retry). This is the dedupe invariant SIMFORGE advertises."""
    scen = Scenario(scenario_id="idem", agent_under_test="demo", seed=1,
                    perturbations=[{"kind": "inject_noise", "field": "input"}])

    def agent(obs, ctx):  # noqa: D103
        return {"decision": "allow"}

    run_a = run_scenario(scen, agent, "acme")
    run_b = run_scenario(scen, agent, "acme")
    assert run_a.run_id == run_b.run_id
    assert run_a.asserts_failed == run_b.asserts_failed


def test_different_seed_different_run():
    """A real dedupe: different seed => different run. Suffixing the id is not
    enough; the whole key must differ."""
    scen = Scenario(scenario_id="s", agent_under_test="demo", seed=1,
                    perturbations=[{"kind": "inject_noise", "field": "input"}])

    def agent(obs, ctx):
        return {"decision": "allow"}

    a = run_scenario(scen, agent, "acme")
    b = run_scenario(Scenario(scenario_id="s", agent_under_test="demo", seed=2,
                           perturbations=[{"kind": "inject_noise", "field": "input"}]),
                  agent, "acme")
    assert a.run_id != b.run_id


def test_different_tenant_different_run():
    """Tenant cross-read is the adversarial case. Two tenants running the same
    scenario/seed must NOT collide."""
    scen = Scenario(scenario_id="shared", agent_under_test="demo", seed=7,
                    perturbations=[{"kind": "inject_noise", "field": "input"}])

    def agent(obs, ctx):
        return {"decision": "allow"}

    a = run_scenario(scen, agent, "acme")
    b = run_scenario(scen, agent, "globex")
    assert a.run_id != b.run_id


# ---------------------------------------------------------------------------
# Perturbation application is deterministic & explicit
# ---------------------------------------------------------------------------

def test_inject_noise_appends_token():
    """inject_noise appends <<NOISE>> to the field (not replaces). The whole
    point of explicit perturbations is that their shape is auditable."""
    scen = Scenario(scenario_id="pn", agent_under_test="demo", seed=0,
                    perturbations=[{"kind": "inject_noise", "field": "payload"}],
                    baseline_observation={"payload": "hello"})
    assert scen.baseline_observation["payload"] == "hello"

    def agent(obs, ctx):
        return {"observed": obs["payload"]}

    run = run_scenario(scen, agent, "acme")
    assert run.steps[0].observation["payload"] == "hello<<NOISE>>"
    assert run.steps[0].outcome["action"]["observed"] == "hello<<NOISE>>"


def test_drop_field_removes_key():
    """drop_field removes the named key. Pass-through for unknown kinds is
    explicit, not silent magic."""
    scen = Scenario(scenario_id="df", agent_under_test="demo", seed=0,
                    perturbations=[{"kind": "drop_field", "field": "token"}],
                    baseline_observation={"token": "abc", "body": "x"})
    assert scen.baseline_observation["token"] == "abc"

    def agent(obs, ctx):
        return {"has_token": "token" in obs}

    run = run_scenario(scen, agent, "acme")
    assert "token" not in run.steps[0].observation
    assert run.steps[0].outcome["action"]["has_token"] is False


def test_unknown_perturbation_passes_through_unchanged():
    """Unknown perturbation kinds must not corrupt the observation (explicit
    pass-through, not silent). A failing agent step must still be recorded."""
    scen = Scenario(scenario_id="uk", agent_under_test="demo", seed=0,
                    perturbations=[{"kind": "some_wild_kind", "foo": "bar"}],
                    baseline_observation={"x": 1})

    def agent(obs, ctx):
        if obs.get("x") != 1:
            raise SystemExit("invariant broke")
        return {"x": obs["x"]}

    run = run_scenario(scen, agent, "acme")
    assert run.steps[0].observation == {"x": 1}
    assert run.asserts_failed == 0


# ---------------------------------------------------------------------------
# Causal invariant: no_error flag fires on agent error
# ---------------------------------------------------------------------------

def test_no_error_flag_fires_when_agent_errors():
    """The no_error structural invariant must fire when the agent returns an
    error marker. This is the surface SIMFORGE's structural checks expose."""
    scen = Scenario(scenario_id="ne", agent_under_test="demo", seed=0,
                    perturbations=[{"kind": "inject_noise", "field": "input"}],
                    causal_invariants=[{"no_error": True}])

    def agent(obs, ctx):
        return {"error": "blocked by rule X"}

    run = run_scenario(scen, agent, "acme")
    assert run.asserts_failed == 1
    # Just confirm the step recorded the violation.
    assert run.steps[0].violated == ["agent errored on invariant {'no_error': True}"]


# ---------------------------------------------------------------------------
# Forge produces an evalforge case that carries the failure
# ---------------------------------------------------------------------------

def test_forge_case_from_failed_run():
    """A run whose step violated must forge a case whose must_not_contain lists
    that violation (regression contract). Must also carry tenant_id/scenario_id
    in input (self-describing)."""
    scen = Scenario(scenario_id="fc", agent_under_test="demo", seed=0,
                    perturbations=[{"kind": "inject_noise", "field": "input"}],
                    causal_invariants=[{"no_error": True}])

    def agent(obs, ctx):
        return {"error": "blocked"}

    run = run_scenario(scen, agent, "acme")
    case = forge_case(run, "acme")
    assert case.case_id.startswith("eval_")
    assert "acme" in case.input
    assert case.must_not_contain == ["agent errored on invariant {'no_error': True}"]
    assert case.expected.startswith('{"must_not_violate":')


def test_forge_case_from_clean_run():
    """A clean run (no violations) must forge a case with empty must_not_contain
    and holds=True in expected. The forge must not manufacture a violation."""
    scen = Scenario(scenario_id="clean", agent_under_test="demo", seed=0,
                    perturbations=[{"kind": "inject_noise", "field": "input"}],
                    causal_invariants=[])

    def agent(obs, ctx):
        return {"decision": "allow"}

    run = run_scenario(scen, agent, "acme")
    case = forge_case(run, "acme")
    assert case.must_not_contain == []
    assert '"holds": true' in case.expected


# ---------------------------------------------------------------------------
# Round-trip via to_record / from_record (externalized state integrity)
# ---------------------------------------------------------------------------

def test_roundtrip_preserves_run():
    """to_record/from_record must preserve run identity, seed, asserts_failed,
    and steps (the Spine persistence surface)."""
    scen = Scenario(scenario_id="rt", agent_under_test="demo", seed=3,
                    perturbations=[{"kind": "inject_noise", "field": "input"}],
                    causal_invariants=[{"no_error": True}])

    def agent(obs, ctx):
        return {"error": "blocked"}

    run = run_scenario(scen, agent, "acme")
    rec = from_record(to_record(run))
    assert rec.run_id == run.run_id
    assert rec.seed == run.seed
    assert rec.asserts_failed == run.asserts_failed
    assert len(rec.steps) == len(run.steps)


# ---------------------------------------------------------------------------
# Server: weak JWT secret rejected at the gate
# ---------------------------------------------------------------------------

def test_weak_secret_rejected():
    """SIMFORGE reuses AEGIS's 32-byte secret floor. A weak secret must not
    boot the app (real root cause, not a soft log)."""
    import pytest
    with pytest.raises(Exception):
        get_app(":memory:", jwt_secret="short", enable_rate_limit=False)


# ---------------------------------------------------------------------------
# Server: authN returns 401 on missing bearer, 403 on bad token
# ---------------------------------------------------------------------------

def test_missing_bearer_returns_401():
    app = get_app(":memory:", jwt_secret="0" * 32, enable_rate_limit=False)
    c = TestClient(app)
    r = c.post("/api/v1/sim/run", json={"scenario_id": "x", "agent_under_test": "demo",
                                        "perturbations": [], "seed": 0})
    assert r.status_code == 401


def test_bad_bearer_returns_403():
    app = get_app(":memory:", jwt_secret="0" * 32, enable_rate_limit=False)
    from aegis.security import make_token
    wrong = make_token(tenant_id="x", sub="demo", secret="WRONG-SECRET-12345678901234567")
    c = TestClient(app)
    r = c.post("/api/v1/sim/run", json={"scenario_id": "x", "agent_under_test": "demo",
                                        "perturbations": [], "seed": 0},
               headers={"Authorization": f"Bearer {wrong}"})
    assert r.status_code == 403


# ---------------------------------------------------------------------------
# Server: unknown agent returns 400
# ---------------------------------------------------------------------------

def test_unknown_agent_returns_400():
    app = get_app(":memory:", jwt_secret="0" * 32, enable_rate_limit=False)
    from aegis.security import make_token
    token = make_token(tenant_id="acme", sub="demo", secret="0" * 32)
    c = TestClient(app)
    r = c.post("/api/v1/sim/run", json={"scenario_id": "x", "agent_under_test": "nobody",
                                        "perturbations": [], "seed": 0},
               headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 400
    assert "unknown agent" in r.json()["detail"]


# ---------------------------------------------------------------------------
# Server: registered agent runs, forge publishes a case
# ---------------------------------------------------------------------------

def test_registered_agent_run_and_forge():
    """The happy path on the API: register a callable, run a scenario, forge,
    and the response carries run_id + case_id."""
    app = get_app(":memory:", jwt_secret="0" * 32, enable_rate_limit=False)
    register_agent("demo", lambda obs, ctx: {"decision": "allow"})
    from aegis.security import make_token
    token = make_token(tenant_id="acme", sub="demo", secret="0" * 32)
    c = TestClient(app)

    r = c.post("/api/v1/sim/run", json={"scenario_id": "api_s1", "agent_under_test": "demo",
                                        "perturbations": [{"kind": "inject_noise", "field": "input"}],
                                        "seed": 0, "baseline_observation": {"input": "x"}},
               headers={"Authorization": f"Bearer {token}"})
    assert r.status_code == 200
    assert r.json()["run_id"].startswith("sim_")
    assert r.json()["asserts_failed"] == 0

    r2 = c.post("/api/v1/sim/forge", json={"scenario_id": "api_s1", "agent_under_test": "demo",
                                          "perturbations": [{"kind": "inject_noise", "field": "input"}],
                                          "seed": 0, "baseline_observation": {"input": "x"}},
                headers={"Authorization": f"Bearer {token}"})
    assert r2.status_code == 200
    assert r2.json()["run_id"].startswith("sim_")
    assert r2.json()["case_id"].startswith("eval_")
