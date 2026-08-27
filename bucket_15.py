from kw import KEYWORDS

# ---- 1) Classify all 496 keywords into 13 non-overlapping clusters (first rule wins) ----
def cluster_of(kw):
    k = kw.lower()
    # LLM integration + foundation models + core concepts
    if any(t in k for t in ["langchain","llamaindex","langgraph","autogen","crewai","instructor",
        "pydantic","vllm","hugging face","ollama","lm studio","openai","anthropic","gemini","cohere",
        "mistral","meta llama","deepseek","flux","midjourney","rag","semantic search","hybrid search",
        "document chunking","semantic caching","prompt","system prompts","few-shot","chain-of-thought",
        "function calling","agentic","tool usage","autonomous agents","multi-agent","synthetic data",
        "context window","hallucination","guardrails","output parsing","structural validation"]):
        return "llm"
    # training / alignment / distributed training / optimization / inference
    if any(t in k for t in ["sft","rlhf","dpo","lora","qlora","peft","spacy","nltk","gensim","tokeniz",
        "ner","intent class","sentiment","dependency parsing","word embeddings","sentence transformer",
        "dialog state","deepspeed","ray ","megatron","flashattention","fsdp","tensor parallel","pipeline parallel",
        "horovod","pytorch lightning","tensorrt","onnx","openvino","triton","ray serve","torchserve",
        "tgi","model pruning","weight quant","knowledge distill","transformer internals","cnns","rnns",
        "lstm","gans","diffusion","autoencoders","recommender","collaborative filtering","matrix factorization",
        "deep & cross","learning-to-rank","lambda","two-tower","contextual multi","q-learning","ppo","deep q",
        "confusion","roc-auc","precision-recall","f1","mae","rmse","ndcg","map","ctr","iou","map ","bleu",
        "rouge","perplexity","rasa","botpress","cognigy","voiceflow","azure ai language","amazon lex"]):
        return "ml"
    # computer vision
    if any(t in k for t in ["opencv","torchvision","yolo","detectron","mediapipe","image segmentation",
        "object detection","face recognition","ocr","vision-language","image classification","video processing",
        "feature extraction"]):
        return "cv"
    # distributed data / lakehouse / warehouse / transform / orchestration / validation / governance
    if any(t in k for t in ["spark","pyspark","flink","beam","mapreduce","hadoop","delta lake","iceberg",
        "hudi","parquet","orc","avro","protobuf","data lakes","modern data stack","snowflake","bigquery",
        "redshift","synapse","databricks","dbt","data vault","star schema","snowflake schema","dimensional",
        "fact and","scd","data lineage","airflow","prefect","dagster","luigi","step functions","great expectations",
        "deequ","soda","data quality","anomaly alerting","atlas","amundsen","datahub","collibra","data catalog",
        "schema registry","schema evolution","dead-letter"]):
        return "data"
    # datastores
    if any(t in k for t in ["postgresql","mysql","sql server","oracle","cockroachdb","spanner","mongodb",
        "cassandra","hbase","couchbase","dynamodb","documentdb","pinecone","milvus","qdrant","weaviate",
        "pgvector","chromadb","faiss","neo4j","neptune","arangodb","graphdb","cypher","redis","memcached",
        "redis insight","distributed caching","s3","gcs","azure blob","minio","elasticsearch","opensearch",
        "influxdb","timescaledb","clickhouse"]):
        return "store"
    # backend / api / messaging / architecture
    if any(t in k for t in ["fastapi","django","flask","spring boot","go gin","nestjs","express","asp.net",
        "rails","restful","graphql","grpc","websockets","soap","webhooks","api contract","openapi","swagger",
        "kafka","rabbitmq","sqs","sns","pulsar","pub/sub","event-driven","asynchronous job","publish-subscribe",
        "exactly-once","microservice","monolithic","clean architecture","domain-driven","event sourcing","cqrs",
        "idempotency","concurrency","multithreading","async programming","distributed locking","connection pooling",
        "database indexing","query execution","circuit breaker","bulkhead"]):
        return "backend"
    # security
    if any(t in k for t in ["oauth","oidc","jwt","saml","rbac","abac","multi-tenancy","api gateway","kong",
        "apigee","cors","xss","csrf","rate limiting","token bucket","leaky bucket"]):
        return "sec"
    # infra / devops / sre / linux
    if any(t in k for t in ["docker","kubernetes","helm","kustomize","podman","containerd","ecs","terraform",
        "terragrunt","cloudformation","pulumi","ansible","github actions","gitlab ci","jenkins","argocd",
        "circleci","tekton","spinnaker","aws","gcp","azure","otel","opentelemetry","prometheus","grafana",
        "datadog","new relic","dynatrace","elk","splunk","jaeger","zipkin","distributed tracing","metrics",
        "centralized logging","alertmanager","slo","sli","sla","chaos","disaster recovery","multi-region",
        "high availability","load balancing","zero-downtime","circuit breaking","capacity planning",
        "blameless","root-cause","linux internals","system calls","ebpf","systemd","network i/o","ipc",
        "shared memory","posix","memory management","bash"]):
        return "infra"
    # stats / experimentation / causal
    if any(t in k for t in ["hypothesis testing","p-value","t-test","anova","chi-square","confidence",
        "statistical power","sample size","central limit","bayesian","markov chain","probability distrib",
        "multivariate","split testing","multi-armed bandit","sequential testing","variance reduction","cuped",
        "sample ratio","a/a","novelty","primacy","cohort","quasi-experiment","synthetic control","difference-in",
        "propensity score","regression discontinuity","instrumental","structural equation","dag","pymc","dowhy"]):
        return "stats"
    # viz / bi
    if any(t in k for t in ["looker","tableau","power bi","matplotlib","seaborn","plotly","shiny","streamlit",
        "dash","exploratory data"]):
        return "viz"
    # sde core / fullstack / mobile / dev workflow / agile
    if any(t in k for t in ["data structures","big o","array","linked list","stack","queue","hash table",
        "binary tree","heap","graph algo","sorting","dynamic programming","greedy","recursion","solid",
        "object-oriented","creational","structural patterns","behavioral","dry","kiss","yagni","tdd","bdd",
        "unit testing","integration testing","end-to-end","contract testing","mutation","playwright","cypress",
        "selenium","junit","pytest","mocha","jest","jmeter","k6","locust","wiremock","mockito","typescript",
        "react","next.js","angular","vue","redux","context api","zustand","tailwind","material-ui","webpack",
        "vite","server-side rendering","static site","client-side","progressive web","localstorage",
        "sessionstorage","service workers","react native","flutter","swift","swiftui","kotlin","jetpack",
        "objective-c","android studio","xcode","mobile app","push notifications","app store","git","github",
        "gitlab","bitbucket","git-flow","semver","monorepos","turborepo","nx","code reviews","trunk-based",
        "feature flags","scrum","kanban","scrumban","safe","jira","confluence","linear","trello","asana",
        "notion","rfc","technical design","adr","sprint planning","story point","burndown","velocity",
        "retrospective","code ownership","technical debt"]):
        return "sde"
    return "sde"  # fallback (should be none)

clusters = {}
unmatched=[]
for kw in KEYWORDS:
    c = cluster_of(kw)
    clusters.setdefault(c, []).append(kw)
    if c == "sde" and kw.lower() not in " ".join(clusters["sde"]).lower():
        pass
total = sum(len(v) for v in clusters.values())
print("CLUSTER SIZES (must sum to 496):")
for c,v in sorted(clusters.items(), key=lambda x:-len(x[1])):
    print(f"  {c:8} {len(v)}")
print("  TOTAL", total, "(expected 496)\n")

CLSIZE = {c: len(v) for c, v in clusters.items()}

# ---- 2) 16 business objectives, each a FULL-STACK enterprise AI platform ----
# relevance: 1.0 core, 0.8 support, 0.0 peripheral (excluded from match count)
# All ideas are full-stack, so most clusters = 1.0/0.8; a few peripherals differ -> score spread.
ideas = {
 "AEGIS — Autonomous Enterprise Control Plane": dict(
   core=["llm","sec","backend","infra","data","store"], support=["ml","sde","stats"], periph=[],
   objective="The mandatory control layer every AI system in the enterprise routes through: signed agent "
             "identities, fail-closed policy, immutable audit, budget caps. Owns: 'no AI action is "
             "unauthorized, unaudited, or unbudgeted.'"),
 "REVENUEIQ — AI Revenue & Pipeline Engine": dict(
   core=["llm","ml","data","store","viz"], support=["backend","infra","stats","sde"], periph=[],
   objective="Reads every email, call, and CRM note; scores live deal risk; drafts the next-best-action; "
             "warns before a quarter slips. Owns: 'the forecast is real and the pipeline is worked.'"),
 "SUPPLYFLOW — AI Supply Chain Brain": dict(
   core=["ml","data","stats","store"], support=["llm","infra","backend","viz"], periph=[],
   objective="Forecasts demand per SKU, flags stockout/overstock, recommends reorders with cost tradeoffs, "
             "and simulates disruptions. Owns: 'we stop bleeding cash on inventory and stockouts.'"),
 "FINANCECLOSE — AI Finance & Close Engine": dict(
   core=["llm","data","store","ml"], support=["backend","infra","stats","sec"], periph=[],
   objective="Reconciles accounts, flags ledger anomalies, drafts cited journal entries, shortens close. "
             "Owns: 'month-end close is faster, cleaner, and audit-ready.'"),
 "PRODUCTECHO — AI Customer Signal Engine": dict(
   core=["ml","llm","data","store"], support=["cv","stats","backend","infra","viz"], periph=[],
   objective="Ingests reviews, tickets, calls, and social; clusters recurring pain; routes to product/eng "
             "with evidence. Owns: 'we know what customers hate before they churn.'"),
 "MARKETGEN — AI Go-To-Market Engine": dict(
   core=["llm","ml","stats","data"], support=["store","backend","infra","viz","sde"], periph=[],
   objective="Generates and A/B-tests campaigns, segments audiences by behavior, measures lift with causal "
             "methods. Owns: 'marketing spend is measurable and compounding.'"),
 "CAREIQ — AI Patient & Clinical Intelligence": dict(
   core=["cv","ml","llm","store","sec"], support=["data","backend","infra","stats"], periph=[],
   objective="Grounded clinical summarization from notes and imaging, with mandatory citations and a "
             "human review queue. Owns: 'clinicians act on evidence, not hallucinations.'"),
 "LEGALFORGE — AI Legal & Contract Intelligence": dict(
   core=["llm","ml","store","sec"], support=["data","backend","infra","sde"], periph=[],
   objective="System of record for every obligation: extracts clauses, flags money-leak risk, tracks "
             "renewal/penalty dates, alerts before breach. Owns: 'we never get burned by a clause.'"),
 "PEOPLEIQ — AI Talent & Workforce Engine": dict(
   core=["ml","llm","data","store"], support=["backend","infra","stats","sde"], periph=[],
   objective="Screens and ranks candidates against real role signal, removes bias drift, drafts structured "
             "interview plans. Owns: 'we hire faster and fairer.'"),
 "RISKSHIELD — AI Risk & Compliance Engine": dict(
   core=["sec","ml","data","store","llm"], support=["backend","infra","stats","sde"], periph=[],
   objective="Continuous control monitoring across systems: policy drift, data-residency, audit evidence "
             "on tap. Owns: 'we are always audit-ready, not audit-scrambling.'"),
 "FACTORYEDGE — AI Manufacturing & Quality Engine": dict(
   core=["cv","ml","data","store"], support=["llm","infra","backend","stats"], periph=[],
   objective="Vision QA on the line, predictive maintenance from sensor streams, defect root-cause. "
             "Owns: 'defects caught at the source, downtime predicted.'"),
 "ENERGYOPT — AI Grid & Energy Optimization": dict(
   core=["ml","data","stats","store"], support=["llm","infra","backend","viz"], periph=[],
   objective="Load forecasting, renewable dispatch optimization, anomaly detection on grid telemetry. "
             "Owns: 'we balance the grid cheaper and greener.'"),
 "RETAILBRAIN — AI Merchandising & Store Ops": dict(
   core=["ml","llm","data","store","cv"], support=["stats","backend","infra","viz"], periph=[],
   objective="Demand-aware assortment, shelf recognition via vision, dynamic pricing, lost-sales detection. "
             "Owns: 'shelves match demand and margins improve.'"),
 "LOGISTICSAI — AI Logistics & Fleet Engine": dict(
   core=["ml","data","store","stats"], support=["llm","infra","backend","viz"], periph=[],
   objective="Route optimization, ETA prediction, warehouse robotics orchestration, exception handling. "
             "Owns: 'every parcel moves on the optimal path.'"),
 "CITIZENGOV — AI Public Services & Civic Engine": dict(
   core=["llm","ml","data","store","sec"], support=["cv","backend","infra","stats","sde"], periph=[],
   objective="Citizen-facing assistants grounded in statute, benefits eligibility, document intake with "
             "fairness guards. Owns: 'public services answer accurately and equitably.'"),
 "CODEWEAVER — AI Engineering Velocity Engine": dict(
   core=["llm","ml","backend","sde"], support=["data","store","infra","stats"], periph=[],
   objective="Reviews PRs for risk, suggests fixes, maps debt, predicts delivery from velocity. "
             "Owns: 'we ship faster with fewer escapes.'"),
}

rows=[]
for name, d in ideas.items():
    matched=0
    detail=[]
    for c, size in CLSIZE.items():
        if c in d["core"]: w=1.0
        elif c in d["support"]: w=0.8
        else: w=0.0
        matched += int(round(size*w))
        detail.append(f"{c}:{size}x{w}")
    pct = matched/total*100
    rows.append((name, matched, pct, d["objective"], detail))

rows.sort(key=lambda x:-x[2])
print(f"{'#':2} {'PRODUCT':46}{'MATCH':>10}{'SCORE':>7}")
for i,(n,m,p,o,det) in enumerate(rows,1):
    print(f"{i:2} {n:46}{f'{m}/{total}':>10}{p:6.1f}%")
print("\n--- DETAIL (business objective + cluster match breakdown) ---")
for i,(n,m,p,o,det) in enumerate(rows,1):
    print(f"\n{i}. {n}  ->  {m}/{total} keywords ({p:.1f}%)")
    print(f"   OBJECTIVE: {o}")
    print(f"   CLUSTER MATCH: {', '.join(det)}")
