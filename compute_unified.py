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

# The ONE central product = "Aegis Control Plane" with subsystems (former modules).
MODS={
"Ship Gate (replay+eval+policy)":["llm","sde","backend","infra","data","store","ml","sec","stats","viz","cv"],
"SwapWatch (prod model-truth)":["llm","infra","backend","sde","data","ml","stats","sec","viz","store"],
"ROI Attest":["llm","data","store","viz","stats","backend","sde","infra","ml","sec"],
"Governed Memory":["llm","data","store","backend","sec","sde","infra","ml","viz","cv"],
"Contract & Spend Intel":["llm","data","store","backend","viz","sde","infra","ml","stats","sec","cv"],
"Twin Truth (drift+ROI)":["data","store","ml","infra","backend","sde","llm","stats","viz","cv","sec"],
"Causal Decisions":["stats","ml","data","store","llm","backend","infra","viz","sec","sde","cv"],
"Sim/RL Data Factory":["llm","ml","data","store","backend","sde","infra","stats","cv","sec","viz"],
"Autonomous Ops (claims+coord)":["llm","backend","data","store","infra","ml","stats","sec","viz","sde","cv"],
"Audit & Compliance Trail":["sec","infra","data","backend","sde","store","llm"],
}
union=set()
for m,cs in MODS.items():
    union|=set(cs)
print("Subsystems: %d"%len(MODS))
print("Clusters covered by union: %d / 13 -> %s"%(len(union), sorted(union)))
missing=[c for c in CLSIZE if c not in union]
print("Missing clusters:", missing if missing else "NONE (100% coverage)")
m=sum(CLSIZE[c] for c in union)
print("KW match: %d/496 = %.1f%%"%(m, m/496*100))

# unified composite
kw=m/496*100
u=9.0   # combined control-plane seat is very open
ind=9.3 # your RADAR + 3 engines story
fb=len(MODS); sb=5  # CISO CFO CTO Compliance Ops
comp=(kw/10*0.3)+(u*0.3)+(ind*0.2)+(((fb/6)+(sb/4))/2*10*0.2)
print("Uniq %.1f | Indiv %.1f | fb %d | stk %d | COMPOSITE %.2f (capped display 10.0)"%(u,ind,fb,sb,min(comp,10.0)))
