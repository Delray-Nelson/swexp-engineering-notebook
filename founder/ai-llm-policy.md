# JBF Dating — One-Page AI & LLM Policy

## 1. Data Tiers (Concrete JBF Examples)
- **Never-prompt (strictly prohibited in external/unapproved prompts):**
  1. API keys, OAuth client secrets, database connection strings, or signing tokens (e.g., Stripe, auth, or model provider keys).
  2. Production user PII, private messages/banter histories, match records, or real user photos/handles.
  3. Unreleased matching/ranking algorithms, proprietary scoring weights, or confidential commercial/legal terms.
- **With-care (redact, anonymize, or isolate first; check approved surface):**
  1. Sanitized bug reports, stack traces, or schema snippets that could contain embedded identifiers or internal URLs.
  2. Aggregated product metrics, prompt-routing evaluation sets, or banter moderation edge cases—strip user IDs, handles, and timestamps first.
  3. Draft product copy, growth experiments, or architectural trade-offs that touch upcoming JBF features.
- **Fine (safe for approved tools under verified non-training settings):**
  1. Synthetic or hand-authored sample banter exchanges and humor/lore rubrics with zero real user data.
  2. Public documentation, open-source libraries, standard language syntax, and general unit-cost/latency math.
  3. Generic engineering templates, regexes, test fixtures, and non-sensitive documentation drafts.

## 2. Approved Tools and Required Settings
- **Approved coding/CLI & chat surfaces:** Only pre-approved vendor accounts/workspaces with model training / data-retention opt-out configured appropriately for the tier used (`[verify & record exact plan name, org ID, training toggle status, verifier name, and verification date before use]`).
- **API & evaluation pipelines:** Only approved API keys and endpoints configured with zero data retention / non-training terms where required, never personal or unvetted consumer chat accounts.
- **Verification log rule:** Any tool, plan tier, or model-training toggle change must be re-verified and logged (`tool | plan | training_off_confirmed | verified_by | date_yyyy_mm_dd`) before routing `with-care` or product-adjacent artifacts.

## 3. Secrets Rule and Enforcement Mechanism
- **Rule:** Never paste credentials, tokens, `.env` contents, or private keys into prompts or chat windows.
- **Secret manager:** Store all credentials in a dedicated secret manager or local environment store—never hardcode keys in prompts, scripts, or committed markdown/logs.
- **Scanning hooks & hygiene:** Run secret scanning checks (pre-commit / CI secret scanners) and scrub shell history or log files before sharing snippets or committing to Git.
- **Rotation procedure:** If any secret is exposed or suspected exposed, revoke and rotate it immediately in the provider console, update the secret manager/deployment config, and invalidate active sessions/tokens.

## 4. Customer-Data Rule
- **Agreement & surface gate:** Live or identifiable user data (profiles, banter threads, location/activity signals, support tickets) may touch an AI system only when covered by appropriate contractual/privacy terms, explicit purpose alignment, and verified non-training/retention controls.
- **Synthetic-data default:** All development, prompt iteration, banter-scoring calibration, and debugging use synthetic or anonymized fixtures by default—never raw production user data.

## 5. First-Hour Incident Procedure (Blameless)
- **Goal:** Act fast and surface mistakes early; this procedure is **blameless** so incidents are reported immediately rather than hidden.
- **Minutes 0–15 — Contain & rotate:** Revoke and rotate any exposed credential or key immediately; take down or restrict any affected test endpoint or shared session.
- **Minutes 15–30 — Record facts (`what / where / when`):** Document what data or secret was entered, which tool/endpoint/repo/session received it, and when it occurred (plus whether any git commit or log captured it).
- **Minutes 30–45 — Check surface behavior:** Check the tool/provider's retention, logging, and training settings/documentation for that specific surface and workspace.
- **Minutes 45–60 — Notify & follow up:** Notify required internal stakeholders and external/contractual parties as required by applicable agreements, log follow-up controls (such as redaction or scan rules), and review how to make the safe path automatic next time.
