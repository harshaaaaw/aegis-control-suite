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
assert sum(CLSIZE.values())==496, sum(CLSIZE.values())

# new bucket: name -> core/support cluster lists (periph omitted from math but noted)
W={
"AGENTGATE":(["llm","sde","backend","infra","data"],["ml","store","stats","sec","cv","viz"]),
"SWAPWATCH":(["llm","infra","backend"],["sde","data","ml","stats","sec","viz"]),
"PROCUREIQ":(["llm","data","store","backend","viz"],["sde","infra","ml","stats","sec","cv"]),
"TWINTRUTH":(["data","store","ml","infra"],["backend","sde","llm","stats","viz","cv","sec"]),
"CAUSALA":(["stats","data","store","ml"],["backend","infra","sde","llm","viz","cv","sec"]),
"SIMFACTORY":(["llm","ml","data","store"],["infra","backend","sde","cv","stats","sec","viz"]),
"KNOWPERMIT":(["llm","data","store","backend","sec"],["infra","sde","ml","stats","cv","viz"]),
"MATTERLABS":(["ml","cv","data","store"],["llm","infra","backend","sde","stats","sec","viz"]),
"PROOFDESK":(["llm","data","store","viz","stats"],["backend","infra","sde","ml","sec","cv"]),
"BEHAVCORE":(["ml","data","store","backend"],["llm","infra","sde","stats","cv","sec","viz"]),
"COORDINA":(["llm","backend","data","store"],["ml","sde","infra","stats","sec","cv","viz"]),
"CLAIMEXEC":(["llm","ml","data","store","backend"],["infra","sde","stats","cv","sec","viz"]),
"CLIMATESIM":(["ml","data","store","infra"],["llm","backend","sde","stats","viz","cv","sec"]),
"ONTOBASE":(["llm","data","store","backend"],["ml","sde","infra","stats","sec","cv","viz"]),
"GREENLEDGER":(["data","store","backend","llm"],["ml","infra","sde","stats","viz","cv","sec"]),
"SOVEREIGNSTACK":(["llm","backend","infra","sec"],["data","store","sde","ml","cv","stats","viz"]),
}
print("CLUSTER SIZES (sum=%d):"%sum(CLSIZE.values()))
for c in sorted(CLSIZE,key=lambda x:-CLSIZE[x]): print("  %-7s %d"%(c,CLSIZE[c]))
print("\nNEW BUCKET KW MATCH:")
rows=[]
for n,(core,sup) in W.items():
    m=sum(CLSIZE[c]*(1.0 if c in core else 0.8) for c in CLSIZE)
    rows.append((n,m,m/496*100))
for n,m,p in sorted(rows,key=lambda r:-r[1]):
    print("  %-14s %5.0f/496  %5.1f%%"%(n,m,p))
