"""Rate the trio against REAL general remote-startup JD requirements."""

DIMS = [
    "llm_prod_evidence",     # orchestration, evals, prompt/model engineering
    "reliability_failures",  # failure modes, retries, idempotency, on-call
    "security_isolation",    # per-firm isolation, audit, secrets
    "backend_fundamentals",  # API design, async, data modeling
    "multitenant_saas",      # row-level security style thinking
    "observability",         # monitoring, tracing, dashboards
    "language_stack_match",  # TS/Node + Python dual expectation
    "integration_surface",   # OAuth, webhooks, rate limits, MCP
    "deployability",         # Docker/AWS/IaC readiness
    "testing_ci_culture",
    "differentiation",       # vs typical applicant portfolio
    "keyword_scan_survival", # recruiter/ATS 6-second pass
]

P = {
 "agent-sentinel": dict(
    llm_prod_evidence=5, reliability_failures=5, security_isolation=5,
    backend_fundamentals=2, multitenant_saas=4, observability=2,
    language_stack_match=2, integration_surface=2, deployability=2,
    testing_ci_culture=5, differentiation=5, keyword_scan_survival=3),
 "token-governor": dict(
    llm_prod_evidence=5, reliability_failures=5, security_isolation=4,
    backend_fundamentals=2, multitenant_saas=4, observability=3,
    language_stack_match=2, integration_surface=2, deployability=2,
    testing_ci_culture=5, differentiation=5, keyword_scan_survival=3),
 "run-replay": dict(
    llm_prod_evidence=4, reliability_failures=4, security_isolation=5,
    backend_fundamentals=2, multitenant_saas=2, observability=4,
    language_stack_match=2, integration_surface=1, deployability=2,
    testing_ci_culture=4, differentiation=5, keyword_scan_survival=3),
}

# what the three sampled JDs weight (rough share of their requirement lists)
W = dict(
    llm_prod_evidence=1.0, reliability_failures=0.9, security_isolation=0.8,
    backend_fundamentals=0.9, multitenant_saas=0.7, observability=0.6,
    language_stack_match=1.0, integration_surface=0.7, deployability=0.7,
    testing_ci_culture=0.6, differentiation=0.5, keyword_scan_survival=0.8,
)

print(f"{'dimension':24s} {'sentinel':>9s} {'governor':>9s} {'run-replay':>10s}  (jd-weight)")
rows = []
for d in DIMS:
    s = [P[p][d] for p in P]
    rows.append((d, s))
    print(f"{d:24s} {s[0]:>9d} {s[1]:>9d} {s[2]:>10d}   x{W[d]}")

print("\n=== weighted totals (max 60) ===")
for i, p in enumerate(P):
    tot = sum(P[p][d] * W[d] for d in DIMS)
    print(f"{p:16s} {tot:5.1f}/60  ({tot/60*100:.0f}% of JD-weighted max)")

combo = {d: max(P[p][d] for p in P) for d in DIMS}
tot = sum(combo[d] * W[d] for d in DIMS)
print(f"{'COMBINED TRIO':16s} {tot:5.1f}/60  ({tot/60*100:.0f}%)")

print("\n=== weakest links across trio (fix-first list) ===")
weak = sorted(DIMS, key=lambda d: sum(P[p][d] for p in P))[:4]
for d in weak:
    print(f"  {d}: {[P[p][d] for p in P]}")
