"""15 enterprise project buckets x 15 buyer POVs, computed ranking."""

POVS = [
    "founder_believability", "staff_code_depth", "recruiter_scan", "cfo_pain",
    "ciso_trust", "devrel_adoption", "demo_wow", "jd_keyword_breadth",
    "vs_existing_oss", "maintenance_realism", "war_story_fit", "lead_relevance",
    "urgency_2026", "portfolio_synergy", "viral_potential",
]

BUCKETS = {
    # name: (one-line, scores per POV 1-5)
    "agent-cost-governor": (
        "Token budget governor: hard caps, circuit breakers, tiered routing, "
        "$/successful-outcome accounting for agent fleets",
        [5, 5, 4, 5, 4, 4, 4, 5, 4, 4, 5, 4, 5, 5, 4]),
    "per-turn-agent-shield": (
        "Sub-100ms classifier firewall scoring every agent turn for injection/"
        "loop/policy violations; labels feed evals and audit trail",
        [5, 4, 4, 3, 5, 4, 5, 5, 4, 4, 5, 5, 5, 4, 5]),
    "otel-agent-tracer": (
        "OpenTelemetry-native agent tracing with tail-based sampling biased to "
        "costly/failed traces + per-tenant cost attribution",
        [4, 5, 3, 4, 4, 5, 3, 5, 2, 4, 5, 3, 4, 4, 3]),
    "doc-intel-at-scale": (
        "Incremental document-intelligence pipeline: MinHash dedup, checkpoint "
        "resume, cost-per-doc benchmarks; generic RADAR",
        [5, 4, 4, 5, 3, 3, 3, 4, 4, 4, 5, 3, 4, 4, 2]),
    "money-movement-core": (
        "Double-entry ledger that survives kill -9; property-tested invariants; "
        "deterministic replay from append-only log",
        [4, 5, 4, 4, 4, 3, 4, 4, 4, 4, 2, 3, 3, 3, 3]),
    "eval-regression-gate": (
        "CI gate for prompts/models: golden-set replay, score diffs block merge, "
        "cost regressions trigger review",
        [4, 4, 4, 4, 3, 4, 3, 5, 3, 4, 4, 4, 4, 4, 3]),
    "rag-freshness-auditor": (
        "Continuously audits vector stores: stale embeddings, orphaned chunks, "
        "grounding failures traced back to source docs",
        [4, 4, 3, 4, 3, 3, 4, 4, 4, 4, 5, 4, 4, 4, 3]),
    "agent-chaos-harness": (
        "Chaos engine for agents: kills tools mid-run, injects malformed args, "
        "proves budgets hold and state recovers",
        [4, 5, 3, 3, 4, 3, 4, 4, 4, 4, 4, 3, 4, 4, 4]),
    "multi-tenant-llm-billing": (
        "Usage-based billing meter for LLM features: per-tenant margin, quotas, "
        "runaway detection, invoice-grade audit",
        [4, 4, 4, 5, 4, 3, 3, 4, 4, 4, 3, 4, 5, 3, 3]),
    "prompt-supply-chain": (
        "Signed prompt/model-version registry with provenance: what prompt ran, "
        "who approved it, what it scored",
        [3, 4, 3, 3, 5, 3, 3, 4, 4, 3, 3, 3, 4, 3, 3]),
    "pii-boundary-proxy": (
        "Proxy that keeps PII out of model context via tokenization vault; "
        "reversible only inside perimeter; compliance reports",
        [4, 4, 4, 3, 5, 4, 4, 4, 4, 3, 4, 4, 5, 4, 4]),
    "sla-aware-router": (
        "Latency-SLA aware cascade router: p95 budget per request class, "
        "escalation trees, live SLO dashboard",
        [4, 4, 3, 4, 3, 4, 4, 4, 3, 4, 3, 4, 4, 4, 3]),
    "agent-forensics-replay": (
        "Time-travel debugger: replay any production agent run step-by-step "
        "with full state snapshots; 'why did it do that'",
        [4, 5, 4, 3, 4, 5, 5, 4, 3, 3, 4, 4, 4, 4, 5]),
    "context-economics-lab": (
        "Benchmark suite proving compression-vs-refetch tradeoff; finds the "
        "40-60% sweet spot per workload empirically",
        [3, 4, 3, 4, 2, 4, 3, 3, 4, 4, 5, 3, 3, 3, 4]),
    "compliance-evidence-pump": (
        "Auto-collects SOC2/ISO evidence from agent infrastructure: access logs, "
        "policy decisions, change approvals into auditor-ready packets",
        [3, 3, 4, 4, 5, 2, 2, 4, 4, 3, 2, 2, 4, 3, 2]),
}

rows = []
for name, (desc, scores) in BUCKETS.items():
    total = sum(scores)
    avg = total / len(POVS)
    rows.append((total, avg, name, desc, dict(zip(POVS, scores))))

rows.sort(reverse=True)
print(f"{'rank':4s} {'total':6s} {'avg':5s} bucket")
for i, (total, avg, name, desc, s) in enumerate(rows, 1):
    top3 = sorted(s.items(), key=lambda kv: -kv[1])[:3]
    tops = ", ".join(k for k, v in top3)
    print(f"{i:>4d} {total:>6d} {avg:>5.2f} {name}")
    print(f"{'':16s}{desc[:90]}")
    print(f"{'':16s}strongest: {tops}")

print("\nTOP 3:", [r[2] for r in rows[:3]])
