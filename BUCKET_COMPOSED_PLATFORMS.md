# Composed Enterprise Platforms (not point tools)

## Why this bucket is different
The previous 16 were single-function products. The research showed the market is fragmenting into point tools (silent-swap OSS, agent on-call SaaS, synthetic-user SaaS, prompt CI). The winning move is the OPPOSITE: fuse several functions into one platform that serves multiple stakeholders (CFO + CISO + CTO + Compliance) at once. That is harder to copy and reads as enterprise, not a feature.

## Scoring
- KW match = sum(cluster size x weight)/496. Platforms touch all 13 clusters -> ~100%.
- Uniqueness = how open the combined seat is vs funded players.
- Individuality = how much it is YOUR story (RADAR-scale doc-intel + agent-reliability engines).
- Composite also rewards functional breadth (fb = # modules fused) and stakeholder breadth (stk = # POVs served).
- Each platform FUSES 4-5 former point-ideas and SERVES 3-4 buyer POVs.

## Ranked
| # | Platform | KW | Uniq | Indiv | fb | stk | Comp |
|---|---|---|---|---|---|---|---|
| 1 | AGENTTRUST PLANE | 100% | 8.5 | 9.2 | 5 | 4 | **9.22** |
| 2 | AIFINANCE COMMAND | 99.5% | 8.3 | 8.8 | 4 | 4 | **8.90** |
| 3 | SOVEREIGN AI PLANE | 100% | 8.2 | 8.4 | 4 | 4 | **8.81** |
| 4 | INDUSTRIAL INTELLIGENCE PLANE | 100% | 8.0 | 8.5 | 4 | 3 | 8.52 |
| 5 | DECISION INTELLIGENCE CORE | 100% | 7.8 | 8.6 | 4 | 3 | 8.48 |
| 6 | REVENUE INTELLIGENCE PLANE | 100% | 7.5 | 8.3 | 4 | 3 | 8.33 |
| 7 | RESEARCH ACCELERATOR PLANE | 100% | 7.6 | 8.0 | 4 | 3 | 8.30 |
| 8 | AUTONOMOUS OPS BACKOFFICE | 100% | 7.2 | 8.2 | 4 | 3 | 8.22 |
| 9 | SUPPLY CHAIN AUTONOMY PLANE | 100% | 7.0 | 8.1 | 4 | 3 | 8.14 |
| 10 | CLIMATE & ESG INTELLIGENCE | 100% | 6.5 | 8.0 | 4 | 3 | 7.97 |

---

## 1. AGENTTRUST PLANE (Comp 9.22) — the agent-reliability platform
**Fuses:** AGENTGATE ship-gate + SWAPWATCH prod-swap watch + PROOFDESK ROI attest + KNOWPERMIT governed memory + agent-sentinel policy.
**Serves:** CISO, CFO, CTO, Compliance. (4 POVs, one platform.)
**In simple words.** One control plane for every AI agent a company runs. It tests agents before ship (gate), watches providers for silent swaps in production (swap-watch), proves the ROI of each agent to the CFO (attest), keeps a permissioned memory of what each agent is allowed to know (governed memory), and enforces security policy (sentinel). Instead of buying 4 tools, the CISO, CFO, CTO and compliance officer all log into ONE plane.
**Why stronger than the point versions.** Point tools each solve one chair. AGENTTRUST is the chair, the desk, and the room. A CISO buys it to satisfy audit; the CFO buys it to prove spend; the CTO buys it to stop incidents; compliance buys it for the paper trail. Four budgets, one sale.
**Enterprise architecture.**
```
[CI plugin] -> [Orchestrator (K8s, Helm)]
   -> Gate (replay + eval + policy) -> Cert Store (Postgres, signed)
   -> SwapWatch (probe canary + fingerprint + SLA ledger)
   -> Attest (cost/value ledger -> signed ROI reports)
   -> Governed Memory (Neo4j + ABAC, role-scoped RAG)
   -> OTel/Prometheus/Grafana + Kafka event bus + RBAC/OIDC + Audit (immutable)
   -> Role-based dashboards: CISO view / CFO view / CTO view / Compliance view
```
**Reuses your engines:** run-replay (gate replay), evalforge (eval), agent-sentinel (policy), plus a memory + swap-watch + attest layer. This is the flagship.
**Self-rating:** Arch realism 9/10, Hire-by-looking 8/10 (it IS your positioning: "agent-reliability engineer at RADAR scale").

---

## 2. AIFINANCE COMMAND (Comp 8.90) — AI spend & risk command center
**Fuses:** PROCUREIQ contracts + SWAPWATCH SLA-cost + PROOFDESK ROI + BEHAVCORE risk.
**Serves:** CFO, Procurement, CTO, Risk.
**In simple words.** The finance side of AI. It reads your vendor contracts for traps (PROCUREIQ), watches whether you're getting the model you paid for at the price you agreed (SWAPWATCH cost-SLA), proves each AI initiative's ROI to the board (PROOFDESK), and scores transaction/behavior risk (BEHAVCORE). CFO sees spend + savings, procurement sees negotiation leverage, CTO sees model truth, risk sees exposure. One plane, four money POVs.
**Why stronger.** Turns "AI is a cost we can't control" into one controlled plane with a single source of financial truth. Contested pieces (runtime cost) are avoided; the combined finance-command angle is open.
**Enterprise architecture.**
```
[Contract repo + Billing + Model endpoints] -> [Ingest (Airflow)]
   -> Contract NER + Rate Benchmark (Snowflake cohort)
   -> SwapWatch SLA-cost ledger
   -> ROI Attest engine
   -> Behavior risk models (transformers/GNN, Triton serving)
   -> Postgres + Neo4j + Redis + S3 -> Looker/Power BI -> RBAC + Audit + OTel
```
**Self-rating:** Arch realism 8.5/10, Hire-by-looking 7.5/10 (CFO-facing, shows business fluency).

---

## 3. SOVEREIGN AI PLANE (Comp 8.81) — compliant on-prem AI control plane
**Fuses:** SOVEREIGNSTACK on-prem + AGENTGATE gate + KNOWPERMIT memory + SWAPWATCH swap-watch.
**Serves:** CISO, CTO, Compliance, Public Sector.
**In simple words.** For regulated / government / EU-Act buyers who cannot use US clouds. One on-prem plane that runs agents, gates them before ship, keeps governed memory, and watches for provider swaps, all inside their firewall. CISO gets the audit, CTO gets the runtime, compliance gets the paper trail, public sector gets sovereignty.
**Why stronger.** Model-layer sovereignty is taken (Aleph Alpha, Sarvam, Sakana). The CONTROL-PLANE sovereignty (run + gate + memory + swap-watch, models optional) for regulated mid-caps is the open seat.
**Enterprise architecture.**
```
[On-prem K8s] -> [Agent runtime (LangGraph)] + [Gate (evalforge+replay+sentinel)]
   -> [Governed Memory (Neo4j+ABAC)] + [SwapWatch] -> [Audit (immutable)] -> [RBAC/OIDC] + [Helm deploy] + [OTel]
```
---

## 4. INDUSTRIAL INTELLIGENCE PLANE (Comp 8.52)
**Fuses:** TWINTRUTH twin-truth + CAUSALA causal-decisions + SIMFACTORY sim-data + MATTERLABS lab-loop.
**Serves:** VP Eng/Ops, CDO, R&D Dir.
**In simple words.** The physical-world AI plane. It keeps digital twins honest (TWINTRUTH), decides which lever actually moves plant output (CAUSALA), turns workflows into training/eval data for your own agents (SIMFACTORY), and runs closed-loop lab experiments (MATTERLABS). One plane for the whole industrial AI lifecycle.
**Enterprise architecture.**
```
[IoT edge (Kafka/Flink)] -> [Twin drift detector + Fidelity cert]
   -> [Causal engine (warehouse-native)] -> [Sim/RL env factory] -> [Lab orchestrator (Temporal)]
   -> [TimescaleDB + Neo4j + S3] -> [Grafana/Tableau] + [OTel] + [RBAC] + [Audit]
```
**Self-rating:** Arch realism 8/10, Hire-by-looking 7/10 (strong industrial breadth, niche buyers).

---

## 5. DECISION INTELLIGENCE CORE (Comp 8.48)
**Fuses:** CAUSALA causal + BEHAVCORE behavior + KNOWPERMIT memory + ONTOBASE ontology.
**Serves:** CDO, CTO, Strategy.
**In simple words.** The "why" plane. Causal inference says what caused outcomes, behavior models predict churn/risk, governed memory holds institutional knowledge, ontology makes AI answers business-meaningful. Strategy and CDO use it to make decisions on causes, not dashboards.
**Enterprise architecture.**
```
[Warehouse (Snowflake/BigQuery)] -> [Causal UDFs (DoWhy/PyMC)]
   -> [Behavior models] -> [Governed Memory (Neo4j+ABAC)] -> [Ontology (Neo4j)]
   -> [Streamlit/Looker] + [RBAC] + [OTel] + [Lineage]
```
**Self-rating:** Arch realism 8/10, Hire-by-looking 7/10 (DS-heavy, less agent flash).

---

## 6. REVENUE INTELLIGENCE PLANE (Comp 8.33)
**Fuses:** CAUSALA revenue-drivers + BEHAVCORE churn/LTV + SIMFACTORY revenue-agent eval + PROOFDESK ROI.
**Serves:** CRO, CTO, Growth.
**In simple words.** The money-growth plane. Tells you which action drove revenue (causal), predicts churn/LTV (behavior), tests your revenue agents before ship (sim-factory), and attests the ROI of growth AI to the board (proofdesk). CRO + Growth live here.
**Enterprise architecture.**
```
[Warehouse + CRM + agent traces] -> [Causal revenue model] -> [Behavior scoring]
   -> [Revenue-agent eval (SIMFACTORY)] -> [ROI attest] -> [Looker/Power BI] + [RBAC] + [OTel]
```
**Self-rating:** Arch realism 8/10, Hire-by-looking 7/10 (CRO-facing, clear value).

---

## 7. RESEARCH ACCELERATOR PLANE (Comp 8.30)
**Fuses:** MATTERLABS lab-loop + SIMFACTORY sim-data + KNOWPERMIT memory + CAUSALA causal.
**Serves:** R&D Dir, CDO, CTO.
**In simple words.** The science plane. Runs propose-execute-verify lab loops, turns them into training data, remembers results with provenance, and finds causal structure in experiments. "1000 experiments a day, every result reusable."
**Enterprise architecture.**
```
[Instrument adapters (OPC-UA)] -> [Temporal orchestrator: propose->exec->verify]
   -> [Sim/env factory] -> [Governed KB (Neo4j+vector)] -> [Causal analysis]
   -> [Grafana/Streamlit] + [RBAC] + [OTel] + [Audit]
```
---

## 8. AUTONOMOUS OPS BACKOFFICE (Comp 8.22)
**Fuses:** CLAIMEXEC claims + COORDINA coordination + KNOWPERMIT memory + PROOFDESK ROI.
**Serves:** Ops VP, CFO, COO.
**In simple words.** The back-office automation plane. Handles insurance claims execution, coordinates voice/email/doc chores, remembers process knowledge, and attests the ROI of the automation. One plane for "the office runs itself."
**Enterprise architecture.**
```
[Legacy core APIs + comms channels] -> [Agent orchestrator (Temporal/LangGraph)]
   -> [Claims exec] + [Coordination workers] -> [Governed memory] -> [ROI attest]
   -> [Postgres + pgvector + S3] -> [Dashboards] + [RBAC] + [OTel] + [Audit]
```
**Self-rating:** Arch realism 8/10, Hire-by-looking 6.5/10 (claims crowded, but combo is broader).

---

## 9. SUPPLY CHAIN AUTONOMY PLANE (Comp 8.14)
**Fuses:** COORDINA coordination + TWINTRUTH network-twin + CLAIMEXEC claims + KNOWPERMIT memory.
**Serves:** COO, Ops VP, CFO.
**In simple words.** The logistics plane. Coordinates shipments/confirmations, keeps a live digital twin of the network truth, handles claims, and remembers playbooks. COO runs the network from one pane.
**Enterprise architecture.**
```
[ERP/WMS + carrier APIs] -> [Coordination agents] -> [Network twin (drift-corrected)]
   -> [Claims exec] -> [Governed memory] -> [Dashboards] + [RBAC] + [OTel] + [Audit]
```
**Self-rating:** Arch realism 7.5/10, Hire-by-looking 6.5/10 (logistics niche).

---

## 10. CLIMATE & ESG INTELLIGENCE (Comp 7.97)
**Fuses:** CLIMATESIM risk + GREENLEDGER ESG + CAUSALA causal-exposure + PROOFDESK attest.
**Serves:** CSO, CFO, Compliance.
**In simple words.** The sustainability plane. Prices physical climate risk per asset, automates ESG disclosure, finds causal exposure, and attests to auditors. Lowest uniqueness (incumbents in climate/ESG) but the combined attestation angle adds defensibility.
**Enterprise architecture.**
```
[Asset registry + hazard feeds + ERP] -> [Risk sim] -> [ESG drafter] -> [Causal exposure] -> [Attest]
   -> [Postgres + S3] -> [Tableau] + [RBAC] + [OTel] + [Audit]
```
**Self-rating:** Arch realism 7.5/10, Hire-by-looking 5.5/10 (crowded base, keep as range only).

---

# MULTI-POV SELF-REVIEW: are these platforms stronger than the point list?

**POV 1 — US agent-infra hiring manager.** "NOW this reads like enterprise. AGENTTRUST PLANE is a platform four executives sign off on, not a feature. That is what a staff/principal engineer ships. The point list made him look like a feature-factory; this makes him look like a platform builder. Hire-by-looking 8/10."

**POV 2 — CISO buyer.** "I don't want 5 dashboards. AGENTTRUST gives me gate (audit), swap-watch (supply chain), attest (board), memory (governance) in one plane with one audit trail. That is a purchase I can defend to the board."

**POV 3 — CFO buyer.** "AIFINANCE COMMAND is the one I care about. Contracts + model-truth + ROI + risk in one financial truth. That is budget I approve."

**POV 4 — Staff engineer screening.** "The architecture is still real (K8s, Kafka, OTel, RBAC, warehouse UDFs). Depth still wins, but now the repo is a platform with clear modules, which is easier to whiteboard than 16 disjoint tools."

**POV 5 — Skeptic (me).** "Composing 5 modules sounds like scope creep. Risk: building a shallow platform is worse than a deep point tool. The fix: build AGENTTRUST's 5 modules as one repo with 5 clearly-tested subsystems, each with its own eval. Prove the fusion works, don't just claim it."

**POV 6 — Differentiator.** "AGENTTRUST is still THE one. It fuses RADAR-scale doc-intel discipline + your three agent-reliability engines into one 'agent-trust platform' story. The other 9 are proof you can platformize any domain."

## Synthesis
These are stronger because each is a PLATFORM serving multiple buyer POVs, not a single function. The prior list handed competitors an easy "that's one feature, I'll add it" response. A platform with four executive buyers and one audit trail is a harder sale to copy and a clearer "I build enterprise AI platforms" signal.

But the hiring truth from before still holds: build AGENTTRUST to real depth (5 tested subsystems), keep the other 9 as proof-of-range. The 496-keyword coverage is now 100% per platform, which maximizes ATS命中 (keyword hit) on every repo.

## Self-rating
- Composed strength: 9/10 (multi-function, multi-POV, enterprise-shaped).
- Math honesty: 9/10 (collision-checked).
- Hire-by-looking: 8/10 for AGENTTRUST specifically.
- Next: build AGENTTRUST PLANE locally as one repo with 5 tested modules. Ready on GO.


