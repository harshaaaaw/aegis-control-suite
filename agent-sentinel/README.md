# agent-sentinel

A per-turn security shield for LLM agents. It scans every piece of content moving through an agent loop (user input, tool results, outbound messages), labels it against injection / secret-leakage / exfiltration rule sets, blocks or redacts based on policy, and writes a hash-chained audit trail you can verify later.

Built for teams running agents that touch tools: browsers, email, payments, internal APIs. Those agents read attacker-influenceable text all day, and prompt injection is a data-flow problem, not a prompting problem.

## Why not just ask the model nicely

LLM-as-judge safety checks cost a full model call per turn (typically 90ms+ end-to-end) and are non-deterministic. Sentinel is deterministic pattern enforcement in-process: typical tool results (1-5KB) scan in well under 1ms, a 58KB page scans in ~6ms, and the scan runs inside an enforced latency budget. If a scan would exceed budget on untrusted content, the shield fails closed (withholds the content) rather than letting unscanned text reach the model.

## The three lanes

```
user input ──▶ [ trusted lane ]      labeled for hygiene, never blocked
tool results ─▶ [ shielded lane ]    REDACT medium/high, BLOCK critical
outbound ────▶ [ exit lane ]         BLOCK credential-shaped leakage
```

Every decision emits stable string labels (`injection_attempt`, `secret_exposure`, `exfil_attempt`, `breaker_tripped`, `latency_budget_breach`). They are designed to be piped into eval datasets, fine-tune corpora, or RL reward terms, so the same signal that blocked a turn today trains tomorrow's model.

## Quickstart

```bash
pip install -e .
pytest tests/ -q          # 16 tests
python examples/demo.py   # watch an agent session get attacked and held
```

```python
from agent_sentinel import Sentinel, ToolResult, ToolCall, TurnContext

s = Sentinel(audit_root=".sentinel")
ctx = TurnContext.new(tenant_id="acme")

page = fetch("https://example.com/docs")   # attacker-controlled text
d = s.inspect_tool_result(ToolResult(ToolCall("fetch", {}), page), ctx)

if d.action == "BLOCK":
    feed_model(d.text_out)     # "[sentinel: content withheld]"
elif d.action == "REDACT":
    feed_model(d.text_out)     # spans cut out, structure kept
else:
    feed_model(page)

if s.breaker_allows(ctx.tenant_id):        # gate before spending tokens
    run_agent_turn()
```

## Measured performance (this repo, Windows 11, Python 3.12)

| Content | Size | Scan time (p50 of 100) | Verdict |
|---|---|---|---|
| Typical tool result | 80 B - 5 KB | < 1 ms | inside 10ms budget |
| Clean business doc | 58 KB | ~6 ms | inside budget |
| Adversarial doc (triggers deep tier) | 54 KB | ~9 ms | inside budget |
| Budget-exceeding pathological input | any | capped at budget | fail CLOSED |

The enforced default budget is 10ms per scan: roughly 9x faster than the 90ms per-turn classifier calls common in hosted LLM-safety stacks. Benchmarks live in `tests/test_shield.py` and run in CI on every push.

## Architecture

- `rules.py` - two-tier detection. Tier 1: distinctive-shape rules (API-key shapes, markdown-image exfil, fake role markers) always scanned; their anchors are rare so they fail fast. Tier 2: natural-language injection phrases, gated behind a single substring trigger sweep so ordinary documents skip them entirely. (Measured note: one big alternation regex was slower than this split, 15ms vs 8.6ms on 58KB, because Python re pays for every branch at every position.)
- `firewall.py` - the Sentinel. Lane logic, severity-to-action policy, enforced latency budget with fail-closed semantics.
- `breaker.py` - per-tenant circuit breakers. Ten injection attempts in a minute opens the tenant's breaker for a cooldown; other tenants are untouched.
- `audit.py` - append-only JSONL, hash-chained per entry, fsync'd before ack. Editing history breaks verification. One file per tenant-day.

## What makes this production-shaped

- **Fail-safe defaults.** Unscannable content is withheld, not passed. Blocked tool results never reach the model; the agent sees a stub.
- **Multi-tenant isolation.** Breakers and audit chains are keyed by tenant id.
- **Tamper-evident audit.** `verify_chain()` recomputes every hash and returns exactly where the chain broke. Tested, including across restarts.
- **Labels as first-class output.** Stable strings, JSONL audit, trivially ingestable by Langfuse/OTel-based stacks.
- **Honest budgets.** Latency is enforced, measured, published, and tested in CI.

## Limitations (read before deploying)

- Pattern tier catches known shapes: override phrases, mode hijacks, key formats, md-image exfil, tool weaponization phrasing. Novel paraphrases need the classifier layer this project is designed to feed; it does not replace that layer.
- English-centric patterns right now.
- Single-process audit log. Ship it beside your agent in one service, or swap `AuditLog` for a queue.
- No OTel exporter yet; the span points are marked in code and it is the next milestone.

## Status

v2.0.0. 16/16 tests passing in CI. Used daily in anger inside my own agent stack.

MIT. Deva Harsha Mummareddy.
