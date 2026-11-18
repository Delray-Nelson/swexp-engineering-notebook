# Submission Workspace

**Source:** Lesson 08 Submission — Deliverable: Pull Request & Peer Review (COLLAB-2028)  
**Engineer:** Hurdle TM · **Date:** 2026-11-18 · **Competency:** Pull Request Lifecycle, Code Review Feedback & Repository Governance  

---

### 1. Ticket & objective
Ship the JSON-export feature (`COLLAB-2028`) through a reviewed Pull Request workflow without pushing directly to `main`, address review feedback via a follow-up commit, author a constructive review on a second Pull Request, and implement repository-level PR templates and `CODEOWNERS` governance.

### 2. What I did
* Reconnected the local repository (`swexp-engineering-notebook`) to GitHub over SSH (`git@github.com:Delray-Nelson/swexp-engineering-notebook.git`) using an Ed25519 key.
* Implemented `.github/pull_request_template.md` and `.github/CODEOWNERS` on `main` so all future PRs enforce a structured description and explicit owner routing (`@Delray-Nelson`).
* Created `feature/json-export`, built `src/export_json.sh` with strict Bash error handling (`set -euo pipefail`), and opened **PR #1** using the new PR template.
* Left inline review feedback on **PR #1** requesting a UTC ISO-8601 `exported_at` timestamp, pushed a follow-up fix commit (`fix(export): add UTC exported_at timestamp per PR review feedback`), and merged **PR #1** into `main`.
* Created a second branch (`docs/pr-workflow-notes`), opened **PR #2** updating `README.md`, authored a constructive peer review with actionable documentation improvements, and merged **PR #2**.

### 3. Evidence
* **Primary Feature PR (with follow-up commit):** https://github.com/Delray-Nelson/swexp-engineering-notebook/pull/1
* **Secondary Peer-Reviewed PR:** https://github.com/Delray-Nelson/swexp-engineering-notebook/pull/2
* **Repository Governance Files:** `.github/pull_request_template.md` and `.github/CODEOWNERS`

#### Constructive Review Text Submitted on PR #2
> **Constructive Review:**
> Clear and concise documentation addition (`README.md`). Two suggestions to make this actionable for incoming contributors:
> 1. Link directly to `.github/pull_request_template.md` and `.github/CODEOWNERS` so readers know where those standards are enforced.
> 2. Clarify whether "at least one follow-up verification check" refers to automated CI status checks or manual reviewer sign-off.
> Once clarified, this is ready to merge!

#### How PR Templates Raise the Floor on PR Quality (Stretch Goal)
* **Eliminates Blank-Slate Friction:** Pre-populates structured prompts (Ticket ID, Summary, Change Type, Verification) so no PR is opened with an empty or vague description.
* **Reduces Reviewer Cognitive Load:** Standardizes where reviewers look for intent and test verification steps before inspecting diffs.
* **Forces Pre-Submission Verification:** Checklists catch unisolated branches, leaked secrets, and unverified diffs before a reviewer is pinged.

### 4. Decisions & trade-offs
* **Preserving Follow-Up Commits on Merge:** Used a standard merge commit rather than squashing PR #1 so the incremental review-response commit remains auditable in the Git history graph.
* **Self-Review Discipline:** Used a second feature branch (`docs/pr-workflow-notes`) to practice evaluating diffs from a reviewer's perspective (clarity, onboarding links, edge-case ambiguity) rather than rubber-stamping changes.

### 5. AI usage (draft → verify → log)
* **Asked:** How to troubleshoot Ed25519 SSH key authentication, structure `.github/pull_request_template.md` and `CODEOWNERS`, and execute the two-PR review workflow.
* **Verified against:** Live GitHub PR URLs (`/pull/1` and `/pull/2`), `ssh -T git@github.com` handshake output, and local `git log --oneline --graph` history.
* **Corrections:** Avoided nested triple-backtick code fences inside heredoc templates to prevent premature shell truncation during deployment.
* **Final, trusted result:** Both PRs merged cleanly over SSH with repository governance files active on `main`.

### 6. Definition of Done
* [x] Opened a real PR with a complete structured description (`.../pull/1`)
* [x] Addressed review feedback via a follow-up commit before merging (`.../pull/1`)
* [x] Wrote a constructive review on a second PR (`.../pull/2`)
* [x] Added `.github/pull_request_template.md` and `.github/CODEOWNERS` and explained how templates raise PR quality

### 7. Reflection
A Pull Request is a collaboration and quality-control layer built on top of Git branches. Combining automated PR templates with disciplined, constructive peer review catches ambiguity and missing edge cases before changes reach `main`.
