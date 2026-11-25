# Week 3 Exercises: Safe Request Routing, Settings Verification Memo & Policy Pressure Test

---

## Exercise 1 — Route the Request (Preserving Utility Without Exposure)

### (a) Debugging a stack trace that includes a connection string
- **Safe workflow:** Keep the full file path, line numbers, exception class, error code, and query/pool context intact, while replacing the connection URI credentials and host with structural placeholders (e.g., `postgres://[DB_USER]:[REDACTED_PASSWORD]@[DB_HOST]:5432/[DB_NAME]?sslmode=require`). Paste only the relevant stack frames rather than the surrounding `.env` dump.
- **Transformation applied:** **Structural secret masking (credential & host redaction)** — removes authentication secrets while preserving protocol, SSL parameters, and error semantics needed to diagnose the failure.

### (b) Drafting an email to a customer where the real thread contains their PII
- **Safe workflow:** Strip names, email addresses, phone numbers, handles, billing IDs, and message timestamps; replace them with role tokens (`[Customer]`, `[Plan Tier]`, `[Issue Summary]`), paste only the non-identifying problem summary and desired tone/outcome to draft the reply, and re-insert real PII locally in your email client before sending.
- **Transformation applied:** **PII stripping & placeholder tokenization** — isolates communication intent and context while keeping identifiable customer records out of the prompt.

### (c) Asking an agent to fix code that reads `STRIPE_SECRET_KEY`
- **Safe workflow:** Let the agent inspect the source file referencing `os.environ["STRIPE_SECRET_KEY"]` (never the `.env` file or live secret value) and run tests against a mock/stubbed `sk_test_mock_placeholder` environment variable or local Stripe mock fixture, keeping `.env` in `.gitignore` and agent ignore rules.
- **Transformation applied:** **Secret indirection & mock fixture substitution** — exposes only the environment variable reference and synthetic test key format so the agent can fix and verify the code path safely.

### (d) Analyzing churn on a real customer CSV
- **Safe workflow:** Run a local Python script (`pandas`) to drop direct identifiers (`email`, `name`, `user_id`, `ip_address`), bucket/generalize quasi-identifiers (`signup_date` -> `signup_cohort_week`, `city` -> `metro_region`), and either feed only aggregated cohort metrics or a schema-matched synthetic/perturbed sample CSV into the AI tool for hypothesis generation, then execute the final cohort queries locally.
- **Transformation applied:** **De-identification, cohort aggregation & synthetic schema mirroring** — preserves statistical churn signals and column structure while eliminating row-level customer identifiability.

---

## Exercise 2 — Settings Verification Memo (Dated: 2026-11-25)

> **Verification Discipline Note:** Per Lesson 3 verification standards, every field below must come directly from settings screens and vendor privacy/data documentation you personally opened on **2026-11-25**—never from model memory. Replace the `[VERIFY IN UI/DOCS]` slots with the exact strings from your open tabs before final submission.

### Tool 1: `[VERIFY IN UI/DOCS — e.g., Claude / ChatGPT / Cursor]`
- **Date verified:** `2026-11-25`
- **Exact plan name (from Billing / Account settings screen):** `[VERIFY IN UI/DOCS — e.g., Claude Pro / Team / Enterprise or ChatGPT Plus / Team]`
- **Training setting & exact UI path:** `[VERIFY IN UI/DOCS — e.g., Settings > Privacy > "Help improve..." toggle = OFF / Workspace admin default off; record exact menu path and toggle label]`
- **Retention statement (from official Privacy Policy / Data Controls page):** `[VERIFY IN UI/DOCS — quote/cite exact retention window and zero-data-retention/deletion rules from official vendor docs]`
- **Transcript sync behavior (from Settings / Sync documentation):** `[VERIFY IN UI/DOCS — state whether conversations sync across web/desktop/mobile cloud history, local disk storage path, and how deletion propagates]`

### Tool 2: `[VERIFY IN UI/DOCS — e.g., CLI Coding Agent / IDE Assistant]`
- **Date verified:** `2026-11-25`
- **Exact plan name (from Account / Subscription screen):** `[VERIFY IN UI/DOCS — exact plan tier & workspace type]`
- **Training setting & exact UI path:** `[VERIFY IN UI/DOCS — exact settings path, toggle label, and verified state]`
- **Retention statement (from official Privacy / Terms page):** `[VERIFY IN UI/DOCS — exact retention statement for prompts, code context, and telemetry]`
- **Transcript sync behavior (from Settings / Docs):** `[VERIFY IN UI/DOCS — local session transcript location vs. cloud sync behavior]`

---

## Exercise 3 — One-Page Policy & Hour-by-Hour Working-Day Pressure Test

### A. One-Page Team Policy Reference (`founder/ai-llm-policy.md`)
1. **Data Tiers:**
   - *Never-prompt:* Production secrets/keys (`.env`, `STRIPE_SECRET_KEY`, DB URIs), live user PII/banter/match logs, unreleased ranking/scoring weights.
   - *With-care:* Redacted stack traces, cohort-aggregated metrics, sanitized support summaries, upcoming feature specs.
   - *Fine:* Synthetic banter fixtures, public docs/libraries, unit-cost/latency scripts (`cost_model.py`), generic templates.
2. **Approved Tools & Settings:** Only verified workspaces/plans with training toggles confirmed OFF and logged (`tool | plan | toggle_path | verified_by | date`).
3. **Secrets Rule & Mechanism:** Zero credentials in prompts; keys live in secret managers/local `.env` excluded from Git/agent reads; run pre-commit/repo secret scans; rotate immediately if exposed.
4. **Customer-Data Rule:** Synthetic-data default for all dev, prompt tuning, and banter evaluation; live customer data permitted only under verified agreements and non-training endpoints.
5. **First-Hour Incident Procedure (Blameless):** `0–15m` revoke & rotate credential; `15–30m` log `what/where/when`; `30–45m` verify surface retention/training behavior; `45–60m` notify required stakeholders/parties and add preventive guardrails.

### B. Hour-by-Hour Pressure Test on a Recent Working Day (JBF Dating Development)
- **09:00–10:00 — Morning setup & repo sync:** Pulled `swexp-engineering-notebook`, reviewed `founder/competitor-matrix.md` and `value-prop-canvas.md`. *Policy tier:* `Fine` (internal strategy docs with zero PII/secrets). *Change:* None needed.
- **10:00–11:30 — Scripting AI token cost & routing model (`cost_model.py`):** Built and executed local Python arithmetic for break-even volume (`44,114` reqs/mo) and 20-turn caching (`38.6%` savings). *Policy tier:* `Fine` (synthetic token counts + public pricing). *Change:* None needed.
- **11:30–13:00 — Debugging auth/database configuration error:** Hit a local connection error while testing environment config. *Policy tier:* `Never-prompt` for raw `.env` / connection URI -> transformed to `With-care`. **Policy-driven change:** Instead of pasting the raw terminal traceback containing local credentials/host parameters into an AI chat, I masked the connection string to `postgres://[USER]:[REDACTED]@[HOST]:5432/[DB]` before asking for diagnostic help.
- **14:00–15:30 — Designing JBF banter-evaluation prompt & fixtures:** Needed test conversations to calibrate humor/lore scoring and check escalation rules. *Policy tier:* `Customer-data rule` (synthetic-data default). **Policy-driven change:** Authored 5 synthetic multi-turn banter fixtures from scratch rather than pulling real user/tester messages or personal DMs into the prompt harness.
- **15:30–17:00 — Repo secret scan & policy documentation:** Ran read-only regex secret pattern scan across workspace files (`0` credential matches) and committed Week 3 notes/exercises to Git. *Policy tier:* `Secrets rule & mechanism`. **Policy-driven change:** Verified untracked files before running `git add` and ran a secret check prior to committing so scratch files never reached `origin/main`.
