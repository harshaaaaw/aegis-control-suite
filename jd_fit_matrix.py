"""JD-fit matrix: current trio vs market stack, computed."""

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

REPOS = {
 'agent-sentinel': {'Python':2,'Agents':2,'Evals/obs':2,'Claude/Anthropic':2,
                    'FastAPI':0,'TypeScript':0,'Next.js':0,'Postgres':0,
                    'AWS':0,'Docker':0,'k8s':0,'Terraform':0,'RAG':0,'MCP':1,
                    'Voice/TTS':0,'Redis':0,'LangChain/LangGraph':1,'Node.js':0},
 'token-governor': {'Python':2,'Agents':2,'Evals/obs':2,'Claude/Anthropic':2,
                    'FastAPI':0,'TypeScript':0,'Next.js':0,'Postgres':0,
                    'AWS':0,'Docker':0,'k8s':0,'Terraform':0,'RAG':0,'MCP':0,
                    'Voice/TTS':0,'Redis':0,'LangChain/LangGraph':1,'Node.js':0},
 'run-replay':     {'Python':2,'Agents':2,'Evals/obs':2,'Claude/Anthropic':2,
                    'FastAPI':0,'TypeScript':0,'Next.js':0,'Postgres':0,
                    'AWS':0,'Docker':0,'k8s':0,'Terraform':0,'RAG':0,'MCP':0,
                    'Voice/TTS':0,'Redis':0,'LangChain/LangGraph':0,'Node.js':0},
}

def coverage(marks):
    num = den = 0
    for tech, (mentions, weight) in MARKET.items():
        if mentions < 7:
            continue
        den += weight * 2
        num += weight * marks.get(tech, 0)
    return num / den * 100

print("=== CURRENT coverage of top-23 market demands ===")
for r in REPOS:
    print(f"  {r:16s} {coverage(REPOS[r]):5.1f}%")
base = {t: max(REPOS[r].get(t, 0) for r in REPOS) for t in MARKET}
print(f"  {'TRIO COMBINED':16s} {coverage(base):5.1f}%")

PLANNED = {
 'FastAPI gateway services': ['FastAPI'],
 'sentinel-middleware TS port': ['TypeScript', 'Node.js'],
 'Postgres schemas + RLS example': ['Postgres'],
 'Dockerfiles + compose demos': ['Docker'],
 'OTel exporters (all three)': ['Evals/obs'],
 'run-replay MCP server': ['MCP'],
 'RAG-ingestion guard example': ['RAG'],
 'Voice-loop red-team demo': ['Voice/TTS'],
 'Terraform module (deploy any demo)': ['Terraform'],
 'k8s manifests': ['k8s'],
 'AWS deploy guide + OIDC CI': ['AWS'],
 'LangGraph adapter package': ['LangChain/LangGraph'],
}

print("\n=== GREEDY ADD ORDER (max coverage gain per piece) ===")
current = {t: base.get(t, 0) for t in MARKET}
remaining = dict(PLANNED)
while remaining:
    best = None
    base_cov = coverage(current)
    for name, techs in remaining.items():
        trial = dict(current)
        for t in techs:
            trial[t] = 2
        gain = coverage(trial) - base_cov
        if best is None or gain > best[0]:
            best = (gain, name, techs)
    gain, name, techs = best
    for t in techs:
        current[t] = 2
    del remaining[name]
    print(f"  +{gain:4.1f}%  {name:38s} -> trio {coverage(current):5.1f}%")
