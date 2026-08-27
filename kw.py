# Canonical keyword universe (transcribed 1:1 from the pasted list).
KEYWORDS = [
 # LLM Integration
 "LangChain","LlamaIndex","LangGraph","AutoGen","CrewAI","Instructor","Pydantic",
 "vLLM","Hugging Face Transformers","Hugging Face Hub","Ollama","LM Studio",
 # Foundation Models & APIs
 "OpenAI API","Anthropic Claude API","Google Gemini API","Cohere","Mistral AI",
 "Meta Llama","DeepSeek","Flux","Midjourney",
 # Core Concepts
 "Retrieval-Augmented Generation (RAG)","Semantic Search","Hybrid Search",
 "Document Chunking","Semantic Caching","Prompt Engineering","Prompt Tuning",
 "System Prompts","Few-Shot Prompting","Chain-of-Thought (CoT)","Function Calling",
 "Agentic Workflows","Tool Usage","Autonomous Agents","Multi-Agent Systems",
 "Synthetic Data Generation","Context Window Optimization","Hallucination Mitigation",
 "AI Guardrails","Output Parsing","Structural Validation",
 # Model Training & Alignment
 "Supervised Fine-Tuning (SFT)","Reinforcement Learning from Human Feedback (RLHF)",
 "Direct Preference Optimization (DPO)","Low-Rank Adaptation (LoRA)",
 "Quantized LoRA (QLoRA)","Parameter-Efficient Fine-Tuning (PEFT)",
 # NLP & Processing
 "spaCy","NLTK","Gensim","Tokenization","Named Entity Recognition (NER)",
 "Intent Classification","Sentiment Analysis","Dependency Parsing","Word Embeddings",
 "Sentence Transformers","Dialog State Tracking",
 # Conversational AI Frameworks
 "Rasa","Botpress","Cognigy","Voiceflow","Azure AI Language Services","Amazon Lex",
 # Distributed Training & Systems
 "DeepSpeed","Ray","Megatron-LM","FlashAttention","Fully Sharded Data Parallel (FSDP)",
 "Tensor Parallelism (TP)","Pipeline Parallelism (PP)","Horovod","PyTorch Lightning",
 # Model Optimization & Inference Servicing
 "TensorRT","ONNX Runtime","OpenVINO","Triton Inference Server","Ray Serve",
 "TorchServe","vLLM Inference","TGI (Text Generation Inference)","Model Pruning",
 "Weight Quantization (INT8, FP16, AWQ, GPTQ)","Knowledge Distillation",
 # Computer Vision (CV)
 "OpenCV","TorchVision","YOLO (You Only Look Once)","Detectron2","MediaPipe",
 "Image Segmentation","Object Detection","Face Recognition",
 "Optical Character Recognition (OCR)","Vision-Language Models (VLMs)",
 "Image Classification","Video Processing","Feature Extraction",
 # ML Architecture Concepts
 "Transformer Internals","Convolutional Neural Networks (CNNs)",
 "Recurrent Neural Networks (RNNs)","Long Short-Term Memory (LSTM)",
 "Generative Adversarial Networks (GANs)","Diffusion Models","Autoencoders",
 "Recommender Systems","Collaborative Filtering","Matrix Factorization",
 "Deep & Cross Networks","Learning-to-Rank (LambdaMART)","Two-Tower Embedding Networks",
 "Contextual Multi-Armed Bandits","Reinforcement Learning (Q-learning, PPO, Deep Q-Networks)",
 # ML Evaluation & Lifecycle
 "Confusion Matrix","ROC-AUC","Precision-Recall","F1-Score","Mean Absolute Error (MAE)",
 "Root Mean Squared Error (RMSE)","NDCG (Normalized Discounted Cumulative Gain)",
 "MAP (Mean Average Precision)","Click-Through Rate (CTR)","Intersect over Union (IoU)",
 "mAP (mean Average Precision for CV)","BLEU score","ROUGE score","Perplexity",
 # Distributed Compute & Processing
 "Apache Spark","PySpark","Spark Streaming","Apache Flink","Apache Beam","MapReduce",
 "Hadoop",
 # Data Lakehouse & File Formats
 "Delta Lake","Apache Iceberg","Apache Hudi","Parquet","ORC","Avro","Protobuf",
 "Data Lakes","Modern Data Stack (MDS)",
 # Cloud Data Warehouses
 "Snowflake","Google BigQuery","Amazon Redshift","Azure Synapse Analytics","Databricks",
 # Data Transformation & Modeling
 "dbt (data build tool)","Data Vault 2.0","Star Schema","Snowflake Schema",
 "Dimensional Modeling","Fact and Dimension Tables",
 "Slowing Changing Dimensions (SCD Type 1/2/3)","Data Lineage",
 # Workflow Orchestration
 "Apache Airflow","Prefect","Dagster","Luigi","AWS Step Functions",
 # Data Validation & Quality
 "Great Expectations","deequ","Soda","Data Quality Monitoring","Anomaly Alerting",
 # Metadata & Governance
 "Apache Atlas","Amundsen","DataHub","Collibra","Data Cataloging","Schema Registry",
 "Schema Evolution","Dead-Letter Queues (DLQ)",
 # RDBMS
 "PostgreSQL","MySQL","Microsoft SQL Server","Oracle Database","CockroachDB","Spanner",
 # NoSQL
 "MongoDB","Cassandra","Apache HBase","Couchbase","DynamoDB","Amazon DocumentDB",
 # Vector & Graph
 "Pinecone","Milvus","Qdrant","Weaviate","pgvector","ChromaDB","FAISS","Neo4j",
 "Amazon Neptune","ArangoDB","GraphDB","Cypher Query Language",
 # Caching
 "Redis","Memcached","Redis Insight","Semantic Caching","Distributed Caching",
 # Object Storage
 "AWS S3","Google Cloud Storage (GCS)","Azure Blob Storage","MinIO",
 # Time-Series & Search Storage
 "Elasticsearch","OpenSearch","InfluxDB","TimescaleDB","ClickHouse",
 # Backend Frameworks
 "FastAPI","Django","Flask","Spring Boot","Go Gin","NestJS","Express.js",
 "ASP.NET Core","Ruby on Rails",
 # API Design
 "RESTful APIs","GraphQL","gRPC","WebSockets","SOAP","Webhooks","API Contract Versioning",
 "OpenAPI / Swagger","Protocol Buffers (Protobuf)",
 # Messaging & Event Streaming
 "Apache Kafka","RabbitMQ","Amazon SQS/SNS","Apache Pulsar","Redis Pub/Sub",
 "Event-Driven Architecture","Asynchronous Job Queues","Publish-Subscribe Pattern",
 "Exactly-Once Processing (EOP)",
 # Systems Architecture
 "Microservices Architecture","Monolithic Architecture","Clean Architecture",
 "Domain-Driven Design (DDD)","Event Sourcing","CQRS (Command Query Responsibility Segregation)",
 "Idempotency","Concurrency Control","Multithreading","Asynchronous Programming",
 "Distributed Locking","Connection Pooling","Database Indexing (B-Tree, GIN, GiST)",
 "Query Execution Plans","Circuit Breakers","Bulkheads",
 # Security & Access
 "OAuth2","OpenID Connect (OIDC)","JWT (JSON Web Tokens)","SAML",
 "Role-Based Access Control (RBAC)","Attribute-Based Access Control (ABAC)",
 "Multi-Tenancy Isolation","API Gateways (Kong, AWS API Gateway, Apigee)","CORS",
 "XSS Prevention","CSRF Protection","Rate Limiting","Token Bucket Algorithm",
 "Leaky Bucket Algorithm",
 # Infra / Orchestration
 "Docker","Kubernetes (K8s)","Helm Charts","Kustomize","Podman","Containerd",
 "Amazon ECS",
 # IaC
 "Terraform","Terragrunt","AWS CloudFormation","Pulumi","Ansible",
 # CI/CD
 "GitHub Actions","GitLab CI/CD","Jenkins","ArgoCD","CircleCI","Tekton","Spinnaker",
 # Cloud
 "Amazon Web Services (AWS)","Google Cloud Platform (GCP)","Microsoft Azure",
 # Observability
 "OpenTelemetry (OTel)","Prometheus","Grafana","Datadog","New Relic","Dynatrace",
 "ELK Stack (Elasticsearch, Logstash, Kibana)","Splunk","Jaeger","Zipkin",
 "Distributed Tracing","Metrics","Centralized Logging","Alertmanager",
 # SRE
 "Service Level Objectives (SLOs)","Service Level Indicators (SLIs)",
 "Service Level Agreements (SLAs)","Chaos Engineering (Gremlin, Chaos Mesh)",
 "Disaster Recovery (DR)","Multi-Region Failover","High Availability (HA)",
 "Load Balancing (NGINX, HAProxy, AWS ALB)","Zero-Downtime Deployment (Blue-Green, Canary, Rolling)",
 "Circuit Breaking","Capacity Planning","Blameless Post-Mortems","Root-Cause Analysis (RCA)",
 # Systems Programming & Linux
 "Linux Internals","System Calls (syscalls)","eBPF","Systemd","Network I/O (epoll, kqueue)",
 "Inter-Process Communication (IPC)","Shared Memory","POSIX Threads",
 "Memory Management (Garbage Collection Tuning, Heap/Stack)","Bash Scripting",
 # Statistical Analysis
 "Hypothesis Testing","p-values","t-test","ANOVA","Chi-Square Test","Confidence Intervals",
 "Statistical Power","Sample Size Estimation","Central Limit Theorem","Bayesian Statistics",
 "Markov Chain Monte Carlo (MCMC)","Probability Distributions (Normal, Binomial, Poisson, Exponential)",
 # Experimentation
 "Multivariate Testing (MVT)","Split Testing","Multi-Armed Bandits","Sequential Testing",
 "Variance Reduction","CUPED (Controlled Experiments Utilization of Over-Sampled Pre-Experiment Data)",
 "Sample Ratio Mismatch (SRM) Detection","A/A Testing","Novelty Effects","Primacy Effects",
 "Cohort Analysis",
 # Causal Inference
 "Quasi-Experiments","Synthetic Controls","Difference-in-Differences (DiD)",
 "Propensity Score Matching (PSM)","Regression Discontinuity Design (RDD)",
 "Instrumental Variables","Structural Equation Modeling (SEM)",
 "Directed Acyclic Graphs (DAGs)","PyMC","DoWhy",
 # Analytical Modeling
 "Time-Series Forecasting","ARIMA","Prophet","NeuralProphet","Exponential Smoothing",
 "Multivariate Regression","Logistic Regression","Linear Regression","Anomaly Detection",
 "Isolation Forest","One-Class SVM","Mahalanobis Distance","Propensity Modeling",
 "Churn Prediction","Customer Lifetime Value (CLV) Modeling","Customer Segmentation",
 "Factor Analysis","Principal Component Analysis (PCA)","t-SNE","UMAP",
 # Data Visualization & BI
 "Looker","Tableau","Power BI","Matplotlib","Seaborn","Plotly","Shiny","Streamlit",
 "Dash","Exploratory Data Analysis (EDA)",
 # SDE Core
 "Data Structures & Algorithms (DSA)","Big O Notation","Array","Linked List","Stack",
 "Queue","Hash Table","Binary Tree","Heap","Graph Algorithms (BFS, DFS, Dijkstra, A* Search)",
 "Sorting and Searching","Dynamic Programming","Greedy Algorithms","Recursion",
 # Design Principles & Patterns
 "SOLID Principles","Object-Oriented Design (OOD)","Creational Patterns (Singleton, Factory, Builder)",
 "Structural Patterns (Adapter, Decorator, Facade, Proxy)",
 "Behavioral Patterns (Observer, Strategy, State, Command)","DRY (Don't Repeat Yourself)",
 "KISS (Keep It Simple, Stupid)","YAGNI (You Aren't Gonna Need It)",
 # Testing & Automation
 "Test-Driven Development (TDD)","Behavior-Driven Development (BDD)","Unit Testing",
 "Integration Testing","End-to-End (E2E) Testing","Contract Testing","Mutation Testing",
 "Playwright","Cypress","Selenium","JUnit","PyTest","Mocha","Jest","JMeter","k6","Locust",
 "WireMock","Mockito",
 # Full-Stack & Web
 "TypeScript","React","Next.js","Angular","Vue.js","Redux","Context API","Zustand",
 "TailwindCSS","Material-UI","Webpack","Vite","Server-Side Rendering (SSR)",
 "Static Site Generation (SSG)","Client-Side Rendering (CSR)","WebSockets",
 "Server-Sent Events (SSE)","Progressive Web Apps (PWA)","LocalStorage","SessionStorage",
 "Service Workers",
 # Mobile
 "React Native","Flutter","Swift","SwiftUI","Kotlin","Jetpack Compose","Objective-C",
 "Android Studio","Xcode","Mobile App Lifecycle","Push Notifications",
 "App Store / Play Store Deployment Pipelines",
 # Dev Workflow
 "Git","GitHub","GitLab","Bitbucket","Git-flow","Semantic Versioning (SemVer)",
 "Monorepos (Turborepo, Nx)","Code Reviews","Trunk-Based Development",
 "Feature Flags / Feature Toggles",
 # Agile
 "Scrum","Kanban","Scrumban","SAFe (Scaled Agile Framework)",
 # PM Tools
 "Jira","Confluence","Linear","Trello","Asana","Notion",
 # Engineering Management
 "Request for Comments (RFCs)","Technical Design Documents (TDDs)",
 "Architecture Decision Records (ADRs)","Capacity Planning","Sprint Planning",
 "Story Point Estimation","Burndown Charts","Velocity Tracking","Retrospectives",
 "Code Ownership","Technical Debt Management",
]
