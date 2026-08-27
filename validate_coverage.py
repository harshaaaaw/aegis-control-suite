# Coverage validator: every keyword you pasted -> owning bucket(s).
# Buckets: B1 AEGIS, B2 ModelForge, B3 StreamForge, B4 TrustPay,
# B5 Helix, B6 DossierIQ, B7 WatchTower, B8 VoiceDesk, B9 TwinForge, B10 OpsCopilot

# Each entry: "keyword": [buckets]. "ALL" => covered by engineering-process layer in every repo.
COVER = {
 # LLM Integration
 "langchain":["B1","B6","B8","B9","B10"], "llamaindex":["B1","B6"],
 "langgraph":["B1","B8","B10"], "autogen":["B1"], "crewai":["B1"],
 "instructor":["B6"], "pydantic":["B1","B6","B8"], "vllm":["B2"],
 "hugging face transformers":["B2"], "hugging face hub":["B2"],
 "ollama":["B1","B2"], "lm studio":["B2"],
 # Foundation Models & APIs
 "openai api":["B1","B2"], "anthropic claude api":["B1","B2"],
 "google gemini api":["B1","B2"], "cohere":["B1","B2"], "mistral ai":["B1","B2"],
 "meta llama":["B1","B2"], "deepseek":["B1","B2"], "flux":["B9"], "midjourney":["B9"],
 # Core Concepts
 "rag":["B1","B5","B6","B8"], "semantic search":["B5","B6"],
 "hybrid search":["B5","B6"], "document chunking":["B6"],
 "semantic caching":["B1","B5"], "prompt engineering":["B1","B2","B8"],
 "prompt tuning":["B2"], "system prompts":["B1","B8"],
 "few-shot prompting":["B2","B8"], "chain-of-thought":["B2","B8"],
 "function calling":["B1","B8"], "agentic workflows":["B1","B10"],
 "tool usage":["B1","B8","B10"], "autonomous agents":["B1"],
 "multi-agent systems":["B1"], "synthetic data generation":["B9"],
 "context window optimization":["B2","B8"], "hallucination mitigation":["B6","B8"],
 "ai guardrails":["B1","B8"], "output parsing":["B1","B6"],
 "structural validation":["B6"],
 # Training & Alignment
 "sft":["B2"], "rlhf":["B2"], "dpo":["B2"], "lora":["B2"], "qlora":["B2"], "peft":["B2"],
 # NLP
 "spacy":["B6"], "nltk":["B6"], "gensim":["B6"], "tokenization":["B2","B6"],
 "ner":["B6","B8"], "intent classification":["B8"], "sentiment analysis":["B8"],
 "dependency parsing":["B6"], "word embeddings":["B6"],
 "sentence transformers":["B5","B8"], "dialog state tracking":["B8"],
 # Conversational
 "rasa":["B8"], "botpress":["B8"], "cognigy":["B8"], "voiceflow":["B8"],
 "azure ai language services":["B8"], "amazon lex":["B8"],
 # Distributed Training
 "deepspeed":["B2"], "ray":["B2"], "megatron-lm":["B2"], "flashattention":["B2"],
 "fsdp":["B2"], "tensor parallelism":["B2"], "pipeline parallelism":["B2"],
 "horovod":["B2"], "pytorch lightning":["B2"],
 # Model Optimization & Inference
 "tensorrt":["B2"], "onnx runtime":["B2","B7"], "openvino":["B2","B7"],
 "triton inference server":["B2"], "ray serve":["B2"], "torchserve":["B2"],
 "vllm inference":["B2"], "tgi":["B2"], "model pruning":["B2"],
 "weight quantization":["B2"], "knowledge distillation":["B2"],
 # CV
 "opencv":["B7"], "torchvision":["B2","B7"], "yolo":["B7"], "detectron2":["B7"],
 "mediapipe":["B7"], "image segmentation":["B7"], "object detection":["B7"],
 "face recognition":["B7"], "ocr":["B6","B7"], "vision-language models":["B6","B7"],
 "image classification":["B7"], "video processing":["B7"], "feature extraction":["B7"],
 # ML Arch
 "transformer internals":["B2"], "cnns":["B2","B7"], "rnns":["B2","B9"],
 "lstm":["B2","B9"], "gans":["B9"], "diffusion models":["B9"], "autoencoders":["B9"],
 "recommender systems":["B5"], "collaborative filtering":["B5"],
 "matrix factorization":["I","B5"], "deep & cross networks":["B5"],
 "learning-to-rank":["B5"], "two-tower embedding networks":["B5","B4"],
 "contextual multi-armed bandits":["B5","B4"], "reinforcement learning":["B5","B4"],
 # Eval
 "confusion matrix":["B2","B7"], "roc-auc":["B2"], "precision-recall":["B2"],
 "f1-score":["B2","B7"], "mae":["B5"], "rmse":["B5"], "ndcg":["B5"], "map":["B5"],
 "ctr":["B5","B4"], "iou":["B7"], "map (cv)":["B7"], "bleu":["B2"], "rouge":["B2"],
 "perplexity":["B2"],
 # Compute
 "spark":["B3"], "pyspark":["B3"], "spark streaming":["B3"], "flink":["B3","B4"],
 "beam":["B3"], "mapreduce":["B3"], "hadoop":["B3"],
 # Lakehouse
 "delta lake":["B3"], "iceberg":["B3"], "hudi":["B3"], "parquet":["B3"], "orc":["B3"],
 "avro":["B3"], "protobuf":["B3","B4"], "data lakes":["B3"], "modern data stack":["B3"],
 # Warehouses
 "snowflake":["B3"], "bigquery":["B3"], "redshift":["B3"], "synapse":["B3"], "databricks":["B3"],
 # Transform/Modeling
 "dbt":["B3"], "data vault 2.0":["B3"], "star schema":["B3"], "snowflake schema":["B3"],
 "dimensional modeling":["B3"], "fact and dimension tables":["B3"], "scd 1/2/3":["B3"],
 "data lineage":["B3"],
 # Orchestration
 "airflow":["B3"], "prefect":["B3"], "dagster":["B3"], "luigi":["B3"], "step functions":["B3"],
 # Quality
 "great expectations":["B3"], "deequ":["B3"], "soda":["B3"],
 "data quality monitoring":["B3"], "anomaly alerting":["B3","B5","B10"],
 # Governance
 "atlas":["B3"], "amundsen":["B3"], "datahub":["B3"], "collibra":["B3"],
 "data cataloging":["B3"], "schema registry":["B3"], "schema evolution":["B3"], "dlq":["B3","B4"],
 # RDBMS
 "postgresql":["B1","B3"], "mysql":["B3"], "sql server":["B3"], "oracle":["B3"],
 "cockroachdb":["B4"], "spanner":["B3"],
 # NoSQL
 "mongodb":["B6"], "cassandra":["B3"], "hbase":["B3"], "couchbase":["B3"],
 "dynamodb":["B3"], "documentdb":["B3"],
 # Vector/Graph
 "pinecone":["B5"], "milvus":["B5"], "qdrant":["B5"], "weaviate":["B5","B6"],
 "pgvector":["B1","B5"], "chromadb":["B5"], "faiss":["B5"], "neo4j":["B6"],
 "neptune":["B6"], "arangodb":["B6"], "graphdb":["B6"], "cypher":["B6"],
 # Cache
 "redis":["B1","B4","B5"], "memcached":["B5"], "redis insight":["B1"],
 "semantic caching (cache)":["B1","B5"], "distributed caching":["B1","B4"],
 # Object storage
 "s3":["B3"], "gcs":["B3","B6"], "blob":["B3","B6"], "minio":["B3"],
 # TS/Search
 "elasticsearch":["B3","B4","B7"], "opensearch":["B5","B7"], "influxdb":["B7"],
 "timescaledb":["B7"], "clickhouse":["B4","B3"],
 # Backend
 "fastapi":["B1"], "django":["B4"], "flask":["B4"], "spring boot":["B4"],
 "go gin":["B4"], "nestjs":["B4"], "express.js":["B4"], "asp.net core":["B4"], "ruby on rails":["B4"],
 # API
 "rest":["ALL"], "graphql":["B4"], "grpc":["B4"], "websockets":["B5","B8"],
 "soap":["B4"], "webhooks":["B1","B4"], "api contract versioning":["B4"],
 "openapi/swagger":["B1"], "protobuf (api)":["B3","B4"],
 # Messaging
 "kafka":["B3","B4"], "rabbitmq":["B4"], "sqs/sns":["B4"], "pulsar":["B4"],
 "redis pub/sub":["B1","B4"], "event-driven architecture":["B1","B4"],
 "async job queues":["B4"], "pub-sub":["B1","B4"], "exactly-once":["B4"],
 # Systems Arch
 "microservices":["B1","B4"], "monolithic":["B1","B4"], "clean architecture":["B1"],
 "ddd":["B1"], "event sourcing":["B4"], "cqrs":["B4"], "idempotency":["B1","B4"],
 "concurrency control":["B4"], "multithreading":["B4","B10"], "async programming":["B1","B4"],
 "distributed locking":["B4"], "connection pooling":["B3","B4"],
 "indexing (b-tree,gin,gist)":["B3"], "query execution plans":["B3"],
 "circuit breakers":["B1","B4"], "bulkheads":["B4"],
 # Security
 "oauth2":["B1"], "oidc":["B1"], "jwt":["B1"], "saml":["B1"], "rbac":["B1","B4"],
 "abac":["B1","B4"], "multi-tenancy":["B1","B3"], "api gateways":["B1"],
 "cors":["B1"], "xss prevention":["B1"], "csrf protection":["B1"],
 "rate limiting":["B1","B4"], "token bucket":["B1","B4"], "leaky bucket":["B1","B4"],
 # Container
 "docker":["B1","B3","B7"], "k8s":["B1","B7"], "helm":["B1","B7"], "kustomize":["B1"],
 "podman":["B1"], "containerd":["B1"], "ecs":["B1"],
 # IaC
 "terraform":["B1"], "terragrunt":["B1"], "cloudformation":["B1"], "pulumi":["B1"], "ansible":["B1"],
 # CI/CD
 "github actions":["B1"], "gitlab ci/cd":["B1"], "jenkins":["B1"], "argocd":["B1"],
 "circleci":["B1"], "tekton":["B1"], "spinnaker":["B1"],
 # Cloud
 "aws":["B1","B3"], "gcp":["B1","B3"], "azure":["B1","B3"],
 # Observability
 "otel":["B1","B10"], "prometheus":["B1","B10"], "grafana":["B1","B10"],
 "datadog":["B10"], "new relic":["B10"], "dynatrace":["B10"], "elk":["B4","B10"],
 "splunk":["B10"], "jaeger":["B4","B10"], "zipkin":["B4","B10"],
 "distributed tracing":["B1","B10"], "metrics":["B1","B10"],
 "centralized logging":["B1","B10"], "alertmanager":["B1","B10"],
 # SRE
 "slo":["B1"], "sli":["B1"], "sla":["B1","B4"], "chaos engineering":["B1","B10"],
 "dr":["B1","B3"], "multi-region failover":["B1","B4"], "ha":["B1","B4"],
 "load balancing":["B1","B4"], "zero-downtime":["B1"], "circuit breaking":["B1","B4"],
 "capacity planning":["B1","B2"], "blameless postmortems":["B1","B10"], "rca":["B10"],
 # Linux
 "linux internals":["B10"], "syscalls":["B10"], "ebpf":["B10"], "systemd":["B10"],
 "epoll":["B10"], "kqueue":["B10"], "ipc":["B10"], "shared memory":["B10"],
 "posix threads":["B10"], "memory management":["B10"], "bash scripting":["B1","B10"],
 # Stats
 "hypothesis testing":["B5"], "p-values":["B5"], "t-test":["B5"], "anova":["B5"],
 "chi-square":["B5"], "confidence intervals":["B5"], "statistical power":["B5"],
 "sample size estimation":["B5"], "clt":["B5"], "bayesian statistics":["B5","B9"],
 "mcmc":["B5","B9"], "distributions":["B5"],
 # Experimentation
 "mvt":["B5"], "split testing":["B5"], "multi-armed bandits":["B5","B4"],
 "sequential testing":["B5"], "variance reduction":["B5"], "cuped":["B5"],
 "srm detection":["B5"], "a/a testing":["B5"], "novelty effects":["B5"],
 "primacy effects":["B5"], "cohort analysis":["B5"],
 # Causal
 "quasi-experiments":["B5"], "synthetic controls":["B5"], "did":["B5"], "psm":["B5"],
 "rdd":["B5"], "iv":["B5"], "sem (causal)":["B5"], "dags (causal)":["B5"],
 "pymc":["B5","B9"], "dowhy":["B5"],
 # Analytics
 "time-series forecasting":["B5"], "arima":["B5"], "prophet":["B5"], "neuralprophet":["B5"],
 "exponential smoothing":["B5"], "multivariate regression":["B5"], "logistic regression":["B5"],
 "linear regression":["B5"], "anomaly detection":["B3","B5","B10"], "isolation forest":["B4","B5"],
 "one-class svm":["B4"], "mahalanobis distance":["B4"], "propensity modeling":["B5"],
 "churn prediction":["B4","B5"], "clv modeling":["B4","B5"], "customer segmentation":["B5"],
 "factor analysis":["B5"], "pca":["B5"], "t-sne":["B5"], "umap":["B5"],
 # BI
 "looker":["B5"], "tableau":["B5"], "power bi":["B5"], "matplotlib":["B5"], "seaborn":["B5"],
 "plotly":["B5"], "shiny":["B5"], "streamlit":["B5"], "dash":["B5"], "eda":["B5"],
 # SDE
 "dsa":["B4","B7","B10"], "big o":["B4","B10"], "array":["B4","B10"], "linked list":["B4","B10"],
 "stack":["B4","B10"], "queue":["B4","B10"], "hash table":["B4","B10"], "binary tree":["B4","B10"],
 "heap":["B4","B10"], "graph algorithms":["B4","B7","B10"], "sorting/searching":["B4","B10"],
 "dp":["B4","B10"], "greedy":["B4","B10"], "recursion":["B4","B10"],
 # Design
 "solid":["ALL"], "ood":["ALL"], "creational patterns":["ALL"], "structural patterns":["ALL"],
 "behavioral patterns":["ALL"], "dry":["ALL"], "kiss":["ALL"], "yagni":["ALL"],
 # Testing
 "tdd":["B1","B4","B5"], "bdd":["B5"], "unit testing":["ALL"], "integration testing":["ALL"],
 "e2e":["B5"], "contract testing":["B4"], "mutation testing":["B5"], "playwright":["B5"],
 "cypress":["B5"], "selenium":["B5"], "junit":["B4"], "pytest":["ALL"], "mocha":["B4","B5"],
 "jest":["B1","B5"], "jmeter":["B4","B5"], "k6":["B4","B5"], "locust":["B4","B5"],
 "wiremock":["B4"], "mockito":["B4"],
 # Fullstack
 "typescript":["B1","B5"], "react":["B1","B5"], "next.js":["B5"], "angular":["B1"], "vue.js":["B7"],
 "redux":["B5"], "context api":["B5"], "zustand":["B5"], "tailwindcss":["B5"],
 "material-ui":["B5"], "webpack":["B5"], "vite":["B1","B5"], "ssr":["B5"], "ssg":["B5"],
 "csr":["B5"], "websockets (fs)":["B5","B8"], "sse":["B5"], "pwa":["B5"],
 "localstorage":["B5"], "sessionstorage":["B5"], "service workers":["B5"],
 # Mobile
 "react native":["B5"], "flutter":["B5"], "swift":["B5"], "swiftui":["B5"], "kotlin":["B5"],
 "jetpack compose":["B5"], "objective-c":["B5"], "android studio":["B5"], "xcode":["B5"],
 "mobile app lifecycle":["B5"], "push notifications":["B5"], "app store deployment":["B5"],
 # Dev Workflow
 "git":["ALL"], "github":["ALL"], "gitlab":["ALL"], "bitbucket":["ALL"], "git-flow":["ALL"],
 "semver":["ALL"], "monorepos":["B1"], "code reviews":["ALL"], "trunk-based":["ALL"],
 "feature flags":["B1"],
 # Agile / PM / Eng-mgmt
 "scrum":["ALL"], "kanban":["ALL"], "scrumban":["ALL"], "safe":["ALL"],
 "jira":["ALL"], "confluence":["ALL"], "linear":["ALL"], "trello":["ALL"], "asana":["ALL"],
 "notion":["ALL"], "rfcs":["B1"], "tdds":["B1"], "adrs":["B1"], "sprint planning":["ALL"],
 "story point estimation":["ALL"], "burndown":["ALL"], "velocity tracking":["ALL"],
 "retrospectives":["ALL"], "code ownership":["ALL"], "technical debt management":["ALL"],
}

import collections
total=len(COVER)
covered=sum(1 for v in COVER.values() if v)
print(f"TOTAL keywords parsed: {total}")
print(f"COVERED (>=1 bucket): {covered}  =>  {100*covered/total:.1f}%")
uncovered=[k for k,v in COVER.items() if not v]
print(f"UNCOVERED: {len(uncovered)}")
for u in uncovered: print("  MISSING:", u)

# per-bucket tally
cnt=collections.Counter()
for v in COVER.values():
    for b in v: cnt[b]+=1
print("\nCoverage count per bucket (how many keywords each owns):")
for b in ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10"]:
    print(f"  {b}: {cnt[b]}")

# save full matrix file
with open(r"C:\Users\Harsh\job-hunt-2026\coverage_matrix.md","w",encoding="utf-8") as f:
    f.write("# Keyword -> Bucket coverage matrix\n\n")
    f.write(f"Overall: {covered}/{total} = {100*covered/total:.1f}%\n\n")
    for k,v in sorted(COVER.items()):
        f.write(f"- **{k}**: {', '.join(v) if v else '**NONE**'}\n")
print("\nfull matrix saved -> coverage_matrix.md")
