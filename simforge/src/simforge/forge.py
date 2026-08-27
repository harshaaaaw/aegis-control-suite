"""SIMFORGE Forge: turn a SimRun into a regression EvalCase + bus event.

This closes the loop: every simulated failure becomes a golden eval case that
AEGIS's Ship Gate must pass before the next deploy. The forged case asserts the
failure is NOT reproduced.
"""
from __future__ import annotations

import json
import uuid

from aegis.backbone import ControlEvent, EventBus, register_subsystem
from aegis.security import get_logger
from evalforge import EvalCase  # type: ignore

from . import SimRun, to_record

log = get_logger("simforge.forge")


def forge_case(run: SimRun, tenant_id: str) -> EvalCase:
    """Build an evalforge.EvalCase asserting each failing step is not reproduced.

    The real EvalCase schema has no scenario/tenant fields, so we embed them in
    the input/expected JSON (self-describing) and use must_not_contain for the
    regression contract (these violation strings must NOT appear in a passing run).
    """
    failing = [s for s in run.steps if s.violated]
    if not failing:
        must_not_contain: list[str] = []
        steps_in = [{"idx": s.idx, "perturbation": s.perturbation,
                     "observation": s.observation} for s in run.steps]
    else:
        # Aggregate violations across ALL failing steps so the regression contract
        # matches run.asserts_failed (which counts every violation).
        must_not_contain = [v for s in failing for v in s.violated]
        steps_in = [{"idx": s.idx, "perturbation": s.perturbation,
                     "observation": s.observation} for s in failing]
    case_input = json.dumps({"tenant_id": tenant_id, "scenario_id": run.scenario_id,
                              "steps": steps_in})
    case_expected = json.dumps({"must_not_violate": must_not_contain, "holds": not failing})
    case = EvalCase(
        case_id="eval_" + uuid.uuid4().hex[:12],
        input=case_input,
        expected=case_expected,
        must_not_contain=must_not_contain,
    )
    log.info("forge_case", extra={"run_id": run.run_id, "case_id": case.case_id,
                                  "failing_steps": len(failing)})
    return case


class ForgeRoom:
    """Bus-facing room: publishes 'sim_certified' so AEGIS Ship Gate consumes the
    golden set."""
    name = "sim_forge"

    def __init__(self, state_dir: str):
        self.state_dir = state_dir

    def register(self, bus: EventBus, spine) -> None:
        register_subsystem(self)

    def handle(self, event) -> None:
        return None

    def publish(self, bus: EventBus, run: SimRun, tenant_id: str) -> EvalCase:
        case = forge_case(run, tenant_id)
        bus.publish(ControlEvent("sim_forge", kind="sim_certified",
                                  payload={"run_id": run.run_id,
                                           "case_id": case.case_id,
                                           "asserts_failed": run.asserts_failed,
                                           "record": to_record(run)},
                                  tenant_id=tenant_id))
        return case
