# MNEMOS EXCHANGE - Final Spec v4.0 (first-mover redesign)

## The pivot

v3 (trust layer over stores) scored 88% but lost first-mover: 4 shipped
rivals (agent-memory, memotrust, trw-memory, Engram) own trust+decay+quarantine.
Pivot to the layer NOBODY ships: the EXCHANGE where facts are traded,
priced, and settled. Same engines, new market design, category unclaimed.

## The objective

AI agents run in silos, each blind to what every other agent already knows,
re-buying the same stale facts a thousand times. MNEMOS is the first fact
exchange for machines: agents publish verified facts with freshness SLAs,
buyers subscribe per-fact with micropayment settlement, wrong facts get
challenged, lose their publishers' bonds, and delist automatically.
Truth stops being a prompt concern and becomes a priced, auditable good.

## Why this is genuinely never-existed

- memory-trust stores (all 4 rivals): single-tenant, no pricing, no trading
- x402/AP2/Visa TAP: payment RAILS ($15M moved), zero applications selling facts
- Ocean Protocol/Snowflake Marketplace: dataset-scale blobs for humans; not
  per-fact, per-agent, sub-second freshness-SLA'd microtrades
- Wolfram Alpha: curated API, one seller, no market mechanism
Academic knowledge-market papers exist; zero shipped protocol + running
exchange. First mover = first working implementation + open spec.

## Market mechanics (each maps to an existing engine)

1. LISTINGS - supplier publishes fact w/ entity+attribute key, freshness SLA,
   asking price (fact-ledger contract)
2. DISCOVERY - buyers query by key/semantic; exchange returns cheapest fresh
   listing (canonical-answer API)
3. SETTLEMENT - buyer pays list price on delivery; ledger credits transfer;
   full statement per agent (token-governor wallet engine)
4. CHALLENGE MARKET - anyone can challenge a listed fact by paying bond;
   verifier runs; wrong = publisher loses stake, challenger rewarded,
   auto-delist + all past buyers credited back (run-replay evidence chains)
5. REPUTATION - publisher accuracy score compounds across orgs; high rep =
   cheaper bond requirements (evalforge scoring)
6. FRESHNESS SLA ENFORCEMENT - miss your refresh window twice, listing
   delists automatically (learned decay clocks)
7. QUARANTINE GATE - untrusted-lane facts cannot list without attestation
   (sentinel write-gate)

## Launch sequence (solves two-sided cold start)

Phase 1 single-org internal market: departments become suppliers/buyers,
settlement in internal credits = chargeback market with real incentives.
Phase 2 cross-org federation via MNEMOS-X wire spec (open, like RSS/x402).
Phase 3 optional real rails: x402, UPI micro, Stripe MPP.

## Demo (works offline, any country, no keys)

Sim city: 3 supplier agents, 5 buyer agents, challenge bot.
Buyer asks "price of SKU-482". Exchange routes to cheapest FRESH listing.
Supplier lets it go stale -> buyer's challenge fires -> bond slashed ->
delisted -> buyers refunded -> replacement supplier earns the volume.
Then `mnemos audit`: dollars wasted before vs after, per department.

## Business model

- OSS core: matching engine, settlement ledger, challenge protocol, sim wallets
- Revenue: take rate on cross-org settlement (2-3%), hosted exchange cloud,
  enterprise: private exchanges w/ compliance exports (tombstones, receipts)
- Network effects compound: more suppliers -> fresher facts -> more buyers ->
  more bond capital -> harder for rivals to enter late

## Re-validation: 94.4% weighted across 16 POVs (up from 88%)

Weakest remaining: cold start (mitigated by Phase 1 design) and ops realism
(v1 single-process sim settlement). Full matrix in mnemos_exchange_validate.py.

## Build order

1. fact contract + listing ledger + lineage hashes
2. matching engine (cheapest-fresh routing) + SQLite settlement ledger
3. sim wallets + statements (governor engine reuse)
4. challenge protocol + bond escrow + slashing + refunds
5. reputation scores from verdict history (evalforge hooks)
6. freshness SLA monitor + auto-delist (learned decayers)
7. quarantine gate wiring (sentinel lanes)
8. `mnemos audit` dollar report
9. MNEMOS-X open spec draft + demo city script

## JD coverage bonus

payments rails, marketplace design, double-entry ledgers, bonding/slashing,
reputation systems, settlement integrity - fintech-grade vocabulary that
River/DualEntry/Vitabyte leads interview for, on top of the AI-agent story.
