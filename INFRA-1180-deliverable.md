- Commit proof: `[master (root-commit) fef0a88] INFRA-1180: dotfiles` (2 files changed, 120 insertions).

## Predict → run → explain
- **Prediction before key command:** Executing `install.sh` will replace `~/.bashrc` with a symbolic link pointing to `~/dotfiles/bashrc`.
- **What actually happened:** File `~/.bashrc` was cleanly symlinked to `$PWD/bashrc` without errors.
- **Plain-language explanation:** `ln -sfn` creates a soft shortcut pointing to the version-controlled `bashrc` inside the repository.
- **How I verified it:** Inspected file links using `ls -la ~/.bashrc` and verified prompt/alias persistence across shell reloads.

## Decisions & tradeoffs
- **Choice:** Used a standalone bash `install.sh` script with `ln -sfn` rather than a complex installer tool like GNU Stow.
- **Tradeoff:** Keeps onboarding dependencies down to zero external packages while remaining portable across standard Linux/WSL distributions.

## AI workflow
- **Asked:** How to optimize dynamic PS1 Git branch evaluation and automate dotfile symlinking.
- **Right:** Suggested `parse_git_branch` vs naive `git status` benchmarking and idempotent `ln -sfn` flags.
- **Wrong/corrected:** Naive prompt checks added ~843ms of filesystem latency in WSL `/mnt/c/`; replaced with lightweight parsing (~72ms).
- **Verified with:** `time (...)` command executions and direct terminal testing.

## Definition of Done
- [x] Sane prompt, aliases, and functions configured.
- [x] Dotfiles version-controlled in Git repository.
- [x] Automated one-command bootstrap script (`install.sh`) created.
- [x] Execution evidence verified and committed.

## Reflection
Exporting scope guarantees child subshells inherit environment configurations. Version controlling dotfiles reduces fresh environment onboarding time from hours to seconds.
