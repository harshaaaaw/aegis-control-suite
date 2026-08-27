"""Keyword frequency analysis over the real 31-JD corpus."""
import json, re
from collections import Counter

jobs = json.load(open(r"C:\Users\Harsh\job-hunt-2026\jd_corpus\all_jobs.json", encoding="utf-8"))
import html as H
def clean(t):
    t = H.unescape(t); t = re.sub(r"<[^>]+>", " ", t)
    return t.lower()

FAM = {
 "AI Engineer": r"\b(AI engineer|LLM|agent|GenAI|generative|prompt|RAG)\b",
 "ML Engineer": r"(machine learning engineer|ML engineer|MLOps|model training|pytorch|tensorflow)",
 "Data Scientist": r"(data scientist|data science)",
 "Data Analyst": r"(data analyst|analytics engineer|BI analyst)",
}
fam_jobs = {k: [] for k in FAM}
for j in jobs:
    txt = clean(j["text"])
    for fam, pat in FAM.items():
        if re.search(pat, txt):
            fam_jobs[fam].append(txt)

KW = ['python','typescript','javascript','react','next.js','node','sql','postgres',
 'mysql','aws','gcp','azure','docker','kubernetes','terraform','llm','gpt','openai',
 'anthropic','claude','gemini','langchain','rag','vector','embedding','fine-tun',
 'pytorch','tensorflow','transformers','hugging face','agents','mcp','eval',
 'guardrail','prompt injection','observability','opentelemetry','tracing',
 'airflow','dbt','spark','kafka','snowflake','tableau','looker','powerbi',
 'excel','dashboard','a/b test','experiment','statistics','pandas','numpy',
 'sklearn','scikit','mlflow','fastapi','rest api','graphql','oauth','redis',
 'ci/cd','unit test','go ','rust','java','scala','r language','matlab',
 'nlp','computer vision','time series','forecast','regression','classification',
 'etl','pipeline','data model','stakeholder','visualization','bigquery','databricks',
 'sagemaker','vertex','ml ops','mlops','monitoring','latency','cost']

print(f"{'keyword':22s} AIeng({len(fam_jobs['AI Engineer'])}) ML({len(fam_jobs['ML Engineer'])}) DS({len(fam_jobs['Data Scientist'])}) DA({len(fam_jobs['Data Analyst'])})")
out={}
for kw in KW:
    counts=[]
    for fam in ["AI Engineer","ML Engineer","Data Scientist","Data Analyst"]:
        texts=fam_jobs[fam]
        n=sum(1 for t in texts if kw in t)
        pct=round(100*n/len(texts)) if texts else 0
        counts.append(pct)
    if max(counts)>=25:
        print(f"{kw:22s} {counts[0]:>4d}% {counts[1]:>4d}% {counts[2]:>4d}% {counts[3]:>4d}%")
        out[kw]=counts

json.dump(out, open(r"C:\Users\Harsh\job-hunt-2026\jd_corpus\kw_freq.json","w"), indent=1)
print("\nsaved kw_freq.json")
