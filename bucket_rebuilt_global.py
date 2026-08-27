from kw import KEYWORDS

# ---- cluster classifier (same 13-cluster split summing to 496) ----
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
assert sum(CLSIZE.values()) == 496

# ---- REBUILT list after global startup/OSS collision check ----
# Each: name, cluster weights, uniqueness(0-10, post-collision), individuality(0-10),
#       old_score (previous uniqueness for delta), competitors found, verdict, objective
ideas = [
 ("AGENTGATE — Pre-Production Certification Gate for Enterprise Agents",
   dict(core=["llm","sde","backend","infra","data"], support=["ml","store","stats","sec"], periph=["cv","viz"]),
   8.8, 9.0, None,
   "Partial only: Arize ($70M C, post-hoc observability), Virtue AI (agent safety testing), Prime Intellect (training-time evals), Mindgard UK (AI security testing). NOBODY owns the pre-production staging/integration gate.",
   "OPEN WEDGE",
   "CI/CD for agents: every agent passes integration-contract tests, sandbox replays, eval thresholds and governance checks BEFORE it can ship. Owns: 'no agent reaches customers untested.' Gartner: >40% agentic projects canceled by 2027 on integration+governance failure; Korea's NC AI $34M mandate is literally built around a production testbed for this gap."),
 ("PROCUREIQ — AI Vendor & Contract Intelligence for Procurement",
   dict(core=["llm","data","store","backend","viz"], support=["sde","infra","ml","stats","sec"], periph=["cv"]),
   8.5, 8.5, "SPENDCAP 9.2 -> 8.5 (runtime FinOps is crowded: TokenJam, Behest, TokenAtlas, Finout)",
   "Runtime token-FinOps is TAKEN (TokenJam 'AI spend control plane', Behest CFO token FinOps, TokenAtlas, Finout). But the PROCUREMENT/contract side (benchmarking, repricing-clause watch, renewal playbooks) is done only by consultants (NPI, SpendHound). No product found.",
   "REFRAMED WEDGE",
   "Reads your AI vendor contracts, flags repricing/credit-redefinition traps, benchmarks your rates vs peers, drafts negotiation positions before renewal. Owns: 'we never get surprise-billed again.' NPI: AI spend +108% YoY, 85% miss forecasts, contracts renegotiated yearly."),
 ("SIMFACTORY — RL Environments & Eval Data Factory",
   dict(core=["llm","ml","data","store"], support=["infra","backend","sde","cv","stats"], periph=["sec","viz"]),
   7.2, 8.0, "SYNTHETICA 8.5 -> 7.2 (standalone synthetic data is very crowded)",
   "Prime Intellect raised $130M @$1B proving demand for agent-training infra+evals, but is hosted/frontier-focused. Synthetic-data pure plays are consolidated (Gretel->NVIDIA $320M, YData->KPMG, MOSTLY AI->Syntho merger). Self-hosted enterprise task-environment factory for fine-tuning YOUR OWN business agents: open.",
   "WEDGE",
   "Turns your company's real workflows into RL environments, golden traces, and eval suites so you can train and certify your own agents without frontier-lab dependency. Owns: 'our agents are trained on OUR work.'"),
 ("TWINTRUTH — Digital Twin Fidelity & ROI Validator",
   dict(core=["data","store","ml","infra"], support=["backend","sde","llm","stats","viz"], periph=["cv","sec"]),
   7.6, 8.5, "8.6 -> 7.6 (niche OSS exists)",
   "Fragmented: STAMM (open-source, soft-sensors only), GameDriver (game-engine twin validation), LTTS LTwin (consulting-built physics twins). No cross-industry productized fidelity-drift + pre-build ROI validator found.",
   "WEDGE",
   "Continuously measures twin-vs-reality drift, certifies twin outputs, and models the business case BEFORE a twin build. Owns: 'twins stay true and prove their worth.' Research: model drift is the #1 twin failure; ROI prediction is buyers' top blocker."),
 ("CAUSALA — Warehouse-Native Causal Decision Engine",
   dict(core=["stats","data","store","ml"], support=["backend","infra","sde","llm","viz"], periph=["cv","sec"]),
   7.0, 8.5, "8.8 -> 7.0 (causaLens/RootCause exist)",
   "causaLens ($51M) pivoted to digital workers; RootCause.ai targets giant enterprises; Argenta is a solo 0-star OSS repo. Mid-market warehouse-native causal ML (HTE/CATE/DAG) is thin.",
   "EARLY WEDGE",
   "Runs causal analysis inside Snowflake/BigQuery: which lever actually moved revenue, per segment, with confidence bounds. Owns: 'decisions cite causes, not correlations.'"),
 ("KNOWPERMIT — Permissioned Institutional Memory (Humans + Agents)",
   dict(core=["llm","data","store","backend","sec"], support=["infra","sde","ml","stats"], periph=["cv","viz"]),
   6.5, 8.0, "MEMORYVAULT 9.3 -> 6.5 (BIG correction)",
   "CROWDED at the API layer: Mem0 ($24.5M, 55k stars, AWS Agent SDK exclusive), Letta ($10M, 22k stars), Zep/Graphiti (20k stars), Supermemory, Oracle Agent Memory, Modus (Israel, Context Warehouse). Surviving wedge: role-scoped memory serving HUMANS and agents together with permission-aware retrieval (Glean-adjacent but memory-not-search).",
   "CROWDED - NARROW WEDGE ONLY",
   "One governed memory graph scoped by role: engineers, agents, and new hires each retrieve exactly what they're entitled to, with provenance. Owns: 'knowledge outlives the people who hold it.'"),
 ("MATTERLABS — Closed-Loop Lab Orchestrator for Industrial R&D",
   dict(core=["ml","cv","data","store"], support=["llm","infra","backend","sde","stats"], periph=["sec","viz"]),
   7.0, 7.5, "MATTERFORGE 9.0 -> 7.0",
   "Preferred Networks' Matlantis (Japan) owns materials SIMULATION; Isomorphic Labs ($2.1B raise) dominates pharma discovery; SDLs are academic. Lab WORKFLOW orchestration (proposal->robot->verify->KB) as productized software: partial gap.",
   "PARTIAL GAP",
   "Orchestrates propose-execute-verify loops across lab instruments and sims, with drift-corrected knowledge base. Owns: '1000 experiments a day, every result reusable.'"),
 ("BEHAVCORE — Transaction Behavior Model API for Mid-Market Finance",
   dict(core=["ml","data","store","backend"], support=["llm","infra","sde","stats"], periph=["cv","sec","viz"]),
   6.0, 7.5, "FINCORE 7.8 -> 6.0",
   "Giants build in-house (Stripe, Visa TransactionGPT, Nubank NuFormer, Revolut PRAGMA, Plaid); NVIDIA published the full recipe. Hosting it for community banks/mid-market fintechs is the only open lane.",
   "THIN WEDGE",
   "One pretrained behavior backbone served as API: credit, churn, LTV, anomalies for institutions that can't train their own. Owns: 'big-bank intelligence at mid-market price.'"),
 ("PROOFDESK — Outcome-Evidence & ROI Attestation for AI Programs",
   dict(core=["llm","data","store","viz","stats"], support=["backend","infra","sde","ml","sec"], periph=["cv"]),
   6.2, 7.5, None,
   "NPI/SpendHound both call AI ROI 'THE unsolved problem'. TokenJam ships a basic declared-value/cost ratio; nobody does auditable, board-ready outcome attestation across the whole AI portfolio.",
   "WEDGE (partially contested by TokenJam)",
   "Instruments every AI initiative's declared outcome vs measured cost/value and produces auditor-ready ROI attestations. Owns: 'every AI dollar can defend itself to the board.'"),
 ("COORDINA — Self-Hosted AI Coordination Workers for Mid-Market Ops",
   dict(core=["llm","backend","data","store"], support=["ml","sde","infra","stats","sec"], periph=["cv","viz"]),
   5.5, 7.5, None,
   "HappyRobot raised $150M @$1.2B doing EXACTLY this (phone/email/document coordination for logistics/insurance/energy, 150+ enterprise customers). Only wedge left: self-hosted/open mid-market.",
   "VALIDATED MARKET, BIG INCUMBENT",
   "Voice/email/doc agents that chase confirmations, fill schedule gaps, reconcile paperwork for companies too small for HappyRobot's enterprise motion."),
 ("CLAIMEXEC — Claims Execution Layer for Insurance",
   dict(core=["llm","ml","data","store","backend"], support=["infra","sde","stats","cv","sec"], periph=["viz"]),
   5.5, 7.0, "UNDERWRITEAI 6.5 -> 5.5",
   "Guidewire (Qusar Agentic Framework), Duck Creek (Agentic AI Platform), NTT DATA AI for Insurance all shipped 2026. Everest Group names an 'execution gap' but the cores themselves are filling it fast.",
   "CROWDED, CLOSING FAST",
   "Execution orchestration over legacy cores: FNOL intake, triage, leakage flags with human review queues."),
 ("ONTOBASE — Mid-Market Ontology Layer for Enterprise AI",
   dict(core=["llm","data","store","backend"], support=["ml","sde","infra","stats","sec"], periph=["cv","viz"]),
   5.0, 7.0, None,
   "Palantir defined it; Mobigen (Korea) is executing 'K-Palantir'; Modus does context warehousing. Hot but contested from multiple directions.",
   "CONTESTED",
   "Maps your systems into a queryable business ontology so AI answers carry business meaning, at 1/10 Palantir's cost."),
 ("SOVEREIGNSTACK — Certified On-Prem Agent Stack for Regulated Mid-Market",
   dict(core=["llm","backend","infra","sec"], support=["data","store","sde","ml"], periph=["cv","stats","viz"]),
   6.0, 6.5, None,
   "Aleph Alpha (now Cohere-owned, deployed in German ministries), Sarvam (India, $1.5B), Sakana (Japan) own the MODEL layer. A certified open agent-stack (models optional) for EU/Asia regulated mid-market is a thinner but real gap.",
   "REGIONAL GAP, SERVICES-HEAVY",
   "GDPR/AI-Act-ready, on-prem agent runtime + eval + audit bundle that regulated mid-caps can run without US clouds."),
 ("GREENLEDGER — ESG Reporting Automation",
   dict(core=["data","store","backend","llm"], support=["ml","infra","sde","stats","viz"], periph=["cv","sec"]),
   5.0, 7.0, "7.5 -> 5.0",
   "SAP Sustainability Control Tower ships AI drafting; Watershed/Persefoni/Workday entrenched; BCG says the gap is integration discipline, not tooling.",
   "CROWDED",
   "Carbon accounting + assurance-ready disclosure drafting wired into ERP data."),
 ("CLIMATESIM — Asset-Level Physical Climate Risk",
   dict(core=["ml","data","store","infra"], support=["llm","backend","sde","stats","viz"], periph=["cv","sec"]),
   5.0, 7.5, "8.0 -> 5.0",
   "Established specialist incumbents (RMS/Moody's, Jupiter Intelligence, One Concern - known players, not re-verified this sweep). Disclosure demand is real but the modeling moat is deep science + decades of cat data.",
   "INCUMBENT-HELD",
   "Prices flood/heat/storm exposure per asset for disclosure and resilience planning."),
 ("HEALTHADMIN — Healthcare Back-Office Agents",
   dict(core=["llm","data","store","backend"], support=["ml","sde","infra","stats","sec"], periph=["cv","viz"]),
   4.5, 7.0, None,
   "Brutally funded incumbents: Hippocratic AI ($3.5B val), EliseAI ($2.2B, health+property admin), Tennr ($605M, provider docs).",
   "AVOID - DOMINATED",
   "Prior-auth, denials, documentation automation for providers."),
]

rows = []
for name, d, u, ind, old, comp, verdict, obj in [(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]) for i in ideas]:
    m = 0.0
    for c in CLSIZE:
        if c in d["core"]: m += CLSIZE[c]*1.0
        elif c in d["support"]: m += CLSIZE[c]*0.8
    pct = m/496*100
    composite = (pct/10 + u + ind)/3
    rows.append((name, m, pct, u, ind, composite, verdict, obj, comp, old))

rows.sort(key=lambda r: -r[5])
print("REBUILT AFTER GLOBAL COLLISION CHECK (sorted by composite)\n")
print(f"{'#':>2} {'PRODUCT':58} {'KWMAT':>11} {'UNIQ':>5} {'INDV':>5} {'COMP':>6}  VERDICT")
for i,(n,m,p,u,ind,c,v,obj,cp,old) in enumerate(rows,1):
    print(f"{i:>2} {n[:58]:58} {m:>4.0f}/{496} {u:>5.1f} {ind:>5.1f} {c:>6.2f}  {v}")

print("\n--- OBJECTIVES ---")
for i,(n,m,p,u,ind,c,v,obj,cp,old) in enumerate(rows,1):
    print(f"\n{i}. {n}  [KW {m:.0f}/496 {p:.1f}% | U {u} | I {ind} | C {c:.2f}]  VERDICT: {v}")
    print(f"   {obj}")
    print(f"   COMPETITION: {cp}")

md = ["# Rebuilt Bucket After Global Startup/OSS Collision Check (Aug 2026)\n"]
md.append("Method: 496 keywords in 13 clusters; KW match = sum(size x weight)/496 (core 1.0, support 0.8).\n"
          "Uniqueness re-scored AGAINST named funded competitors found in US/UK/EU/DE/JP/CN/IN/IL/KR sweep.\n"
          "Composite = (KW% as 0-10 + Uniqueness + Individuality)/3.\n")
md.append("## Region snapshot\n")
md.append("| Region | Anchors (verified this sweep) | Theme |")
md.append("|---|---|---|")
md.append("| US | Hippocratic $3.5B, EliseAI $2.2B, Vanta $4.15B, Writer $1.9B, HappyRobot $1.2B, Prime Intellect $1B, Arize $70M-C, Tennr $605M, Thrive Holdings $12B | Vertical agent ops + agent infra + AI deployment PE |")
md.append("| UK | Nscale $14.6B, ElevenLabs $11B, Wayve $8.6B, Synthesia $4B, Quantexa $2.6B, Isomorphic $2.1B raise, Luminance ~$1B, Tractable $1B, Tessl $750M | Frontier infra + deep vertical AI |")
md.append("| Germany/EU | Aleph Alpha (acquired by Cohere), Black Forest Labs $431M, DeepL ~EUR 2B, Mistral FR, Langdock | Sovereignty, GDPR, EU AI Act |")
md.append("| Japan | Sakana AI $2B, Preferred Networks (Matlantis), LayerX, Turing, gov yen 1T plan | Efficient local models + industrial/robotics AI |")
md.append("| China | Zhipu ~$80B, DeepSeek raising ~$7B, Moonshot ~$30B sought, MiniMax $20B listed, ByteDance Doubao/Volcano | Coding agents, brutal pricing, on-prem deployments |")
md.append("| India | Sarvam $234M @ $1.5B, Krutrim (pivot to cloud), Bhashini | Sovereign multilingual models |")
md.append("| Israel | Modus $10M (Context Warehouse), Unframe $50M (week-long agent delivery) | Context layer + rapid agent deployment |")
md.append("| Korea | NC AI $34M state mandate w/ Gabia live testbed, Mobigen Grapio (K-Palantir), K-Moonshot won 10.1T | Production-testbed agentic AI, ontology |\n")
md.append("## Final ranked list\n")
md.append("| # | Product | KW match | Uniq | Indiv | Composite | Verdict |")
md.append("|---|---------|----------|------|-------|-----------|---------|")
for i,(n,m,p,u,ind,c,v,obj,cp,old) in enumerate(rows,1):
    md.append(f"| {i} | {n.split(' — ')[0]} — {n.split(' — ')[1] if ' — ' in n else ''} | {m:.0f}/496 ({p:.1f}%) | {u} | {ind} | {c:.2f} | {v} |")
md.append("\n## Detail\n")
for i,(n,m,p,u,ind,c,v,obj,cp,old) in enumerate(rows,1):
    md.append(f"### {i}. {n}\n- KW {m:.0f}/496 ({p:.1f}%) | Uniqueness {u} | Individuality {ind} | Composite {c:.2f}\n- Objective: {obj}\n- Competition: {cp}\n- Verdict: **{v}**\n")
md.append("""## What got corrected vs the previous bucket (honesty log)
- MEMORYVAULT 9.3 -> 6.5: agent-memory APIs are a FUNDED category (Mem0, Letta, Zep, Modus, Oracle).
- SPENDCAP 9.2 -> reframed to PROCUREIQ 8.5: runtime token-FinOps is taken (TokenJam, Behest, TokenAtlas, Finout);
  procurement/contract side is consultant-only turf, so the wedge moved there.
- SYNTHETICA 8.5 -> folded into SIMFACTORY 7.2: standalone synthetic data consolidated (Gretel->NVIDIA,
  YData->KPMG, MOSTLY AI->Syntho).
- CAUSALA 8.8 -> 7.0: causaLens and RootCause.ai exist; mid-market warehouse-native lane stays open.
- MATTERFORGE 9.0 -> 7.0: Matlantis (simulation) and Isomorphic (pharma) hold neighbors; lab-loop orchestration stays open.
- TWINTRUTH 8.6 -> 7.6: niche OSS exists (STAMM, GameDriver); cross-industry validator still unowned.
- UNDERWRITEAI 6.5 -> 5.5: Guidewire/Duck Creek/NTT DATA shipped agentic platforms in 2026.
- DROPPED: HEALTHADMIN (Hippocratic/EliseAI/TENNr dominate), PROPTECHIQ (EliseAI), standalone ESG and climate-risk
  (entrenched), kept below the line with honest low scores.
## New ideas the landscape itself suggested
- AGENTGATE (#1): Gartner >40% agentic-project cancellations + Korea building a state testbed for exactly this =
  nobody owns the pre-production gate.
- PROCUREIQ (#2): 108% spend growth, 85% forecast misses, and the whole tooling wave attacks RUNTIME cost;
  the CONTRACT side is still consultants with spreadsheets.
- PROOFDESK: NPI and SpendHound both name AI ROI attribution THE unsolved problem.
""")

with open("BUCKET_REBUILT_GLOBAL.md", "w", encoding="utf-8") as f:
    f.write("\n".join(md))
print("\nWROTE BUCKET_REBUILT_GLOBAL.md")
