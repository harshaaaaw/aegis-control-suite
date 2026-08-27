# Cold Outreach Strategy: Harsha x Top-10 HN Leads

Written August 2026. Ground truth sources: live GitHub audit of harshaaaaw, scraped context from the Aug 2026 Who's Hiring thread, company sites fetched the same week.

---

## Part 1: Who Harsha actually is (verified facts only)

- AI/data architect. Built and ran GE Aerospace RADAR: a 4-petabyte document-intelligence pipeline. That number is rare. Use it once, precisely, in the right emails.
- Production stack: n8n orchestration, LangGraph agent graphs, Pinecone retrieval, AWS.
- Security side: real HackerOne findings, live exploitation work, CDP-driven browser automation. Not a hobbyist claim; there are receipts.
- Starting MPI-CIS (research master's) November 2026: graph-augmented retrieval and cyclic multi-agent systems.
- B.E. CSE with DevOps specialization, graduated 2025.
- Based in India. Wants abroad roles or remote. Needs sponsorship or a remote-first employer. This filters half the list immediately.
- GitHub today: 31 repos, 18 forks, thin descriptions, no pinned story. Fixable in weeks, fatal if ignored.

## Part 2: Lead ratings against that profile

Score = skill fit (40%) x reply probability (30%) x visa/location feasibility (30%).

| Rank | Lead | Fit | Reply odds | Visa odds | Score | Verdict |
|---|---|---|---|---|---|---|
| 1 | recruiting@phonely.ai | Voice AI agents; he ships TTS/STT pipelines and agent loops | Recruiting inbox, monitored | CA startup, remote unknown | 8.1 | Attack first |
| 2 | amber.auslander@matterhaul.com | AI agents for industrial ops; his agent + doc-intel work maps 1:1 | Named human, founder-adjacent | US, small team, flexible | 7.8 | Attack first |
| 3 | recruiting@starbridge.ai | Public-sector contracts are document hell; RADAR is the exact scar tissue | Recruiting inbox | NYC, funded, hiring many | 7.4 | Attack first |
| 4 | ivanc@dualentry.com | AI ERP = ingestion + correctness; both his strengths | Named person | NY, early stage | 6.9 | Week 2 |
| 5 | tarek@rivergtm.com | LLM workflows + browser-use agent demos; literally his nightly build | Works directly w/ founders | ONSITE NYC = blocked unless remote appears | 6.5 | Ask, don't pitch |
| 6 | kyle@snout.com | Node/AWS backend needs; he has AWS depth, TS gap shows | Founder post, gets floods | US pet-tech | 5.8 | After repos ship |
| 7 | george@vitabyte.com | Correctness culture + payments adjacency; BankingBot too stale | Founder post | NYC, needs Go | 5.5 | After repos ship |
| 8 | careers@doubling.io | Fintech infra fits | 1099 contract: almost never sponsors, tax friction for India | 4.2 | Only if they say remote-world OK |
| 9 | heather@radicalnumerics.ai | Research lab prestige; MPI-CIS start helps later | All-onsite SF, bar extreme | 3.8 | Revisit post-MPI-CIS |
| 10 | nicholas.hanson@govstar.us | Infra work fits | US govtech usually needs clearance/citizenship | 2.9 | Skip unless they post non-clearance |

Sequence: Tier A (leads 1-3) get emails in week 1. Tier B (4-7) get warm-up touches now, pitches after the three repos land. Tier C waits.

## Part 3: The gap matrix

What their posts asked for vs what his GitHub proves today.

| Company wants | Evidence he has it | GitHub proves it | Gap action |
|---|---|---|---|
| LLM agents in prod | LangGraph + personal agent running daily | Nothing visible | Project 1 (agent-sentinel) |
| TypeScript/full-stack | n8n custom nodes, but no TS repo | No | Project 2 (ledgerlens, in TS) |
| Data pipelines at scale | 4PB RADAR, MinHash dedup, resumability | RADAR repo undescribed, empty-looking | Project 3 (docforge) + RADAR rewrite |
| Payments/money correctness | Theory only | Stale BankingBot from 2024 | Project 2 covers invariants |
| Voice AI | TTS/STT pipelines in his agent stack | No | Fold a demo into Project 1 |
| DevOps/infra maturity | DevOps degree, CI on bounty work | Invisible | CI badges on all 3 repos |
| Communication | Writes daily (Reddit agent ops, reports) | Invisible | READMEs written like a human, not slop |

The single biggest gap, confirmed: proof of work. Not skills, proof. Recruiters cannot verify a 4PB war story. They can verify a repo in 90 seconds.

## Part 4: 17 points of view (how each actor sees your email)

1. **The hiring manager at 7am.** Inbox has 47 unread, 12 are applicants. She triages on subject line + first sentence. Your subject must name her problem ("injection-proof agent tooling"), never your need ("job seeking").
2. **The skeptical technical founder.** He has been burned by resume inflation. First thing he does: open your GitHub. If pins show forks and empty repos, you're done before paragraph two. Everything else in this plan protects this moment.
3. **The recruiter speed-reader.** Six seconds. Looks for: role keyword match, one number that impresses, one link that works. Format emails with exactly those three anchors, nothing else.
4. **The peer engineer who'll vet you.** Wants evidence you debug, not just build. READMEs need a "what broke and how I found it" section. War stories beat feature lists.
5. **The visa realist.** Half these startups have never sponsored. Lead with value, surface location in sentence three, offer contractor/trial paths so "no" costs them something.
6. **The budget-cycle watcher.** Startups hire when funding lands or someone quits. Their post is 3 weeks old; momentum decays weekly. Email within days of scraping, follow up on a Tuesday or Wednesday morning their time.
7. **The proof-over-paper believer.** Most technical founders now trust repos over resumes. Three tight repos with real commits over months say "this person ships" louder than any bullet point.
8. **The warm-path advocate.** A thoughtful public reply on their HN post before the email doubles open-to-reply rates. It converts cold to familiar. Costs 20 minutes.
9. **The referral hunter.** Check LinkedIn for shared connections (Chandigarh alumni at these firms, GE people, Indian founding teams). One intro beats ten cold emails.
10. **The portfolio narrator.** Three random repos are noise. Three repos telling one story ("I make LLM agents safe, correct, and cheap at scale") are a thesis. Pin in that order: sentinel, ledgerlens, docforge.
11. **The demo-first judge.** A 30-second GIF of an injection being blocked live beats 1,000 words. Every repo needs one at the top of its README.
12. **The risk-minimizer.** Hiring is risk removal. Your email's job: show you've already survived production scale (4PB), so onboarding you is low-risk. Say it with one number, not adjectives.
13. **The economics observer.** India-based senior talent is a genuine cost advantage for cash-strapped startups, but never lead with price. Lead with output; let them do the math.
14. **The follow-up strategist.** One email is a lottery ticket. Three touches (day 0 value, day 4 artifact, day 9 graceful close) convert 2-3x better. Each touch adds something new, never "just bumping this."
15. **The channel chooser.** Email for recruiting@ inboxes and named founders. HN private message for solo founders. LinkedIn DM only after an email bounce. Never connect-request without a note.
16. **The anti-slop sentry.** Founders smell ChatGPT instantly. Every outbound line passes the humanizer filter: no em dashes, no "I hope this finds you well," no "not just X but Y." Write like the terminal logs he reads all day: short, concrete, numbered.
17. **The whole-person assessor.** They're hiring a coworker. Your GitHub bio, pinned order, even commit message hygiene signal what working with you feels like. Clean those like you'd clean your desk before guests.

## Part 5: The math on projects

Why exactly three: one is luck, two is a coincidence, three is a pattern. Each targets a different JD family, all share the agent-infrastructure thesis:

1. **agent-sentinel (Python).** Prompt-injection firewall for LLM agents that call tools. Treats every tool result like untrusted network input, applies policy rules, logs decisions for audit. Speaks to: Phonely, Starbridge, Matterhaul, DualEntry, River, and every "AI safety" checkbox in 2026 JDs. Killer demo: paste a poisoned webpage, watch the agent try to exfiltrate, watch the firewall block and log it.
2. **ledgerlens (TypeScript).** Double-entry money-movement core that survives kill -9. Property-based invariants (sum of debits equals credits, no phantom balances), deterministic replay from append-only log, chaos test in CI that kills the process mid-transfer and proves zero drift on restart. Speaks to: Vitabyte, Doubling, Snout, any fintech-adjacent JD. Killer demo: the recovery GIF plus the invariant report.
3. **docforge (Python).** Incremental document-intelligence pipeline: MinHash/LSH dedup, checkpoint-resume, cost-per-document benchmarks. The generic, open version of RADAR. Speaks to: DualEntry, Starbridge, Snout backends, every "data pipeline" line in JDs. Killer demo: benchmark chart showing 40x cheaper reindex when 2% of docs change.

Commit discipline: each repo gets 15-25 commits spread across separate days with real messages ("fix: LSH band collision on near-dup threshold", not "update"). One-day dump = detectable. CI on all three (GitHub Actions, tests green badges). Honest LIMITATIONS sections; admitting scope reads senior, hiding it reads junior.

## Part 6: Profile conversion funnel

Order a stranger sees: avatar, name line, bio, pinned row. Rewrite each:
- Name line: "Deva Harsha Mummareddy | AI infrastructure & agent safety"
- Bio: one sentence with the 4PB number and agent focus. Location: India (Remote-friendly).
- Pins: sentinel, ledgerlens, docforge. Nothing else visible by default.
- Profile README: short origin story, the three repos as chapters, contact line. Written in first person, humanizer-clean.

## Part 7: Outreach assets (drafted after repos ship)

Three tiers, three touches each, all humanizer-filtered, all under 120 words per email. Tier A drafts ready in outreach/. Subject lines name their problem. Every claim links to a receipt.

## Part 8: Self-rating rubric (applied after each piece, loop until 9+/10)

Rate each deliverable on: would a skeptical founder believe it (0-4), does it survive a 6-second scan (0-2), does it survive a 5-minute code read (0-4)? Anything under 9 total gets another pass. Log scores here as pieces complete.

Current baseline scores:
- GitHub profile pre-work: 3/10 (audited today)
- Target after 3 repos + profile: 9/10
