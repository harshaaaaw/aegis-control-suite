# Rate sibling products that ALL stay in the AI-Engineer / agent-control lane.
# Research-validated pain clusters: reliability, observability, stale-context, cost.
# Each product must map to >=1 cluster and NOT require ML/DS training or pandas/numpy skills.
W = dict(pain=0.34, scarcity=0.22, hire=0.28, feas=0.16)  # hire+feas matter for "will they hire me fast"

cands = {
 # AEGIS: fail-closed governance control plane (your 7 engines as organs)
 "AEGIS": dict(pain=10, scarcity=8, hire=10, feas=9,
   maps="reliability+observability+governance",
   note="Immutable replay, earned autonomy ladder, policy sidecar, audit. Engines already built."),
 # PROBE: failure-mode eval harness (the 'biggest unsolved' gap)
 "PROBE": dict(pain=10, scarcity=6, hire=9, feas=7,
   maps="reliability (measurable)",
   note="15-mode agent failure taxonomy probes + dataset + report. 89% lack this."),
 # LEDGERSCALE: agent FinOps + runaway-loop kill
 "LEDGERSCALE": dict(pain=9, scarcity=7, hire=9, feas=9,
   maps="cost",
   note="Per-action token caps, double-entry ledger, budget SLOs, one-click kill. Cost=#4 pain."),
 # MNEMOS: canonical truth/context layer
 "MNEMOS": dict(pain=9, scarcity=7, hire=9, feas=8,
   maps="stale-context (root cause)",
   note="TTL decay, hash-chained provenance, poison quarantine, canonical-answer API."),
 # SENTINEL-GW: ingress API gateway for agents (confused-deputy fix)
 "SENTINEL-GW": dict(pain=8, scarcity=8, hire=8, feas=8,
   maps="reliability+observability+governance",
   note="Identity-per-agent at the edge, scoped tokens never in context, CORS/rate-limit/audit. Fixes confused-deputy."),
 # TANGENT: deterministic guardrail compiler
 "TANGENT": dict(pain=8, scarcity=9, hire=8, feas=7,
   maps="reliability",
   note="Turns natural-language guardrails into a fail-closed policy DSL compiled to a sidecar. Few do this explicitly."),
}
scored={}
for k,v in cands.items():
    scored[k]=round(sum(v[p]*W[p] for p in W),2)
ranked=sorted(scored.items(),key=lambda x:-x[1])
print(f"{'PRODUCT':13}{'SCORE':6} MAPS                        NOTE")
for k,s in ranked:
    v=cands[k]
    print(f"{k:13}{s:6} {v['maps']:27} {v['note'][:60]}")
print("\nBUILD SET (>=8.4):",[k for k,s in ranked if s>=8.4])
print("DROP (spec-only / <8.4):",[k for k,s in ranked if s<8.4])
