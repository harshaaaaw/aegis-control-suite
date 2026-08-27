# POV self-rating of candidate products. Weighted composite, honest.
# POVs: pain (research-validated need), scarcity (few competitors=good),
# hire (would a hiring mgr want this person), feas (can I build a credible demo),
# kw (keyword coverage weight it carries).
import json

cands = {
 "AEGIS": dict(pain=10, scarcity=8, hire=10, feas=9, kw=9,
   note="Fail-closed control plane: immutable replay + earned autonomy + audit. Maps to reliability+observability+governance pain. Engines done."),
 "MNEMOS": dict(pain=9, scarcity=7, hire=9, feas=8, kw=8,
   note="Canonical context/truth layer: TTL decay, provenance, poison quarantine. tsukumo's #1 root cause = stale truth."),
 "PROBE": dict(pain=10, scarcity=6, hire=9, feas=7, kw=7,
   note="Agent failure-mode eval harness (15-mode taxonomy). Called biggest unsolved gap, $1-3M, 89% lack it. Braintrust/LangSmith partial competitors."),
 "LEDGERSCALE": dict(pain=9, scarcity=7, hire=9, feas=9, kw=8,
   note="Agent FinOps + runaway-loop kill: per-action caps, double-entry ledger, budget SLOs. Cost is #4 operating problem."),
 "HELIX": dict(pain=6, scarcity=2, hire=7, feas=6, kw=10,
   note="DS/ML/CV/commerce umbrella. SATURATED category but carries the widest keyword spread; catch-all for coverage."),
 "STREAMFORGE": dict(pain=5, scarcity=2, hire=6, feas=5, kw=8,
   note="Lakehouse. Crowded (Databricks/Snowflake). Lower hire pull as standalone."),
 "MODELFORGE": dict(pain=5, scarcity=3, hire=6, feas=4, kw=8,
   note="Train/serve. Crowded (vLLM/Triton/Bento). Hard to stand out."),
 "TRUSTPAY": dict(pain=7, scarcity=4, hire=8, feas=6, kw=8,
   note="Payments/fraud. Niche, fintech-relevant, but payments is its own hard domain."),
 "VOICEDESK": dict(pain=5, scarcity=4, hire=6, feas=5, kw=6,
   note="Contact center. Crowded (Rasa/etc)."),
 "WATCHTOWER": dict(pain=4, scarcity=4, hire=5, feas=4, kw=6,
   note="Video security. Narrow buyer."),
 "DOSSIERIQ": dict(pain=5, scarcity=4, hire=6, feas=5, kw=6,
   note="Doc intel. Crowded (RAGFlow/etc)."),
 "TWINFORGE": dict(pain=4, scarcity=4, hire=5, feas=4, kw=5,
   note="Synthetic data. Niche."),
 "OPSCOPILOT": dict(pain=6, scarcity=5, hire=7, feas=5, kw=7,
   note="AI SRE. Interesting but OpsCopilot-like tools exist."),
}
# weights: pain and hire matter most for 'will they hire me'
W = dict(pain=0.30, scarcity=0.20, hire=0.25, feas=0.15, kw=0.10)
scored = {}
for k,v in cands.items():
    s = sum(v[p]*W[p] for p in W)
    scored[k] = round(s,2)
ranked = sorted(scored.items(), key=lambda x:-x[1])
print(f"{'PRODUCT':14} {'SCORE':6}  POV(pain/scarc/hire/feas/kw)")
for k,s in ranked:
    v=cands[k]
    print(f"{k:14} {s:6}  {v['pain']}/{v['scarcity']}/{v['hire']}/{v['feas']}/{v['kw']}  {v['note'][:70]}")
print()
print("TIER-1 hire-magnets (>=8.5):", [k for k,s in ranked if s>=8.5])
print("TIER-2 coverage/niche (<8.5):", [k for k,s in ranked if s<8.5])
