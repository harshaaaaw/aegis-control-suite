# AEGIS Control Suite

**One room. Three products. One business objective: ship trustworthy enterprise agents.**

AEGIS certifies, CAUSALA explains, SIMFORGE stresses before you ship. Together they close the loop enterprises running agents at scale actually need - and nobody has shipped as one package.

| Product | Does | Where it lives |
|---|---|---|
| **AEGIS** | Certifies an agent run, signs the verdict, watches for drift later, records ROI without fake numbers | `aegis/` |
| **CAUSALA** | Answers "why did this happen?" and "what happens if we do X?" with citation-backed causes, not model hallucinations | `causala/` |
| **SIMFORGE** | Runs an agent under perturbation, checks its rules hold, and turns any failure into a regression case that AEGIS must pass next deploy | `simforge/` |

The three are not separate tools. They are one trust loop: **exercise -> understand -> guard -> ship**. The integration test in `aegis/tests/integration/` is the proof that the loop actually closes end to end.

## Selling it in one line each

- **AEGIS** - "Enterprises running hundreds of AI agents touching money and production systems cannot control what each may do autonomously, nor prove it afterward. AEGIS gives each agent exactly as much freedom as it has earned, auto-demotes violators, and hands regulators receipts."
- **CAUSALA** - "Nobody sells the mid-market, audit-ready, agent-native causal decision twin. Fortune-500 causal incumbents do not go down-market. CAUSALA gives every executive and agent a causally-grounded, confidence-bounded, defensible answer using their own data and an expert-encoded causal graph."
- **SIMFORGE** - "Agents now pay for things and touch production. Before you ship a change, run the agent through its worst case, prove your causal invariants still hold, and turn any failure into a golden regression case AEGIS will block on if it ever comes back."

## Quickstart

### AEGIS (zero config, no Kubernetes, no JWT needed to try)

```bash
pip install -e "./aegis[test]"
export AEGIS_JWT_SECRET=$(python -c "import secrets; print(secrets.token_hex(16))")

# 1. Certify a recorded agent run (JSONL of steps)
cat > run.jsonl <<'EOF'
{"idx":0,"kind":"MODEL_CALL","name":"planner","in":{"x":1},"out":{"y":2},"state":{"x":1},"ms":5}
EOF
aegis certify run.jsonl

# 2. Re-verify a verdict's signature + hash chain
aegis verify <verdict_id>

# 3. Check behavior drift (live run vs certified baseline)
aegis drift run-1 baseline.jsonl live.jsonl

# 4. Whole control-plane posture in one view
aegis posture --tenant acme

# 5. SSRF guard check for an agent tool URL
aegis ssrf http://169.254.169.254/latest

# 6. Serve the HTTP API locally
aegis server --port 8000
```

### CAUSALA (causal IR, compile-once, citation-backed)

```bash
pip install -e "./causala"
export AEGIS_JWT_SECRET=$(python -c "import secrets; print(secrets.token_hex(16))")

# Ingest a causal claim (compiled once, with provenance)
causala ingest --cause cache_miss --effect cost_up --conf 0.8 --source finops-3

# Why did cost go up? -> cites finops-3
causala explain --effect cost_up

# What if we have cache misses? -> cites finops-3
causala whatif --cause cache_miss

# Multi-hop causal chain (cite-backed at every hop)
causala ingest --cause cost_up --effect margin_down --conf 0.7 --source finops-4
causala path --from cache_miss --to margin_down
```

### SIMFORGE (adversarial simulation -> golden cases -> AEGIS regression set)

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

## The three rooms, in one sentence each

**AEGIS** - the control plane ("the room") where ten subsystems live: Ship Gate (certify/block via forensic replay + shield + eval), SwapWatch (behavior drift), ROI Attest (tamper-evident ledger, no fake ROI), Governed Memory, Contract Intel, Twin Truth (counterfactual digital twin), Causal Decisions (OLS with honest CI), Sim/RL Factory, Autonomous Ops (graduated trust), and Panes (one-view posture).

**CAUSALA** - the IR subsystem. Agents ask "why" and "what if" and get citation-backed causes from a compiled-once causal graph. No per-query rediscovery, no invented causes, confidence floor below 0.5 is flagged contested.

**SIMFORGE** - the stress room. A scenario is an agent plus perturbations plus causal invariants to hold. Run it, assert the invariants (optionally against CAUSALA), and forge any failure into an evalforge golden case published to the AEGIS bus under `sim_certified`. AEGIS's Ship Gate consumes it into the regression set.

## The loop, proven by an integration test

```python
# 1. SIMFORGE runs an agent under a perturbation
run = run_scenario(scenario, demo_agent, "acme")

# 2. SIMFORGE forges a golden case + publishes sim_certified on the bus
case = ForgeRoom("runs").publish(bus, run, "acme")

# 3. AEGIS Ship Gate consumes it into its regression set
goldens = gate.golden_cases("acme")
assert any(g["case_id"] == case.case_id for g in goldens)
```

That is `tests/integration/test_integration.py`. It is one test, and it proves the whole loop closes.

## Quality (measured, not claimed)

These numbers are from running the local test suite on the machine that built them. They are not aspirational.

| Product | Tests | Coverage | Ruff | Mypy | Bandit |
|---|---|---|---|---|---|
| AEGIS | 42 | 95% (1338 stmts) | 0 | 0 | clean |
| CAUSALA | 30 | 91% | 0 | 0 | clean |
| SIMFORGE | 8 | server covered | 0 | 0 | clean |
| Integration | 2 | — | — | — | — |

Run the whole thing:

```bash
pytest aegis/tests/ causa/tests/ simforge/tests/ -q
```

## Security model (honest, short)

- Every AEGIS/CAUSALA/SIMFORGE HTTP endpoint requires a Bearer JWT (HS256, >=32-byte secret floor; 11-byte secrets are rejected at the gate).
- Verdicts are HMAC-signed and hash-chained; tenant-scoped reads.
- SSRF guard blocks metadata, loopback, and RFC1918 hosts before any outbound call.
- Bus subscribers are failure-isolated: one crashing subsystem never takes down the others (verified by a chaos test that kills a subscriber mid-flow).
- Tamper-evident Spine (SQLite, hash-chained runs) is the trust root.

## Production deployment

- AEGIS: `aegis/Dockerfile`, `aegis/deploy/k8s/` (async API, KEDA on queue depth, gVisor sandbox for untrusted tool exec, least-privilege RBAC, NetworkPolicy, gradual-trust promotion).
- CAUSALA: `causala/Dockerfile` (causal IR, tenant-scoped SQLite, OTel metrics).
- SIMFORGE: `simforge/Dockerfile` (async sim API, rate limited, tenant-scoped, in-process agent registry; the API never executes foreign code).

See `deploy/` for the k8s manifests and the SLO/error-budget story.

## Honest limitations

- CAUSALA's natural-language `explain`/`whatif` use a keyword heuristic to pick the canonical cause/effect token. For free-text, plug an LLM in front to emit the key; the graph lookup stays deterministic. The precise API is `explain_effect` / `what_if_cause` / `retrieve_path`.
- CAUSALA retrieves asserted causal claims; it does not itself establish causation. That is upstream ingestion (e.g. AEGIS Causal Decisions' OLS estimator) or expert input.
- SIMFORGE's in-process agent registry means the API does not execute foreign code - hosts register real agent callables by name. The demo agent in the CLI is there so the CLI works out of the box.
- SIMFORGE's metrics endpoint currently renders a stub Prometheus exposition of the OTel counters; wire an OTel exporter via `OTEL_EXPORTER_*` env for a real collector.

## License

MIT.
