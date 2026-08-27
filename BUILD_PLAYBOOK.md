# Build Playbook — AEGIS, CAUSALA, Simforge (one by one, premium)

This is the playbook the `agentic-product-build` skill enforces. Run each product through the full loop before moving to the next. Do NOT skip the HUMAN GATE between PLAN and BUILD.

## Load order (skills to have active)
1. `agentic-product-build` (master methodology) — LOAD THIS FIRST.
2. `mattpocock-skills/plan` — for spec structuring.
3. `software-development/test-driven-development` — RED→GREEN→REFACTOR.
4. `software-development/systematic-debugging` — on any failure.
5. `software-development/requesting-code-review` + `mattpocock-skills/code-review` — pre-EVALUATE.
6. Reference: `references/belcort-harness/` — concrete PGE agent prompts to adapt.

## The loop (per product, per subsystem)
```
PLAN      → write SPEC.md (data model, FR list, AC table, eval criteria, non-functional)
            HUMAN GATE: user approves spec (no code before this)
NEGOTIATE → propose HOW + test names; evaluator reviews; ≤3 rounds → contract.md
BUILD     → TDD per FR; anchor APIs to real docs; no bare except; idempotent writes
SIMULATE  → prod stack + AC drive + cumulative regression
EVALUATE  → 4 criteria, hard thresholds; fail on P1 → rebuild
DEPLOY    → agentic k8s (async, externalized state, KEDA, sandbox, graduated trust, OTel)
VALIDATE  → drift detect, SLOs, eval regression guard in CI, signed audit export
```

## Product 1 — AEGIS (AEGIS_PRODUCT_SPEC.md, 496/496 verified)
Reuses on-disk engines: run-replay, evalforge, agent-sentinel.
- Phase 0: Backbone (FastAPI orchestrator, Postgres cert store, S3 evidence, Redis lock, OTel, OIDC/RBAC, Audit Spine).
- Phase 1: Ship Gate wires run-replay + evalforge + agent-sentinel to Spine. Shippable alone.
- Phase 2-5: SwapWatch, ROI Attest, Governed Memory, Contract&Spend, Twin Truth, Causal, Sim/RL, Ops, panes — each as a service on the bus.
- Build order: backbone → gate → one subsystem at a time, each passing EVALUATE before next.

## Product 2 — CAUSALA (CAUSALA_FULL_SPEC.md, finish Appendix C + verify)
Decision-twin: causal graph (expert DAG + client warehouse/ERP/CRM) + PyMC effect-size fitter + DoWhy + honest uncertainty.
- Build: causal-graph service, Bayesian fitter, explainability, audit trail, agent connector.
- Reuses backbone pattern from AEGIS (don't rebuild spine; fork the template).

## Product 3 — Simforge (Simforge idea, document then build)
Synthetic-user simulation factory: persona engine + conversation simulator + scorer (reuses evalforge + agent-sentinel).
- Build: persona library, multi-turn simulator, failure surfacer with transcripts, eval suite generator feeding AEGIS Gate.

## Anti-slop P1 gate (block merge if any hit)
- bare except / except Exception present and unjustified
- read-modify-write not atomic (no idempotency key)
- unfamiliar API/method not verified against real docs
- auth boolean logic trusts client-controlled value
- test would pass if function deleted (fake test)
- CI coverage/security lowered or hooks bypassed

## Eval gate (CI, block merge on fail)
- DeepEval: G-Eval + faithfulness + answer relevancy vs golden dataset, threshold set
- Promptfoo: prompt-injection / jailbreak / PII red-team, fail on success
- RAGAS: only if retrieval present
- regression: PR vs main delta < -5% blocks

## Deploy gate (k8s)
- async queue + 202 + poll (never block HTTP on agent)
- externalized state (pgvector/Redis), KEDA on queue depth
- per-agent RBAC + sandbox + automountServiceAccountToken: false
- graduated trust via GitOps, never day-one prod creds
- Langfuse/OTel traces; chaos drill (kill mid-run → fail-safe)

## Rules
- Local-first; no public push without explicit GO + PAT (`~/.ianvs_gh_token`, rotate after).
- Self-rate every artifact in loop; research more if a claim is unsupported.
- One product at a time; depth over breadth; prove fusion via the Audit Spine, not claims.
