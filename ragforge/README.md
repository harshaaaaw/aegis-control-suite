# ragforge

Structure-aware RAG: markdown-heading chunking with section provenance, hybrid dense+keyword search, and the honest numbers on why the lazy 512-token window loses.

Naive RAG breaks in predictable ways. Fixed-size windows cut sentences in half, orphan table rows, and blur exact identifiers (error codes, SKU strings) into semantic mush. This library is the fix pattern hiring loops probe for ("how big are your chunks, and why?" / "what happens to error-code lookups?"), made runnable.

## What's inside

| Piece | Why it matters |
|---|---|
| `markdown_aware()` | splits on heading boundaries, keeps sections whole, carries `heading_path` so answers cite *which section* they came from |
| `fixed_window()` | the naive baseline, kept so you can measure the gap yourself |
| `hybrid_search()` | RRF merge of dense cosine + keyword jaccard; dense catches meaning, keywords catch exact identifiers |
| pluggable `Embedder` | deterministic offline embedder for tests/demos; swap Voyage/OpenAI/pgvector models without touching call sites |
| provenance in every result | citations point at real sections; evalforge's `citations_valid` check consumes this directly |

## Quickstart

```bash
pip install -e .
pytest tests/ -q
```

```python
from ragforge import Document, VectorStore, markdown_aware

store = VectorStore()
for doc in load_docs():                       # Document(doc_id, text)
    store.upsert(markdown_aware(doc))

rep = store.search("what is error E-4182", k=3)
top = rep.results[0]
print(top.chunk.heading_path)   # ["Engineering runbook", "Error E-4182: index lag"]
print(f"{rep.latency_ms:.1f}ms")
```

## Measured behavior (this repo's own test suite)

- Section-integrity: no chunk straddles two markdown sections.
- Exact-identifier query (`E-4182`): hybrid search lands the right section in top-3 where pure dense retrieval blurs it against unrelated prose.
- Heading provenance survives every strategy so downstream answers can cite `"Engineering runbook > Error E-4182"` instead of a naked chunk id.

## Pairs with

- **evalforge**: feed retrieved chunks as contexts; its `recall@k` and `citations_valid` checks score this retriever end to end.
- **agent-sentinel**: scanned tool results are exactly what should (and shouldn't) enter this index.

## Limitations

- In-memory store; production path is pgvector (schema ships in the token-governor repo's SQL conventions).
- Offline hash embedder is lexical, not semantic; it exists so CI never pays API tokens. Real embeddings plug into `Embedder.embed`.
- No reranking stage yet (query rewriting + cross-encoder rerank is the next milestone).

## Status

v1.0.0. 6/6 tests green in CI.

MIT. Deva Harsha Mummareddy.
