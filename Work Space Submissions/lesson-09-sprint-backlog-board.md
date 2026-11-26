# Lesson 09 Deliverable — Sprint Backlog & Board

## 1. Sprint 1 Backlog Issues (JBF Dating)

### Issue #1: Enforce data-tier redaction and synthetic fixture default for LLM prompts
- **Labels:** `type:security`, `priority:high`, `sprint-1`
- **Priority:** High (1st)
- **Context:** JBF Dating cannot risk pasting credentials, raw user banter/PII, or unreleased matching weights into external prompts or training-enabled surfaces.
- **Acceptance criteria:**
  - [ ] Redaction helper masks connection strings, bearer tokens, API keys, and PII fields before outbound LLM calls.
  - [ ] Function fails closed (blocks outbound call and returns an explicit error) if redaction encounters an unparsed sensitive block.
  - [ ] Synthetic banter fixtures cover local/CI tests with zero real user records.

### Issue #2: Configure repository secret scan and blameless first-hour rotation runbook
- **Labels:** `type:security`, `priority:high`, `sprint-1`
- **Priority:** High (2nd)
- **Context:** Secrets or tokens in transcripts, logs, or commits require fast detection and a blameless response so mistakes are surfaced immediately rather than hidden.
- **Acceptance criteria:**
  - [ ] Secret scan check runs against repo files and exits non-zero when credential or private-key patterns match.
  - [ ] First-hour incident runbook documents `0–15m` revoke/rotate, `15–30m` `what/where/when` log, `30–45m` surface retention/training check, and `45–60m` stakeholder/contract notification.
  - [ ] Current tracked files pass the scan with zero active secret matches.

### Issue #3: Implement two-tier banter/lore evaluator with cache-safe prompt prefix
- **Labels:** `type:feature`, `priority:high`, `sprint-1`
- **Priority:** High (3rd)
- **Context:** JBF Dating differentiates on humor/lore fluency and banter-first matching while keeping per-turn inference costs low across multi-turn sessions.
- **Acceptance criteria:**
  - [ ] Static system prompt and banter/lore rubric sit at the start of the prompt without timestamps, request IDs, or random tokens.
  - [ ] Evaluator invokes the small model first and escalates to the flagship model when schema validation fails after 1 retry or confidence falls below `0.80` (proposed threshold).
  - [ ] Output returns a structured JSON result with score, tier used, and escalation reason.

### Issue #4: Maintain `cost_model.py` with failure-adjusted cost, break-even volume, and 20-turn cache math
- **Labels:** `type:tooling`, `priority:medium`, `sprint-1`
- **Priority:** Medium (4th)
- **Context:** Model tier routing and caching decisions depend on repeatable cost math—such as the `~44k` monthly requests break-even point and `~38%` 20-turn caching savings—rather than ad-hoc estimates.
- **Acceptance criteria:**
  - [ ] Script computes per-request cost, failure-adjusted cost (`raw_cost / acceptable_rate`), break-even request count, and 20-turn cached vs. uncached cost.
  - [ ] Rates, token counts, and acceptable rates are parameterized cleanly.
  - [ ] Running the script prints all summary metrics cleanly and exits `0`.

### Issue #5: Define banter thread, profile preference, and match state data models
- **Labels:** `type:feature`, `priority:medium`, `sprint-1`
- **Priority:** Medium (5th)
- **Context:** Banter-first matching and multi-turn exchange tracking require explicit data structures and validation rules before wiring UI flows.
- **Acceptance criteria:**
  - [ ] Models define user banter preferences, active match/thread state, and ordered message turns with required fields.
  - [ ] Invalid or missing fields raise explicit validation errors rather than silent defaults.
  - [ ] Unit tests verify model creation, validation errors, and retention/deletion metadata fields.

---

## 2. Sprint 1 Board Snapshot

| Todo | In progress | In review | Done |
| :--- | :--- | :--- | :--- |
| #2 Secret scan & blameless rotation runbook | #1 Data-tier redaction & synthetic fixture helper | | |
| #3 Two-tier banter evaluator & cache-safe prefix | | | |
| #4 `cost_model.py` failure, break-even & cache math | | | |
| #5 Banter thread, preference & match data models | | | |

---

## 3. Prioritization Reasoning

1. **Security and data-hygiene guardrails first (#1, #2):** Every subsequent prompt, synthetic test fixture, and Git commit depends on blocking `never-prompt` data and scanning for leaked credentials before running agent or LLM workflows.
2. **Core banter evaluation and cost economics second (#3, #4):** Once data boundaries are enforced, building the cache-safe, two-tier banter/lore evaluator alongside `cost_model.py` validates JBF Dating's core differentiator without uncontrolled token spend.
3. **Domain data models third (#5):** Defining banter thread, profile preference, and match state schemas follows once evaluation inputs and retention metadata requirements are concrete.

---

## 4. PR Auto-Close Verification (`Closes #1`)

1. Branch from `main`: `git switch -c feat/jbf-prompt-redaction`
2. Implement the redaction helper and synthetic fixture tests, commit, and open a Pull Request targeting `main` (or a test branch if `main` is protected) with `Closes #1` in the PR description.
3. Merge the PR and confirm Issue `#1` automatically transitions to **Closed** and moves to **Done** on the Sprint 1 board.
