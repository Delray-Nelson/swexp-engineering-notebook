# Submission Workspace

**Source:** Lesson 07 Submission — Synchronize with the Engineering Team  
**Engineer:** Hurdle TM · **Date:** 2026-11-16 · **Competency:** Upstream Synchronization, Merge vs. Rebase & Conflict Resolution  

---

### 1. Ticket & objective
Reproduce a rejected non-fast-forward push caused by a teammate pushing upstream changes first, inspect the diverged commit graph, and analyze how `git pull --rebase` and `git pull --no-rebase` handle integration and merge conflicts.

### 2. What I did
* Simulated a multi-developer workflow in `/tmp/swexp-l07` with a bare remote repository (`origin.git`) and two local clones (`you` and `teammate`).
* Pushed an upstream commit from `teammate` while committing a conflicting edit locally in `you` without fetching first.
* Observed the expected `! [rejected] main -> main (fetch first)` error when attempting `git push origin main`.
* Ran `git fetch origin` and inspected the diverged DAG using `git log --oneline --graph --all`.
* Attempted `git pull --rebase origin main` and `git pull --no-rebase origin main`, observing how Git halts integration with `CONFLICT (content): Merge conflict in app.txt` and prevents pushing (`non-fast-forward`) until conflicts are manually resolved and staged.

### 3. Evidence
Key terminal outputs demonstrating push rejection, history divergence, and conflict blocking:

```bash
# 1. Rejected push due to upstream movement
hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l07/you$ git push origin main
To /tmp/swexp-l07/origin.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '/tmp/swexp-l07/origin.git'

# 2. Diverged history graph after git fetch origin
hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l07/you$ git log --oneline --graph --all
- bacaae4 (HEAD -> main) Your edit
| * 2313b62 (origin/main, origin/HEAD) Teammate edit
|/
- a2dffa6 Initial

# 3. Conflict triggered during rebase integration
hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l07/you$ git pull --rebase origin main
Auto-merging app.txt
CONFLICT (content): Merge conflict in app.txt
error: could not apply bacaae4... Your edit
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".

# 4. Attempting merge while rebase conflict is still unresolved
hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l07/you$ git pull --no-rebase origin main
error: Pulling is not possible because you have unmerged files.
fatal: Exiting because of an unresolved conflict.
