# CAUSALA

Causal-inference **Information Retrieval** over a compiled causal knowledge layer.
CAUSALA is the IR subsystem of the AEGIS control plane: agents ask "why did this
happen?" or "what happens if we do X?" and get **citation-backed** causal answers,
not model hallucinations.

Built on the Hermes **llm-wiki** pattern: compile causal relationships ONCE into a
linked causal graph (with confidence + provenance), then retrieve deterministically
with citations. No per-query rediscovery, no invented causes.

## Quickstart

```bash
pip install -e "./causala"

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

- **Compiled-once knowledge**: cause→effect claims ingested with confidence +
  source. Not rediscovered per query.
- **Citation-backed answers**: every returned cause/effect carries its `source`.
  We never answer from a cause we did not ingest (no hallucination by construction).
- **Confidence floor**: claims < 0.5 are flagged `contested` for human review,
  never silently trusted.
- **Tenant isolation**: all retrieval scoped by `tenant_id` (no cross-tenant leak).
- **Multi-hop traversal**: `networkx` BFS over the causal graph; each hop is a
  real ingested, cited claim.
- **Externalized state**: SQLite-backed; the AEGIS control bus delivers
  `causal_ingest` / `causal_explain` events to it (failure-isolated).

## Honest limitations

- The natural-language `explain`/`what_if` use a keyword heuristic to pick the
  effect/cause token. For free-text, plug an LLM in front to emit the canonical
  key; the graph lookup stays deterministic. Explicit `explain_effect` /
  `what_if_cause` / `retrieve_path` are the precise API.
- Correlation vs causation: the graph stores asserted causal claims; CAUSALA
  retrieves them, it does not itself establish causality (that is upstream
  ingestion, e.g. AEGIS Causal Decisions' OLS estimator).

## As an AEGIS subsystem

`causala.service.CausalaSubsystem` registers on the AEGIS `EventBus` as the
`causala` room. Ingest via `causal_ingest` events; query via the engine API/CLI.
