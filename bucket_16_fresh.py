from kw import KEYWORDS

# ---- cluster classifier (same 13-cluster split, sizes sum to 496) ----
def cluster_of(kw):
    k = kw.lower()
    if any(t in k for t in ["langchain","llamaindex","langgraph","autogen","crewai","instructor",
        "pydantic","vllm","hugging face","ollama","lm studio","openai","anthropic","gemini","cohere",
        "mistral","meta llama","deepseek","flux","midjourney","rag","semantic search","hybrid search",
        "document chunking","semantic caching","prompt","system prompts","few-shot","chain-of-thought",
        "function calling","agentic","tool usage","autonomous agents","multi-agent","synthetic data",
        "context window","hallucination","guardrails","output parsing","structural validation"]):
        return "llm"
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
    if any(t in k for t in ["opencv","torchvision","yolo","detectron","mediapipe","image segmentation",
        "object detection","face recognition","ocr","vision-language","image classification","video processing",
        "feature extraction"]):
        return "cv"
    if any(t in k for t in ["spark","pyspark","flink","beam","mapreduce","hadoop","delta lake","iceberg",
        "hudi","parquet","orc","avro","protobuf","data lakes","modern data stack","snowflake","bigquery",
        "redshift","synapse","databricks","dbt","data vault","star schema","snowflake schema","dimensional",
        "fact and","scd","data lineage","airflow","prefect","dagster","luigi","step functions","great expectations",
        "deequ","soda","data quality","anomaly alerting","atlas","amundsen","datahub","collibra","data catalog",
        "schema registry","schema evolution","dead-letter"]):
        return "data"
    if any(t in k for t in ["postgresql","mysql","sql server","oracle","cockroachdb","spanner","mongodb",
        "cassandra","hbase","couchbase","dynamodb","documentdb","pinecone","milvus","qdrant","weaviate",
        "pgvector","chromadb","faiss","neo4j","neptune","arangodb","graphdb","cypher","redis","memcached",
        "redis insight","distributed caching","s3","gcs","azure blob","minio","elasticsearch","opensearch",
        "influxdb","timescaledb","clickhouse"]):
        return "store"
    if any(t in k for t in ["fastapi","django","flask","spring boot","go gin","nestjs","express","asp.net",
        "rails","restful","graphql","grpc","websockets","soap","webhooks","api contract","openapi","swagger",
        "kafka","rabbitmq","sqs","sns","pulsar","pub/sub","event-driven","asynchronous job","publish-subscribe",
        "exactly-once","microservice","monolithic","clean architecture","domain-driven","event sourcing","cqrs",
        "idempotency","concurrency","multithreading","async programming","distributed locking","connection pooling",
        "database indexing","query execution","circuit breaker","bulkhead"]):
        return "backend"
    if any(t in k for t in ["oauth","oidc","jwt","saml","rbac","abac","multi-tenancy","api gateway","kong",
        "apigee","cors","xss","csrf","rate limiting","token bucket","leaky bucket"]):
        return "sec"
    if any(t in k for t in ["docker","kubernetes","helm","kustomize","podman","containerd","ecs","terraform",
        "terragrunt","cloudformation","pulumi","ansible","github actions","gitlab ci","jenkins","argocd",
        "circleci","tekton","spinnaker","aws","gcp","azure","otel","opentelemetry","prometheus","grafana",
        "datadog","new relic","dynatrace","elk","splunk","jaeger","zipkin","distributed tracing","metrics",
        "centralized logging","alertmanager","slo","sli","sla","chaos","disaster recovery","multi-region",
        "high availability","load balancing","zero-downtime","circuit breaking","capacity planning",
        "blameless","root-cause","linux internals","system calls","ebpf","systemd","network i/o","ipc",
        "shared memory","posix","memory management","bash"]):
        return "infra"
    if any(t in k for t in ["hypothesis testing","p-value","t-test","anova","chi-square","confidence",
        "statistical power","sample size","central limit","bayesian","markov chain","probability distrib",
        "multivariate","split testing","multi-armed bandit","sequential testing","variance reduction","cuped",
        "sample ratio","a/a","novelty","primacy","cohort","quasi-experiment","synthetic control","difference-in",
        "propensity score","regression discontinuity","instrumental","structural equation","dag","pymc","dowhy"]):
        return "stats"
    if any(t in k for t in ["looker","tableau","power bi","matplotlib","seaborn","plotly","shiny","streamlit",
        "dash","exploratory data"]):
        return "viz"
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
    return "sde"

clusters = {}
for kw in KEYWORDS:
    clusters.setdefault(cluster_of(kw), []).append(kw)
CLSIZE = {c: len(v) for c, v in clusters.items()}
assert sum(CLSIZE.values()) == 496, sum(CLSIZE.values())

# ---- 16 FRESH, NON-SECURITY enterprise AI business ideas ----
# Each is a full-stack platform. core=1.0, support=0.8, periph=0.0
# uniqueness = market novelty (few incumbents / novel framing), 0-10
# individuality = owns its own data type + core engine + buyer + metric, 0-10
ideas = [
 ("SPENDCAP — AI Spend & Token Governance",
   dict(core=["infra","backend","data","store","llm"],
        support=["ml","sde","stats","sec"], periph=["cv","viz"],
        objective="Controls cloud/LLM token and API consumption like a financial discipline: per-BU budgets, "
                  "peer price benchmarks, TCO with human-oversight labor, contract repricing alerts. "
                  "Owns: 'AI spend is forecastable and accountable.'",
        uniqueness=9.2, individuality=9.0,
        buyer="CFO / IT Procurement", metric="$ saved vs forecast",
        why="NPI: AI spend +108% YoY, 85% miss forecasts; SpendHound: half can't show ROI. No dominant player.")),
 ("CONTRACTLOGIC — Data Contracts & Quality Shift-Left",
   dict(core=["data","store","backend","infra"],
        support=["ml","sde","llm","stats"], periph=["cv","sec","viz"],
        objective="Machine-enforced data contracts at the source: schema, semantics, quality SLOs, ownership, "
                  "feedback loops that trace impact. Owns: 'data is trustable before it is used.'",
        uniqueness=8.0, individuality=8.5,
        buyer="Data Engineering / Platform", metric="incidents prevented",
        why="Ataccama shift-left playbook; data contracts emerging but few enforce-at-source platforms.")),
 ("SYNTHETICA — Privacy-Safe Synthetic Data Facility",
   dict(core=["ml","data","store","llm"],
        support=["infra","backend","sde","cv","stats"], periph=["sec","viz"],
        objective="Generates privacy-safe synthetic datasets for dev/test/rare-event training with lineage and "
                  "quality gates. Owns: 'ship realistic data with zero PII exposure.'",
        uniqueness=8.5, individuality=8.7,
        buyer="ML Platform / Privacy", metric="privacy score + coverage",
        why="Synthetic data services market $0.42B->$2.27B by 2031 (32.8% CAGR); suppliers moving to governance.")),
 ("CAUSALA — Causal Experimentation Engine",
   dict(core=["stats","data","store","ml"],
        support=["backend","infra","sde","llm"], periph=["cv","sec","viz"],
        objective="Warehouse-native causal ML: heterogeneous treatment effects, CATE, DAG discovery, "
                  "holdout validation. Owns: 'we know what actually caused the lift.'",
        uniqueness=8.8, individuality=9.0,
        buyer="CDO / Growth", metric="causal lift ($)",
        why="RootCause/Argenta show demand; most dashboards are correlational, causal at enterprise scale is rare.")),
 ("GREENLEDGER — AI ESG & Sustainability Reporting",
   dict(core=["data","store","backend","llm"],
        support=["ml","infra","sde","stats","viz"], periph=["cv","sec"],
        objective="Aggregates ESG data, computes carbon accounting, drafts audit-ready disclosures with "
                  "human-held accountability. Owns: 'disclosure is fast and defensible.'",
        uniqueness=7.5, individuality=8.0,
        buyer="Sustainability / Finance", metric="audit-ready reports",
        why="BCG: AI ESG value blocked by lack of structured integration, not tool availability.")),
 ("MATTERFORGE — Self-Driving Lab for Materials R&D",
   dict(core=["ml","cv","data","store"],
        support=["llm","infra","backend","sde","stats"], periph=["sec","viz"],
        objective="Closed-loop lab: LLM+Bayesian proposal of candidates, robot execution, DFT verification, "
                  "drift-corrected knowledge base. Owns: 'we run 1000 experiments a day.'",
        uniqueness=9.0, individuality=8.8,
        buyer="R&D / Materials Science", metric="candidates validated/day",
        why="Self-driving labs emerging; synthesisability gap (<2% realized) is open. Few platforms.")),
 ("MEMORYVAULT — Enterprise Agent Memory & Knowledge Fabric",
   dict(core=["llm","data","store","backend","infra"],
        support=["ml","sde","stats"], periph=["cv","sec","viz"],
        objective="Database-native scoped memory for agents and humans: extraction, consolidation, retrieval "
                  "under role scope, revision lifecycle. Owns: 'institutional knowledge is queryable, not social.'",
        uniqueness=9.3, individuality=9.1,
        buyer="CIO / Engineering", metric="rediscovery time cut",
        why="Oracle Agent Memory + Thoughtworks knowledge fabric + institutional KG papers all 2026; very new.")),
 ("TWINTRUTH — Digital Twin Drift & ROI Validator",
   dict(core=["data","store","ml","infra"],
        support=["backend","sde","llm","stats","viz"], periph=["cv","sec"],
        objective="Continuously validates twin fidelity vs reality, detects model drift, and models business "
                  "case before twin build. Owns: 'the twin is true and worth building.'",
        uniqueness=8.6, individuality=8.6,
        buyer="Ops / Engineering", metric="drift detected early",
        why="Research: model drift is #1 twin failure; ROI prediction is the top unmet buyer concern.")),
 ("UNDERWRITEAI — Insurance Underwriting & Claims Agentic",
   dict(core=["llm","ml","data","store","backend"],
        support=["infra","sde","stats","sec"], periph=["cv","viz"],
        objective="Agentic workbench for submission-to-quote and FNOL: intake, triage, enrich, decision-ready "
                  "with human review. Owns: 'quote faster, leak less.'",
        uniqueness=6.5, individuality=7.5,
        buyer="P&C Insurer", metric="loss-ratio improvement",
        why="Duck Creek/Guidewire/NTT DATA all shipping agentic; angle is execution-layer, still differentiating.")),
 ("FINCORE — Transaction Behavior Foundation Model",
   dict(core=["ml","data","store","backend"],
        support=["llm","infra","sde","stats"], periph=["cv","sec","viz"],
        objective="Pretrains a transformer on transaction sequences; one backbone for credit, LTV, segmentation, "
                  "next-best-action. Owns: 'behavior is one vector space.'",
        uniqueness=7.8, individuality=8.2,
        buyer="Risk / Data Science", metric="AP lift over XGBoost",
        why="NVIDIA: Stripe/Nubank/Visa training transaction FMs; platform play (not in-house) is open.")),
 ("AGRIBRAIN — AI Agriculture & Crop Intelligence",
   dict(core=["cv","ml","data","store"],
        support=["llm","infra","backend","sde","stats"], periph=["sec","viz"],
        objective="Satellite + field-vision yield prediction, disease detection, irrigation optimization, "
                  "harvest planning. Owns: 'yield up, input cost down.'",
        uniqueness=7.0, individuality=7.8,
        buyer="Agronomy / Farm Ops", metric="yield %",
        why="Agtech exists but CV+foundation-model crop intelligence at mid-market is underbuilt.")),
 ("MEDDISCOVERY — AI Drug / Molecule Discovery",
   dict(core=["ml","data","store","llm"],
        support=["cv","infra","backend","sde","stats"], periph=["sec","viz"],
        objective="Literature-mined, generative molecule proposal with synthesis-aware planning and closed-loop "
                  "lab verification. Owns: 'hit candidates in weeks, not years.'",
        uniqueness=8.2, individuality=8.3,
        buyer="Pharma R&D", metric="credible hits",
        why="Inverse-design + synthesis-first paradigm shift; discovery-credibility ladder is 2026 hot topic.")),
 ("CLIMATESIM — Climate & Physical-Risk Modeling",
   dict(core=["ml","data","store","infra"],
        support=["llm","backend","sde","stats","viz"], periph=["cv","sec"],
        objective="Models asset-level physical risk (flood, heat, storm) and transition scenarios for disclosure "
                  "and resilience planning. Owns: 'we can price climate exposure.'",
        uniqueness=8.0, individuality=8.1,
        buyer="Risk / ESG", metric="exposure $",
        why="Physical-risk disclosure demand rising; few AI-native scenario engines.")),
 ("EDUCOG — AI Adaptive Learning & Education",
   dict(core=["llm","ml","data","store"],
        support=["backend","infra","sde","stats","cv"], periph=["sec","viz"],
        objective="Models each learner, generates adaptive paths and assessments, measures outcome gains with "
                  "causal methods. Owns: 'learners finish and retain more.'",
        uniqueness=6.8, individuality=7.4,
        buyer="L&D / EdTech", metric="outcome gain",
        why="Adaptive learning crowded in K-12; enterprise upskilling + causal measurement is fresher.")),
 ("PROPTECHIQ — Real Estate & Property AI",
   dict(core=["llm","data","store","backend"],
        support=["ml","infra","sde","cv","stats"], periph=["sec","viz"],
        objective="Unifies listings, valuations, vision inspection, and demand forecasting into a property "
                  "graph with decision assist. Owns: 'priced right, maintained proactively.'",
        uniqueness=6.5, individuality=7.2,
        buyer="Real Estate / REITs", metric="ROI per asset",
        why="Proptech mature but AI-native unified property graph + vision inspection is still patchy.")),
 ("TELCOBRAIN — Telecom Network & Revenue AI",
   dict(core=["ml","data","store","infra"],
        support=["llm","backend","sde","stats","cv"], periph=["sec","viz"],
        objective="Network telemetry foundation models for churn prediction, QoE, fraud-lite anomaly, and "
                  "dynamic pricing. Owns: 'network pays for itself.'",
        uniqueness=7.2, individuality=7.6,
        buyer="NetOps / Revenue", metric="churn + QoE",
        why="Telco AI ops exists but unified telemetry foundation model + revenue loop is underbuilt.")),
]

# ---- compute match ----
rows = []
for name, d in ideas:
    match = 0.0
    for c, w in [("llm",1.0),("ml",1.0),("cv",1.0),("data",1.0),("store",1.0),
                 ("backend",1.0),("sec",1.0),("infra",1.0),("stats",1.0),("viz",1.0),("sde",1.0)]:
        if c in d["core"]: match += CLSIZE[c]*1.0
        elif c in d["support"]: match += CLSIZE[c]*0.8
        # periph => 0
    pct = match/496*100
    match10 = pct/10.0
    comp = (match10 + d["uniqueness"] + d["individuality"]) / 3.0
    rows.append((name, match, pct, d["uniqueness"], d["individuality"], comp, d))

rows.sort(key=lambda r: -r[5])
print("ALL 16 FRESH, NON-SECURITY. Sorted by composite (match+uniqueness+individuality)/3\n")
print(f"{'#':>2} {'PRODUCT':42} {'KWMAT':>6} {'UNIQ':>5} {'INDV':>5} {'COMP':>5}")
for i,(n,m,p,u,ind,comp,d) in enumerate(rows,1):
    print(f"{i:>2} {n[:42]:42} {m:>4.0f}/{496} {u:>5.1f} {ind:>5.1f} {comp:>5.2f}")

print("\n--- DETAIL (objective + buyer + metric + research why) ---")
for i,(n,m,p,u,ind,comp,d) in enumerate(rows,1):
    print(f"\n{i}. {n}  | KW {m:.0f}/496 ({p:.1f}%)  UNIQ {u}  INDV {ind}  COMP {comp:.2f}")
    print(f"   OBJECTIVE: {d['objective']}")
    print(f"   BUYER: {d['buyer']}   METRIC: {d['metric']}")
    print(f"   RESEARCH: {d['why']}")

# write markdown
md = "# 16 Fresh Enterprise AI Business Ideas (non-security, full keyword-universe coverage)\n\n"
md += "Method: all 496 keywords classified into 13 clusters. Each idea is a full-stack platform.\n"
md += "KW match = sum(cluster_size x weight)/496, weight core=1.0, support=0.8, peripheral=0.0.\n"
md += "Uniqueness = market novelty (few incumbents / novel framing). Individuality = owns its own data type + engine + buyer + metric.\n"
md += "Composite = (KW% as 0-10 + Uniqueness + Individuality)/3.\n\n"
md += "| # | Product | KW match | Uniqueness | Individuality | Composite |\n"
md += "|---|---------|----------|------------|---------------|-----------|\n"
for i,(n,m,p,u,ind,comp,d) in enumerate(rows,1):
    md += f"| {i} | {n} | {m:.0f}/496 ({p:.1f}%) | {u} | {ind} | {comp:.2f} |\n"
md += "\n## Detail\n\n"
for i,(n,m,p,u,ind,comp,d) in enumerate(rows,1):
    md += f"### {i}. {n}  (KW {m:.0f}/496, {p:.1f}% | UNIQ {u} | INDV {ind} | COMP {comp:.2f})\n"
    md += f"- **Objective:** {d['objective']}\n"
    md += f"- **Buyer:** {d['buyer']}  |  **Metric it owns:** {d['metric']}\n"
    md += f"- **Why now (research):** {d['why']}\n\n"

with open("BUCKET_16_FRESH.md","w") as f:
    f.write(md)
print("\nWROTE BUCKET_16_FRESH.md")
