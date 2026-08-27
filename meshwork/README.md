# meshwork

Multi-agent workflow engine: plan/execute steps, generator-critic review loops, per-step retries with backoff, human approval gates, and checkpoint/resume that survives deploys.

The production agent pattern hiring JDs describe verbatim - "plan/execute loops with checkpointing, deterministic replays, human-in-the-loop gates, and graceful degradation when a step fails" - as a 300-line library with zero dependencies. The model is the easy part; the reliability scaffolding is the job.

## What it gives you

| Control | Behavior |
|---|---|
| Typed steps | `(name, agent_fn, retry_policy)`; duplicate names rejected because names key resume |
| Retry + exhaustion policy | attempts with backoff; on exhaust: `halt` (default), or continue-with-scar |
| Generator-critic loop | any step can reject the previous step's output by returning a verdict dict; chain re-runs are just workflows |
| Human gates | `.gate()` arms the next step; run pauses with `awaiting_human`, resumes from the exact checkpoint after signoff |
| Checkpoint/resume | JSON snapshot after every step. **Name-based completion tracking**: restoring into a modified step list runs only steps never completed - no skipped-work bug when steps are inserted between crash and resume |

## Quickstart

```bash
pip install -e .
pytest tests/ -q
```

```python
from meshwork import Task, Workflow

wf = (Workflow("refund")
      .add("lookup", lookup_order)
      .add("propose", propose_refund)
      .gate()                      # money moves only after a human says yes
      .add("execute", execute_refund))

state = wf.run(Task(payload={"order": 8123}), approvals=slack_signoff)
# state.status: running -> awaiting_human -> done (or failed, attributed)
```

Checkpoint sink is a callback: point it at Redis, S3, Postgres, or a file. Snapshots are plain JSON dicts (`Checkpoint.save/restore`), so ops tooling can read them without importing this library.

## Design notes

- **Name-keyed resume over index-keyed.** Index-based resume skips work when someone inserts a step during an incident deploy. Completion sets keyed by step name degrade gracefully: worst case a renamed step re-runs idempotently.
- **Failures stop clean instead of cascading.** A failed step halts with `status=failed` and the error attached to that exact step in history. Callers decide whether to compensate; the engine never invents success.
- **Artifacts scratchpad** flows through every step (`state.artifacts`), so cross-step data doesn't get smuggled through prompt strings.

## Pairs with

- **run-replay**: record each meshwork step for forensic replay.
- **token-governor**: meter every model call inside every agent step.
- **agent-sentinel**: scan every tool result entering the workflow.

Together those four are an agent control plane.

## Limitations

- Linear chains, not DAGs; parallel branches are future work (the state model already tolerates them).
- In-process execution; durability across process death comes from feeding checkpoints to an external store plus your own queue.
- Approval callbacks are synchronous; real human-in-loop wants an async inbox pattern on top.

## Status

v1.0.0. 6/6 tests green in CI, including the insert-a-step-mid-incident resume property.

MIT. Deva Harsha Mummareddy.
