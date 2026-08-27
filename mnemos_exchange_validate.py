"""MNEMOS EXCHANGE pivot: computed 16-POV re-validation of the market design."""

POVS = {
 # pov: (weight, score 1-5, note)
 "skeptical_founder":      (1.0, 5, "'your agents trade facts' explains itself in 5 seconds"),
 "staff_engineer_depth":   (1.0, 5, "market design + clearing + reputation bonds = hard systems"),
 "recruiter_6sec_scan":    (1.0, 5, "'built the first fact exchange for agents' - instant standout"),
 "cfo_pain":               (0.9, 5, "prices make truth costs VISIBLE; chargeback per department"),
 "ciso_trust":             (0.9, 4, "bonds + challenges = economic security, not just regexes"),
 "devrel_adoption":        (0.8, 4, "sim-wallet demo offline; needs clean SDK"),
 "demo_wow":               (1.0, 5, "watch a stale fact get challenged, discounted, delisted LIVE"),
 "jd_keyword_breadth":     (0.9, 5, "payments, ledgers, marketplaces, reputation, settlement"),
 "vs_existing_players":    (0.9, 5, "all 4 rivals are stores; NOBODY is an exchange - clear air"),
 "maintenance_realism":    (0.7, 4, "v1 single-process sim settlement keeps ops sane"),
 "war_story_fit":          (0.8, 5, "RADAR doc pipelines = lived fact-supply-chain scars"),
 "lead_relevance":         (0.8, 4, "fintech leads (River/DualEntry) see payments DNA immediately"),
 "urgency_2026":           (0.9, 5, "x402 did $15M/109M txns; rails EXIST, no app uses them for facts"),
 "portfolio_synergy":      (1.0, 5, "all 7 engines become exchange organs"),
 "viral_potential":        (0.8, 5, "nobody can reply 'X already did this' - empty Google results"),
 "india_global_sell":      (0.8, 4, "UPI-native micropayments story lands in India instantly"),
}

total_w = sum(w for w, _, _ in POVS.values())
scored = sum(w * s for w, s, _ in POVS.values())
pct = scored / (total_w * 5) * 100
print(f"{scored:.1f}/{total_w*5:.1f} = {pct:.1f}%")

print("\n=== KILL ATTEMPTS ===")
kills = [
 ("two-sided cold start", True,
  "REAL: buyers need sellers, sellers need buyers. FIX: launch single-org "
  "(departments trade internally = chargeback market), cross-org second."),
 ("crypto smell scares enterprises", False,
  "settlement is ledger credits by default; x402/UPI just optional rails. "
  "No token, no blockchain required."),
 ("markets price everything, even garbage", False,
  "that IS the feature: garbage gets challenged, loses its bond, delists. "
  "The mechanism replaces moderation."),
 ("too complex for one dev", False,
  "v1 = one process, sim wallets, 3 seed suppliers, challenge bot, SQLite "
  "settlement ledger. Same scale as governor which took one session."),
 ("academic 'knowledge markets' papers exist", False,
  "papers are not shippable protocol + running exchange. First mover = "
  "first working implementation + open spec."),
]
for claim, valid, resp in kills:
    print(f"[{'REAL RISK' if valid else 'survives'}] {claim}\n   -> {resp}")

print("\n=== WHY FIRST-MOVER HOLDS ===")
print("searched: 4 memory-trust stores (all single-tenant), x402/AP2 (payments,")
print("not facts), Ocean/Snowflake (dataset-scale, human buyers), Wolfram (curated")
print("API, no market). Per-fact agent exchange with freshness SLAs + bonds:")
print("zero shipped implementations found. Category unclaimed.")
