"""Coverage honesty check: AEGIS v2 against FOUR role families, not just AI-eng."""

# skill -> (typical mention weight in that role family's JDs)
FAMILIES = {
 "AI Engineer": {
   'Python':(1.0,.95),'LLM integration':(1.0,1.0),'RAG':(.9,.9),
   'Agents':(.85,.9),'TypeScript':(.7,.8),'FastAPI/APIs':(.8,.85),
   'Postgres':(.7,.7),'AWS':(.6,.6),'Evals/observability':(.7,.8),
   'Prompt/injection security':(.5,.8),'Docker':(.5,.6),'CI':(.4,.6),
 },
 "ML Engineer": {
   'Python':(1.0,.95),'Training/fine-tuning':(.8,.85),'MLFlow/experiments':(.6,.7),
   'Feature/pipelines':(.7,.75),'GPU/serving':(.6,.7),'Airflow/orchestration':(.5,.6),
   'Docker/k8s':(.7,.7),'AWS':(.6,.65),'API serving':(.6,.7),
   'Evals/monitoring':(.5,.7),'SQL':(.5,.6),'Agents':(.3,.5),
 },
 "Data Scientist": {
   'Python':(.95,.9),'Statistics/experiments':(.85,.9),'pandas/numpy':(.85,.9),
   'sklearn/modeling':(.7,.8),'SQL':(.9,.9),'Notebooks/viz':(.6,.6),
   'A/B testing':(.55,.85),'Storytelling/stakeholders':(.5,.6),'LLM work':(.35,.5),
   'Dashboards':(.3,.4),'Production eng':(.15,.2),
 },
 "Data Analyst": {
   'SQL':(1.0,1.0),'Excel/Sheets':(.7,.8),'Tableau/Looker/PowerBI':(.7,.85),
   'Dashboards/Reporting':(.75,.9),'Python-lite':(.45,.5),'Statistics-lite':(.4,.5),
   'Stakeholder comms':(.5,.6),'Data cleaning':(.6,.7),'LLM/analytics-eng':(.15,.3),
 },
}

# what AEGIS v2 actually demonstrates (2=strong artifact,1=partial,0=no)
AEGIS = {'Python':2,'LLM integration':2,'RAG':2,'Agents':2,'TypeScript':2,
 'FastAPI/APIs':2,'Postgres':2,'AWS':1,'Evals/observability':2,
 'Prompt/injection security':2,'Docker':2,'CI':2,
 'Training/fine-tuning':0,'MLFlow/experiments':1,'Feature/pipelines':1,
 'GPU/serving':0,'Airflow/orchestration':1,'SQL':1,'Statistics/experiments':0,
 'pandas/numpy':0,'sklearn/modeling':0,'Notebooks/viz':0,'A/B testing':0,
 'Storytelling/stakeholders':0,'Dashboards':1,'Production eng':2,
 'Excel/Sheets':0,'Tableau/Looker/PowerBI':0,'Dashboards/Reporting':1,
 'Python-lite':2,'Statistics-lite':0,'Stakeholder comms':0,'Data cleaning':0,
 'LLM/analytics-eng':2}

def cov(fam):
    num=den=0
    for s,(w,dem) in fam.items():
        den += w*dem*2
        num += w*dem*AEGIS.get(s,0)
    return num/den*100

print("=== HONEST COVERAGE BY ROLE FAMILY (AEGIS v2 as specced) ===")
for name,fam in FAMILIES.items():
    print(f"  {name:14s} {cov(fam):5.1f}%")

# extension: analytics layer over the evidence lake
EXT = {'Statistics/experiments':2,'pandas/numpy':2,'A/B testing':2,
       'Dashboards/Reporting':2,'Tableau/Looker/PowerBI':1,'Statistics-lite':2,
       'Data cleaning':1,'SQL':2,'Notebooks/viz':1,'Storytelling/stakeholders':1,
       'MLFlow/experiments':1,'Airflow/orchestration':1}
cur=dict(AEGIS); cur.update(EXT)
def cov2(fam,m): 
    num=den=0
    for s,(w,dem) in fam.items():
        den+=w*dem*2; num+=w*dem*m.get(s,0)
    return num/den*100
print("\n=== WITH 'AEGIS INSIGHTS' ANALYTICS LAYER ADDED ===")
for name,fam in FAMILIES.items():
    print(f"  {name:14s} {cov2(fam,cur):5.1f}%")
