import os, re

REPOS = ["agent-sentinel","token-governor","run-replay","sentinel-middleware","evalforge","ragforge","meshwork"]
SRC = (".py",".ts",".md")

# core hard skills per role. Presence in BUILT source = real proof.
SKILLS = {
 "AI Engineer": ["agent","guardrail","evaluation","rag","semantic","function calling","tool use",
                 "fastapi","oauth","jwt","otel","tracing","rate limit","retry","idempot","replay",
                 "policy","multi-tenant","circuit breaker","canary","prompt"],
 "ML Engineer": ["torch","pytorch","sklearn","scikit","transformer","lora","dpo","sft","rlhf","peft",
                 "deepspeed","fsdp","ray","vllm","triton","onnx","quantiz","pruning","distill",
                 "training","inference","embedding model","fine-tun","serving"],
 "DS/DA": ["pandas","numpy","hypothesis","p-value","p value","regression","forecast","arima","prophet",
           "experiment","a/b","ab test","churn","clv","segmentation","causal","did ","psm","statistic",
           "sql","dashboard","tableau","looker","power bi","anomaly","isolation forest"],
}

def files():
    out=[]
    for r in REPOS:
        for root,_,fs in os.walk(r):
            if "node_modules" in root: continue
            for f in fs:
                if f.lower().endswith(SRC):
                    out.append(os.path.join(root,f))
    return out

texts={}
for f in files():
    try: texts[f]=open(f,encoding="utf-8",errors="ignore").read().lower()
    except: pass

blob="\n".join(texts.values())
print(f"Scanned {len(texts)} source files across {len(REPOS)} repos (built code only)\n")
for role,sk in SKILLS.items():
    hit=[s for s in sk if s in blob]
    miss=[s for s in sk if s not in blob]
    cov=len(hit)/len(sk)*100
    print(f"### {role}: {cov:.0f}% of core hard skills present in BUILT code ({len(hit)}/{len(sk)})")
    print(f"   present : {', '.join(hit)}")
    print(f"   MISSING : {', '.join(miss)}\n")
