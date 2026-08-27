# AEGIS Control Plane

Trust, govern, and prove enterprise AI agents. AEGIS is a control plane ("the
room" where 10 agent subsystems live) that records every agent run, gates
whether a change is safe to ship, and produces tamper-evident verdicts you can
audit later.

## Quickstart (zero config, no Kubernetes, no JWT)

```bash
pip install -e "./aegis[test]"

# 1. Certify a recorded agent run (JSONL of steps)
echo '{"idx":0,"kind":"MODEL_CALL","name":"planner","in":{"x":1},"out":{"y":2},"state":{"x":1},"ms":5}' > run.jsonl
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

## The 10 subsystems (the room)

1. **Ship Gate** — certify/block a change via forensic replay + shield + eval.
2. **SwapWatch** — flags behavior drift after certification.
3. **ROI Attest** — tamper-evident cost/benefit ledger (no fake ROI).
4. **Governed Memory** — versioned, capability-gated agent memory.
5. **Contract Intel** — blocks unauthorized tool calls (scope creep).
6. **Twin Truth** — digital-twin counterfactual simulation.
7. **Causal Decisions** — real OLS effect estimator with honest CI.
8. **Sim/RL Factory** — turns production failures into regression cases.
9. **Autonomous Ops** — graduated trust (shadow -> autonomous).
10. **Panes** — one-view posture of the whole plane.

## HTTP API

All endpoints require a `Bearer` JWT (HS256, >=32-byte secret). Rate limited.

- `POST /api/v1/runs` — begin (idempotent) a run
- `POST /api/v1/gate/evaluate` — produce a signed CERTIFY/BLOCK verdict
- `GET  /api/v1/verdicts/{verdict_id}` — tenant-scoped verify
- `GET  /metrics` — Prometheus

## Production deployment

See `deploy/k8s/`: async API, KEDA scaled on queue depth (not CPU), gVisor
sandbox sidecar for untrusted tool exec, least-privilege RBAC, NetworkPolicy,
gradual-trust promotion. CI runs the full EVALUATE gate (pytest + evalforge
golden set + anti-slop scan + bandit + pip-audit) on every push.

## Security

See [SECURITY.md](SECURITY.md). Verdicts are HMAC-signed and hash-chained;
tenant-scoped; secrets must be >=32 bytes; SSRF guard blocks metadata/loopback/
RFC1918 hosts.
