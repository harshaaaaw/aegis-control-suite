"""Extract job posts (hiring-side comments) from HN thread 49156683."""
import json, re, unicodedata

d = json.load(open(r"C:\Users\Harsh\job-hunt-2026\jd_corpus\thread.json", encoding="utf-8"))

jobs = []
def walk(node):
    t = node.get("text") or ""
    if t and re.search(r"\b(hire|hiring|we.?re looking|join us|role:|position|remote)\b", t[:400], re.I) \
       and len(t) > 300:
        jobs.append({"id": node.get("id"), "text": t})
    for ch in node.get("children", []):
        walk(ch)
walk(d)

print(f"hiring-side posts found: {len(jobs)}")
# classify by role family
FAM = {
 "AI Engineer": r"(AI engineer|LLM|agent|GenAI|generative|prompt|RAG)",
 "ML Engineer": r"(machine learning engineer|ML engineer|MLOps|model training|pytorch|tensorflow)",
 "Data Scientist": r"(data scientist|data science)",
 "Data Analyst": r"(data analyst|analytics engineer|BI analyst)",
}
rows = {k: [] for k in FAM}
for j in jobs:
    for fam, pat in FAM.items():
        if re.search(pat, j["text"], re.I):
            rows[fam].append(j)

for k, v in rows.items():
    print(f"{k}: {len(v)}")

json.dump(jobs, open(r"C:\Users\Harsh\job-hunt-2026\jd_corpus\all_jobs.json","w",encoding="utf-8"),
          ensure_ascii=False, indent=1)
