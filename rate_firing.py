# Self-interrogation rating: which ideas are 'firing' (broad, quick-sell, anti-disaster)?
# Same 7 engines, reframed around UNIVERSAL business pain, not agent-infra jargon.
W = dict(breadth=0.28, quicksell=0.26, firing=0.26, smart=0.12, kw=0.08)

ideas = {
 "AEGIS (Seatbelt for AI)": dict(
   breadth=9, quicksell=9, firing=10, smart=9, kw=9,
   pitch="Stop every AI you ship from breaking the business: fail-closed, auditable, provable.",
   buyer="Any company shipping AI in 2026 (i.e. every company)."),
 "LEDGERSCALE (AI Cost Control)": dict(
   breadth=10, quicksell=10, firing=9, smart=8, kw=8,
   pitch="Know what every AI call costs, per user, per feature. Kill runaway loops automatically.",
   buyer="Every CFO / eng lead with an AI bill."),
 "PROBE (QA for AI)": dict(
   breadth=9, quicksell=9, firing=9, smart=9, kw=7,
   pitch="Test your AI like software before customers see it. Catch the 15 known failure modes.",
   buyer="Every eng team shipping any model to users."),
 "SENTINEL-GW (AI Firewall)": dict(
   breadth=9, quicksell=9, firing=10, smart=8, kw=8,
   pitch="Block data leaks and rogue calls at the edge. Scoped AI identity, never in context.",
   buyer="Every CISO / security team."),
 "MNEMOS (Truth Layer)": dict(
   breadth=9, quicksell=8, firing=8, smart=9, kw=8,
   pitch="Stop your AI from answering from stale or made-up data. Canonical, provenanced truth.",
   buyer="Every knowledge-worker / search / copilot product."),
 "CONTRACTIQ (AI Contract Auditor)": dict(
   breadth=10, quicksell=10, firing=9, smart=8, kw=7,
   pitch="Scan every contract for risky clauses and money leaks in minutes, with citations.",
   buyer="Every legal / finance team at any company. Reuses ragforge+sentinel+evalforge."),
 "SUPPORTIQ (100% Support QA)": dict(
   breadth=10, quicksell=9, firing=8, smart=7, kw=6,
   pitch="Grade 100% of support conversations, not 2%. Catch bad agents, surface trends.",
   buyer="Every support org. Reuses sentinel+evalforge+ragforge."),
}
scored={k:round(sum(v[p]*W[p] for p in W),2) for k,v in ideas.items()}
ranked=sorted(scored.items(),key=lambda x:-x[1])
print(f"{'IDEA':34}{'SCORE':6} ONE-LINE PITCH")
for k,s in ranked:
    print(f"{k:34}{s:6} {ideas[k]['pitch'][:62]}")
print("\nFIRE-TIER (>=8.8):",[k for k,s in ranked if s>=8.8])
print("SPINOFF-TIER (<8.8, broad but reuses engines):",[k for k,s in ranked if s<8.8])
