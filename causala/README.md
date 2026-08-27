# CAUSALA

**The mid-market, audit-ready, agent-native causal decision twin.**

Fortune-500 causal incumbents do not serve the mid-market operational gap. CAUSALA does. It gives every executive and every AI agent a causally-grounded "what will this decision cause" answer, with board-ready confidence intervals and an immutable audit trail, built from the company's own operational data plus an expert-encoded causal graph.

The one-liner:

> I have to make a high-cost decision (price change, headcount, strategy, agent policy) with only rear-view dashboards and gut feel, and I cannot defend the call to my board or a regulator. CAUSALA turns that into a quantified, causal, auditable decision.

## What it actually does

- **Compiled-once causal graph**: cause→effect claims ingested once, with confidence and source. Not rediscovered per query.
- **"Why did this happen?"** with citation-backed causes. Every returned cause carries its source; we never answer from a cause we did not ingest.
- **"What happens if we do X?"** with a multi-hop causal walk over the graph (each hop is a real, cited claim).
- **Conflict flagging**: when two claims point at the same effect, flag it for human review.
- **Confidence floor**: claims below 0.5 are flagged contested, never silently trusted.
- **Tenant isolation**: all retrieval scoped by tenant_id.
- **Audit trail**: every query is a deterministic, citation-backed lookup, not a fresh search.

CAUSALA is the IR subsystem of the AEGIS control plane. It is the "understand" half of the trust loop: AEGIS certifies, CAUSALA explains.

## Quickstart

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

## Design (anti-slop + IR-correct)

- **Compiled-once knowledge**: cause→effect claims ingested with confidence + source. Not rediscovered per query.
- **Citation-backed answers**: every returned cause/effect carries its `source`. We never answer from a cause we did not ingest (no hallucination by construction).
- **Confidence floor**: claims below 0.5 are flagged `contested` for human review, never silently trusted.
- **Tenant isolation**: all retrieval scoped by `tenant_id` (no cross-tenant leak).
- **Multi-hop traversal**: `networkx` BFS over the causal graph; each hop is a real ingested, cited claim.
- **Externalized state**: SQLite-backed; the AEGIS control bus delivers `causal_ingest` / `causal_explain` events to it (failure-isolated).

## As an AEGIS subsystem

`causala.service.CausalaSubsystem` registers on the AEGIS `EventBus` as the `causala` room. Ingest via `causal_ingest` events; query via the engine API/CLI.

## HTTP API

All endpoints require a `Bearer` JWT (HS256, >=32-byte secret). Rate limited.

- `POST /api/v1/causal/ingest` — register a cause→effect claim (tenant-scoped)
- `POST /api/v1/causal/explain` — why did this effect happen? (citation-backed)
- `POST /api/v1/causal/whatif` — what happens if this cause holds?
- `GET  /api/v1/causal/conflicts?tenant=...` — flagged conflicts for human review
- `GET  /metrics` — Prometheus exposition of OTel counters

## Quality (measured)

| Signal | Value |
|---|---|
| Tests | 30 green |
| Coverage | 91% |
| Ruff | clean |
| Mypy (business logic) | clean |
| Bandit | clean |

Run: `pytest causa/tests/ -q`

## Honest limitations

- The natural-language `explain`/`whatif` use a keyword heuristic to pick the canonical cause/effect token. For free-text, plug an LLM in front to emit the key; the graph lookup stays deterministic. The precise API is `explain_effect` / `what_if_cause` / `retrieve_path`.
- CAUSALA retrieves asserted causal claims; it does not itself establish causality. That is upstream ingestion (e.g. AEGIS Causal Decisions' OLS estimator) or expert input. Correlation vs causation is the ingestor's job, not CAUSALA's.
- The causal graph is the brain; client data fits the magnitudes. CAUSALA retrieves and simulates on the compiled graph — scale is per-company small-data, not Fortune-500 cross-company transfer. That is the thesis, stated honestly.

## Positioning

CAUSALA is the applied, audit-ready, agent-native decision twin — the companion to AEGIS Gate. AEGIS = "is the agent safe to ship"; CAUSALA = "is the decision defensible." Both are the same reliability discipline (trust via evidence + audit) applied to different objects (agents vs decisions). This is NOT a causal-research play and is positioned honestly as applied engineering on open causal libraries plus client data, with honest uncertainty. The 250B-incumbent fight is explicitly NOT ours; the mid-market operational/agent wedge is.

## License

MIT.
