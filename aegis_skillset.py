"""AEGIS full skill-set + tech-stack list, generated from spec + measured JD data."""

SKILLS = {
 "Languages": [
   ("Python 3.10-3.12", "all 7 engines + control plane", "JD: 44-100% all families"),
   ("TypeScript (strict)", "sentinel-middleware, dashboard, MCP facade", "JD: 33%/20%/30%"),
   ("SQL", "Postgres schema, RLS, warehouse views", "JD: 17/40/40/100%"),
 ],
 "Backend / API": [
   ("FastAPI (async, Pydantic v2)", "/v1 control-plane gateway", "JD: FastAPI+REST"),
   ("REST + OpenAPI/Swagger", "every endpoint self-documented", "interview loop ask"),
   ("Webhooks + event bus", "policy events fan-out", "integration-surface gap fix"),
   ("MCP server protocol", "AEGIS exposed AS an MCP server", "2 of 4 live JDs verbatim"),
   ("OAuth2 / OIDC / JWT", "agents as first-class signed identities", "Entra-Agent-ID pattern"),
   ("Idempotency keys", "settlement ledger safety", "senior-backend signal"),
   ("Rate limiting + circuit breakers", "governor + sentinel engines", "reliability JDs"),
 ],
 "Data / Storage": [
   ("PostgreSQL (+ row-level security)", "multi-tenant core schema", "JD: 17/40/30/0"),
   ("Redis", "budget-cache tier", "JD: ML 40%, AI-eng add-on"),
   ("Kafka-compatible ingest", "evidence event stream", "JD: ML-family 40%"),
   ("dbt-style models + Parquet/CSV BI exports", "AEGIS Insights layer", "DS/DA coverage"),
   ("pandas / numpy / scipy", "Insights notebooks + stats tests", "JD: DS 60%/40%"),
 ],
 "AI / LLM": [
   ("RAG pipeline (chunking, hybrid search)", "ragforge engine", "JD study: 64% baseline"),
   ("Prompt-injection defense / guardrails", "sentinel two-tier engine", "28% AI-eng JDs"),
   ("LLM evaluation (golden sets, recall@k, faithfulness)", "evalforge engine", "28% + interview loops"),
   ("Drift detection", "nightly eval suites per agent", "Matterhaul JD verbatim"),
   ("Model routing / cascade", "cheap->frontier w/ verifier (60x savings)", "cost JDs"),
   ("Token budgeting / FinOps ($-per-outcome)", "governor ledger + wallets", "85% miss forecasts stat"),
   ("Agent orchestration (checkpointing, HITL gates)", "meshwork engine", "Matterhaul JD verbatim"),
   ("Forensic replay / time-travel debugging", "run-replay hash chains", "Matterhaul JD verbatim"),
   ("Autonomy ladder / progressive authorization", "the never-shipped piece", "Google SRE paper pattern"),
   ("EU AI Act / SOC2 evidence export", "compliance packet generator", "Aug 2026 deadline"),
 ],
 "Frontend": [
   ("React 18 + Next.js (App Router)", "fleet dashboard, Insights tab", "JD: React 88 HN mentions"),
   ("Charts/dashboards", "spend, ladder positions, incident feed", "DA coverage"),
 ],
 "Infra / DevOps": [
   ("Docker + docker-compose", "one-command full stack up", "JD: 11-40%"),
   ("AWS (ECS Fargate, RDS, ALB)", "terraform deploy target", "JD: AWS 22-40%"),
   ("Terraform (IaC module)", "one-command cloud deploy", "JD: 26 HN mentions"),
   ("GitHub Actions CI (py3.10-3.12 + node20)", "matrix + eval-gates in pipeline", "all eng JDs"),
   ("Kubernetes manifests/helm", "scale path", "JD: k8s 60% ML family"),
   ("OpenTelemetry + Grafana", "traces on every engine boundary", "obs 23 mentions"),
   ("SLOs / error budgets / burn-rate alerts", "per-agent reliability contracts", "SRE-for-agents wave"),
 ],
 "Testing / Quality": [
   ("pytest + vitest", "55 green tests across engines", "table stakes"),
   ("chaos/failure injection", "governor deadlock caught by own test", "war story gold"),
   ("statistical A/B testing (z-test, bootstrap CI)", "Insights stats module", "DS interviews"),
 ],
 "Security": [
   ("Trust lanes / quarantine attestation", "untrusted-lane memories gated", "OWASP agentic risks"),
   ("Hash-chained append-only audit logs", "tamper-evident everything", "auditor-grade proof"),
   ("Secret hygiene (fail-closed scanning)", "sk-/AKIA/xox patterns blocked at egress", "CISO talking points"),
 ],
}

total = sum(len(v) for v in SKILLS.values())
print(f"AEGIS FULL SKILL SET - {total} entries\n")
for cat, items in SKILLS.items():
    print(f"## {cat}")
    for name, where, jd in items:
        print(f"  - {name}")
        print(f"      artifact: {where}")
        print(f"      demand:   {jd}")
    print()
