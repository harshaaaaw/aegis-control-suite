# token-governor

Budgets, kill switches and cost-per-successful-outcome accounting for LLM agent fleets.

Agent sessions burn 1-3.5M tokens per task (50-500x a chat turn), 85% of companies miss their AI cost forecasts by more than 10%, and EY's whole "Agent FinOps" paper exists because finance teams cannot see where agent money goes until the invoice lands. This library is the enforcement layer those papers ask for: it sits between your agent loop and the model API.

## The four controls

| Control | What it does | Default behavior |
|---|---|---|
| **Daily budgets** | Per-tenant and per-workflow caps with soft alert thresholds | SOFT fires once at 80%; HARD refuses new spend for the UTC day |
| **Cascade router** | Cheap tier first; escalates to mid/frontier only when quality checks fail | ~87% cost cut vs frontier-everything when escalation is selective |
| **Runaway breakers** | Rolling-window spend/call/failure-streak limits per session | Trips after $5 or 120 calls in 5 min; opens for 15 min cooldown |
| **Outcome ledger** | Append-only JSONL tying every call to its outcome id | Rolls up to cost-per-SUCCESSFUL-outcome and retry waste |

The metric that matters is not cost per call. A workflow that costs $0.50 per call but fails 30% of the time costs $0.71 per success. Governor prices outcomes, so product decisions use real unit economics.

## Quickstart

```bash
pip install -e .
pytest tests/ -q          # 11 tests, sub-second
python examples/demo.py   # watch a retry storm hit a kill switch
```

```python
from token_governor import Governor, TurnContext, SpendRefused

g = Governor(state_dir=".governor")
g.set_tenant_cap("acme", cap_usd=50.00)
g.set_workflow_cap("acme", "support", cap_usd=5.00)

ctx = TurnContext.new(tenant_id="acme", workflow="support")
g.begin_outcome(ctx)
try:
    out = g.gated_call(
        ctx,
        prompt_tokens=4200, max_output_tokens=900,
        generate=lambda tier, _t: call_model(tier),   # your API call
        quality_ok=lambda: answer_passes_checks(),
    )
    g.end_outcome(ctx, success=True)
except SpendRefused as e:
    degrade_gracefully(e)      # budget refused the call BEFORE money moved
```

## Escalation economics, measured

With the default price table (cheap $0.25/$1.25, mid $3/$15, frontier $15/$75 per Mtok):

| Pattern | Cost per logical call |
|---|---|
| Frontier always | $0.0375 (1k in / 400 out) |
| Cascade, cheap passes (the common case) | $0.000625 (**60x cheaper**) |
| Cascade with two quality failures then frontier pass | $0.0381 (+2% for the insurance) |

The router meters every hop, re-checks budgets before each escalation, and stops mid-cascade if a cap bites. Escalation policy is pluggable: `quality_ok` is your verifier, and routing without one is supported but visible in the ledger as unverified.

## Design notes worth stealing

- **Refuse before spend.** Budget precheck uses worst-case output tokens; HARD caps mean no invoice surprise, ever. Tested: a call whose estimate alone exceeds the cap never reaches `generate`.
- **Reentrancy bug found by chaos test.** The breaker originally deadlocked when a retry storm tripped it while holding its own lock (`Lock` + self-inspection = hang). Now `RLock` with an inline open-check. The storm test that caught it runs in CI.
- **Ledger is append-only JSONL.** Rollups are computed reads, so the audit trail and the analytics can never disagree.
- **Prices are config, not code.** `PriceTable` with family fallback (`claude-opus-4.6` -> family entry); swap tables without touching logic.

## Limitations

- Fixed-window accounting (not sliding); window edges allow up to 2x burst within one window across boundaries.
- Single-process state. For multi-service fleets, back `Budgets`/`RunawayBreaker` with Redis; interfaces are already narrow.
- UTC day buckets only; no timezone-localized billing days yet.
- No OTel exporter yet (same milestone as agent-sentinel).

## Status

v1.0.0. 11/11 tests passing in CI on Python 3.10-3.12. Runs daily inside my own multi-agent stack, which pays its own bills through this governor.

MIT. Deva Harsha Mummareddy.
