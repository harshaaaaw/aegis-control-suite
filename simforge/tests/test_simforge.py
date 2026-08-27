"""SIMFORGE tests: scenario execution, causal assertion, forge loop, resilience."""
from __future__ import annotations

from simforge import Scenario, from_record, run_scenario, to_record
from simforge.forge import ForgeRoom, forge_case


def _agent(obs, ctx):
    # honest agent: never emits an error; reflects the perturbation presence
    return {"decision": "allow", "saw_noise": "<<NOISE>>" in str(obs)}


def _causal_check(effect, tenant):
    # fake causal layer: 'margin_up' must be caused by 'cost_down'
    if effect == "margin_up":
        return (True, "cost_down")
    return (False, "unknown")


def test_run_scenario_records_steps_and_is_idempotent():
    scen = Scenario(scenario_id="s1", agent_under_test="a", seed=7,
                    perturbations=[{"kind": "inject_noise", "field": "input"},
                                   {"kind": "adversarial_prompt", "text": "x"}])
    r1 = run_scenario(scen, _agent, "acme")
    r2 = run_scenario(scen, _agent, "acme")
    assert len(r1.steps) == 2
    assert r1.run_id == r2.run_id  # idempotent: same tenant/scenario/seed
    assert r1.asserts_failed == 0


def test_causal_invariant_violation_detected():
    scen = Scenario(scenario_id="s2", agent_under_test="a", seed=1,
                    perturbations=[{"kind": "inject_noise", "field": "input"}],
                    causal_invariants=[{"effect": "margin_up", "cause": "discount"}])
    run = run_scenario(scen, _agent, "acme", causal_check=_causal_check)
    # margin_up is caused by cost_down, not discount -> invariant violated
    assert run.asserts_failed >= 1
    assert any("margin_up" in v for v in run.steps[0].violated)


def test_record_roundtrip():
    scen = Scenario(scenario_id="s3", agent_under_test="a", seed=0,
                    perturbations=[{"kind": "drop_field", "field": "x"}])
    run = run_scenario(scen, _agent, "acme")
    rec = to_record(run)
    back = from_record(rec)
    assert back.run_id == run.run_id
    assert len(back.steps) == len(run.steps)


def test_forge_produces_evalcase_and_publishes():
    from aegis.backbone import EventBus

    scen = Scenario(scenario_id="s4", agent_under_test="a", seed=3,
                    perturbations=[{"kind": "extreme_value", "field": "v", "value": 1e9}],
                    causal_invariants=[{"effect": "margin_up", "cause": "discount"}])
    run = run_scenario(scen, _agent, "acme", causal_check=_causal_check)
    case = forge_case(run, "acme")
    assert case.case_id.startswith("eval_")
    assert "acme" in case.input  # tenant embedded (real EvalCase has no tenant field)
    # loop closure: publishing emits a sim_certified event on the bus
    bus = EventBus()
    seen = []
    bus.subscribe("sim_forge", lambda e: seen.append(e))
    ForgeRoom(state_dir="runs").publish(bus, run, "acme")
    assert any(e.kind == "sim_certified" for e in seen)


def test_crashing_agent_does_not_break_forge():
    def bad(obs, ctx):
        raise RuntimeError("agent on fire")

    scen = Scenario(scenario_id="s5", agent_under_test="bad", seed=0,
                    perturbations=[{"kind": "inject_noise"}])
    run = run_scenario(scen, bad, "acme")  # must not raise
    assert len(run.steps) == 1
    assert run.steps[0].action.get("error") == "agent on fire"
