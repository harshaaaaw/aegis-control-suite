# New Bucket — Built From The Research (Aug 2026)

## Method
- 496 keywords in 13 clusters. KW match = sum(cluster size x weight) / 496, where core cluster = 1.0, support = 0.8. (So every idea below carries every cluster; differences are only weight.)
- Uniqueness re-scored against the second research sweep: US/UK/EU/DE/JP/CN/IN/IL/KR startups PLUS the newest OSS/product signals (silent model-swap OSS, agent on-call SaaS, synthetic-user SaaS, prompt-regression CI).
- Composite = (KW% as 0-10 + Uniqueness + Individuality) / 3.
- Verdicts are honest: OPEN WEDGE (nobody owns it), WEDGE (one side open), CROWDED (narrow only), AVOID (dominated).

## What the second research sweep proved
| Fragment | Who owns it | Left open |
|---|---|---|
| Silent model-swap detection | OSS only: gpt-drift, Rift, Codeform, llm-provider-audit. No enterprise product. | SWAPWATCH |
| Agent on-call / incident response | TAKEN: Trefur, Kelet, Relvy, TuringPulse | nothing |
| Synthetic-user stress testing | TAKEN: Humanly, UserPersona.ai, UserTrace, Gen.QA | nothing |
| Prompt regression CI | TAKEN as feature: promptfoo GitHub Action, LangSmith; OpenAI acquiring promptfoo | nothing |

The decisive insight: every piece of the "agent reliability" story exists as a **point tool**, but nobody **composes them into one ship/no-ship gate with a certificate**. That is AGENTGATE.

## Cluster sizes (sum = 496)
sde 119, ml 76, infra 57, llm 52, data 47, backend 41, store 35, stats 34, sec 14, cv 12, viz 9

## Ranked table
| # | Product | KW match | Uniq | Indiv | Comp | Verdict |
|---|---|---|---|---|---|---|
| 1 | AGENTGATE — Pre-production certification gate | 460/496 (92.7%) | 8.5 | 9.0 | **8.92** | OPEN WEDGE |
| 2 | PROCUREIQ — AI vendor & contract intelligence | 434/496 (87.4%) | 8.5 | 8.5 | **8.46** | REFRAMED WEDGE |
| 3 | TWINTRUTH — Digital twin fidelity & ROI validator | 440/496 (88.7%) | 7.6 | 8.5 | **8.28** | WEDGE |
| 4 | SWAPWATCH — Provider-truth SLA & silent-swap watchdog | 427/496 (86.0%) | 8.0 | 7.5 | **8.03** | EARLY WEDGE |
| 5 | SIMFACTORY — RL environments & eval data factory | 439/496 (88.5%) | 7.2 | 8.0 | **7.90** | WEDGE |
| 6 | CAUSALA — Warehouse-native causal decision engine | 435/496 (87.7%) | 7.0 | 8.5 | **7.74** | EARLY WEDGE |
| 7 | KNOWPERMIT — Permissioned institutional memory | 435/496 (87.6%) | 6.5 | 8.0 | **7.37** | CROWDED (narrow) |
| 8 | MATTERLABS — Closed-loop lab orchestrator | 431/496 (86.9%) | 7.0 | 7.5 | **7.13** | PARTIAL GAP |
| 9 | PROOFDESK — AI ROI attestation | 432/496 (87.1%) | 6.2 | 7.5 | **6.94** | WEDGE |
| 10 | BEHAVCORE — Transaction behavior API | 437/496 (88.0%) | 6.0 | 7.5 | **6.83** | THIN |
| 11 | CLAIMEXEC — Insurance claims execution | 447/496 (90.1%) | 5.5 | 7.0 | **6.79** | CROWDED closing |
| 12 | COORDINA — Self-hosted coordination workers | 432/496 (87.1%) | 5.5 | 7.5 | **6.66** | Validated, incumbent |
| 13 | CLIMATESIM — Physical climate risk | 440/496 (88.7%) | 5.0 | 7.5 | **6.59** | INCUMBENT-HELD |
| 14 | ONTOBASE — Mid-market ontology layer | 432/496 (87.1%) | 5.0 | 7.0 | **6.40** | CONTESTED |
| 15 | GREENLEDGER — ESG reporting | 432/496 (87.1%) | 5.0 | 7.0 | **6.37** | CROWDED |
| 16 | SOVEREIGNSTACK — Certified on-prem agent stack | 430/496 (86.6%) | 6.0 | 6.5 | **6.37** | REGIONAL GAP |

## Details

### 1. AGENTGATE — Pre-Production Certification Gate (KW 92.7% | U 8.5 | I 9.0 | C 8.92)
**Objective.** One gate every enterprise agent must pass before it touches a customer: integration-contract tests, sandbox replays, eval thresholds, and governance checks. Output is a signed certificate ("this agent is cleared to ship, version X, passed suites A/B/C"). Nobody owns the composed gate: Gartner says >40% of agentic projects die by 2027 on integration + governance failures, and Korea's $34M NC AI mandate is literally a production testbed for this exact gap.
**Why it wins vs fragments.** Silent-swap OSS (gpt-drift/Rift), agent on-call (Trefur/Kelet), synthetic users (Humanly), and prompt CI (promptfoo) each cover ONE slice. AGENTGATE is the conductor: it calls each, then decides ship/no-ship and issues the cert. Start from your repos: run-replay (sandbox replays), evalforge (eval thresholds), agent-sentinel (policy).
**Keywords covered.** All 13 clusters (core: llm, sde, backend, infra, data; support: the rest).
**Verdict. OPEN WEDGE — highest keyword match and highest individuality in the bucket.**

### 2. PROCUREIQ — AI Vendor & Contract Intelligence (KW 87.4% | U 8.5 | I 8.5 | C 8.46)
**Objective.** Reads your AI vendor contracts, flags repricing / credit-redefinition traps, benchmarks your rates vs peers, and drafts renewal negotiation positions. Owns: "we never get surprise-billed again."
**Research.** NPI: AI spend +108% YoY, 85% of teams miss their forecast, contracts renegotiated yearly. Runtime token-FinOps is TAKEN (TokenJam, Behest, TokenAtlas, Finout) — the CONTRACT/PROCUREMENT side is still consultants with spreadsheets. That is the open lane.
**Keywords.** core: llm, data, store, backend, viz; support: sde, infra, ml, stats, sec, cv.

### 3. TWINTRUTH — Digital Twin Fidelity & ROI Validator (KW 88.7% | U 7.6 | I 8.5 | C 8.28)
**Objective.** Continuously measures twin-vs-reality drift, certifies twin outputs, and models the business case BEFORE a twin build. Owns: "twins stay true and prove their worth."
**Research.** Model drift is the #1 twin failure mode; ROI prediction is buyers' top blocker. Fragmented incumbents (STAMM OSS soft-sensors, GameDriver game-engine validation, LTTS consulting twins) but no cross-industry productized validator.
**Keywords.** core: data, store, ml, infra; support: backend, sde, llm, stats, viz, cv, sec.

### 4. SWAPWATCH — Provider-Truth SLA & Silent-Swap Watchdog (KW 86.0% | U 8.0 | I 7.5 | C 8.03)
**Objective.** Watches your LLM providers for silent model swaps, quantization, RLHF drift, and SLA cheating behind a "stable" alias. Pays you back the gap when the model you paid for is not the model you got. CFO + CISO buy-in.
**Research.** This is the newest open seat: gpt-drift, Rift, Codeform, llm-provider-audit prove the NEED and the METHOD, but they are OSS/research, not an enterprise product with SLA, billing reconciliation, and multi-provider coverage. The product layer is empty.
### 5. SIMFACTORY — RL Environments & Eval Data Factory (KW 88.5% | U 7.2 | I 8.0 | C 7.90)
**Objective.** Turns your company's real workflows into RL environments, golden traces, and eval suites so you can train and certify your own agents without frontier-lab dependency. Owns: "our agents are trained on OUR work."
**Research.** Prime Intellect raised $130M @ $1B (hosted, frontier-focused) proving demand; standalone synthetic data consolidated (Gretel→NVIDIA, YData→KPMG, MOSTLY AI→Syntho). Self-hosted enterprise task-environment factory for fine-tuning YOUR OWN business agents stays open.

### 6. CAUSALA — Warehouse-Native Causal Decision Engine (KW 87.7% | U 7.0 | I 8.5 | C 7.74)
**Objective.** Runs causal analysis inside Snowflake/BigQuery: which lever actually moved revenue, per segment, with confidence bounds. Owns: "decisions cite causes, not correlations."
**Research.** causaLens ($51M) pivoted to digital workers; RootCause.ai targets giant enterprises; Argenta is a 0-star solo OSS repo. Mid-market warehouse-native causal ML (HTE/CATE/DAG) is thin.

### 7. KNOWPERMIT — Permissioned Institutional Memory (KW 87.6% | U 6.5 | I 8.0 | C 7.37)
**Objective.** One governed memory graph scoped by role: engineers, agents, and new hires each retrieve exactly what they are entitled to, with provenance. Owns: "knowledge outlives the people who hold it."
**Research.** CROWDED at the API layer: Mem0 ($24.5M, 55k stars, AWS Agent SDK exclusive), Letta ($10M), Zep/Graphiti (20k stars), Supermemory, Oracle Agent Memory, Modus. Only a narrow permission-scoped wedge survives (Glean-adjacent but memory-not-search).

### 8. MATTERLABS — Closed-Loop Lab Orchestrator (KW 86.9% | U 7.0 | I 7.5 | C 7.13)
**Objective.** Orchestrates propose-execute-verify loops across lab instruments and sims, with a drift-corrected knowledge base. Owns: "1000 experiments a day, every result reusable."
### 9. PROOFDESK — AI ROI Attestation (KW 87.1% | U 6.2 | I 7.5 | C 6.94)
**Objective.** Instruments every AI initiative's declared outcome vs measured cost/value and produces auditor-ready ROI attestations. Owns: "every AI dollar can defend itself to the board."
**Research.** NPI and SpendHound both name AI ROI attribution THE unsolved problem. TokenJam ships a basic declared-value/cost ratio; nobody does auditable, board-ready attestation across the whole portfolio.

### 10. BEHAVCORE — Transaction Behavior API (KW 88.0% | U 6.0 | I 7.5 | C 6.83)
**Objective.** One pretrained behavior backbone served as API: credit, churn, LTV, anomalies for institutions that cannot train their own. Owns: "big-bank intelligence at mid-market price."
**Research.** Giants build in-house (Stripe, Visa TransactionGPT, Nubank NuFormer, Revolut PRAGMA, Plaid); NVIDIA published the recipe. Hosting it for community banks / mid-market fintechs is the only open lane.

### 11. CLAIMEXEC — Insurance Claims Execution (KW 90.1% | U 5.5 | I 7.0 | C 6.79)
**Objective.** Execution orchestration over legacy cores: FNOL intake, triage, leakage flags with human review queues.
**Research.** Guidewire (Qusar), Duck Creek (Agentic AI Platform), NTT DATA all shipped 2026. Everest Group names an "execution gap" but the cores are filling it fast. CROWDED, closing.

### 12. COORDINA — Self-Hosted Coordination Workers (KW 87.1% | U 5.5 | I 7.5 | C 6.66)
**Objective.** Voice/email/doc agents that chase confirmations, fill schedule gaps, reconcile paperwork for companies too small for enterprise incumbents.
**Research.** HappyRobot raised $150M @ $1.2B doing EXACTLY this (150+ enterprise customers). Only the self-hosted/open mid-market lane is open. Validated market, big incumbent.

### 13. CLIMATESIM — Physical Climate Risk (KW 88.7% | U 5.0 | I 7.5 | C 6.59)
**Objective.** Prices flood/heat/storm exposure per asset for disclosure and resilience planning.
**Research.** Established specialist incumbents (RMS/Moody's, Jupiter Intelligence, One Concern). Disclosure demand is real but the science + cat-data moat is deep. INCUMBENT-HELD.

### 14. ONTOBASE — Mid-Market Ontology Layer (KW 87.1% | U 5.0 | I 7.0 | C 6.40)
**Objective.** Maps your systems into a queryable business ontology so AI answers carry business meaning, at 1/10 Palantir's cost.
**Research.** Palantir defined it; Mobigen (Korea) runs "K-Palantir"; Modus does context warehousing. CONTESTED from multiple directions.

### 15. GREENLEDGER — ESG Reporting (KW 87.1% | U 5.0 | I 7.0 | C 6.37)
**Objective.** Carbon accounting + assurance-ready disclosure drafting wired into ERP data.
**Research.** SAP Sustainability Control Tower ships AI drafting; Watershed/Persefoni/Workday entrenched. CROWDED.

### 16. SOVEREIGNSTACK — Certified On-Prem Agent Stack (KW 86.6% | U 6.0 | I 6.5 | C 6.37)
**Objective.** GDPR/AI-Act-ready, on-prem agent runtime + eval + audit bundle for regulated mid-caps without US clouds.
**Research.** Aleph Alpha (now Cohere), Sarvam (India $1.5B), Sakana (Japan) own the MODEL layer. A certified open agent-stack (models optional) for EU/Asia regulated mid-market is a real but services-heavy gap.

## Honesty log vs prior buckets
- MEMORYVAULT 9.3 -> KNOWPERMIT 6.5: agent memory is now a funded category (Mem0, Letta, Zep, Modus, Oracle).
- SPENDCAP 9.2 -> PROCUREIQ 8.5: runtime token-FinOps taken (TokenJam, Behest, TokenAtlas, Finout); procurement side is consultant-only.
- SYNTHETICA 8.5 -> folded into SIMFACTORY 7.2: synthetic data consolidated (Gretel->NVIDIA, YData->KPMG, MOSTLY AI->Syntho).
- CAUSALA 8.8 -> 7.0: causaLens and RootCause.ai exist.
- NEW THIS SWEEP: SWAPWATCH (8.0) — silent model-swap is proven by OSS but ungated as a product. AGENTGATE stays #1 because it COMPOSES the fragments (silent-swap OSS + agent on-call SaaS + synthetic-user SaaS + prompt CI) into the one missing thing: the ship/no-ship gate.
- DROPPED: HEALTHADMIN (Hippocratic/EliseAI/Tennr dominate), PROPTECHIQ (EliseAI), standalone ESG/climate kept below the line.

## Build recommendation
AGENTGATE first. It has the highest keyword match (92.7%), highest individuality (9.0), sits on an OPEN WEDGE, and reuses your existing engines (run-replay, evalforge, agent-sentinel) so a real first version is buildable this week. SWAPWATCH is the cheapest to prove next because the OSS method (gpt-drift/Rift) already hands you the detection core.
