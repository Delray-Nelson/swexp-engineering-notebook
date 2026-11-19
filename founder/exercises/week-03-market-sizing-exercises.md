# Week 3 Exercises: Market Sizing (JBF Dating)

## Exercise 1 — Kill the Top-Down Habit

### Top-Down Claim
The global online dating market is estimated at **$13.0B in 2026** (Grand View Research, 2026); capturing just **1%** of that figure would equal **$130M/year**.

### Definition Divergence (Two Sentences)
First, a global analyst figure aggregates worldwide markets, multiple currencies, and broad dating/relationship platforms rather than single adults in the U.S. who specifically suffer from dating-app small-talk exhaustion and want humor-first banter. Second, an arbitrary "1% capture" assumes frictionless global distribution and ignores two-sided local density requirements, whereas a bottom-up model starts from named customer counts and an explicit price.

### Side-by-Side Comparison & Discrepancy
- **Top-Down Claim (1% of $13.0B global market):** **$130,000,000 / year** `(source: Grand View Research, 2026 for $13.0B global estimate; assumption, confidence: low for 1% capture)`
- **Bottom-Up TAM (25M–35M U.S. dating-app users × $120–$180/yr):** **$3.00B – $6.30B / year** `(assumption, confidence: medium; anchored to U.S. user-base & challenger pricing assumptions)`
- **Discrepancy:** The top-down "1% slice" ($130M) is roughly **23x to 48x smaller** than the full bottom-up U.S. TAM ($3.0B–$6.3B), while the top-down *total* ($13.0B global) is roughly **2.1x to 4.3x larger** than the U.S. bottom-up TAM because it includes non-U.S. regions and non-specific dating segments.

### Which I Would Defend Under Questioning (and Why)
I would defend the **bottom-up model** under questioning because every number can be traced to a named audience count, a concrete annual price, and an explicit set of assumptions—so if an assumption is wrong, I can point to the exact input and test it rather than defending an unactionable "1%" slice.

---

## Exercise 2 — Price the Pain

### Interview & Market Spend Anchors
1. **Anchor 1 — Direct Subscription Spend on Dating Apps:** Major dating apps charge roughly **$22–$33/month** (`~$264–$396/year`) on paid tiers `(source: Match Group / Bumble public filings; assumption, confidence: medium)`. Even when users feel burnout or small-talk fatigue, paying subscribers already spend hundreds of dollars annually trying to get better matches and outcomes.
2. **Anchor 2 — Time & Opportunity Cost of Low-Signal Swiping & Small Talk:** In `founder/value-prop-canvas.md`, users report losing motivation to repetitive small talk and sifting through profiles during downtime `(source: founder/value-prop-canvas.md; assumption, confidence: low)`. Conservatively valuing just **15–30 minutes per week** of wasted swiping/small-talk time at a modest **$15–$25/hour** personal time value equals **~$195–$650/year** in friction cost `(assumption, confidence: low)`.

### Price Consistency (One Sentence)
JBF Dating's modeled annual price (**$120–$180/year**, or `$10–$15/month`) sits intentionally below existing dating-app subscription tiers (~$264–$396/year) and below conservative personal-time friction estimates (~$195–$650/year) to lower switching friction while testing willingness to pay for banter-first matching.

---

## Exercise 3 — The Order-of-Magnitude Cross-Check

### Method A — User-Base & Adoption Share Estimate (U.S. Dating App Users)
- **Method:** Start from ~117M unmarried U.S. adults, apply ~30% overall U.S. adult dating-app adoption (~52% among never-married adults; ~53% among 18–29 adults), and bound the active/addressable U.S. user pool to **25,000,000 – 35,000,000 users** `(source: Pew Research Center, 2023; assumption, confidence: medium)`.

### Method B — Top-Down Revenue / ARPU Decomposition
- **Method:** Take the U.S. online dating market revenue estimate of **~$3.23B–$3.47B** (Market Data Forecast, 2025–2026), note that industry benchmarks show paid subscribers are a minority subset (~15–25% of users) paying roughly **$240–$300/year**, and infer the implied active U.S. user pool:
  - Revenue ~$3.23B–$3.47B ÷ ~$250/yr implied payer spend ≈ **12.9M–13.9M paying users**, which at a **~20%–35%** payer share implies roughly **37M–70M total users** `(source: Market Data Forecast, 2025–2026; assumption, confidence: low)`.

### Comparison & Factor-of-10 Check
- **Method A range:** `25,000,000 – 35,000,000` users
- **Method B implied range:** `37,000,000 – 70,000,000` users
- **Ratio check:** The midpoint/bounds differ by roughly **1.5x to 2.8x**—well within a single order of magnitude (`< 10x`). Because both independent decompositions land in the tens of millions rather than hundreds of millions or hundreds of thousands, I keep the **25,000,000 – 35,000,000** U.S. user count range for the model while flagging that active/paying vs. "ever-used" remains a medium-confidence assumption to validate with real user behavior.
