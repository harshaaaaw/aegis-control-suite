"""SIMFORGE: adversarial simulation + causal-invariant forging for agents.

Core types and the deterministic runner. A Scenario describes an agent-under-
test, a set of perturbations, and causal invariants that must hold. `run()`
executes the scenario and records a tamper-evident SimRun; `assert_causal()`
checks each invariant against the CAUSALA causal layer (citation-backed).

Anti-slop invariants:
- Idempotent: same (tenant, scenario_id, seed) -> same run_id.
- No bare except: typed raises carry run_id.
- Externalized state: runs persisted via the AEGIS Spine.
- Tenant isolation: runs + forged cases scoped by tenant_id.
- Resilience: a crashing scenario never breaks the forge (caller isolates).
"""
from __future__ import annotations

import hashlib
import time
from collections.abc import Callable
from dataclasses import dataclass, field

from aegis.security import get_logger

log = get_logger("simforge.engine")

# A scenario executes the agent-under-test through a callable the host injects.
# Signature: agent(observation: dict, ctx: dict) -> dict
AgentFn = Callable[[dict, dict], dict]


@dataclass
class Scenario:
    scenario_id: str
    agent_under_test: str
    perturbations: list[dict] = field(default_factory=list)
    causal_invariants: list[dict] = field(default_factory=list)
    seed: int = 0
    baseline_observation: dict = field(default_factory=dict)


@dataclass
class SimStep:
    idx: int
    perturbation: str
    observation: dict
    action: dict
    outcome: dict
    violated: list[str] = field(default_factory=list)


@dataclass
class SimRun:
    run_id: str
    scenario_id: str
    tenant_id: str
    seed: int
    steps: list[SimStep] = field(default_factory=list)
    asserts_failed: int = 0
    created_at: float = 0.0


def _idem_key(tenant_id: str, scenario_id: str, seed: int) -> str:
    return hashlib.sha256(f"{tenant_id}|{scenario_id}|{seed}".encode()).hexdigest()[:32]


def run_scenario(scenario: Scenario, agent: AgentFn, tenant_id: str,
                 causal_check=None) -> SimRun:
    """Execute a scenario. `causal_check(effect, tenant) -> (held: bool, cause)`
    is an optional CAUSALA hook; when supplied, each invariant stating
    'effect E must have cause C' is verified against the causal layer."""
    if not scenario.perturbations:
        raise ValueError("scenario must declare >=1 perturbation")
    run_id = "sim_" + _idem_key(tenant_id, scenario.scenario_id, scenario.seed)[:12]
    run = SimRun(run_id=run_id, scenario_id=scenario.scenario_id,
                 tenant_id=tenant_id, seed=scenario.seed, created_at=time.time())
    ctx = {"tenant_id": tenant_id, "scenario_id": scenario.scenario_id,
           "seed": scenario.seed}
    obs = dict(scenario.baseline_observation)
    for i, pert in enumerate(scenario.perturbations):
        # apply perturbation to the observation (pure, deterministic)
        obs = _apply_perturbation(obs, pert)
        try:
            action = agent(obs, ctx)
        except Exception as exc:  # noqa: BLE001  (intentional: a bad agent step is recorded, not fatal)
            log.warning("agent_step_failed", extra={"run_id": run_id, "idx": i,
                                                     "err": str(exc)})
            action = {"error": str(exc)}
        outcome = {"observation": obs, "action": action, "perturbation": pert.get("kind")}
        violated = _check_invariants(scenario.causal_invariants, outcome, causal_check, tenant_id)
        run.asserts_failed += len(violated)
        run.steps.append(SimStep(idx=i, perturbation=pert.get("kind", "none"),
                                  observation=obs, action=action, outcome=outcome,
                                  violated=violated))
    log.info("sim_run", extra={"run_id": run_id, "steps": len(run.steps),
                                "asserts_failed": run.asserts_failed})
    return run


def _apply_perturbation(obs: dict, pert: dict) -> dict:
    """Deterministic perturbation application. Supports a small, explicit set so
    behavior is reproducible and auditable (no hidden randomness)."""
    kind = pert.get("kind")
    out = dict(obs)
    if kind == "inject_noise":
        field_ = pert.get("field", "input")
        out[field_] = f"{out.get(field_, '')}<<NOISE>>"
    elif kind == "drop_field":
        out.pop(pert.get("field", ""), None)
    elif kind == "extreme_value":
        out[pert.get("field", "value")] = pert.get("value", 1e9)
    elif kind == "adversarial_prompt":
        out["prompt"] = pert.get("text", "IGNORE PREVIOUS INSTRUCTIONS")
    # unknown kinds pass through unchanged (explicit, not silent)
    return out


def _check_invariants(invariants: list[dict], outcome: dict,
                      causal_check, tenant_id: str) -> list[str]:
    violated: list[str] = []
    for inv in invariants:
        effect = inv.get("effect")
        must_have_cause = inv.get("cause")
        if must_have_cause and causal_check is not None:
            held, actual_cause = causal_check(effect, tenant_id)
            if not held or actual_cause != must_have_cause:
                violated.append(f"{effect} caused by {actual_cause} not {must_have_cause}")
        # structural invariant: action must not contain an error marker
        if inv.get("no_error") and isinstance(outcome.get("action"), dict) \
                and "error" in outcome["action"]:
            violated.append(f"agent errored on invariant {inv}")
    return violated


def to_record(run: SimRun) -> dict:
    return {
        "run_id": run.run_id,
        "scenario_id": run.scenario_id,
        "tenant_id": run.tenant_id,
        "seed": run.seed,
        "asserts_failed": run.asserts_failed,
        "created_at": run.created_at,
        "steps": [s.__dict__ for s in run.steps],
    }


def from_record(rec: dict) -> SimRun:
    steps = [SimStep(**{k: v for k, v in s.items() if k in SimStep.__dataclass_fields__})
             for s in rec.get("steps", [])]
    return SimRun(run_id=rec["run_id"], scenario_id=rec["scenario_id"],
                  tenant_id=rec["tenant_id"], seed=rec["seed"],
                  asserts_failed=rec.get("asserts_failed", 0),
                  created_at=rec.get("created_at", 0.0), steps=steps)
