# Week 3 Exercises: Break-Even, 20-Turn Cache Estimate & Two-Model Routing

## 1. Break-Even Finder
- **Implication for current usage:** At early JBF Dating prototype/single-metro volume (a few hundred to a few thousand evaluations per month), the dollar spread between small and flagship models is smaller than a single engineer-day (`$800.00`), so **output quality, latency, and avoiding debugging rework matter more early on**—whereas once volume crosses **82,645 requests/month**, small-vs-flagship savings exceed a full engineer-day every month and require strict tier discipline.

## 2. Cache-Aware 20-Turn Estimate (30k Stable Context)
- Caching the 30k stable context prefix at `0.10x` input cost cuts total session spend sharply across 20 turns (`$1.3980` to `$0.8580` on flagship, saving `$0.5400` or **38.6%**).
- **Volatile content note:** Putting timestamps, per-turn counters, or random request IDs inside rules files or system-prompt prefixes breaks prefix matching on every turn, turning `0.10x` cached reads back into full-price input tokens and quietly inflating multi-turn agent bills.

## 3. Two-Model Routing Sketch (JBF Banter & Lore Scorer)
- **Small model handles:** Routine banter tone/safety classification, simple spam/low-effort filtering, and high-confidence lore/humor tags on clear-cut exchanges (`1,200` in / `180` out tokens).
- **Flagship escalates:** Ambiguous sarcasm/irony where tone confidence is low, borderline safety/harassment flags, or multi-turn thread disputes.
- **Checkable escalation trigger:** Escalate to flagship whenever `confidence < 0.80` on tone/safety classification, required JSON schema validation fails after 1 retry, or `message_length > 250` chars with `sarcasm_flag == True` (modeled at a **15%** escalation rate: `$0.000504` blended per item vs. `$0.000210` single-small and `$0.008400` single-flagship).
