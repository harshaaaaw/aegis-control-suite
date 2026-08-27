# Break out of the security/audit lane. Cover UNIVERSAL enterprise functions:
# revenue, cost, speed-to-market, people/ops, product quality. AI does real work.
W = dict(biz=0.30, exec=0.24, aiwork=0.20, scale=0.16, kw=0.10)

ideas = {
 "REVENUEIQ — AI Deal & Pipeline Engine": dict(
   biz=10, exec=10, aiwork=8, scale=9, kw=8,
   what="Not a dashboard. It reads every email, call, and CRM note, scores deal risk in real time, "
        "drafts the next-best-action, and warns before a quarter slips. Owns: 'the forecast is real.'",
   buyer="CRO / sales ops",
   engines="ragforge (grounding on CRM/docs) + evalforge (draft quality) + sentinel (PII guard)"),
 "SUPPLYFLOW — AI Supply & Inventory Brain": dict(
   biz=10, exec=9, aiwork=9, scale=9, kw=8,
   what="Forecasts demand across SKUs, auto-flags stockout/overstock, recommends reorders with "
        "cost tradeoffs. Owns: 'we stop bleeding cash on inventory and stockouts.'",
   buyer="COO / supply chain",
   engines="time-series (Arima/Prophet) + anomaly (Isolation Forest) + bandits for reorder"),
 "TALENTSCAN — AI Hiring & Talent Engine": dict(
   biz=9, exec=9, aiwork=8, scale=8, kw=7,
   what="Screens and ranks candidates against the role's real signal, removes bias drift, drafts "
        "structured interview plans. Owns: 'we hire faster and fairer.'",
   buyer="CHRO / recruiting",
   engines="ragforge (JD/resume grounding) + evalforge (ranking eval) + sentinel (fairness guard)"),
 "PRODUCTECHO — AI Customer Signal Engine": dict(
   biz=9, exec=9, aiwork=9, scale=9, kw=7,
   what="Ingests reviews, tickets, calls, social; clusters recurring pain; routes to product/eng "
        "with evidence. Owns: 'we know what customers hate before churn.'",
   buyer="CPO / product",
   engines="NLU (NER/sentiment/topic) + ragforge + anomaly"),
 "MARKETGEN — AI Go-To-Market Engine": dict(
   biz=9, exec=9, aiwork=9, scale=8, kw=7,
   what="Generates and A/B-tests campaigns, landing copy, segments audiences by behavior, measures "
        "lift with causal methods. Owns: 'marketing spend is measurable and improving.'",
   buyer="CMO / growth",
   engines="generation + causal inference (DiD/PSM) + experiment (CUPED/SRM) + bandits"),
 "OPSCOPILOT — AI Ops & Ticketing Engine": dict(
   biz=8, exec=8, aiwork=8, scale=9, kw=8,
   what="Triages internal tickets, roots cause, drafts fixes, learns from resolutions. "
        "Owns: 'internal ops MTTR drops.'",
   buyer="Head of Ops / IT",
   engines="ragforge + evalforge + run-replay (resolution replay)"),
 "CODEWEAVER — AI Engineering Velocity Engine": dict(
   biz=8, exec=8, aiwork=9, scale=9, kw=9,
   what="Reviews PRs for risk, suggests fixes, maps debt, predicts delivery dates from velocity. "
        "Owns: 'we ship faster with fewer escapes.'",
   buyer="VP Eng",
   engines="ragforge (code grounding) + evalforge (review quality) + sentinel-middleware"),
 "FINANCECLOSE — AI Finance & Close Engine": dict(
   biz=10, exec=10, aiwork=8, scale=9, kw=7,
   what="Reconciles accounts, flags anomalies in ledgers, drafts journal entries with citations, "
        "shortens close. Owns: 'month-end close is faster and cleaner.'",
   buyer="CFO / controller",
   engines="ragforge (policy grounding) + evalforge + anomaly (Isolation Forest)"),
}
scored={k:round(sum(v[p]*W[p] for p in W),2) for k,v in ideas.items()}
ranked=sorted(scored.items(),key=lambda x:-x[1])
print(f"{'PRODUCT':32}{'SCORE':6} BUYER / WHAT IT OWNS")
for k,s in ranked:
    v=ideas[k]
    print(f"{k:32}{s:6} {v['buyer']:18} {v['what'][:44]}")
print("\nTOP BUILD SET (>=8.6):",[k for k,s in ranked if s>=8.6])
print("SPEC-ONLY (<8.6):",[k for k,s in ranked if s<8.6])
print("\n--- engines per top item (reuse story) ---")
for k,s in ranked:
    if s>=8.6:
        print(f"{k} -> {ideas[k]['engines']}")
