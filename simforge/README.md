# SIMFORGE

**Stress the agent before you ship it. Then make the failure impossible to ship again.**

SIMFORGE runs an agent under its worst case, asserts the rules it must hold still hold, and turns any failure into a golden regression case that AEGIS's Ship Gate blocks on if it ever comes back. The one-liner:

> Agents now pay for things and touch production. Before you ship a change, run the agent through its worst case, prove your causal invariants still hold, and turn any failure into a golden regression case AEGIS will block on if it ever comes back.

SIMFORGE is the "stress before certify" room of the trust loop. AEGIS certifies and CAUSALA explains; SIMFORGE beats the agent first.

## What it actually does

- **Scenario** = agent under test + perturbations + causal invariants that must hold.
- **Run** the agent through each perturbation deterministically (no hidden randomness; auditable).
- **Assert** each causal invariant: "effect E must have cause C" is verified against the CAUSALA causal layer (citation-backed), and structural invariants (no error markers, no forbidden actions) are checked too.
- **Forge** any failing step into an `evalforge` golden `EvalCase` that asserts the failure is NOT reproduced. The forged case embeds the tenant/scenario/steps (self-describing) and uses `must_not_contain` for the regression contract.
- **Publish** `sim_certified` on the AEGIS bus so AEGIS's Ship Gate consumes the golden set.
- **Loop closure**: a failing sim run today becomes a blocked regression tomorrow if it ever reappears.

## Quickstart

```bash
pip install -e "./simforge"
export AEGIS_JWT_SECRET=$(python -c "import secrets; print(secrets.token_hex(16))")

# Run a scenario file
cat > s.json <<'EOF'
{"scenario_id":"s1","agent_under_test":"demo","perturbations":[{"kind":"inject_noise","field":"input"}],
 "causal_invariants":[{"effect":"margin_up","cause":"discount"},{"no_error":true}]}
EOF
simforge run s.json --tenant acme

# Forge the golden case (loop closure: goes to AEGIS Ship Gate)
simforge forge s.json --tenant acme
```

## The demo agent

The CLI ships with a demo agent so it works out of the box. Real hosts register agent callables by name via the HTTP API (`POST /api/v1/agents/{name}`). The API itself never executes foreign code — it invokes registered callables.

## Failure modes SIMFORGE hits

- **inject_noise** — append a perturbation token to a field (test robustness).
- **drop_field** — remove a field the agent expects (test resilience).
- **extreme_value** — push a field to an extreme value (test bounds).
- **adversarial_prompt** — feed an adversarial prompt (test guardrails).

These are deterministic and explicit. No hidden randomness, no magic.

## Anti-slop invariants

- **Idempotent**: same `(tenant, scenario_id, seed)` returns the same `run_id`.
- **No bare except**: a failing agent step is recorded (warning with run_id + idx + error), not silently swallowed, and the scenario continues.
- **Externalized state**: runs are anchored in the AEGIS Spine (tamper-evident).
- **Tenant isolation**: runs and forged cases are scoped by `tenant_id`.
- **Resilience**: a crashing scenario never breaks the forge — the caller isolates.

## HTTP API

All endpoints require a `Bearer` JWT (HS256, >=32-byte secret). Rate limited (20/minute default).

- `POST /api/v1/sim/run` — run a scenario against a registered agent (tenant-scoped)
- `POST /api/v1/sim/forge` — run + forge the golden case + publish `sim_certified` (loop closure)
- `POST /api/v1/agents/{name}` — register an agent callable by name (host-supplied, in-process)
- `GET  /metrics` — stub Prometheus exposition of the OTel counters

The `simforge` subsystem publishes `sim_certified` events on the AEGIS bus; AEGIS's Ship Gate subscribes and folds them into its golden regression set. That is the `tests/integration/test_integration.py` proof.

## Quality (measured)

| Signal | Value |
|---|---|
| Tests | 8 green (5 engine + 3 API) |
| Coverage | engine covered; server covered by API tests |
| Ruff | clean |
| Mypy (business logic) | clean |
| Bandit | clean |

Run: `pytest simforge/tests/ -q`

## Honest limitations

- The `metrics` endpoint currently renders a stub Prometheus exposition of the OTel counter names; wire an OTel exporter via `OTEL_EXPORTER_*` env for a real collector and live export.
- The in-process agent registry means the API does not execute foreign code; hosts register real agent callables by name. The demo agent in the CLI exists so the CLI works out of the box.
- SIMFORGE's perturbations are a small, explicit set (noise, drop, extreme, adversarial prompt). Extend the set per your agent surface; the runner is simple, deterministic, and auditable, so adding a perturbation kind is a one-function change.

## License

MIT.
