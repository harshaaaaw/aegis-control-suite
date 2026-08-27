# SIMFORGE — Product 3 (Architecture + Spec)

## The single business problem (shared central room with AEGIS + CAUSALA)
"Ship trustworthy enterprise agents." All three products serve ONE buyer: the
platform/AI leader who must put autonomous agents into production without
getting burned. The three rooms cover the lifecycle:
- AEGIS   = govern + prove (gate, drift, ROI, audit) — the control plane.
- CAUSALA = understand (why did X happen; causal IR over a compiled layer).
- SIMFORGE = stress BEFORE you certify (simulate adversity, generate the eval
  golden set that AEGIS's Ship Gate consumes, assert causal invariants while
  the agent is under load).

SIMFORGE is the left side of the loop: it manufactures the failure corpus and
the regression tests. AEGIS subsystem 8 (Sim/RL Factory) is the in-plane version;
SIMFORGE is the standalone, API-first product that reuses it.

## What SIMFORGE does (one product, multiple POVs)
- As a QA lead: "Throw 200 adversarial scenarios at my agent and tell me which
  behaviors break, with evidence."
- As a safety reviewer: "Prove the agent still respects its causal invariants
  (e.g. 'discount never raises margin without cost change') under perturbation."
- As an eval owner: "Turn every production incident into a replayable sim + a
  golden eval case that AEGIS's Ship Gate must pass before next deploy."

## Architecture (reuses AEGIS bus + Spine + CAUSALA causal layer)
```
simforge/
  __init__.py     Scenario, SimRun, SimOutcome; run(), assert_causal()
  scenario.py     Scenario spec: agent_under_test + perturbations + causal_invariants
  runner.py       SimRunner: executes scenarios, records steps via run_replay.Recorder
  forge.py        Forge: turns a SimOutcome into evalforge.EvalCase (golden set) +
                  publishes 'sim_certified' on the AEGIS bus
  server.py       FastAPI: POST /sim/run, POST /sim/forge, GET /metrics (reuse AEGIS auth)
  cli.py          typer: simforge run <scenario.json> --db, simforge forge <run_id>
  service.py      bus adapter (publishes sim events; consumes causal expectations from CAUSALA)
tests/            scenario execution, causal assertion, forge->evalcase, fault injection
```
- Auth/tenancy: reuse `aegis.security` (JWT, 32-byte secret floor, SSRF guard).
- Persistence: reuse `aegis.spine` (tamper-evident SQLite) for run records.
- Causal checks: call CAUSALA `explain_effect`/`what_if_cause` to assert that a
  simulated outcome respects the stated causal invariants (citation-backed).
- Loop closure: `forge()` emits `evalforge.EvalCase` and a `sim_certified` event
  the AEGIS Ship Gate subscribes to (golden set auto-feeds the gate).

## Anti-slop invariants (same bar as AEGIS/CAUSALA)
- Idempotent run: same (tenant, scenario_id, seed) -> same run_id.
- No bare except: typed raises with run_id.
- Externalized state: runs live in Spine, never process memory.
- Tenant isolation: sim runs + forged cases scoped by tenant_id.
- Observability: OTel counters (sims run, asserts failed, cases forged).
- Resilience: a crashing scenario must not take down the forge (bus isolation).
