"""MNEMOS validation: 16 POVs x 1-5, computed. Plus kill-attempts."""

POVS = {
 # pov: (weight, score, note)
 "skeptical_founder":        (1.0, 4, "believes pain instantly; doubts teams will pay vs free prompts"),
 "staff_engineer_depth":     (1.0, 5, "decay clocks, provenance chains, quarantine = real systems work"),
 "recruiter_6sec_scan":      (1.0, 5, "'memory with bodyguards' reads instantly"),
 "cfo_pain":                 (0.9, 5, "measured 60% token cut = direct line item"),
 "ciso_trust":               (0.9, 4, "memory poisoning is their nightmare; quarantine wins"),
 "devrel_adoption":          (0.8, 4, "great demo; needs dead-simple SDK to spread"),
 "demo_wow":                 (1.0, 5, "expired-price catch + bill drop lands every room"),
 "jd_keyword_breadth":       (0.9, 4, "memory, RAG, provenance, TTL, embeddings; not infra-heavy"),
 "vs_existing_players":      (0.9, 3, "Mem0/Zep/Letta own 'memory storage'; we must own 'memory TRUST'"),
 "maintenance_realism":      (0.7, 4, "single-process fine first year; decay tuning is ongoing science"),
 "war_story_fit":            (0.8, 5, "RADAR doc-intel + agent fleet = lived these scars daily"),
 "lead_relevance":           (0.8, 4, "Phonely/Voiceops voice agents need durable memory badly"),
 "urgency_2026":             (0.9, 5, "HN wave NOW; agents-in-prod week-one pain"),
 "portfolio_synergy":        (1.0, 5, "reuses replay+sentinel+evalforge as organs"),
 "viral_potential":          (0.8, 4, "'Git for agents' got 129pts; deeper wedge rides that"),
 "india_global_sell":        (0.8, 4, "no-regulator needed; sells by demo anywhere"),
}

total_w = sum(w for w, _, _ in POVS.values())
scored = sum(w * s for w, s, _ in POVS.values())
pct = scored / (total_w * 5) * 100

print(f"{'POV':24s} {'w':>4s} {'score':>5s}")
for k, (w, s, note) in sorted(POVS.items(), key=lambda kv: -kv[1][1]*kv[1][0]):
    print(f"{k:24s} {w:>4.1f} {s:>5d}   {note}")
print(f"\nWEIGHTED TOTAL: {scored:.1f} / {total_w*5:.1f}  = {pct:.1f}%")
print(f"VERDICT BAND: {'BUILD - strong' if pct >= 78 else 'build with focus' if pct >= 70 else 'rethink'}")

print("\n=== KILL ATTEMPTS (steelman the 'no') ===")
kills = [
 ("Mem0/Zep just add TTL", False,
  "TTL is trivial for them BUT provenance chains + poison quarantine + contradiction "
  "resolution + attestation are an architecture, not a flag. We ship the whole trust "
  "model day one; they'd be bolting features on a storage product."),
 ("Teams just re-derive facts each run", True,
  "VALID until token bills arrive. Counter: the 60%-cut measurement IS the pitch. "
  "Mitigation: lead every README with the money number, not the security story."),
 ("Memory needs are app-specific; no one-size", True,
  "Partially valid. Mitigation: Mnemos ships policies per fact-TYPE, not one global "
  "clock; default policies cover 80%, custom decayers are the extension point."),
 ("Embedding-based memory makes this obsolete", False,
  "Vector recall is exactly the problem: it retrieves plausible stale truth confidently. "
  "Mnemos is a layer ABOVE vectors: freshness+provenance gates what retrieval may return."),
 ("Too early - nobody has prod agents long enough to care", False,
  "KORE1/zylos data says fleets ARE in prod now; silent-failure posts prove pain phase."),
]
for claim, valid, response in kills:
    tag = "REAL RISK" if valid else "survives"
    print(f"[{tag}] {claim}\n    -> {response[:150]}")

print("\n=== WEDGE (what we alone ship v1) ===")
for w in ["provenance chains (hash-linked to run records)",
          "per-fact-type decay clocks w/ contradiction flags",
          "write-time poison quarantine",
          "canonical-answer API with measured token savings"]:
    print(f"  - {w}")
