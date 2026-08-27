# evalforge

Golden-set evaluation harness with CI merge gates for LLM pipelines. Deterministic checks (exact match, must-contain, forbidden strings, regex, citation validity) plus judge hooks, regression attribution, and the two numbers interviewers ask for: recall@k and faithfulness.

Hiring managers say it directly: candidates who have built an eval harness before are the ones worth hiring, because "it looked good in testing" is how teams ship an agent that quietly burns budget for three weeks. This is that harness, extracted from my own agent stack.

## The workflow it enforces

```
golden-set v1.2.0 (versioned, rot tracked)
   │
   ├─ pipeline change ──▶ run(suite) ──▶ RunReport(pass_rate, recall@k, faithfulness)
   │                                            │
   └─ diff vs baseline ──▶ ScoreDiff ──▶ verdict: PASS | WARN | BLOCK
                                 │
                        regressions named per case_id
```

A prompt tweak that fixes one case and silently breaks four others cannot merge. The gate blocks on any regression or a pass-rate drop over 2%.

## Quickstart

```bash
pip install -e .
pytest tests/ -q
```

```python
from evalforge import EvalCase, GoldenSet, EvalRunner

suite = GoldenSet.new("support-rag", "1.2.0")
suite.cases = [
    EvalCase("q1", "What is the refund window?",
             contexts=["Refunds are accepted within 30 days."],
             must_contain=["30 days"], require_citation=True),
    # ...
]

runner = EvalRunner(state_dir=".evalforge")
report = runner.run(suite, my_rag_pipeline)      # callable: case -> answer
print(report.pass_rate, report.faithfulness)

# in CI: diff candidate vs baseline, block merge on regression
diff = EvalRunner.diff(base_report, cand_report, base_cases, cand_cases)
if diff.should_block_merge:
    sys.exit(1)
```

## Check library

| Check | Catches |
|---|---|
| `exact_match` | content equality; citation markers stripped first so formatting never masks drift |
| `contains:` / `not_contains:` | required facts, forbidden phrases (leaks, PII patterns, "drop table") |
| `regex` | structured outputs: order numbers, SLA figures, ISO dates |
| `citations_valid` | faithfulness proxy: every [n] points at a real retrieved context |
| LLM-as-judge hook | subjective quality; marked UNCALIBRATED until you score agreement against human labels |

Judge calibration is a first-class concept here: `calibration_agreement()` measures judge-vs-human agreement before you trust automated scores. An uncalibrated judge is labeled as such in every result line.

## Design decisions

- **Golden sets are versioned.** Score diffs compare against a known baseline version; when cases rot, bump the version instead of quietly editing history.
- **Per-case attribution.** A BLOCK names exactly which cases regressed and which improved, so the fix loop starts immediately.
- **Deterministic checks are free.** They catch what they can at zero token cost; judges only earn their keep on what remains.
- **Run artifacts persist** as JSONL per run id, so flaky-pipeline bisection is grep, not archaeology.

## Limitations

- Faithfulness here is a citation-validity proxy, not entailment checking. Real NLI scoring is the next milestone.
- No online/production sampling yet; this gates changes offline, by design.
- Single-process. Wire `EvalRunner._persist` to your warehouse for fleet-wide views.

## Status

v1.0.0. 6/6 tests green. Gates real prompt changes in my own stack's CI.

MIT. Deva Harsha Mummareddy.
