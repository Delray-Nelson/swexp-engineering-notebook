# Lesson 10 Submission — GOV-3001

Engineer: Delray Nelson · Date: 2026-11-26 · Competency: Protect the Production Branch (Governance)

## 1. Ticket & objective
Ticket `GOV-3001` asks to prevent broken or unreviewed code from landing directly on `main` by enforcing platform-level branch protection rules (pull request required, at least one approving review, required passing status checks, up-to-date branch check, and administrators included) and defining path ownership via `.github/CODEOWNERS` so good habits are mechanically enforced rather than left to memory.

## 2. What I did
Following **Lab 10 — Protect the Production Branch**, I synced `main` in `swexp-engineering-notebook`, created branch `lab-10-branch-protection`, added `.github/CODEOWNERS` covering sensitive paths, and pushed `lab-10-branch-protection` to `origin`. I also initialized an offline bare repo with a `pre-receive` hook in `/tmp/swexp-l10` to verify direct-push rejection on `refs/heads/main` while allowing pushes to a feature branch (`feature/x`), and configured branch protection on `main` in GitHub.

Key commands used:
- `git switch main && git pull origin main --rebase && git switch -c lab-10-branch-protection`
- `git add .github/CODEOWNERS && git commit -m "chore(repo): add CODEOWNERS for protected and config paths"`
- `git push -u origin lab-10-branch-protection`
- `/tmp/swexp-l10/origin.git/hooks/pre-receive` rejecting `refs/heads/main` with exit status `1` while allowing `refs/heads/feature/x`

## 3. Evidence
- Offline `pre-receive` hook blocked direct push to `main`:
  - `remote: POLICY: direct pushes to main are blocked. Open a PR.`
  - `! [remote rejected] main -> main (pre-receive hook declined)`
- Feature branch push succeeded:
  - `* [new branch]      feature/x -> feature/x`
- Notebook branch & commit state:
  - Branch `lab-10-branch-protection` created from `main` (`03991aa`) and pushed with `.github/CODEOWNERS` (`39966af`).
- Rule-to-failure mapping:
  - Pull request required (`>= 1` approval): prevents unreviewed direct commits and force-pushes to `main`.
  - Required status checks & up-to-date branch: prevents broken builds, failing checks, and stale branches from merging into `main`.
  - Include administrators: prevents emergency shortcuts or admin overrides from bypassing review and check gates.
  - `.github/CODEOWNERS` (`*`, `/.github/`, `/founder/`, `/billing/`, `*.yml`): auto-requests `@Delray-Nelson` on changes to critical workflows, policy/founder files, billing paths, and YAML configs.

## 4. Decisions & trade-offs
- Platform enforcement + `CODEOWNERS` over manual reminders: relies on GitHub rules/hooks rather than human memory, while routing sensitive path edits to an explicit owner.
- Offline `pre-receive` hook in `/tmp/swexp-l10` alongside GitHub rules: gave a fast local demonstration of server-side push blocking before testing PR gating checks in GitHub.
- Deferred / follow-up: capturing a full PR check-failure-to-pass unblock screenshot once automated CI checks are wired in Lesson 11.

## 5. AI usage (draft -> verify -> log)
- Asked: Asked for a Lab 10 walkthrough, branch protection policy recommendations, and a Lesson 10 submission file for `GOV-3001`.
- Verified against: Terminal output from `git switch`, `git commit`, `git push`, `pre-receive` hook execution in `/tmp/swexp-l10`, and `git log`.
- Corrections: Caught a nested code-fence issue during pasting that caused shell lines to run as commands, re-created `/tmp/swexp-l10/work` cleanly, and ensured `.github/CODEOWNERS` uses `* @Delray-Nelson` as the wildcard fallback line.
- Final, trusted result: Verified `.github/CODEOWNERS` on `lab-10-branch-protection`, confirmed `pre-receive` hook rejection on `main`, and committed the submission to `Work Space Submissions/lesson-10-protect-production-branch.md`.

## 6. Definition of Done
- [x] Branch protection configured on `main` (PR required, `>= 1` approval, status checks/up-to-date gating, admins included) -> Configured on GitHub branch protection for `main`.
- [x] `.github/CODEOWNERS` added for sensitive paths -> Added in `.github/CODEOWNERS` on `lab-10-branch-protection`.
- [x] Each rule documented with the failure it prevents -> Documented in Section 3 above.
- [x] Evidence of blocked direct push captured -> Verified via `pre-receive` hook rejection output in `/tmp/swexp-l10` and `main` protection rules.
- [ ] Blocked merge later unblocked in PR UI -> Record PR merge state after required review/check conditions are satisfied.

## 7. Reflection
Relying on teammates or myself to "just be careful with `main`" breaks down as soon as speed, context switching, or team size increases. Platform-enforced branch protection and `CODEOWNERS` turn good habits into mechanical constraints, while still requiring real checks and thoughtful reviews so the gate protects quality without creating unnecessary deadlocks.
