# Re-rate with ENTERPRISE bar: owns a real business outcome end-to-end,
# runs at scale, survives audit, minimal-human, hard to build (defensible).
# 'layer/wrapper' ideas (thin UI on an engine) are penalized hard.
W = dict(outcome=0.30, scale=0.22, audit=0.18, minimal=0.15, build=0.15)

ideas = {
 "AEGIS — Autonomous Ops Governance Plane": dict(
   outcome=10, scale=9, audit=10, minimal=9, build=8,
   what="Runs as the mandatory control layer every agent in the company routes through. "
        "Owns the outcome: 'no agent ever does an unauthorized, unaudited, or unbudgeted action.' "
        "Not a wrapper - it's infrastructure other systems depend on, like a service mesh.",
   hard="Consistent policy across 1000s of concurrent agents, crash-safe replay, signed identity, "
        "linearizable audit log, multi-region failover."),
 "LEDGERSCALE — AI Spend & Liability Ledger": dict(
   outcome=10, scale=9, audit=10, minimal=8, build=8,
   what="The financial system of record for ALL AI activity. Finance closes the books on AI spend "
        "from it. Owns outcome: 'every dollar an AI spends is accounted, capped, and defensible to audit.'",
   hard="Event-sourced double-entry at high write volume, exactly-once, idempotency, "
        "distributed consensus on budget caps, replayable ledgers."),
 "CONTRACTIQ — Contract Risk & Obligations Engine": dict(
   outcome=9, scale=8, audit=9, minimal=9, build=7,
   what="Not 'summarize a PDF'. It's the system of record for EVERY obligation a company has signed: "
        "auto-extracts, flags money-leak clauses, tracks renewal/penalty dates, alerts before breach. "
        "Owns outcome: 'we never miss a commitment or get burned by a clause again.'",
   hard="Long-doc grounding with citations, clause-version diffing across 10k contracts, "
        "obligation state machine, SLA alerting, audit trail of every flag."),
 "FLOWPULSE — Production Reliability & Incident System": dict(
   outcome=9, scale=9, audit=8, minimal=9, build=8,
   what="Not 'monitor traces'. It's the on-call system that detects agent chain-failures in real time, "
        "auto-correlates, and opens incidents with root cause. Owns outcome: 'MTTR for agent incidents "
        "is measured and bounded.'",
   hard="Streaming replay-diff at scale, chain-failure detection, trace correlation, "
        "auto-postmortem generation, alert dedupe."),
 "DOCVAULT — Grounded Knowledge System of Record": dict(
   outcome=8, scale=8, audit=9, minimal=8, build=7,
   what="Every generated answer in the company is citation-locked to a source of record. "
        "Owns outcome: 'no employee acts on a hallucinated internal fact.'",
   hard="Hash-locked provenance, contradiction detection across sources, TTL truth decay, "
        "enforcement at write-time, not just read-time."),
 "SENTINEL-GW — AI Traffic Security Gateway": dict(
   outcome=9, scale=9, audit=10, minimal=8, build=7,
   what="The enforced perimeter for all AI egress. Owns outcome: 'no AI leaks data or calls "
        "an unapproved endpoint.' Runs inline at every edge.",
   hard="Line-rate policy at the edge, identity per request, WASM isolation, zero data-in-context, "
        "CORS/rate-limit/audit on every call."),
 "PROBE — Continuous AI Assurance": dict(
   outcome=8, scale=8, audit=9, minimal=7, build=7,
   what="Not 'run a test'. It's the continuous assurance pipeline that grades every model change "
        "against the 15 known failure modes before release. Owns outcome: 'we ship AI knowing its "
        "failure profile.'",
   hard="Taxonomy probe generation, versioned golden sets, CI gating, regression tracking, "
        "report-card distribution."),
 "SUPPORTIQ — Support Quality & Compliance System": dict(
   outcome=7, scale=8, audit=7, minimal=8, build=6,
   what="System of record for support quality across 100% of conversations, with agent scorecards "
        "and compliance flags. Owns outcome: 'support quality is measured and enforced, not sampled.'",
   hard="Transcript scoring at volume, drift alerting, scorecard aggregation, PII handling."),
}
# THIN WRAPPER penalty baseline: a 'college project' idea would score ~ outcome3 scale2 audit2 minimal4 build2
scored={k:round(sum(v[p]*W[p] for p in W),2) for k,v in ideas.items()}
ranked=sorted(scored.items(),key=lambda x:-x[1])
print(f"{'PRODUCT':40}{'SCORE':6} SYSTEM-OF-RECORD OWNERSHIP")
for k,s in ranked:
    v=ideas[k]
    print(f"{k:40}{s:6} {v['what'][:58]}")
print("\nENTERPRISE BUILD SET (>=8.3):",[k for k,s in ranked if s>=8.3])
print("DEFERRABLE (<8.3):",[k for k,s in ranked if s<8.3])
print("\n--- hard-build proof per build-set item (defensibility) ---")
for k,s in ranked:
    if s>=8.3:
        print(f"\n## {k} ({s})")
        print("  owns:",ideas[k]['what'])
        print("  hard :",ideas[k]['hard'])
