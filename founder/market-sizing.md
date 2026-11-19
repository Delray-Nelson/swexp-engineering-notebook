# Market Model: JBF Dating (Just Be Funny)

## Part 1 — Definitions in Your Own Terms

- **TAM entity:** Single adults in the United States who experience dating app fatigue, small-talk exhaustion, and superficial photo bias while looking for romantic connection or dates. *(Note: `founder/problem-hypothesis.md` currently holds a draft log-triage hypothesis; for JBF Dating, the intended customer segment is single adults tired of generic dating app small talk who want banter-first matching.)*
- **Annual revenue per entity:** **$120 – $180 / year** ($10–$15/month challenger subscription tier), anchored below major dating app tiers (~$22–$33/month) to lower willingness-to-pay friction for a humor-first alternative.
- **SAM filters:**
  - `f1` (segment fraction — small-talk fatigue & humor-openness): **0.50 – 0.70**
  - `f2` (geography / language / platform fraction — single launch metro, English mobile/web): **0.015 – 0.030**
  - `f3` (near-term product scope fraction — humor-prompt & banter MVP without video/events): **0.55 – 0.65**
- **SOM window:** **12–24 months** via channels: **hyper-local comedy/social scenes, short-form humor content (Reels/TikTok/shorts), local singles/young-professional communities, and organic peer referrals operated by a solo technical founder**.

---

## Part 2 — Research the Count (Two Independent Sources)

1. **Source A — Pew Research Center (U.S. Online Dating Adoption):**
   - **Figure:** **30%** of U.S. adults overall have ever used an online dating site or app (**52%** of never-married U.S. adults; **53%** of adults under 30; **9%** used in the past year) `(source: Pew Research Center, 2023)`. Applied to ~117M unmarried U.S. adults (or broader U.S. adult dating user base), a working U.S. addressable user count is **~25,000,000 – 35,000,000 users** `(assumption, confidence: medium)`.
   - **Fit to our definition:** Strong demographic/behavioral match for U.S. dating app users, though "ever used" is broader than active users experiencing small-talk fatigue right now.

2. **Source B — Industry Market Sizing (Global & North America Online Dating Revenue):**
   - **Figure:** Global online dating market estimated at **~$12.1B–$13.0B** (2025–2026) `(source: Grand View Research, 2026)` and **~$6.09B** in 2026 `(source: Precedence Research, 2026)`, with North America accounting for **~36%** of global share `(source: Grand View Research, 2026)` and the U.S. accounting for **~83.1%** of North America `(source: Mordor Intelligence, 2026)` (and U.S. online dating market estimated at **~$3.23B–$3.47B** in 2025–2026 `(source: Market Data Forecast, 2026)`).
   - **Fit to our definition:** Useful as a top-down cross-check on paid category spend, though revenue-based reports measure existing subscription/ad monetization rather than counting every small-talk-fatigued single directly.

---

## Part 3 — The Model (Recomputable Formulas, Low & High Cases)

### Inputs & Tags
- `count_low` = `25,000,000` users `(assumption, confidence: medium; derived from Pew Research Center 2023 adoption shares)`
- `count_high` = `35,000,000` users `(assumption, confidence: medium; derived from Pew Research Center 2023 adoption shares)`
- `price_low` = `$120` / year `(assumption, confidence: medium)`
- `price_high` = `$180` / year `(assumption, confidence: medium)`
- `f1_low` = `0.50`, `f1_high` = `0.70` `(assumption, confidence: medium; burnout/small-talk fatigue share)`
- `f2_low` = `0.015`, `f2_high` = `0.030` `(assumption, confidence: high; single launch metro share of U.S.)`
- `f3_low` = `0.55`, `f3_high` = `0.65` `(assumption, confidence: medium; humor-first MVP scope fit)`
- `reachable_low` = `15,000` users, `reachable_high` = `40,000` users `(assumption, confidence: low; solo founder 12–24 month local reach)`
- `conv_low` = `0.03` (3%), `conv_high` = `0.06` (6%) `(assumption, confidence: medium; freemium-to-paid conversion)`

### 1. TAM Formula
`TAM = (number of entities with the problem) x (annual revenue per entity)`
- **Low case:** `25,000,000 x $120` = **`$3,000,000,000` (`$3.00B / year`)**
- **High case:** `35,000,000 x $180` = **`$6,300,000,000` (`$6.30B / year`)**

### 2. SAM Formula (2-Year Single-Metro Launch Scope)
`SAM = TAM x f1 x f2 x f3`
- **Low case:** `$3,000,000,000 x 0.50 x 0.015 x 0.55` = **`$12,375,000` (`~$12.4M / year`)**
- **High case:** `$6,300,000,000 x 0.70 x 0.030 x 0.65` = **`$85,995,000` (`~$86.0M / year`)**

### 3. SOM Formula (12–24 Month Window)
`SOM = (reachable pool) x (conversion fraction) x (annual revenue per entity)`
- **Low case:** `15,000 x 0.03 x $120` = **`$54,000` / year** *(450 paying subscribers)*
- **High case:** `40,000 x 0.06 x $180` = **`$432,000` / year** *(2,400 paying subscribers)*

---

## Part 4 — Sensitivity and Verdict

- **Highest-leverage input to verify:** **Local reachable pool & two-sided liquidity (`reachable_low` / `reachable_high`) paired with early user retention/conversion (`conv`)**. Because a dating app fails if users are spread thin across a city without active local matches, 10,000 scattered signups matter far less than dense local engagement. I can verify this cheaply before building a full-featured app by running a hyper-local landing page / humor-prompt waitlist test in one target city and tracking prompt-completion and return rates.
- **Verdict:** At a 12–24 month **SOM of ~$54K–$432K** in a single launch metro (out of a **~$12.4M–$86.0M** local SAM and **~$3.0B–$6.3B** U.S. TAM), JBF Dating starts as a **lean, liquidity-constrained bootstrap / independent product bet** rather than an instant venture-scale outcome—and I am holding myself to proving **dense local user activity and humor-prompt engagement in one metro** before expanding city count or building complex secondary features. If local liquidity and prompt-to-conversation conversion stay weak after initial testing, I will narrow the launch wedge to a specific campus/nightlife community or pivot the core mechanic before scaling spend.
