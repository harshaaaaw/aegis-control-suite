# FIVE ENTERPRISE PRODUCTS - bucket menu (choose from these)

## P1. MODELFORGE - Enterprise ML Training & Serving Platform
Objective: one platform that takes any model from experiment -> trained ->
quantized -> served -> monitored, with GPU money accounted per team.
Business problem: companies run training jobs on shared GPUs with zero
accounting; models ship unquantized (5x inference cost); silent drift burns
revenue; no lineage from dataset to deployed weights.
Architecture: Ray-cluster job orchestrator (FSDP/DeepSpeed configs),
LoRA/QLoRA/DPO fine-tune pipelines, quantization farm (AWQ/GPTQ/INT8),
Triton+vLLM serving fleet with canary rollouts, model registry with full
lineage, Kafka metrics -> ClickHouse drift/anomaly monitors, eval harness
(ROC-AUC/NDCG/BLEU/ROUGE per task type).
Keywords owned: DeepSpeed, Ray, FlashAttention, FSDP, TP/PP, TensorRT,
ONNX Runtime, Triton, vLLM, TGI, TorchServe, pruning, quantization,
distillation, SFT/RLHF/DPO/PEFT, PyTorch Lightning, HF Transformers/Hub,
CV suite (YOLO/OCR/VLM), ML eval metrics, MLflow-pattern registry.
Engine reuse: evalforge patterns -> model eval gates.
Build size: LARGEST. Honest note: training demos use small open models
(Qwen-0.5B class) on CPU/small GPU - architecture is the point.

## P2. STREAMFORGE - Streaming Lakehouse Data Platform
Objective: trustworthy numbers at scale - ingest everything, validate
everything, trace every number back to its source row.
Business problem: exec dashboards contradict each other; broken pipelines
found by CEO not by alerts; nobody can answer "where did this KPI come from".
Architecture: Kafka+CDC ingestion, medallion lakehouse (bronze/silver/gold)
on Iceberg+Parquet, Spark structured streaming + Flink CEP, dbt transformation
layer with star-schema marts + SCD2, Dagster/Airflow orchestration,
Great-Expectations-style quality gates w/ quarantine + DLQs, column-level
lineage graph, schema registry + evolution rules, anomaly alerting on fresh data.
Keywords owned: Spark, PySpark, Flink, Beam, Iceberg/Delta/Hudi, Parquet/ORC/
Avro, dbt, star/snowflake schema, SCD 1/2/3, data lineage, Airflow/Prefect/
Dagster, Great Expectations/deequ/Soda, Atlas/DataHub-pattern catalog,
schema registry, DLQ, Snowflake/BigQuery patterns (self-hosted ClickHouse).
Engine reuse: replay chains -> pipeline audit trail; sentinel -> PII gates.
Build size: LARGE (simulated 10-source estate runs locally).

## P3. AEGIS - Agent Autonomy Control Plane (designed already)
Objective: control room for company agent fleets - earned freedom, budgets,
tamper-proof receipts, regulator exports.
Business problem: agents touch money/production with no governance; MS sells
it locked; open version missing; EU AI Act bites Aug 2026.
Architecture: FastAPI control plane, OIDC agent identities, policy sidecar
(out-of-process trust boundary), autonomy-ladder state machine, Postgres RLS
multi-tenancy, OTel traces, webhook bus, MCP facade, React dashboard,
compose+terraform deploy.
Keywords owned: agents, multi-agent, function calling, guardrails, evals,
MCP, OAuth2/OIDC/JWT, RBAC/ABAC, multi-tenancy, SLO/error budgets, OTel,
Grafana, circuit breakers, event-driven, RLS, FastAPI, React/Next.js.
Engine reuse: ALL SEVEN existing repos become organs.
Build size: MEDIUM-LARGE (engines done; glue is the work).

## P4. TRUSTPAY - Real-Time Payments & Fraud Decisioning Engine
Objective: settle machine-speed payments with a ledger that cannot lie and
fraud decisions under 100ms, ready for the agentic-commerce wave.
Business problem: instant-payment fraud is exploding exactly when AI agents
start spending (x402 $15M, Visa TAP, AP2); legacy batch fraud systems miss
sub-second attacks; chargeback disputes have no evidence trail.
Architecture: event-sourced double-entry ledger (Kafka, exactly-once),
CQRS read models, Flink CEP rule engine + isolation-forest scoring service,
Redis token-bucket limits, distributed locks + idempotency everywhere,
two-tower embeddings for merchant/device similarity, multi-armed bandits for
rule tuning, gRPC internal + REST/GraphQL external, ABAC permissions,
dispute evidence bundles (hash-chained receipts), multi-region failover design.
Keywords owned: Kafka exactly-once/EOP, RabbitMQ/SQS patterns, event sourcing,
CQRS, idempotency, concurrency control, distributed locking, Redis, ClickHouse
(fraud mart), Elasticsearch (entity search), gRPC/GraphQL/Webhooks,
OAuth2/RBAC/ABAC, token/leaky bucket, bulkheads, chaos engineering,
Isolation Forest, bandits, CLV/churn propensity models.
Engine reuse: governor wallets/breakers, replay dispute receipts, sentinel
scoring lanes.
Build size: LARGE. Fintech-interview goldmine.

## P5. HELIX - Commerce Intelligence & Experimentation Platform
Objective: make an online store measurably richer every week - better search,
better recommendations, honest experiments proving which changes paid.
Business problem: search returns junk (conversion bleed), recommendations are
generic, teams ship changes without knowing if they worked, promos cannibalize.
Architecture: two-tower retrieval + LambdaMART re-ranker, pgvector+OpenSearch
hybrid search, semantic cache, matrix-factorization + contextual-bandit
recommendations, full experimentation service (split engine, CUPED variance
reduction, SRM detection, sequential tests), causal promo analysis (DiD,
synthetic controls), churn/CLV models, Next.js storefront + SSE real-time,
Playwright E2E suite, Streamlit/Plotly analyst workbench.
Keywords owned: two-tower, LambdaMART, learning-to-rank, collaborative
filtering, matrix factorization, bandits, hybrid/semantic search, semantic
caching, A/B/MVT/sequential/CUPED/SRM, DiD/synthetic controls/PSM, ARIMA/
Prophet forecasting, PCA/t-SNE/UMAP, churn/CLV/segmentation, Tableau/Looker-
pattern BI, Next.js/React/SSE, Playwright/Jest/k6 load tests.
Engine reuse: ragforge retrieval core, evalforge gate discipline, replay
session forensics.
Build size: MEDIUM-LARGE. Widest keyword spread incl. DS/stats cluster.

## COMPARISON
| # | Product | Keyword cluster | Uniqueness | Difficulty | Job market |
|---|---|---|---|---|---|
| P1 | ModelForge | MLE/training/serving | medium (compete w/ MLFoundry etc.) | hardest | MLE roles ($ heavy) |
| P2 | StreamForge | data-eng/lakehouse | medium | hard | DE roles (huge vol) |
| P3 | AEGIS | agents/governance | HIGHEST (never-shipped ladder) | medium (engines done) | AI-eng 97.5% match |
| P4 | TrustPay | fintech/payments/fraud | high (agentic-payments wedge) | hard | fintech (leads fit!) |
| P5 | Helix | search/recsys/experimentation | medium-high | medium | DS/ML/fullstack |

RECOMMENDATION ORDER: P3 (finish what we started, engines ready) ->
P4 (your Tier-A leads are fintech-heavy) -> P5 (widest resume spread) ->
P2 -> P1. Any three together = staff-engineer portfolio spanning every
keyword family you pasted.
