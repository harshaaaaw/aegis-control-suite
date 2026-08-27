# run-replay

Time-travel forensics for LLM agent runs. Record every step of an agent loop (model calls, tool calls, state snapshots), then replay it deterministically, verify nothing was tampered with, and answer the question every agent team dreads: "why did it do that?"

Agent failures are not reproducible by re-running. The model is non-deterministic, tools are live systems, and by morning the world has moved on. The trace is the only witness. This library makes the witness tamper-evident and queryable.

## The forensic loop

```
record  ─▶  runs/<run_id>.jsonl   (one line per step: digests + data + state hash)
verify  ─▶  re-hash everything; any edit to history breaks the chain
travel  ─▶  time_travel(events, to_step=N): what did the agent know at step N?
diverge ─▶  swap one step's output; see exactly where trajectories split
```

## Quickstart

```bash
pip install -e .
pytest tests/ -q          # 6 tests, sub-second
python examples/demo.py   # full incident walkthrough on a refund-gone-wrong run
```

```python
from run_replay import Recorder, StepKind, Replayer, time_travel

rec = Recorder(state_dir=".runs", meta=RunMeta(agent_name="support", seed=42))

state = {"goal": "refund order 8123"}
rec.step(StepKind.MODEL_CALL, "planner-v2",
         inp={"prompt": p}, out={"action": "call_tool"},
         state=state, wall_ms=412)

# ... later, during the incident review ...
meta, events = rec.load_run(rec.path)
res = Replayer(events).verify()        # digests_match=True -> history intact
world = time_travel(events, to_step=1) # exactly what the agent knew pre-refund
alt  = Replayer(events).divergence(1, {"status": "lost_in_transit"})
# alt.diverged_at == 1: this is the step where a different tool answer changes everything
```

## Why hashes everywhere

Every event commits to `sha256(canonical_json)` of its input and output, plus the hash of the full agent state after the step. Stored data is checked against its digest on every load. If anyone edits the JSONL, `verify()` names the exact step where history was rewritten. In regulated or money-touching agents, that is the difference between a debugging tool and admissible evidence.

## What this is not (yet)

- Not a visual timeline UI; output is structured text your editor or notebook renders fine.
- Not distributed tracing; one process, one run per file. Cross-service correlation is future work.
- Not a model-call cache, though deterministic replay means you can skip re-paying for steps whose digests match.

## Design notes

- Canonical JSON (`sort_keys`, tight separators) before hashing so equivalent dicts hash identically across processes.
- Large payloads can be nulled to store-only-digests (`input_data=None`) without breaking verification; the recorder treats missing data as unverifiable-but-unbroken.
- RNG seed captured in run metadata for stacks that seed their sampling.

## Status

v1.0.0. 6/6 tests passing in CI. Born from real 3am incidents in my own agent fleet.

MIT. Deva Harsha Mummareddy.
