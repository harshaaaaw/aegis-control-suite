from kw import KEYWORDS

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
    return "sde"

clusters = {}
for kw in KEYWORDS:
    clusters.setdefault(cluster_of(kw), []).append(kw)
CLSIZE = {c: len(v) for c, v in clusters.items()}
assert sum(CLSIZE.values()) == 496

# 15 BRAND-NEW ideas, each mined from a specific verified research gap.
# tuple: name, dict(core/support/periph), uniqueness, individuality, gap_source, check_vs_market, objective
ideas = [
 ("SWITCHPROOF — Model Migration Certification Harness",
   dict(core=["llm","sde","infra","data"], support=["backend","store","ml","stats"], periph=["cv","viz","sec"]),
   8.4, 8.8,
   "Fallbrook 2026: vendors re-tier models mid-contract; advice is 'build the evaluation harness with portability in mind'. Advice only, no product.",
   "Checked: eval tools (Arize, Weights&Biases) measure quality in general; nobody certifies BEHAVIOR PARITY for a vendor swap. Lock-in fear is documented on both US and China price-war coverage.",
   "Runs your real workload through old model and new model, diffs every behavioral change, issues a go/no-go certificate before you cut over. Owns: 'switching AI vendors is safe and provable.'"),

 ("OUTCOMEBASE — Outcome Metering & Verdict Engine",
   dict(core=["llm","backend","data","store","stats"], support=["sde","ml","infra","viz"], periph=["cv","sec"]),
   8.2, 9.0,
   "Fallbrook: outcome-based pricing (pay per successful resolution) is emerging and 'requires careful definition of success'. Unframe charges only on customer-declared satisfaction.",
   "Checked: usage-billing vendors (Metronome, Orb class) meter tokens and seats. Nobody meters DEFINED SUCCESS. Fusion of eval verdicts with billing is unowned.",
   "Turns 'success' into an executable contract, judges every AI interaction against it, and produces the billable verdict stream. Owns: 'AI gets paid for results, not tokens.'"),

 ("ORGMIRROR — Living Model of the Organization",
   dict(core=["data","llm","store","viz"], support=["ml","sde","backend","infra","stats"], periph=["cv","sec"]),
   8.6, 8.4,
   "Gartner runs DTO (Digital Twin of the Organization) platform evaluations; ProcureInsights shows the whole stack lacks a validation layer ('Phase 0'): nothing checks the model matches the real company.",
   "Checked: org-chart tools and process mining (Celonis class) capture snapshots. Continuous reality-sync plus drift alerts on decision rights and value flow: no product found.",
   "Ingests HR, ticketing, code, and money flows into a living org graph; alerts when reality drifts from the official model. Owns: 'leaders decide on the company as it IS.'"),

 ("FULLCOST — Pre-Signature AI Purchase Validator",
   dict(core=["llm","data","store","stats","viz"], support=["backend","sde","ml","infra"], periph=["cv","sec"]),
   7.6, 7.8,
   "NPI 2026: TCO rarely includes review labor, oversight shifts, forward-deployed-engineer time; 'math changes when oversight labor is added back'. Consultants do this by hand today.",
   "Checked: token-FinOps players watch runtime spend (taken). Pre-purchase business-case stress-testing with hidden-cost ledgers: no software found.",
   "Models any AI purchase with full hidden costs (human review hours, FDE days, repricing clauses) and shows break-even under stress. Owns: 'no AI deal signs on fantasy math.'"),

 ("PERMITFLOW — Regulatory Bottleneck Compressor for Built Assets",
   dict(core=["llm","data","store","backend","cv"], support=["ml","sde","infra","stats","viz"], periph=["sec"]),
   5.5, 7.4,
   "Thrive Holdings ($12B, OpenAI-backed) just launched a whole vertical on permits, inspection docs, compliance tracking. Pain confirmed at the highest capital level.",
   "Checked: giant entrant with $2B fresh. Honest verdict: validated market, contested NOW. Only angles left: mid-market focus or one geography done deeply (India/UK).",
   "Prepares, tracks, and chases approvals and inspection evidence for construction and infrastructure projects. Owns: 'projects stop dying in approval queues.'"),

 ("DUTYDATA — Incident Command for Data Quality",
   dict(core=["data","backend","infra","store"], support=["llm","sde","stats","ml","viz"], periph=["cv","sec"]),
   6.8, 7.8,
   "Ataccama's playbook ends at detect-triage-remediate; Grab had to BUILD Kinabalu internally because no product routes data incidents with ownership and postmortems.",
   "Checked: Monte Carlo/observability tools alert. Alert-to-resolution workflow (paging, ownership, blameless postmortems for data): thin product layer.",
   "Routes data incidents to owners with blast radius, SLAs, and postmortem records, PagerDuty-style. Owns: 'data fires get put out by process, not heroics.'"),

 ("ACTREADY — EU AI Act Conformity Evidence Pipeline",
   dict(core=["llm","sde","data","backend"], support=["infra","store","ml","stats","sec"], periph=["cv","viz"]),
   7.4, 7.6,
   "Verified in sweep: EU AI Act high-risk obligations take effect August 2026; documented provenance and auditability become mandatory. Timing is now.",
   "Checked: Vanta ($4.15B) automates general compliance frameworks; AI-Act-specific technical-evidence generation for AI SYSTEMS (not companies) is young territory.",
   "Collects, versions, and packages the technical documentation, test results, and provenance records high-risk AI systems must file. Owns: 'our AI ships legally, on schedule.'"),

 ("DATAREADY — AI Data Readiness Scorer",
   dict(core=["data","store","stats","ml"], support=["llm","backend","sde","infra","viz"], periph=["cv","sec"]),
   6.2, 7.0,
   "TechTarget/Drexel-Precisely 2026: 43% of data leaders name data readiness the TOP barrier to AI value, ahead of infra (42%) and skills (41%).",
   "Checked: assessments are sold as consulting. A repeatable scoring product (grade my pipelines/features/governance for AI use, with fix plan) barely exists.",
   "Scores every dataset and pipeline for AI-readiness against weighted criteria and emits a ranked remediation plan. Owns: 'we know exactly why our data blocks AI, and what fixes it first.'"),

 ("CERTCHAIN — Certified Data Product Registry",
   dict(core=["data","store","backend","llm"], support=["infra","sde","stats","ml","viz"], periph=["cv","sec"]),
   6.5, 7.4,
   "Grab's internal certification engine cut their most-used messy tables by 58% in a year. Proof that certification changes behavior. Most companies cannot build what Grab built.",
   "Checked: Ataccama and DataHub carry certification features; standalone cross-platform registry with query-routing-to-certified-only is still a narrow offer.",
   "Certifies data products against live contracts and lets consumers route queries to certified assets only. Owns: 'people and agents use certified data by default.'"),

 ("VOICESURE — Production QA for Voice Agents",
   dict(core=["llm","ml","sde","backend"], support=["infra","data","store","stats"], periph=["cv","viz","sec"]),
   7.0, 8.2,
   "ElevenLabs at $330M ARR and agentic FNOL launches show voice agents exploding. Your own Tier-A lead Phonely lives in this exact wave. QA for voice (interruptions, latency budgets, accent regressions) lags far behind text QA.",
   "Checked: a few young players circulate (Hamming.ai, Coval class) but the space is early and unconsolidated; flag: needs a deeper competitor pass before committing.",
   "Regression-tests voice agents across accents, noise, interruptions, and latency budgets before and after every deploy. Owns: 'no bad voice release reaches a customer.'"),

 ("EXPLOCK — Experiment Preregistration Governance",
   dict(core=["stats","data","backend","store"], support=["llm","sde","ml","viz","infra"], periph=["cv","sec"]),
   7.2, 8.4,
   "causal-agent and xpyrment (2026 OSS) both implement frozen designs and refuse post-hoc dressing. Science solved this years ago; enterprise experimentation still allows silent reruns.",
   "Checked: Statsig/LaunchDarkly/Optimizely RUN experiments; none enforce locked preregistration with tamper evidence across an enterprise portfolio.",
   "Freezes hypothesis, metrics, and stopping rules cryptographically before launch; any deviation is flagged, never silent. Owns: 'our win rates are real, provably.'"),

 ("TABLELIFE — Automated Data Lifecycle Manager",
   dict(core=["data","store","backend","infra"], support=["llm","sde","stats","viz","ml"], periph=["cv","sec"]),
   7.0, 7.6,
   "Grab built Ouroboros internally to retire tables by contract clauses; every large warehouse is a graveyard nobody dares clean because impact is unknown.",
   "Checked: catalogs list lineage; lifecycle ENFORCEMENT (safe retirement, archival, cost reclaim with blast-radius proof) is internal-tooling territory, unproductized.",
   "Proposes and executes safe retirement plans for dead tables, dashboards, and pipelines with full downstream proof. Owns: 'our data estate shrinks on purpose, safely.'"),

 ("GREENPROOF — Sustainability Claim Verification",
   dict(core=["llm","cv","data","store"], support=["ml","backend","infra","stats","sde"], periph=["viz","sec"]),
   7.6, 7.8,
   "Sweep verified greenwashing enforcement is now global (EU + regulators); Halkwinds documents satellite imagery and alt-data being used to CHECK corporate claims.",
   "Checked: rating agencies diverge and sell opinions; buyers and procurement teams lack an independent verification product for SUPPLIER claims.",
   "Verifies supplier environmental claims against satellite, regulatory, and media evidence; flags divergence before you sign. Owns: 'we never buy a fake green claim.'"),

 ("SYMBIONT — Hybrid Rules + LLM Decision Engine",
   dict(core=["llm","backend","ml","data"], support=["store","sde","infra","stats","sec"], periph=["cv","viz"]),
   6.6, 7.8,
   "Duck Creek ships neuro-symbolic reasoning for insurance because pure LLM decisions fail auditors. Pattern validated in one vertical; horizontal productization is open.",
   "Checked: rules engines (old world) and LLM stacks (new world) ship separately; a governed blend where determinism is mandatory and LLM fills judgment gaps: few horizontal offers.",
   "Routes each decision step to rules or model by policy, keeping an explainable trail end to end. Owns: 'regulated decisions get AI speed with audit-proof logic.'"),

 ("ASSUREDEAL — Warranty Layer for AI Pilot Outcomes",
   dict(core=["stats","llm","data","viz"], support=["backend","store","sde","ml","infra"], periph=["cv","sec"]),
   8.0, 7.2,
   "Unframe's pay-only-if-satisfied model converts at unusual rates; NPI reports buyers burned by pilots. Demand for risk transfer is visible on both sides of the table.",
   "Checked: nobody insures/warranties AI pilot outcomes as a product. Wildcard: needs actuarial guts and reference customers; hardest to bootstrap on this list.",
   "Underwrites defined pilot outcomes: if agreed success criteria fail, payout covers remediation cost. Owns: 'AI pilots stopped being leapfrog bets.'"),
]

rows = []
for name, d, u, ind, src, chk, obj in ideas:
    m = sum(CLSIZE[c] * (1.0 if c in d["core"] else 0.8) for c in CLSIZE if c in d["core"] or c in d["support"])
    pct = m / 496 * 100
    comp = (pct/10 + u + ind)/3
    rows.append((name, m, pct, u, ind, comp, src, chk, obj))

rows.sort(key=lambda r: -r[5])
print("NEW BUCKET: 15 IDEAS MINED FROM RESEARCH GAPS (sorted by composite)\n")
print(f"{'#':>2} {'PRODUCT':55} {'KWMAT':>11} {'UNIQ':>5} {'INDV':>5} {'COMP':>6}")
for i,(n,m,p,u,ind,c,src,chk,obj) in enumerate(rows,1):
    print(f"{i:>2} {n[:55]:55} {m:>4.0f}/496  {u:>5.1f} {ind:>5.1f} {c:>6.2f}")

print("\n--- DETAIL ---")
for i,(n,m,p,u,ind,c,src,chk,obj) in enumerate(rows,1):
    print(f"\n{i}. {n}  [KW {m:.0f}/496 ({p:.1f}%) | UNIQ {u} | INDV {ind} | COMP {c:.2f}]")
    print(f"   OBJECTIVE: {obj}")
    print(f"   GAP SOURCE: {src}")
    print(f"   MARKET CHECK: {chk}")

md = ["# New Bucket: 15 Ideas Mined Directly From Research Gaps (Aug 2026)\n"]
md.append("Every idea was born from a gap named in the US/UK/EU/DE/JP/CN/IN/IL/KR sweep, then checked against existing players.\n")
md.append("KW match = cluster-weighted coverage of the 496-keyword universe (core 1.0, support 0.8).\n")
md.append("Composite = (KW% as 0-10 + Uniqueness + Individuality)/3.\n\n")
md.append("| # | Product | KW match | Uniq | Indiv | Composite | One-line objective |")
md.append("|---|---------|----------|------|-------|-----------|--------------------|")
for i,(n,m,p,u,ind,c,src,chk,obj) in enumerate(rows,1):
    md.append(f"| {i} | {n.split(' — ')[0]} | {m:.0f}/496 ({p:.1f}%) | {u} | {ind} | {c:.2f} | {obj[:110]} |")
md.append("\n## Detail\n")
for i,(n,m,p,u,ind,c,src,chk,obj) in enumerate(rows,1):
    md.append(f"### {i}. {n}\n- KW {m:.0f}/496 ({p:.1f}%) | Uniqueness {u} | Individuality {ind} | Composite {c:.2f}\n- Objective: {obj}\n- Gap source: {src}\n- Market check: {chk}\n")

with open("BUCKET_NEW_FROM_RESEARCH.md","w",encoding="utf-8") as f:
    f.write("\n".join(md))
print("\nWROTE BUCKET_NEW_FROM_RESEARCH.md")
