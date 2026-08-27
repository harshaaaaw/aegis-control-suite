from kw import KEYWORDS
def cluster_of(kw):
    k = kw.lower()
    if any(t in k for t in ["langchain","llamaindex","langgraph","autogen","crewai","instructor","pydantic","vllm","hugging face","ollama","lm studio","openai","anthropic","gemini","cohere","mistral","meta llama","deepseek","flux","midjourney","rag","semantic search","hybrid search","document chunking","semantic caching","prompt","system prompts","few-shot","chain-of-thought","function calling","agentic","tool usage","autonomous agents","multi-agent","synthetic data","context window","hallucination","guardrails","output parsing","structural validation"]): return "llm"
    if any(t in k for t in ["sft","rlhf","dpo","lora","qlora","peft","spacy","nltk","gensim","tokeniz","ner","intent class","sentiment","dependency parsing","word embeddings","sentence transformer","dialog state","deepspeed","ray ","megatron","flashattention","fsdp","tensor parallel","pipeline parallel","horovod","pytorch lightning","tensorrt","onnx","openvino","triton","ray serve","torchserve","tgi","model pruning","weight quant","knowledge distill","transformer internals","cnns","rnns","lstm","gans","diffusion","autoencoders","recommender","collaborative filtering","matrix factorization","deep & cross","learning-to-rank","lambda","two-tower","contextual multi","q-learning","ppo","deep q","confusion","roc-auc","precision-recall","f1","mae","rmse","ndcg","map","ctr","iou","map ","bleu","rouge","perplexity","rasa","botpress","cognigy","voiceflow","azure ai language","amazon lex"]): return "ml"
    if any(t in k for t in ["opencv","torchvision","yolo","detectron","mediapipe","image segmentation","object detection","face recognition","ocr","vision-language","image classification","video processing","feature extraction"]): return "cv"
    if any(t in k for t in ["spark","pyspark","flink","beam","mapreduce","hadoop","delta lake","iceberg","hudi","parquet","orc","avro","protobuf","data lakes","modern data stack","snowflake","bigquery","redshift","synapse","databricks","dbt","data vault","star schema","snowflake schema","dimensional","fact and","scd","data lineage","airflow","prefect","dagster","luigi","step functions","great expectations","deequ","soda","data quality","anomaly alerting","atlas","amundsen","datahub","collibra","data catalog","schema registry","schema evolution","dead-letter"]): return "data"
    if any(t in k for t in ["postgresql","mysql","sql server","oracle","cockroachdb","spanner","mongodb","cassandra","hbase","couchbase","dynamodb","documentdb","pinecone","milvus","qdrant","weaviate","pgvector","chromadb","faiss","neo4j","neptune","arangodb","graphdb","cypher","redis","memcached","redis insight","distributed caching","s3","gcs","azure blob","minio","elasticsearch","opensearch","influxdb","timescaledb","clickhouse"]): return "store"
    if any(t in k for t in ["fastapi","django","flask","spring boot","go gin","nestjs","express","asp.net","rails","restful","graphql","grpc","websockets","soap","webhooks","api contract","openapi","swagger","kafka","rabbitmq","sqs","sns","pulsar","pub/sub","event-driven","asynchronous job","publish-subscribe","exactly-once","microservice","monolithic","clean architecture","domain-driven","event sourcing","cqrs","idempotency","concurrency","multithreading","async programming","distributed locking","connection pooling","database indexing","query execution","circuit breaker","bulkhead"]): return "backend"
    if any(t in k for t in ["oauth","oidc","jwt","saml","rbac","abac","multi-tenancy","api gateway","kong","apigee","cors","xss","csrf","rate limiting","token bucket","leaky bucket"]): return "sec"
    if any(t in k for t in ["docker","kubernetes","helm","kustomize","podman","containerd","ecs","terraform","terragrunt","cloudformation","pulumi","ansible","github actions","gitlab ci","jenkins","argocd","circleci","tekton","spinnaker","aws","gcp","azure","otel","opentelemetry","prometheus","grafana","datadog","new relic","dynatrace","elk","splunk","jaeger","zipkin","distributed tracing","metrics","centralized logging","alertmanager","slo","sli","sla","chaos","disaster recovery","multi-region","high availability","load balancing","zero-downtime","circuit breaking","capacity planning","blameless","root-cause","linux internals","system calls","ebpf","systemd","network i/o","ipc","shared memory","posix","memory management","bash"]): return "infra"
    if any(t in k for t in ["hypothesis testing","p-value","t-test","anova","chi-square","confidence","statistical power","sample size","central limit","bayesian","markov chain","probability distrib","multivariate","split testing","multi-armed bandit","sequential testing","variance reduction","cuped","sample ratio","a/a","novelty","primacy","cohort","quasi-experiment","synthetic control","difference-in","propensity score","regression discontinuity","instrumental","structural equation","dag","pymc","dowhy"]): return "stats"
    if any(t in k for t in ["looker","tableau","power bi","matplotlib","seaborn","plotly","shiny","streamlit","dash","exploratory data"]): return "viz"
    return "sde"
CLSIZE={}
for kw in KEYWORDS:
    c=cluster_of(kw); CLSIZE[c]=CLSIZE.get(c,0)+1

# Composed platforms: each fuses several former point-ideas into one multi-stakeholder platform.
# core = clusters exercised at full depth; support = present but lighter.
# fb = functional breadth (modules fused); stk = stakeholder POVs served.
P=[
("AGENTTRUST PLANE",["llm","sde","backend","infra","data","store","ml","stats","sec","viz","cv"],
  ["llm","backend","infra","data","store","ml","sec","stats","sde","viz","cv"],
  ["AGENTGATE ship-gate","SWAPWATCH prod-swap watch","PROOFDESK ROI attest","KNOWPERMIT governed memory","agent-sentinel policy"],
  ["CISO","CFO","CTO","Compliance"],8.5,9.2),
("AIFINANCE COMMAND",["llm","data","store","backend","infra","stats","ml","sec","viz","sde"],
  ["llm","data","store","backend","infra","stats","ml","sec","viz","sde"],
  ["PROCUREIQ contracts","SWAPWATCH SLA-cost","PROOFDESK ROI","BEHAVCORE risk"],
  ["CFO","Procurement","CTO","Risk"],8.3,8.8),
("INDUSTRIAL INTELLIGENCE PLANE",["data","store","ml","infra","backend","llm","stats","viz","cv","sec","sde"],
  ["data","store","ml","infra","backend","llm","stats","viz","cv","sec","sde"],
  ["TWINTRUTH twin-truth","CAUSALA causal-decisions","SIMFACTORY sim-data","MATTERLABS lab-loop"],
  ["VP Eng/Ops","CDO","R&D Dir"],8.0,8.5),
("DECISION INTELLIGENCE CORE",["stats","ml","data","store","llm","backend","infra","viz","sec","sde","cv"],
  ["stats","ml","data","store","llm","backend","infra","viz","sec","sde","cv"],
  ["CAUSALA causal","BEHAVCORE behavior","KNOWPERMIT memory","ONTOBASE ontology"],
  ["CDO","CTO","Strategy"],7.8,8.6),
("AUTONOMOUS OPS BACKOFFICE",["llm","backend","data","store","infra","ml","stats","sec","viz","sde","cv"],
  ["llm","backend","data","store","infra","ml","stats","sec","viz","sde","cv"],
  ["CLAIMEXEC claims","COORDINA coordination","KNOWPERMIT memory","PROOFDESK ROI"],
  ["Ops VP","CFO","COO"],7.2,8.2),
("SOVEREIGN AI PLANE",["llm","backend","infra","sec","data","store","ml","stats","sde","viz","cv"],
  ["llm","backend","infra","sec","data","store","ml","stats","sde","viz","cv"],
  ["SOVEREIGNSTACK on-prem","AGENTGATE gate","KNOWPERMIT memory","SWAPWATCH swap-watch"],
  ["CISO","CTO","Compliance","Public Sector"],8.2,8.4),
("CLIMATE & ESG INTELLIGENCE",["ml","data","store","infra","stats","llm","backend","viz","sec","sde","cv"],
  ["ml","data","store","infra","stats","llm","backend","viz","sec","sde","cv"],
  ["CLIMATESIM risk","GREENLEDGER ESG","CAUSALA causal-exposure","PROOFDESK attest"],
  ["CSO","CFO","Compliance"],6.5,8.0),
("REVENUE INTELLIGENCE PLANE",["stats","ml","data","store","llm","backend","infra","viz","sec","sde","cv"],
  ["stats","ml","data","store","llm","backend","infra","viz","sec","sde","cv"],
  ["CAUSALA revenue-drivers","BEHAVCORE churn/LTV","SIMFACTORY revenue-agent eval","PROOFDESK ROI"],
  ["CRO","CTO","Growth"],7.5,8.3),
("SUPPLY CHAIN AUTONOMY PLANE",["llm","backend","data","store","infra","ml","stats","cv","sec","viz","sde"],
  ["llm","backend","data","store","infra","ml","stats","cv","sec","viz","sde"],
  ["COORDINA coordination","TWINTRUTH network-twin","CLAIMEXEC claims","KNOWPERMIT memory"],
  ["COO","Ops VP","CFO"],7.0,8.1),
("RESEARCH ACCELERATOR PLANE",["ml","cv","data","store","llm","infra","backend","stats","sec","viz","sde"],
  ["ml","cv","data","store","llm","infra","backend","stats","sec","viz","sde"],
  ["MATTERLABS lab-loop","SIMFACTORY sim-data","KNOWPERMIT memory","CAUSALA causal"],
  ["R&D Dir","CDO","CTO"],7.6,8.0),
]
print("COMPOSED PLATFORMS (each fuses 4-5 former point-ideas, serves 3-4 stakeholder POVs)\n")
rows=[]
for n,core,sup,mods,stk,u,ind in P:
    m=sum(CLSIZE[c]*(1.0 if c in core else 0.8) for c in CLSIZE)
    kw=m/496*100
    fb=len(mods); sb=len(stk)
    comp=(kw/10*0.3)+(u*0.3)+(ind*0.2)+(((fb/6)+(sb/4))/2*10*0.2)
    rows.append((n,kw,u,ind,fb,sb,comp,mods,stk))
for n,kw,u,ind,fb,sb,comp,mods,stk in sorted(rows,key=lambda r:-r[6]):
    print("  %-30s KW %5.1f%% | U %4.1f | I %4.1f | fb %d | stk %d | COMP %5.2f"%(n,kw,u,ind,fb,sb,comp))
print("\nDETAIL (modules + stakeholders):")
for n,kw,u,ind,fb,sb,comp,mods,stk in sorted(rows,key=lambda r:-r[6]):
    print("  %s"%n)
    print("    fuses: %s"%"; ".join(mods))
    print("    serves: %s"%", ".join(stk))
