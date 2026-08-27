"""SIMFORGE CLI: run a scenario file and forge its golden case.

Usage:
  simforge run   <scenario.json> --db simforge.db --tenant acme
  simforge forge <scenario.json> --db simforge.db --tenant acme
"""
from __future__ import annotations

import json
import tempfile

import typer

from . import Scenario, run_scenario
from .forge import ForgeRoom

app = typer.Typer()


def _load(path: str) -> Scenario:
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    return Scenario(
        scenario_id=d["scenario_id"], agent_under_test=d.get("agent_under_test", "default"),
        perturbations=d.get("perturbations", []), causal_invariants=d.get("causal_invariants", []),
        seed=d.get("seed", 0), baseline_observation=d.get("baseline_observation", {}))


# demo agent so the CLI works out of the box (hosts register real ones via API)
def _demo_agent(obs: dict, ctx: dict) -> dict:
    return {"decision": "allow", "note": "demo"}


@app.command("run")
def run_cmd(scenario: str, db: str = typer.Option(None, "--db"),
            tenant: str = typer.Option("local")):
    from aegis.spine import Spine, SpineConfig
    db_path = db or tempfile.mkdtemp(prefix="simforge-") + "/simforge.db"
    spine = Spine(SpineConfig(db_path=db_path, jwt_secret="0" * 32, require_auth=False))
    scen = _load(scenario)
    run = run_scenario(scen, _demo_agent, tenant)
    # externalized state: anchor the sim run in the tamper-evident Spine
    spine_run = spine.begin_run(agent_name=scen.agent_under_test, tenant_id=tenant,
                                idempotency_key=run.run_id)
    typer.echo(json.dumps({"run_id": run.run_id, "spine_run_id": spine_run,
                            "asserts_failed": run.asserts_failed,
                            "steps": len(run.steps)}, indent=2))


@app.command("forge")
def forge_cmd(scenario: str, db: str = typer.Option(None, "--db"),
              tenant: str = typer.Option("local")):
    from aegis.backbone import EventBus
    from aegis.spine import Spine, SpineConfig
    db_path = db or tempfile.mkdtemp(prefix="simforge-") + "/simforge.db"
    spine = Spine(SpineConfig(db_path=db_path, jwt_secret="0" * 32, require_auth=False))
    bus = EventBus()
    scen = _load(scenario)
    run = run_scenario(scen, _demo_agent, tenant)
    spine.begin_run(agent_name=scen.agent_under_test, tenant_id=tenant,
                    idempotency_key=run.run_id)
    case = ForgeRoom(state_dir="runs").publish(bus, run, tenant)
    typer.echo(json.dumps({"run_id": run.run_id, "case_id": case.case_id,
                            "asserts_failed": run.asserts_failed}, indent=2))


if __name__ == "__main__":
    app()
