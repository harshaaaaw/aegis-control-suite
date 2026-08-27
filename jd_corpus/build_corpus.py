"""Build the 20+ JD corpus: top AI-eng JDs + all ML/DS/DA, cleaned."""
import json, re, html

jobs = json.load(open(r"C:\Users\Harsh\job-hunt-2026\jd_corpus\all_jobs.json", encoding="utf-8"))

FAM = {
 "AI Engineer": r"\b(AI engineer|LLM|agent|GenAI|generative|prompt|RAG)\b",
 "ML Engineer": r"(machine learning engineer|ML engineer|MLOps|model training|pytorch|tensorflow)",
 "Data Scientist": r"(data scientist|data science)",
 "Data Analyst": r"(data analyst|analytics engineer|BI analyst)",
}
def clean(t):
    t = html.unescape(t)
    t = re.sub(r"<p>|<br>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"\n{3,}", "\n\n", t).strip()

picked = {"AI Engineer": [], "ML Engineer": [], "Data Scientist": [], "Data Analyst": []}
for j in jobs:
    txt = clean(j["text"])
    for fam, pat in FAM.items():
        if re.search(pat, txt, re.I):
            picked[fam].append({"id": j["id"], "chars": len(txt), "text": txt})

# AI-eng: keep the 14 longest (real JDs, not one-liners); ML/DS/DA: keep all
corpus = []
for fam in ["ML Engineer", "Data Scientist", "Data Analyst"]:
    for j in sorted(picked[fam], key=lambda x: -x["chars"])[:8]:
        corpus.append({"family": fam, **j})
for j in sorted(picked["AI Engineer"], key=lambda x: -x["chars"])[:14]:
    corpus.append({"family": "AI Engineer", **j})

with open(r"C:\Users\Harsh\job-hunt-2026\jd_corpus\corpus.md", "w", encoding="utf-8") as f:
    f.write("# HN Who-is-Hiring Aug 2026 - JD Corpus\n\n")
    for i, c in enumerate(corpus, 1):
        f.write(f"## JD-{i:02d} [{c['family']}] id={c['id']} ({c['chars']} chars)\n\n")
        f.write(c["text"][:3500] + "\n\n---\n\n")

print(f"corpus size: {len(corpus)} JDs")
from collections import Counter
print(Counter(c['family'] for c in corpus))
