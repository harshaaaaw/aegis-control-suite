"""AEGIS scaled against the JD research: coverage math + lead mapping."""

MARKET = {
    'Python': (95, 1.00), 'React': (88, 1.00), 'Agents': (85, 1.00),
    'TypeScript': (78, 1.00), 'Postgres': (63, 0.95), 'AWS': (50, 0.85),
    'Go': (49, 0.60), 'k8s': (34, 0.70), 'Rust': (29, 0.50),
    'Terraform': (26, 0.65), 'Node.js': (25, 0.80), 'Evals/obs': (23, 0.90),
    'Claude/Anthropic': (23, 0.85), 'Docker': (22, 0.75), 'Next.js': (17, 0.70),
    'Redis': (13, 0.55), 'Voice/TTS': (13, 0.50), 'GraphQL': (12, 0.40),
    'LangChain/LangGraph': (10, 0.80), 'Kafka/queues': (10, 0.55),
    'MCP': (8, 0.70), 'FastAPI': (7, 0.90), 'RAG': (7, 0.95),
}

# AEGIS v1 as scoped: control plane + wired engines + dashboard + deploy layer
AEGIS_V1 = {
 'Python': 2, 'Agents': 2, 'TypeScript': 2, 'Node.js': 2,
 'Postgres': 2, 'FastAPI': 2, 'React': 2, 'Next.js': 1,
 'Evals/obs': 2, 'Claude/Anthropic': 2, 'RAG': 2, 'MCP': 2,
 'LangChain/LangGraph': 2, 'Docker': 2,
 'Redis': 1, 'Kafka/queues': 1, 'k8s': 1, 'Terraform': 1, 'AWS': 1,
 'Go': 0, 'Rust': 0, 'GraphQL': 0, 'Voice/TTS': 0,
}

def cov(marks):
    num = den = 0
    for t, (m, w) in MARKET.items():
        den += w * 2
        num += w * marks.get(t, 0)
    return num / den * 100

SEVEN = {'Python':2,'Agents':2,'TypeScript':2,'Node.js':2,'Evals/obs':2,
         'Claude/Anthropic':2,'RAG':2,'MCP':1,'LangChain/LangGraph':2}

print("=== COVERAGE LADDER ===")
print(f"trio repos        {cov(SEVEN | {'x':0} if False else SEVEN):5.1f}%")
print(f"AEGIS v1 complete {cov(AEGIS_V1):5.1f}%")

# greedy: what remains, max gain first
remaining = {
 'Voice-loop demo (Phonely-style)': ['Voice/TTS'],
 'Redis budget cache tier': ['Redis'],
 'Kafka evidence ingest': ['Kafka/queues'],
 'k8s manifests + helm chart': ['k8s'],
 'Terraform module (one-command AWS)': ['Terraform', 'AWS'],
}
cur = dict(AEGIS_V1)
print("\n=== REMAINING GAPS, GREEDY ORDER ===")
while remaining:
    base = cov(cur)
    best = None
    for name, techs in remaining.items():
        t = dict(cur)
        for x in techs: t[x] = max(t.get(x, 0), 2)
        g = cov(t) - base
        if best is None or g > best[0]: best = (g, name, techs)
    g, name, techs = best
    for x in techs: cur[x] = max(cur.get(x, 0), 2)
    del remaining[name]
    print(f"  +{g:4.1f}%  {name:38s} -> {cov(cur):5.1f}%")

# per-lead mapping
LEADS = {
 'Matterhaul ($200-260K founding AI)': [
   ('plan/execute loops with checkpointing', 'meshwork engine'),
   ('deterministic replays', 'run-replay engine'),
   ('prompt-injection defense on transcripts', 'sentinel engine'),
   ('tool authorization', 'policy sidecar'),
   ('token-level tracing, cost per workflow', 'governor ledger'),
   ('latency budgets per step', 'sentinel budget enforcement'),
   ('drift detection', 'evalforge nightly runs'),
   ('model routing across tiers', 'governor cascade'),
   ('eval harness tied to CI w/ golden sets', 'evalforge gates'),
 ],
 'Phonely AI (voice agents)': [
   ('voice-loop latency budgets', 'sentinel enforced budget'),
   ('per-call cost caps', 'governor wallets'),
   ('call forensics/compliance', 'replay chains'),
   ('knowledge freshness for answers', 'ragforge provenance'),
 ],
 'Starbridge (insurance AI, NYC)': [
   ('PII handling + audit trail', 'sentinel lanes + tombstones'),
   ('human-in-loop for claims', 'meshwork gates'),
   ('SOC2-ready evidence', 'one-click export'),
 ],
}
print("\n=== TIER-A LEAD MAPPING (JD line -> AEGIS part) ===")
for lead, rows in LEADS.items():
    print(f"\n{lead}")
    for jd, part in rows:
        print(f"  {jd:44s} <- {part}")
