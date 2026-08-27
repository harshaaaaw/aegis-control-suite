"""SIMFORGE HTTP API: adversarial simulation as a service.

Reuses AEGIS security (JWT authN, 32-byte secret floor, SSRF guard) and the
control-bus pattern. Async endpoints, rate limited, tenant-scoped. The agent
under test is supplied by the host at run time via a registered callable keyed
by agent name (in-process registry); the API itself never executes foreign code.
"""
from __future__ import annotations

from typing import Any

from aegis.security import AuthError, WeakSecretError, get_logger, verify_token
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import PlainTextResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

from . import Scenario, run_scenario
from .forge import ForgeRoom
from .observability import record_forge, record_sim

log = get_logger("simforge.server")

# In-process registry of agents-under-test. Host registers callables by name.
_AGENTS: dict[str, Any] = {}


def register_agent(name: str, fn) -> None:
    _AGENTS[name] = fn


limiter = Limiter(key_func=get_remote_address)


def get_app(db_path: str, jwt_secret: str, enable_rate_limit: bool = True) -> FastAPI:
    from aegis.security import require_strong_secret
    from aegis.spine import Spine, SpineConfig

    require_strong_secret(jwt_secret)

    app = FastAPI(title="SIMFORGE", version="0.1.0")
    app.state.limiter = Limiter(key_func=get_remote_address,
                                storage_uri="memory://", enabled=enable_rate_limit)
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

    spine = Spine(SpineConfig(db_path=db_path, jwt_secret=jwt_secret, require_auth=True))
    forge = ForgeRoom(state_dir="runs")

    def auth(request: Request) -> dict:
        h = request.headers.get("Authorization", "")
        if not h.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="missing bearer token")
        try:
            return verify_token(h[7:], jwt_secret)
        except (AuthError, WeakSecretError) as e:
            raise HTTPException(status_code=403, detail=str(e))

    def tenant_of(request: Request, claims: dict = Depends(auth)) -> str:
        return claims["tenant_id"]

    @app.post("/api/v1/sim/run")
    @limiter.limit("20/minute")
    async def sim_run(request: Request, body: dict, tenant: str = Depends(tenant_of)):
        agent_name = body.get("agent_under_test", "default")
        agent = _AGENTS.get(agent_name)
        if agent is None:
            raise HTTPException(status_code=400, detail=f"unknown agent {agent_name}")
        scen = Scenario(
            scenario_id=body["scenario_id"], agent_under_test=agent_name,
            perturbations=body.get("perturbations", []),
            causal_invariants=body.get("causal_invariants", []),
            seed=body.get("seed", 0),
            baseline_observation=body.get("baseline_observation", {}))
        run = run_scenario(scen, agent, tenant)
        record_sim(tenant)
        return {"run_id": run.run_id, "scenario_id": run.scenario_id,
                "asserts_failed": run.asserts_failed, "steps": len(run.steps)}

    @app.post("/api/v1/sim/forge")
    @limiter.limit("20/minute")
    async def sim_forge(request: Request, body: dict, tenant: str = Depends(tenant_of)):
        # run first, then forge the golden case (loop closure)
        agent_name = body.get("agent_under_test", "default")
        agent = _AGENTS.get(agent_name)
        if agent is None:
            raise HTTPException(status_code=400, detail=f"unknown agent {agent_name}")
        scen = Scenario(
            scenario_id=body["scenario_id"], agent_under_test=agent_name,
            perturbations=body.get("perturbations", []),
            causal_invariants=body.get("causal_invariants", []),
            seed=body.get("seed", 0),
            baseline_observation=body.get("baseline_observation", {}))
        run = run_scenario(scen, agent, tenant)
        case = forge.publish(_bus(), run, tenant)
        record_forge(tenant)
        return {"run_id": run.run_id, "case_id": case.case_id,
                "asserts_failed": run.asserts_failed}

    @app.get("/metrics")
    async def metrics() -> PlainTextResponse:
        lines = ["# SIMFORGE metrics (OpenTelemetry)"]
        for name in ("simforge.sims", "simforge.forges"):
            lines.append(f"# TYPE {name} counter")
        return PlainTextResponse("\n".join(lines) + "\n")

    app.state.spine = spine
    return app


_BUS: Any = None


def _bus():
    global _BUS
    if _BUS is None:
        from aegis.backbone import EventBus
        _BUS = EventBus()
    return _BUS
