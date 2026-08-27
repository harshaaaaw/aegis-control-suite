"""Single source of truth: 10 AI product buckets + their keyword coverage.

Generates TEN_PRODUCTS.md and validates that EVERY keyword in kw.py
appears in the bucket texts. If something is missing, it prints and fails.
"""
from kw import KEYWORDS

# Each bucket: id, name, one-line business pain, the AI core, the build, and
# the exact keywords it covers. Union of all keyword lists must == kw.KEYWORDS.
BUCKETS = {
 "B1": {
  "name": "AEGIS - Agent Autonomy Control Plane",
  "pain": "Companies run AI agents that spend money and touch production with no control and no proof for auditors.",
  "ai_core": "LangGraph/AutoGen/CrewAI multi-agent orchestration wrapped in a policy sidecar that guards every Function Calling and Tool Usage; AI Guardrails and Hallucination Mitigation at the boundary; eval-driven autonomy ladder.",
  "build": "FastAPI control plane, OIDC/JWT/SAML agent identities, out-of-process policy sidecar, autonomy ladder L0-L4, Postgres multi-tenancy, MCP facade, React dashboard, Terraform deploy.",
  "kw": ["LangChain","LangGraph","AutoGen","CrewAI","Pydantic","vLLM","OpenAI API","Anthropic Claude API","Google Gemini API","Cohere","Mistral AI","Meta Llama","DeepSeek",
   "Retrieval-Augmented Generation (RAG)","Agentic Workflows","Tool Usage","Autonomous Agents","Multi-Agent Systems","Hallucination Mitigation","AI Guardrails","Output Parsing","Structural Validation",
   "FastAPI","RESTful APIs","GraphQL","WebSockets","Webhooks","OpenAPI / Swagger","gRPC",
   "OAuth2","OpenID Connect (OIDC)","JWT (JSON Web Tokens)","SAML","Role-Based Access Control (RBAC)","Attribute-Based Access Control (ABAC)","Multi-Tenancy Isolation","API Gateways (Kong, AWS API Gateway, Apigee)","CORS","XSS Prevention","CSRF Protection","Rate Limiting","Token Bucket Algorithm","Leaky Bucket Algorithm",
   "PostgreSQL","Redis","Semantic Caching","Distributed Caching",
   "Docker","Kubernetes (K8s)","Helm Charts","Terraform","AWS CloudFormation","Amazon ECS","Amazon Web Services (AWS)","Google Cloud Platform (GCP)","Microsoft Azure",
   "GitHub Actions","GitLab CI/CD","OpenTelemetry (OTel)","Prometheus","Grafana","Jaeger","Distributed Tracing","Centralized Logging","Alertmanager",
   "Service Level Objectives (SLOs)","Service Level Indicators (SLIs)","Service Level Agreements (SLAs)","High Availability (HA)","Load Balancing (NGINX, HAProxy, AWS ALB)","Zero-Downtime Deployment (Blue-Green, Canary, Rolling)","Circuit Breaking","Capacity Planning","Blameless Post-Mortems","Root-Cause Analysis (RCA)",
   "Microservices Architecture","Clean Architecture","Domain-Driven Design (DDD)","Event Sourcing","CQRS (Command Query Responsibility Segregation)","Idempotency","Concurrency Control","Distributed Locking","Circuit Breakers","Bulkheads",
   "TypeScript","React","Next.js","TailwindCSS","Material-UI",
   "Architecture Decision Records (ADRs)","Technical Design Documents (TDDs)","Request for Comments (RFCs)","Scrum","Kanban","Jira","Confluence","Code Reviews","Feature Flags / Feature Toggles","Monorepos (Turborepo, Nx)","Semantic Versioning (SemVer)",
   "Test-Driven Development (TDD)","Unit Testing","Integration Testing","End-to-End (E2E) Testing","Contract Testing","PyTest","Jest","Playwright","Cypress"],
 },
 "B2": {
  "name": "ModelForge - GPU FinOps Training & Serving Platform",
  "pain": "GPU clusters burn cash with no per-team accounting; models ship unquantized at 5x cost; drift found by customers.",
  "ai_core": "Ray + DeepSpeed + FSDP distributed training of Transformer internals and CNNs/RNNs/LSTM; SFT/RLHF/DPO/LoRA/QLoRA/PEFT alignment; TensorRT/ONNX/OpenVINO/Triton/vLLM/TGI quantization and serving; full eval zoo (F1, ROC-AUC, BLEU, ROUGE, Perplexity).",
  "build": "Ray-cluster training orchestrator, LoRA/DPO pipelines, quantization farm (AWQ/GPTQ/INT8), Triton+vLLM fleet with canary rollouts, model registry with lineage, drift/anomaly monitors.",
  "kw": ["Hugging Face Transformers","Hugging Face Hub","Ollama","LM Studio","vLLM Inference","Flux","Midjourney",
   "Supervised Fine-Tuning (SFT)","Reinforcement Learning from Human Feedback (RLHF)","Direct Preference Optimization (DPO)","Low-Rank Adaptation (LoRA)","Quantized LoRA (QLoRA)","Parameter-Efficient Fine-Tuning (PEFT)",
   "DeepSpeed","Ray","Megatron-LM","FlashAttention","Fully Sharded Data Parallel (FSDP)","Tensor Parallelism (TP)","Pipeline Parallelism (PP)","Horovod","PyTorch Lightning",
   "TensorRT","ONNX Runtime","OpenVINO","Triton Inference Server","Ray Serve","TorchServe","TGI (Text Generation Inference)","Model Pruning","Weight Quantization (INT8, FP16, AWQ, GPTQ)","Knowledge Distillation",
   "OpenCV","TorchVision","YOLO (You Only Look Once)","Detectron2","MediaPipe","Image Segmentation","Object Detection","Face Recognition","Optical Character Recognition (OCR)","Vision-Language Models (VLMs)","Image Classification","Video Processing","Feature Extraction",
   "Transformer Internals","Convolutional Neural Networks (CNNs)","Recurrent Neural Networks (RNNs)","Long Short-Term Memory (LSTM)","Generative Adversarial Networks (GANs)","Diffusion Models","Autoencoders",
   "Confusion Matrix","ROC-AUC","Precision-Recall","F1-Score","Mean Absolute Error (MAE)","Root Mean Squared Error (RMSE)","NDCG (Normalized Discounted Cumulative Gain)","MAP (Mean Average Precision)","Click-Through Rate (CTR)","Intersect over Union (IoU)","mAP (mean Average Precision for CV)","BLEU score","ROUGE score","Perplexity",
   "Django","Flask","Spring Boot","Go Gin","NestJS","Express.js","ASP.NET Core","Ruby on Rails",
   "RabbitMQ","Redis Pub/Sub","Asynchronous Job Queues","Publish-Subscribe Pattern","Event-Driven Architecture",
   "MySQL","Microsoft SQL Server","Oracle Database","CockroachDB","Spanner","MongoDB","Cassandra","Apache HBase","Couchbase","DynamoDB","Amazon DocumentDB",
   "Kubernetes (K8s)","Kustomize","Containerd","Podman","Pulumi","Ansible","Jenkins","ArgoCD","CircleCI","Tekton","Spinnaker",
   "Datadog","New Relic","Dynatrace","Splunk","ELK Stack (Elasticsearch, Logstash, Kibana)","Zipkin","Metrics","Chaos Engineering (Gremlin, Chaos Mesh)","Disaster Recovery (DR)","Multi-Region Failover",
   "Linux Internals","System Calls (syscalls)","Bash Scripting","Network I/O (epoll, kqueue)","POSIX Threads","Memory Management (Garbage Collection Tuning, Heap/Stack)","Inter-Process Communication (IPC)","Shared Memory","Systemd",
   "SOLID Principles","Object-Oriented Design (OOD)","Creational Patterns (Singleton, Factory, Builder)","Structural Patterns (Adapter, Decorator, Facade, Proxy)","Behavioral Patterns (Observer, Strategy, State, Command)","DRY (Don't Repeat Yourself)","KISS (Keep It Simple, Stupid)","YAGNI (You Aren't Gonna Need It)",
   "Mutation Testing","JUnit","Mocha","JMeter","k6","Locust","WireMock","Mockito","Behavior-Driven Development (BDD)","Selenium",
   "Git","GitHub","GitLab","Bitbucket","Git-flow","Trunk-Based Development","Story Point Estimation","Burndown Charts","Velocity Tracking","Retrospectives","Code Ownership","Technical Debt Management","Linear","Trello","Asana","Notion","Scrumban","SAFe (Scaled Agile Framework)","Sprint Planning"],
 },
 "B3": {
  "name": "StreamForge - Governed Streaming Lakehouse",
  "pain": "Exec dashboards contradict each other; broken pipelines found by the CEO; nobody traces a KPI to source rows.",
  "ai_core": "Anomaly Detection and Isolation Forest on streaming features feed AI data-quality monitors; embeddings via Sentence Transformers for catalog search.",
  "build": "Kafka+CDC ingest, Iceberg medallion lakehouse, Spark/Flink/Beam, dbt Data-Vault-2.0 marts + SCD1/2/3, Great Expectations quality gates with DLQ, column-lineage graph.",
  "kw": ["Apache Spark","PySpark","Spark Streaming","Apache Flink","Apache Beam","MapReduce","Hadoop",
   "Delta Lake","Apache Iceberg","Apache Hudi","Parquet","ORC","Avro","Protobuf","Data Lakes","Modern Data Stack (MDS)",
   "Snowflake","Google BigQuery","Amazon Redshift","Azure Synapse Analytics","Databricks",
   "dbt (data build tool)","Data Vault 2.0","Star Schema","Snowflake Schema","Dimensional Modeling","Fact and Dimension Tables","Slowing Changing Dimensions (SCD Type 1/2/3)","Data Lineage",
   "Apache Airflow","Prefect","Dagster","Luigi","AWS Step Functions",
   "Great Expectations","deequ","Soda","Data Quality Monitoring","Anomaly Alerting",
   "Apache Atlas","Amundsen","DataHub","Collibra","Data Cataloging","Schema Registry","Schema Evolution","Dead-Letter Queues (DLQ)",
   "Apache Kafka","Amazon SQS/SNS","Apache Pulsar","Exactly-Once Processing (EOP)","Connection Pooling","Database Indexing (B-Tree, GIN, GiST)","Query Execution Plans","Asynchronous Programming","Multithreading",
   "Elasticsearch","OpenSearch","InfluxDB","TimescaleDB","ClickHouse",
   "AWS S3","Google Cloud Storage (GCS)","Azure Blob Storage","MinIO",
   "Memcached","Redis Insight",
   "Monolithic Architecture","SOLID Principles"],
 },
 "B4": {
  "name": "TrustPay - Real-Time Payments & Fraud Decisioning Engine",
  "pain": "Instant-payment fraud explodes as AI agents start spending; legacy batch fraud misses sub-second attacks; disputes evidenceless.",
  "ai_core": "Flink CEP + Isolation Forest + One-Class SVM scoring; two-tower merchant similarity; Contextual Multi-Armed Bandits for rule tuning; Reinforcement Learning PPO for policy.",
  "build": "Event-sourced double-entry ledger (Kafka exactly-once), CQRS read models, fraud scoring, Redis token-bucket limits, graph fraud-ring BFS, polyglot microservices (Go sidecar, Spring Boot ledger, NestJS webhooks), chaos harness.",
  "kw": ["Semantic Search","Hybrid Search","Graph Algorithms (BFS, DFS, Dijkstra, A* Search)","Recommender Systems","Collaborative Filtering","Matrix Factorization","Contextual Multi-Armed Bandits","Reinforcement Learning (Q-learning, PPO, Deep Q-Networks)","Deep & Cross Networks",
   "Anomaly Detection","Isolation Forest","One-Class SVM","Mahalanobis Distance",
   "Event Sourcing","CQRS (Command Query Responsibility Segregation)","Exactly-Once Processing (EOP)","Idempotency","Concurrency Control","Distributed Locking","Connection Pooling","Bulkheads","Microservices Architecture",
   "SOAP","API Contract Versioning","Protocol Buffers (Protobuf)","GraphQL",
   "Redis","Redis Pub/Sub","Distributed Caching",
   "Neo4j","Amazon Neptune","ArangoDB","GraphDB","Cypher Query Language",
   "Chaos Engineering (Gremlin, Chaos Mesh)","Jaeger","Zipkin","Load Balancing (NGINX, HAProxy, AWS ALB)","Zero-Downtime Deployment (Blue-Green, Canary, Rolling)","Circuit Breaking",
   "JUnit","Mockito","WireMock","k6","JMeter",
   "Go Gin","Spring Boot","NestJS","Express.js"],
 },
 "B5": {
  "name": "Helix - Commerce Intelligence & Experimentation OS",
  "pain": "Store search returns junk (conversion bleed); recommendations generic; teams ship changes with no proof they worked.",
  "ai_core": "Two-tower retrieval + LambdaMART re-ranker; pgvector+OpenSearch hybrid with Semantic Caching; matrix-factorization and Contextual Multi-Armed Bandits recsys; full experimentation service (CUPED, SRM, sequential, MVT); causal module (DiD, PSM, RDD, PyMC); forecasting.",
  "build": "Retrieval + ranking service, recsys, experimentation platform, causal-analysis service, forecasting, Next.js PWA storefront + React Native app + Streamlit workbench.",
  "kw": ["Hugging Face Hub","Semantic Search","Hybrid Search","Document Chunking","Semantic Caching","Prompt Engineering","Prompt Tuning","System Prompts","Few-Shot Prompting","Chain-of-Thought (CoT)","Function Calling","Context Window Optimization","Synthetic Data Generation",
   "Learning-to-Rank (LambdaMART)","Two-Tower Embedding Networks","Recommender Systems","Collaborative Filtering","Matrix Factorization",
   "Pinecone","Milvus","Qdrant","Weaviate","pgvector","ChromaDB","FAISS",
   "Multivariate Testing (MVT)","Split Testing","Multi-Armed Bandits","Sequential Testing","Variance Reduction","CUPED (Controlled Experiments Utilization of Over-Sampled Pre-Experiment Data)","Sample Ratio Mismatch (SRM) Detection","A/A Testing","Novelty Effects","Primacy Effects","Cohort Analysis",
   "Quasi-Experiments","Synthetic Controls","Difference-in-Differences (DiD)","Propensity Score Matching (PSM)","Regression Discontinuity Design (RDD)","Instrumental Variables","Structural Equation Modeling (SEM)","Directed Acyclic Graphs (DAGs)","PyMC","DoWhy",
   "Time-Series Forecasting","ARIMA","Prophet","NeuralProphet","Exponential Smoothing","Multivariate Regression","Logistic Regression","Linear Regression","Propensity Modeling","Churn Prediction","Customer Lifetime Value (CLV) Modeling","Customer Segmentation","Factor Analysis","Principal Component Analysis (PCA)","t-SNE","UMAP",
   "Hypothesis Testing","p-values","t-test","ANOVA","Chi-Square Test","Confidence Intervals","Statistical Power","Sample Size Estimation","Central Limit Theorem","Bayesian Statistics","Markov Chain Monte Carlo (MCMC)","Probability Distributions (Normal, Binomial, Poisson, Exponential)",
   "Looker","Tableau","Power BI","Matplotlib","Seaborn","Plotly","Shiny","Streamlit","Dash","Exploratory Data Analysis (EDA)",
   "Next.js","Angular","Vue.js","Redux","Context API","Zustand","Server-Side Rendering (SSR)","Static Site Generation (SSG)","Client-Side Rendering (CSR)","Server-Sent Events (SSE)","Progressive Web Apps (PWA)","LocalStorage","SessionStorage","Service Workers",
   "React Native","Flutter","Swift","SwiftUI","Kotlin","Jetpack Compose","Objective-C","Android Studio","Xcode","Mobile App Lifecycle","Push Notifications","App Store / Play Store Deployment Pipelines",
   "Webpack","Vite","React","TypeScript","Material-UI"],
 },
 "B6": {
  "name": "DossierIQ - Clinical & Legal Document Intelligence",
  "pain": "Hospitals and law firms drown in PDFs; hallucinated summaries are a liability risk.",
  "ai_core": "OCR + VLM page understanding, grounded RAG with mandatory citations, spaCy NER + Dependency Parsing relations, Neo4j knowledge graph, Instructor/Pydantic strict contracts, human review queue.",
  "build": "Document ingest (OCR/VLM), grounded generator with citations, NER/relation extractor, graph store, review UI, API.",
  "kw": ["spaCy","NLTK","Gensim","Tokenization","Named Entity Recognition (NER)","Intent Classification","Sentiment Analysis","Dependency Parsing","Word Embeddings","Sentence Transformers","Dialog State Tracking",
   "Retrieval-Augmented Generation (RAG)","Instructor","Output Parsing","Structural Validation","Hallucination Mitigation",
   "Optical Character Recognition (OCR)","Vision-Language Models (VLMs)","Image Classification","Feature Extraction",
   "MongoDB","Amazon DocumentDB",
   "Cypher Query Language","GraphDB",
   "WebSockets","RESTful APIs"],
 },
 "B7": {
  "name": "WatchTower - Natural-Language Video Security Ops",
  "pain": "Hundreds of cameras, zero searchability; investigations take hours of manual scrubbing.",
  "ai_core": "OpenCV/YOLO/Detectron2/MediaPipe on edge (OpenVINO), VLM captioning, English queries over footage ('red jacket near dock 3, 02:00'), face recognition with consent registry, IoU/mAP eval harness.",
  "build": "Edge inference pipeline, VLM caption store, NL query API, face registry, Vue console, Helm deploy.",
  "kw": ["OpenCV","YOLO (You Only Look Once)","Detectron2","MediaPipe","Image Segmentation","Object Detection","Face Recognition","Vision-Language Models (VLMs)","Video Processing","Feature Extraction","Image Classification",
   "OpenVINO","TensorRT",
   "Intersect over Union (IoU)","mAP (mean Average Precision for CV)","Confusion Matrix","Precision-Recall","F1-Score",
   "TimescaleDB","InfluxDB","Elasticsearch","OpenSearch","ClickHouse",
   "Vue.js","Angular","Material-UI","TailwindCSS",
   "Helm Charts","Kubernetes (K8s)","Docker","eBPF","Network I/O (epoll, kqueue)","Linux Internals","System Calls (syscalls)"],
 },
 "B8": {
  "name": "VoiceDesk - AI Contact-Center Operating System",
  "pain": "Call centers bleed wages; QA samples under 2% of calls so bad interactions go unnoticed.",
  "ai_core": "Streaming ASR to a LangGraph dialog engine with explicit Dialog State Tracking, Intent Classification + Sentiment Analysis, NLU via spaCy; live agent-assist over WebSockets; auto-QA on 100% of calls; forensic replay.",
  "build": "ASR ingest, dialog engine, intent/sentiment, Rasa/Botpress/Voiceflow/Lex importers, agent-assist UI, QA scoring, replay store.",
  "kw": ["Rasa","Botpress","Cognigy","Voiceflow","Azure AI Language Services","Amazon Lex",
   "Dialog State Tracking","Intent Classification","Sentiment Analysis","Named Entity Recognition (NER)","Word Embeddings","Sentence Transformers","Tokenization",
   "LangGraph","LangChain","Agentic Workflows","Tool Usage","Autonomous Agents","Multi-Agent Systems",
   "WebSockets","Server-Sent Events (SSE)","RESTful APIs","gRPC",
   "Redis","PostgreSQL","MongoDB",
   "React","Next.js","TypeScript","TailwindCSS","Material-UI"],
 },
 "B9": {
  "name": "TwinForge - Synthetic Data & Privacy Factory",
  "pain": "Legal blocks data sharing; models overfit rare classes; no privacy-safe training data.",
  "ai_core": "GAN/Diffusion/VAE generators for tabular, image and text; LSTM/Transformer sequence synthesis; membership-inference privacy scoring; PyMC Bayesian utility checks; CI seed-data vending API.",
  "build": "Generator registry, privacy-scoring service, Bayesian validator, synthetic-data API with lineage, quality gates.",
  "kw": ["Generative Adversarial Networks (GANs)","Diffusion Models","Autoencoders",
   "Recurrent Neural Networks (RNNs)","Long Short-Term Memory (LSTM)","Transformer Internals",
   "Synthetic Data Generation","Synthetic Controls",
   "Bayesian Statistics","Markov Chain Monte Carlo (MCMC)","PyMC","Probability Distributions (Normal, Binomial, Poisson, Exponential)","Hypothesis Testing","Confidence Intervals",
   "Anomaly Detection","Isolation Forest","One-Class SVM","Mahalanobis Distance",
   "Data Quality Monitoring","Great Expectations","deequ","Soda",
   "FastAPI","Django","Flask","NestJS",
   "AWS S3","Google Cloud Storage (GCS)","MinIO","Azure Blob Storage",
   "Pinecone","Weaviate","pgvector","FAISS"],
 },
 "B10": {
  "name": "OpsCopilot - AI SRE Incident Command",
  "pain": "On-call burnout; MTTR in hours because context lives across 12 tools.",
  "ai_core": "eBPF/systemd collectors, log-trace-metric correlation importing from Datadog/Splunk/etc., LangGraph triage agent with runbook tools, blast-radius graph reasoning, auto-drafted blameless postmortems, Chaos Mesh launcher.",
  "build": "Collector agents, correlation engine, triage LLM agent, knowledge graph, postmortem generator, chaos launcher, Grafana plugin.",
  "kw": ["OpenTelemetry (OTel)","Prometheus","Grafana","Datadog","New Relic","Dynatrace","ELK Stack (Elasticsearch, Logstash, Kibana)","Splunk","Jaeger","Zipkin","Distributed Tracing","Metrics","Centralized Logging","Alertmanager",
   "Service Level Objectives (SLOs)","Service Level Indicators (SLIs)","Service Level Agreements (SLAs)","Chaos Engineering (Gremlin, Chaos Mesh)","Disaster Recovery (DR)","Multi-Region Failover","High Availability (HA)","Load Balancing (NGINX, HAProxy, AWS ALB)","Zero-Downtime Deployment (Blue-Green, Canary, Rolling)","Circuit Breaking","Capacity Planning","Blameless Post-Mortems","Root-Cause Analysis (RCA)",
   "Linux Internals","System Calls (syscalls)","eBPF","Systemd","Network I/O (epoll, kqueue)","Inter-Process Communication (IPC)","Shared Memory","POSIX Threads","Memory Management (Garbage Collection Tuning, Heap/Stack)","Bash Scripting",
   "LangGraph","AutoGen","CrewAI","Agentic Workflows","Autonomous Agents","Multi-Agent Systems","Tool Usage","Function Calling",
   "Neo4j","Amazon Neptune","ArangoDB","GraphDB","Cypher Query Language","Graph Algorithms (BFS, DFS, Dijkstra, A* Search)",
   "Terraform","Terragut","AWS CloudFormation","Pulumi","Ansible","GitHub Actions","GitLab CI/CD","Jenkins","ArgoCD","CircleCI","Tekton","Spinnaker",
   "Amazon Web Services (AWS)","Google Cloud Platform (GCP)","Microsoft Azure",
   "Docker","Kubernetes (K8s)","Helm Charts","Kustomize","Podman","Containerd","Amazon ECS",
   "SOLID Principles","Object-Oriented Design (OOD)","DRY (Don't Repeat Yourself)","KISS (Keep It Simple, Stupid)","YAGNI (You Aren't Gonna Need It)","Clean Architecture","Domain-Driven Design (DDD)",
   "Test-Driven Development (TDD)","Unit Testing","Integration Testing","End-to-End (E2E) Testing","Contract Testing","Mutation Testing","PyTest","Jest","Playwright","Cypress","Selenium",
   "Git","GitHub","GitLab","Bitbucket","Git-flow","Semantic Versioning (SemVer)","Monorepos (Turborepo, Nx)","Code Reviews","Trunk-Based Development","Feature Flags / Feature Toggles",
   "Scrum","Kanban","Scrumban","SAFe (Scaled Agile Framework)","Jira","Confluence","Linear","Trello","Asana","Notion",
   "Request for Comments (RFCs)","Technical Design Documents (TDDs)","Architecture Decision Records (ADRs)","Capacity Planning","Sprint Planning","Story Point Estimation","Burndown Charts","Velocity Tracking","Retrospectives","Code Ownership","Technical Debt Management",
   "Data Structures & Algorithms (DSA)","Big O Notation","Array","Linked List","Stack","Queue","Hash Table","Binary Tree","Heap","Sorting and Searching","Dynamic Programming","Greedy Algorithms","Recursion"],
 },
}

def main():
    import os
    # 1. Build the markdown doc
    lines = ["# TEN ENTERPRISE AI PRODUCT BUCKETS\n",
      "Every bucket is AI-core, solves a real enterprise pain, and together they cover 100% of the pasted keyword universe.\n",
      "Coverage is machine-verified: run `python validate_buckets.py`.\n"]
    seen = set()
    for bid, b in BUCKETS.items():
        lines.append(f"\n## {bid}. {b['name']}\n")
        lines.append(f"**Business pain:** {b['pain']}\n")
        lines.append(f"**AI core:** {b['ai_core']}\n")
        lines.append(f"**What you build:** {b['build']}\n")
        lines.append(f"**Keywords covered ({len(b['kw'])}):** " + ", ".join(b['kw']) + "\n")
        for k in b['kw']:
            seen.add(k)
    out = os.path.join(os.path.dirname(__file__), "TEN_PRODUCTS.md")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # 2. Validate full coverage
    missing = [k for k in KEYWORDS if k not in seen]
    if missing:
        print(f"COVERAGE FAIL: {len(missing)} keywords missing:")
        for m in missing:
            print("  -", m)
        return 1
    print(f"OK: all {len(KEYWORDS)} keywords covered across {len(BUCKETS)} buckets.")
    print(f"TEN_PRODUCTS.md written ({len(KEYWORDS)} keywords, {sum(len(b['kw']) for b in BUCKETS.values())} total mentions).")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
