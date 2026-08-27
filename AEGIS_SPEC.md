# AEGIS SPEC v2 - JD-hardened (every researched JD line bound to an artifact)

## v3 KEYWORD/Tech-stack alignment layer (added after role-family math)

Computed coverage (aegis_role_coverage.py): AI-Eng 97.5% / ML 38.3% / DS 25.9% / DA 27.5%.
Fix = AEGIS INSIGHTS analytics layer over the evidence lake + exact keyword
mapping below. Target: README keywords literally match JD vocabulary.

### AEGIS INSIGHTS (new component - unlocks DS/DA coverage)
- SQL views on the event warehouse: violations/day, $ per workflow, eval pass-rate trends
- stats module: two-proportion z-tests + bootstrap CIs for A/B prompts
  ("did prompt v2 reduce violations vs v1?" -> p-value, effect size)
- pandas/numpy analysis notebooks committed as examples/
- Looker/Tableau-ready CSV/Parquet exports + dbt-style models folder
- Grafana JSON dashboards (ops) AND BI exports (business) from same lake

### Exact keyword -> where it appears (README/scm searchability)
Python, FastAPI, async, OpenAPI/Swagger, PostgreSQL, row-level security,
SQL, dbt-style models, pandas, numpy, scipy (stats tests), Docker, docker-compose,
AWS ECS/Fargate, Terraform, GitHub Actions CI, OpenTelemetry, Grafana,
React, Next.js, TypeScript, Node.js, Redis (budget cache tier),
Kafka-compatible event ingest, MCP server, OAuth2/OIDC/JWT, webhooks,
LangChain/LangGraph adapters, RAG (ragforge), prompt-injection defense,
guardrails, LLM evaluation, golden sets, recall@k, faithfulness, drift detection,
model routing/cascade, token budgeting, FinOps/$-per-outcome, circuit breakers,
idempotency keys, rate limiting, multi-tenant, SLO/error budgets,
EU AI Act/SOC2 evidence export, hash-chained audit logs, replay/time-travel debugging,
autonomy ladder/progressive authorization, human-in-the-loop approvals.

### MEASURED from real scraped corpus (31 JDs, HN Aug 2026 thread 49156683)
corpus: jd_corpus/corpus.md - AI-eng 14, ML 8, DS 8, DA 1 (full texts kept)
keyword hit-rates per family (AIeng/ML/DS/DA):
python 44/80/60/100 - typescript 33/20/30/0 - sql 17/40/40/100 -
postgres 17/40/30/0 - aws 22/40/20/0 - docker 11/40/10/0 - k8s 11/60/10/0 -
llm 33/40/30/0 - openai 11/40/0/0 - langchain 11/40/0/0 - PYTORCH 6/100/20/0 -
tensorflow 0/40/0/0 - agents 28/0/10/0 - evals 28/20/0/0 - spark 6/40/0/0 -
kafka 0/40/10/0 - snowflake 0/40/10/0 - redis 0/40/10/0 - scala 0/40/20/0 -
pipeline 22/40/30/0
CONFIRMS: AEGIS targets AI-eng (agents+evals+llm+ts present only there).
ML-family demands training stack (pytorch/tf/scala/kafka/snowflake) we
honestly exclude. DS family: sql+pandas+stats confirmed core.


- AI Engineer: "97.5% of the surveyed AI-engineer stack, every keyword above has a runnable artifact behind it."
- Data Scientist: "AEGIS Insights = production telemetry + real A/B statistics; notebooks included."
- Data Analyst: "Warehouse views and BI-ready exports over agent events; dashboards in one command."
- ML Engineer (honest): "operates/scores/routes models; training itself is out of scope by design."

### v4 build delta (Insights layer)
1. Postgres views + example notebooks (pandas/numpy/scipy)
2. stats.py: proportion z-test + bootstrap CI helpers w/ tests
3. BI export endpoints (CSV/Parquet) + dbt-style models dir
4. Second dashboard tab (Insights) in React app

## Rule applied

Every line from the researched JD corpus (Matterhaul founding JD, 4 live
postings, 420-post HN frequencies, 425-JD Dexity study, KORE1 survey,
2026 interview-loop reports) maps to ONE NAMED ARTIFACT in the repo.
No JD line left unclaimed. No feature without a JD backer.

## JD line -> artifact bindings

### Matterhaul founding-AI JD ($200-260K) - 9/9 already mapped, hardened:
- plan/execute loops + checkpointing      -> meshwork engine wired at /v1/runs
- deterministic replays                   -> run-replay chains, /v1/evidence/{run}/replay
- prompt-injection defense on transcripts -> sentinel lanes on every ingest
- tool authorization                      -> policy sidecar w/ per-tool scopes
- token-level tracing                     -> governor ledger spans (OTel-exported)
- cost per workflow                       -> governor $/outcome rollups per run_id
- latency budgets per step                -> sentinel enforced budgets, breach=block
- drift detection                         -> evalforge nightly suites per agent
- model routing across tiers              -> governor cascade w/ caller verifier
- eval harness tied to CI w/ golden sets  -> evalforge gates block promotion PRs

### Integration surface (was our weakest score: 2/5) - now explicit artifacts:
- OAuth2/OIDC                             -> agents are FIRST-CLASS IDENTITIES:
                                             each agent gets OIDC client cred;
                                             every call signed; registry verifies.
                                             Mirrors MS Entra Agent ID pattern -
                                             open-source equivalent, nobody ships it
- Webhooks                                -> policy events fan out: violation,
                                             demotion, budget-exhaust, promotion
                                             -> Slack/PagerDuty/webhook subscribers
- MCP                                     -> AEGIS exposes itself AS an MCP server:
                                             tools: register_agent, query_policy,
                                             get_autonomy_level, fetch_evidence.
                                             Agents integrate natively; MCP appears
                                             verbatim in 2 of 4 researched JDs

### Backend fundamentals (was 2/5):
- async API design                        -> FastAPI async throughout, OpenAPI doc
- multi-tenant data model                 -> Postgres w/ ROW LEVEL SECURITY;
                                             schema.sql reviewed like a design doc
- idempotency/retries                     -> settlement ledger idempotency keys
                                             (governor engine heritage)

### Deployability (was 2/5):
- Docker                                  -> compose: control-plane + postgres +
                                             sidecar + 3 demo agents, one command
- AWS/IaC                                 -> terraform module: ECS Fargate + RDS
                                             + ALB; one-command deploy target
- CI                                      -> GH Actions matrix py3.10-3.12 +
                                             node20; evalforge gate in pipeline

### Observability (23 HN mentions, 0.90 weight):
- OTel trace exporter on every engine boundary (spans: sentinel verdict,
  governor charge, meshwork step, replay append)
- Grafana dashboard JSON committed; SLO burn-rate alerts defined

## Interview-question -> demo table (2026 loop patterns)

| They ask | We open |
|---|---|
| "50 docs -> Q&A + recall@5 + faithfulness" | ragforge+evalforge live run printing both numbers |
| "this agent loops forever - fix it" | replay time-travel: pin exact divergence step, show breaker firing |
| "how do you stop prompt injection?" | sentinel live: poisoned page -> BLOCK 121us receipt |
| "how do you control agent spend?" | governor: kill switch mid-storm, ledger shows where money stopped |
| "who approves what an agent may do alone?" | THE ladder demo: L0->L2 earned, violation, instant demotion, receipt |
| "show me production-grade evidence for auditors" | one-click EU-AI-Act/SOC2 packet export |

## Numbers we publish (honesty = senior signal)

- sentinel p50 scan latency (measured, ~10ms budget, fail-closed)
- governor cascade savings multiple (60x when cheap tier verifies)
- evalforge pass-rate deltas blocking real prompt changes
- ladder: days-of-evidence thresholds + violation demotion latency (<1s)
- coverage: this file IS the audit trail of JD claims -> features

## v2 build order (delta over v1)

1. OIDC agent identity + signed calls (registry upgrade)
2. MCP server facade over control plane
3. Webhook event bus (policy events)
4. OTel exporters + Grafana JSON
5. Terraform module + compose polish
6. Voice-loop demo (Phonely-flavored) using all engines
7. Evidence exporter packet format (EU AI Act Art.15 / SOC2 sections)
