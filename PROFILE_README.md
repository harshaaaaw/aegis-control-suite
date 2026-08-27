# Deva Harsha Mummareddy

AI infrastructure engineer. I build the control layer around LLM agents: the security shield, the budget governor, and the forensic recorder that answers "why did it do that" at 3am.

Currently running a multi-agent stack in production where these three tools earn their keep daily. Previously built and operated a 4-petabyte document-intelligence pipeline (GE Aerospace RADAR) on n8n, LangGraph, Pinecone, and AWS. Starting an AI research master's (MPI-CIS) in November, focused on graph-augmented retrieval and cyclic multi-agent systems.

## The agent control plane (pinned below)

| | |
|---|---|
| **agent-sentinel** | Per-turn security shield. Scans every tool result for prompt injection and secret leakage in under a millisecond for typical pages, enforces its own latency budget, fails closed, writes a tamper-evident audit chain. |
| **token-governor** | Budgets and kill switches for agent fleets. Hard daily caps per tenant and workflow, cascade routing that cuts cost ~60x when the cheap tier passes, circuit breakers for retry storms, cost-per-successful-outcome accounting. |
| **run-replay** | Time-travel forensics. Records every step of an agent run with sha256-chained digests, verifies logs were not touched, reconstructs what the agent knew at any step, pins the exact step where a different tool answer would have changed everything. |

## What I actually do

- Production agents: LangGraph orchestration, retrieval pipelines, tool sandboxes, evaluation harnesses.
- Cost discipline: my own fleet bills through token-governor; I know my dollars-per-successful-outcome to four decimals.
- Security side work on HackerOne when I want to stay sharp about how attackers think.

## Contact

Open to roles where someone owns agent reliability end to end. Best reach: email or LinkedIn.

<!--
Note to self before publishing: create as github.com/harshaaaaw/harshaaaaw,
pin the three repos above in this order: sentinel, governor, replay.
-->
