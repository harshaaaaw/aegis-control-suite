# AI-Engineer Lane: AEGIS + Siblings
# Thesis: own the AGENT CONTROL PLANE lane. Not another framework, not ML/DS.
# Every product below maps to one of the 4 research-validated operating problems:
#   reliability, observability, stale-context, cost.
# Source pain: IBM CAP/MAP (306 practitioners), IEEE (95% pilots fail), Cockroach Labs,
# Fast Company, tsukumo (4 operating problems), LaderaLABS (500 deployments).

## BUILD SET (rate >= 8.4; PROBE kept on pain=10 tie)

### 1. AEGIS — Agent Autonomy Control Plane  (score 9.4)
Business problem: companies run agents that call tools, move money, change prod data with
no fail-closed governance. 90% of agents are over-permissioned. EU AI Act demands proof of
control. Microsoft sells a locked cloud version; the open gap is wide.
How it works: a FastAPI control plane registers every agent as a signed identity (OAuth2,
OpenID Connect, JWT, SAML). Each agent is wrapped by a policy sidecar that inspects every
tool call before it runs, enforcing AI guardrails, function calling limits, output parsing
and structural validation. Agents climb an autonomy ladder (L0 human-approves to L4 fully
autonomous) by earning trust through LLM evaluation. Semantic caching and context window
optimization cut cost. OpenTelemetry traces every run; Kafka streams policy events; a
React/Next.js dashboard shows the fleet. MCP lets agents register natively. SLOs, error
budgets, circuit breakers, bulkheads keep it alive. Terraform + Docker deploy it.
Your 7 engines are its organs: sentinel (guard), governor (treasurer), run-replay (evidence
vault), evalforge (exam board), meshwork (dispatcher), ragforge (grounding), middleware.
Keywords: agentic workflows, function calling, tool usage, autonomous agents, multi-agent
systems, AI guardrails, output parsing, structural validation, RAG, hallucination mitigation,
RBAC/ABAC, multi-tenancy isolation, rate limiting (token bucket, leaky bucket), CORS, circuit
breakers, OpenTelemetry, Prometheus, Grafana, SLO/SLI/SLA, canary, blue-green, feature flags,
ADRs, microservices, CQRS, event-driven, Kafka, Redis, PostgreSQL, FastAPI, gRPC, GraphQL,
OpenAPI, Docker, Kubernetes, Helm, Terraform, GitHub Actions.

### 2. LEDGERSCALE — Agent FinOps + Runaway-Loop Kill  (score 8.56)
Business problem: cost is the #4 operating problem. Loops don't terminate. Retries cascade.
Spend spikes unseen across a fleet. tsukumo: "the token bill is the meter on the other three."
How it works: every agent action carries a token and dollar budget. A double-entry ledger
(event-sourced via Kafka, exactly-once, idempotency, distributed locking, CQRS) records each
spend. Budget SLOs auto-kill a run that breaches its cap. ClickHouse stores the spend time
series; an Isolation Forest flags anomalous sessions; contextual bandits tune per-task
budgets. Redis enforces rate limits. A React dashboard shows live burn per agent/tenant.
Keywords: Kafka, RabbitMQ, SQS/SNS, exactly-once processing, idempotency, distributed locking,
event sourcing, CQRS, Redis, ClickHouse, PostgreSQL, anomaly detection, Isolation Forest,
One-Class SVM, Mahalanobis distance, contextual multi-armed bandits, circuit breakers,
bulkheads, FastAPI, OpenTelemetry, Grafana, Docker, Kubernetes, Terraform.

### 3. MNEMOS — Canonical Truth / Context Layer  (score 8.4)
Business problem: agents act on stale, reconstructed truth (tsukumo's root cause of
unreliability and the biggest cost line). They reread the repo every session and rework.
How it works: every fact an agent relies on gets a TTL that decays and a hash-chained
provenance trail. A RAG pipeline with hybrid search and semantic caching on Redis/pgvector
serves the canonical answer on demand (measured 60% token saving in the research). Poisoned
or contradicted facts are quarantined. Neo4j + Cypher stores the provenance graph. A
sentence-transformers reranker keeps relevance high.
Keywords: RAG, semantic search, hybrid search, document chunking, semantic caching, context
window optimization, hallucination mitigation, knowledge distillation, NER, intent
classification, sentiment analysis, word embeddings, sentence transformers, Pinecone, Milvus,
Qdrant, Weaviate, pgvector, ChromaDB, FAISS, Neo4j, Cypher, Redis, OpenAI/Anthropic/Gemini
APIs, FastAPI, React, OpenTelemetry.

### 4. PROBE — Agent Failure-Mode Eval Harness  (score 8.36, kept on pain=10)
Business problem: the eval-harness gap is called "the single largest unsolved problem for
production agentic deployments." 89% of teams lack one. Degradation is silent until a
catastrophe. Builders of eval harnesses "capture durable strategic position."
How it works: implements the published 15-mode taxonomy (drift, state management,
coordination, termination, adversarial, tool-interface). Ships targeting probes per mode,
synthetic data generation for hard cases, a versioned golden dataset, and a report card
(recall, faithfulness, tool-call accuracy, chain-failure rate). Integrates with CI
(GitHub Actions) so every prompt/model change re-runs the suite. Publishes the methodology
as the differentiator.
Keywords: LLM evaluation, golden datasets, recall@k, faithfulness, drift detection, synthetic
data generation, chaos engineering, ROC-AUC, F1, precision-recall, perplexity, BLEU, ROUGE,
A/B testing, causal DAGs, PyMC, DoWhy, structural validation, output parsing, FastAPI,
GitHub Actions, Docker.

## SPEC-ONLY (below 8.4 threshold; keep as architecture docs for range, do not build first)

### 5. TANGENT — Deterministic Guardrail Compiler  (score 8.06)
Turns natural-language guardrails into a fail-closed policy DSL compiled to a sidecar.
Few do explicit guardrail compilation. Keywords: AI guardrails, policy as code, output
parsing, structural validation, function calling limits, sidecar, WebAssembly sandbox.

### 6. SENTINEL-GW — Agent API Gateway  (score 8.0)
Identity-per-agent at the edge; scoped tokens never sit in the context window (fixes the
confused-deputy exploit). CORS, rate limit, audit on every call. Keywords: API gateways
(Kong, AWS API Gateway, Apigee), OAuth2/OIDC/JWT, RBAC/ABAC, multi-tenancy, rate limiting,
CORS, XSS/CSRF protection, audit logging, gRPC, GraphQL, WebSockets.
