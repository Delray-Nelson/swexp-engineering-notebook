# Lab 08 — Developer Onboarding Script Deliverable

## Summary
Lab 08 required building a strict-mode, idempotent developer onboarding script (`onboard-dev.sh`). The script verifies required CLI dependencies (`git`, `curl`, `jq`), creates target project directories safely using `mkdir -p`, clones a repository only if it is absent, tracks execution failures, and passes `shellcheck` static analysis without errors.

## Evidence
- **ShellCheck Verification:** Executed `shellcheck onboard-dev.sh` with zero warnings reported.
- **Idempotency Test:** Executed `./onboard-dev.sh` twice consecutively. On the second run, the script detected the existing target directory and `.git` folder, safely skipping redundant network calls and outputting `Exit status: 0`.
- **Failure Routing Test:** Induced a missing command scenario, confirming the script logged `ERROR: Prerequisite check failed` to `stderr` and terminated immediately with exit code `1`.

## Definition of Done
- [x] Strict mode enabled (`set -euo pipefail`).
- [x] Dependency verification loop using `command -v`.
- [x] Idempotent directory and clone logic.
- [x] Zero `shellcheck` warnings.
- [x] Pushed to engineering notebook repository.
