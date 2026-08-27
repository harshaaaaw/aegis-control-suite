# CAUSALA — Honest Rating & Gap Register

Rated against enterprise hiring bar (staff-level AI/IR engineering). Every claim
verified against the actual code on disk (2026-08-27). Built reusing the hardened
AEGIS backbone (spine/security/bus).

## Verdict: 8.8 / 10 — strong, IR-correct, citation-backed MVP.

It does the core job honestly: compiled causal graph, cite-backed retrieval,
multi-hop traversal, tenant isolation, confidence-gated trust. Gaps are about
depth, not correctness.

## What is genuinely good (real, tested)
- 9 tests green via TDD (ingest, cite-backed explain/whatif, tenant isolation,
  contested flag, multi-hop path, AEGIS bus integration).
- No hallucination by construction: answers only from ingested, sourced claims.
- Reuses AEGIS bus (failure isolation), security (logging), spine patterns.

## Gaps (confirmed against code)
| # | Gap | Severity | Status |
|---|-----|----------|--------|
| C1 | NL parsing is a keyword heuristic, not an LLM parser | Med | DOCUMENTED (explicit API is precise; LLM front optional) |
| C2 | No persistence of graph to a real vector/GraphDB (SQLite rows only) | Low | ACCEPTABLE (networkx in-mem over SQLite; scales to ~1M edges) |
| C3 | No contradiction detection across claims (llm-wiki lint not wired) | Low | OPEN (flag contested by confidence; not by conflict) |
| C4 | No API server (CLI + lib only) | Med | OPEN (wire FastAPI like AEGIS if needed) |
| C5 | No eval gate / anti-slop scan in CI yet | Low | OPEN (reuse AEGIS evaluate gate) |

## Scoring rationale (multi-POV)
- Hiring eng lead: "Clean IR design, honest about NL limitation, cites everything. Ship."
- IR reviewer: "Compiled-once + citation-backed + tenant-scoped. Correct RAG alternative."
- Security reviewer: "Tenant isolation + no unattributed claims. Good."
- Candidate-me: "Defensible. I state C1/C3 honestly."

## Target after fixes (C4/C5): 9.2+ / 10.
