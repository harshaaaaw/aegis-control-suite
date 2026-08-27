# Force each product to have a DISTINCT identity: own mechanism, own data type,
# own buyer, own core engine. Penalize overlap with the agent-engine skeleton.
# distinctness = how different its core mechanic is from 'wrap agent in policy'.
W = dict(distinct=0.34, breadth=0.22, firing=0.24, smart=0.12, kw=0.08)

ideas = {
 "AEGIS — Autonomy Control Plane": dict(
   distinct=7, breadth=9, firing=10, smart=9, kw=9,
   mechanic="Policy sidecar fails closed; autonomy ladder earned by eval score",
   datatype="agent tool-call traces", buyer="AI platform / infra eng",
   engine="agent-sentinel+governor+run-replay (new: ladder orchestrator)"),
 "LEDGERSCALE — AI Spend Ledger": dict(
   distinct=8, breadth=10, firing=9, smart=8, kw=8,
   mechanic="Double-entry token/dollar ledger + budget SLO auto-kill",
   datatype="per-call cost events", buyer="CFO / finops eng",
   engine="token-governor (new: ledger+ClickHouse)"),
 "PROBE — Failure-Mode Eval": dict(
   distinct=8, breadth=9, firing=9, smart=9, kw=7,
   mechanic="15-mode failure taxonomy probes + golden set + CI report card",
   datatype="eval datasets + probe results", buyer="ML/AI quality eng",
   engine="evalforge (new: taxonomy probes)"),
 "SENTINEL-GW — AI Traffic Firewall": dict(
   distinct=9, breadth=9, firing=10, smart=8, kw=8,
   mechanic="Identity-per-request at the edge; scoped tokens never in context",
   datatype="live API traffic", buyer="CISO / security",
   engine="sentinel-middleware (new: gateway+WASM)"),
 "CONTRACTIQ — Clause Risk Auditor": dict(
   distinct=9, breadth=10, firing=9, smart=8, kw=7,
   mechanic="Differential clause scoring vs your approved-playbook corpus",
   datatype="legal PDFs + clause library", buyer="legal / procurement",
   engine="ragforge+sentinel (new: clause diff model)"),
 "SUPPORTIQ — Conversation QA": dict(
   distinct=8, breadth=10, firing=8, smart=7, kw=6,
   mechanic="100% transcript scoring + drift alerting + agent scorecard",
   datatype="call/chat transcripts", buyer="support director",
   engine="evalforge+ragforge (new: transcript scorer)"),
 "DOCVAULT — Grounded Document OS": dict(
   distinct=9, breadth=9, firing=8, smart=9, kw=8,
   mechanic="Every generated sentence cites a hash-locked source; contradiction = block",
   datatype="internal docs + generated content", buyer="knowledge/ops teams",
   engine="ragforge+MNEMOS (new: citation-enforcement)"),
 "FLOWPULSE — Agent Reliability Monitor": dict(
   distinct=9, breadth=9, firing=9, smart=8, kw=7,
   mechanic="Real-time chain-failure-rate + replay-diff anomaly detection in prod",
   datatype="production traces (streaming)", buyer="SRE / on-call",
   engine="run-replay+OTel (new: streaming diff)"),
}
scored={k:round(sum(v[p]*W[p] for p in W),2) for k,v in ideas.items()}
ranked=sorted(scored.items(),key=lambda x:-x[1])
print(f"{'PRODUCT':32}{'SCORE':6} DISTINCT MECHANIC / BUYER")
for k,s in ranked:
    v=ideas[k]
    print(f"{k:32}{s:6} {v['mechanic'][:34]} / {v['buyer']}")
print("\nIdentity spread check (distinct>=8.5, no two share core engine):")
for k,v in sorted(ideas.items(),key=lambda x:-x[1]['distinct']):
    print(f"  {k:32} distinct={v['distinct']}  engine={v['engine'].split('(')[0]}")
