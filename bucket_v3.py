from clusters import cluster_of, KEYWORDS

clusters = {}
for kw in KEYWORDS:
    clusters.setdefault(cluster_of(kw), []).append(kw)
CLSIZE = {c: len(v) for c, v in clusters.items()}
assert sum(CLSIZE.values()) == 496, sum(CLSIZE.values())

# NEW BUCKET v3 - research-verified Aug 2026.
# Evidence baked into uniqueness scores. Each: (name, weights, uniq, indv, evidence, objective)
ideas = [
 ("AGENTGATE — Agent Certification Gate",
   dict(core=["llm","sde","backend","infra","data"], support=["ml","store","stats","sec"], periph=["cv","viz"]),
   "8.8",
   "9.0",
   "Point tools all exist (Arize obs, promptfoo evals+GH action, Humanly/UserTrace synthetic users, Rift/gpt-drift drift) but NOBODY composes them into the ship/no-ship GATE + certificate. Gartner >40% agent projects canceled by 2027; Korea funded a $34M state testbed for this exact gap.",
   "CI/CD for agents: integration-contract tests + sandbox replays + eval thresholds + governance checks must PASS before an agent ships. Owns: 'no untested agent reaches customers.'"),

 ("SWAPWATCH — Model Identity & Silent-Swap Sentinel",
   dict(core=["llm","infra","backend","data"], support=["ml","stats","sde","store","sec"], periph=["cv","viz"]),
   "8.2",
   "8.8",
   "OSS probes exist (gpt-drift, Rift Observatory, Codeform canary, llm-provider-audit) but all are dev CLIs; no enterprise product with fleet dashboards, alerting, procurement-grade $/correct reports. Providers swap models behind stable aliases without notice - every buyer exposed.",
   "Continuously fingerprints every model endpoint you pay for; alerts when the thing behind the alias changes; produces before/after behavior and cost evidence for renegotiation. Owns: 'we always know what we are actually buying.'"),

 ("PROCUREIQ — AI Vendor Contract Intelligence",
   dict(core=["llm","data","store","backend","viz"], support=["sde","infra","ml","stats","sec"], periph=["cv"]),
   "8.5",
   "8.5",
   "NPI/SpendHound: AI spend +108% YoY, 85% miss forecasts, contracts renegotiated yearly. Runtime FinOps taken (TokenJam, Behest); CONTRACT side is consultant-only turf, no product found.",
   "Reads AI vendor contracts, flags repricing/credit-redefinition traps, benchmarks rates vs peers, drafts negotiation positions pre-renewal. Owns: 'never surprise-billed again.'"),

 ("TWINTRUTH — Digital Twin Fidelity & ROI Validator",
   dict(core=["data","store","ml","infra"], support=["backend","sde","llm","stats","viz"], periph=["cv","sec"]),
   "7.6",
   "8.5",
   "Fragmented niche OSS (STAMM soft-sensors, GameDriver game-engine twins); consulting-built twins (LTTS). No cross-industry productized drift validator + pre-build ROI modeler. Research: drift is #1 twin failure; ROI prediction is buyers' top blocker.",
   "Measures twin-vs-reality drift continuously, certifies twin outputs, models business case BEFORE build. Owns: 'twins stay true and prove their worth.'"),

 ("CAUSALA — Warehouse-Native Causal Decision Engine",
   dict(core=["stats","data","store","ml"], support=["backend","infra","sde","llm","viz"], periph=["cv","sec"]),
   "7.0",
   "8.5",
   "causaLens ($51M) pivoted to digital workers; RootCause.ai serves giant enterprises only; Argenta is a solo repo. Mid-market warehouse-native causal ML thin.",
   "Causal analysis inside Snowflake/BigQuery: which lever actually moved revenue, per segment, with confidence bounds. Owns: 'decisions cite causes, not correlations.'"),

 ("SIMFACTORY — Enterprise RL Environments & Eval Factory",
   dict(core=["llm","ml","data","store"], support=["infra","backend","sde","cv","stats"], periph=["sec","viz"]),
   "7.2",
   "8.0",
   "Prime Intellect ($130M@$1B) proves demand for agent-training infra but is hosted/frontier-focused. Synthetic-data pure plays consolidated away. Self-hosted factory turning YOUR workflows into training environments: open.",
   "Converts real company workflows into RL environments, golden traces, eval suites to train and certify own agents. Owns: 'our agents trained on OUR work.'"),

 ("PROOFDESK — AI Program Outcome Attestation",
   dict(core=["llm","data","store","viz","stats"], support=["backend","infra","sde","ml","sec"], periph=["cv"]),
   "6.4",
   "7.6",
   "NPI+SpendHound both call AI ROI attribution THE unsolved problem. TokenJam has a basic declared-value/cost ratio; no auditable board-ready attestation across whole AI portfolio.",
   "Instruments declared outcome vs measured cost/value per AI initiative; auditor-ready ROI attestations. Owns: 'every AI dollar defends itself to the board.'"),

 ("KNOWPERMIT — Permissioned Institutional Memory",
   dict(core=["llm","data","store","backend","sec"], support=["infra","sde","ml","stats"], periph=["cv","viz"]),
   "6.5",
   "8.0",
   "API layer crowded (Mem0 55k stars/AWS exclusive, Letta, Zep, Modus). Surviving wedge: role-scoped memory serving HUMANS + agents with permission-aware retrieval.",
   "One governed memory graph scoped by role: engineers, agents, new hires each retrieve exactly what they may see, with provenance. Owns: 'knowledge outlives its holders.'"),
]

rows = []
for name, d, u, ind, ev, obj in ideas:
    m = 0.0
    for c in CLSIZE:
        if c in d["core"]: m += CLSIZE[c]
        elif c in d["support"]: m += CLSIZE[c]*0.8
    pct = m/496*100
    comp = (pct/10 + float(u) + float(ind))/3
    rows.append((name, m, pct, float(u), float(ind), comp, ev, obj))
rows.sort(key=lambda r: -r[5])

print("NEW BUCKET v3 (research-verified, sorted by composite)\n")
print(f"{'#':>2} {'PRODUCT':52} {'KWMAT':>11} {'U':>4} {'I':>4} {'COMP':>5}")
for i,(n,m,p,u,ind,c,ev,obj) in enumerate(rows,1):
    print(f"{i:>2} {n[:52]:52} {m:>4.0f}/{496} {u:>4.1f} {ind:>4.1f} {c:>5.2f}")

md = ["# New Bucket v3 — Research-Verified Ideas (Aug 2026)\n"]
md.append("Scores use the global startup/OSS collision check + fresh point-tool sweep.\n"
          "KW match = sum(cluster size x weight)/496 over 13 clusters (core 1.0, support 0.8).\n"
          "Uniqueness = post-collision market novelty. Individuality = own data type/engine/buyer/metric.\n"
          "Composite = (KW% as 0-10 + Uniqueness + Individuality)/3.\n")
md.append("| # | Product | KW match | Uniq | Indiv | Composite |\n|---|---|---|---|---|---|\n")
for i,(n,m,p,u,ind,c,ev,obj) in enumerate(rows,1):
    short = n.split(" — ")
    md.append(f"| {i} | **{short[0]}** — {short[1] if len(short)>1 else ''} | {m:.0f}/496 ({p:.1f}%) | {u} | {ind} | {c:.2f} |\n")
md.append("\n## Detail\n\n")
for i,(n,m,p,u,ind,c,ev,obj) in enumerate(rows,1):
    md.append(f"### {i}. {n}\n- KW {m:.0f}/496 ({p:.1f}%) | Uniqueness {u} | Individuality {ind} | Composite {c:.2f}\n- **Objective:** {obj}\n- **Evidence:** {ev}\n\n")

open("BUCKET_V3.md","w",encoding="utf-8").write("".join(md))
print("WROTE BUCKET_V3.md")
