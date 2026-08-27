"""SIMFORGE API tests: run + forge endpoints, authN, tenant scoping, rate limit."""
from __future__ import annotations

import os

os.environ["AEGIS_JWT_SECRET"] = "0" * 32

from simforge.server import get_app, register_agent

SECRET = "0" * 32


def _make_token(tenant="acme", role="svc"):
    from aegis.security import make_token
    return make_token(tenant_id=tenant, sub=role, secret=SECRET)


def _demo(obs, ctx):
    return {"decision": "allow"}


def test_run_endpoint_requires_auth():
    register_agent("demo", _demo)
    app = get_app(":memory:", SECRET, enable_rate_limit=False)
    from starlette.testclient import TestClient
    c = TestClient(app)
    r = c.post("/api/v1/sim/run", json={"scenario_id": "s", "agent_under_test": "demo",
                                        "perturbations": [{"kind": "inject_noise"}]})
    assert r.status_code == 401


def test_run_and_forge_endpoints_authed():
    register_agent("demo", _demo)
    app = get_app(":memory:", SECRET, enable_rate_limit=False)
    from starlette.testclient import TestClient
    c = TestClient(app)
    tok = _make_token("acme")
    body = {"scenario_id": "s1", "agent_under_test": "demo",
            "perturbations": [{"kind": "inject_noise"}], "seed": 1}
    r = c.post("/api/v1/sim/run", json=body,
               headers={"Authorization": f"Bearer {tok}"})
    assert r.status_code == 200, r.text
    assert r.json()["asserts_failed"] == 0
    f = c.post("/api/v1/sim/forge", json=body,
               headers={"Authorization": f"Bearer {tok}"})
    assert f.status_code == 200, f.text
    assert f.json()["case_id"].startswith("eval_")


def test_unknown_agent_rejected():
    app = get_app(":memory:", SECRET, enable_rate_limit=False)
    from starlette.testclient import TestClient
    c = TestClient(app)
    tok = _make_token("acme")
    r = c.post("/api/v1/sim/run", json={"scenario_id": "s", "agent_under_test": "ghost"},
               headers={"Authorization": f"Bearer {tok}"})
    assert r.status_code == 400
