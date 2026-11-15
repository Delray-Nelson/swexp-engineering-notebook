# Submission Workspace

**Source:** Lesson Submission — GIT-1060  
**Engineer:** Hurdle TM · **Date:** 2026-11-15 · **Competency:** Undo a broken change without losing good work  

---

### 1. Ticket & objective
**Engineering Ticket:** GIT-1060 (P1)  
**Objective:** Undo a breaking change introduced onto a shared branch safely using the correct recovery tool (`git revert` vs `git reset` modes) to prevent data loss and preserve team commit history.

### 2. What I did
* Initialized an isolated test repository (`/tmp/swexp-l05/repo`) and simulated a broken commit sequence on top of valid history (`v1` -> `good feature` -> `broken change`).
* Executed `git revert HEAD --no-edit` to safely back out the broken commit on a shared branch while preserving the linear audit trail.
* Created a temporary scratch branch and tested the three primary `git reset` modes:
  1. `git reset --soft`: Undoes the commit while keeping changes staged.
  2. `git reset --mixed`: Undoes the commit and unstages changes, keeping them in the working directory.
  3. `git reset --hard`: Completely discards changes and resets the working tree back to a clean state.

### 3. Evidence
Key output logs from the workspace:

```bash
hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l05/repo$ git revert HEAD --no-edit
[main fedb700] Revert "Add broken change"
 1 file changed, 1 deletion(-)

hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l05/repo$ git log --oneline
fedb700 (HEAD -> main) Revert "Add broken change"
011fdb2 Add broken change
85607a4 Add good feature
69eb1fc Add app v1

hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l05/repo$ git reset --soft HEAD~1 && git status
On branch scratch
Changes to be committed:
        modified:   app.txt

hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l05/repo$ git reset --hard HEAD~1 && git status
HEAD is now at 011fdb2 Add broken change
On branch scratch
nothing to commit, working tree clean
4. Decisions & trade-offs
Approach: Used git revert for shared branch history preservation, and tested --soft, --mixed, and --hard reset modes for local granular state management.

Trade-offs: Destructive resets (--hard) are fast for cleaning up messy local experiments, but dangerous on shared remotes because they destroy commit history and disrupt teammates. Non-destructive reverts add an extra commit to the log but guarantee history integrity.

5. AI usage (draft → verify → log)
Asked: How to differentiate between git revert and the various git reset flags when undoing breaking commits.

Verified against: Local lab execution in WSL terminal output and Git behavior.

Corrections: Ensured distinction between public branch safety (revert) and local workspace experimentation (reset).

Final, trusted result: Verified command execution logs matching expected state transitions.

6. Definition of Done
[x] Can discard working-tree changes, unstage, and move/erase commits (Evidence: Section 2 & 3)

[x] Can distinguish revert (safe, shared) from reset (rewrites history) (Evidence: Section 4)

[x] Choose the right tool for "shared vs local" and justify it (Evidence: Section 4)

[x] No unintended work is lost (Evidence: Section 2 & 3)

7. Reflection
Understanding the operational differences between resetting and reverting ensures that correcting a mistake does not inadvertently destroy valid teammate contributions or corrupt shared remote repositories.
