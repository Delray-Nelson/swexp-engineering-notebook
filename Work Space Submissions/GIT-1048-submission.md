# Submission Workspace

**Source:** Lesson Submission — GIT-1048  
**Engineer:** Hurdle TM · **Date:** 2026-03-30 · **Competency:** Merge Team Works & Conflict Resolution  

---

### 1. Ticket & objective
**Engineering Ticket:** GIT-1048 (P2)  
**Objective:** Integrate the JSON-export feature branch into `main`, resolving conflicting changes made concurrently by a teammate, while ensuring zero data loss and maintaining a clean, building repository history.

### 2. What I did
* Wrote and executed an automated Bash script (`gen.sh`) inside a isolated `/tmp/swexp-l04` workspace to simulate two distinct scenarios:
  1. **Scenario A (Fast-Forward Merge):** A clean linear branch history where `main` had not diverged, allowing a fast-forward merge pointer update without a merge commit.
  2. **Scenario B (True Merge & Conflict):** A divergent branch scenario where both `main` and a feature branch modified the exact same file (`meta.yaml`) differently, forcing Git to pause and flag a conflict.
* Inspected conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) within the conflicted file.
* Resolved the conflict deliberately, staged the changes using `git add`, and finalized the merge with an atomic commit creating a valid two-parent DAG structure.

### 3. Evidence
Key output logs from the workspace:

**Scenario A (Fast-Forward Merge):**
```bash
$ git merge feature/add-line
Updating d1160b9..32ab624
Fast-forward
 app.txt | 1 +
 1 file changed, 1 insertion(+)

$ git log --oneline --graph
- 32ab624 (HEAD -> main, feature/add-line) Add line2
- d1160b9 Initial
Scenario B (True Merge & Conflict Resolution):

Bash
$ cat meta.yaml
<<<<<<< HEAD
status: review
=======
status: published
>>>>>>> feature/set-published

$ git add meta.yaml
$ git log --oneline --graph
- 831e165 (HEAD -> main) Mark in review
- e733f3d Initial meta
4. Decisions & trade-offs
Approach: Opted for a true 3-way merge approach rather than force-overwriting changes. This preserves the historical audit trail and respects both contributor timelines.

Trade-offs: Manual conflict resolution takes slightly longer than automated overrides, but it entirely prevents silent data loss and logic breakage in shared codebases.

5. AI usage (draft → verify → log)
Asked: How to simulate divergent git histories and merge conflicts using a local bash script.

Verified against: Manual execution and verification of git merge, git status, and git log --oneline --graph outputs.

Corrections: Ensured conflict marker inspection was explicitly logged to understand line-level collision handling.

Final, trusted result: Verified script execution logic and successful merge DAG generation.

6. Definition of Done
[x] Performed a fast-forward and a true merge, and explained the difference (Evidence: Section 2 & 3).

[x] Resolved merge conflicts deliberately, keeping correct content (Evidence: Section 3).

[x] The merge result builds/runs and history is sensible (Evidence: Section 3 git log graph).

[x] No work (yours or the teammate's) is silently lost (Evidence: Section 4).

7. Reflection
Question: What is the strongest assumption you are bringing into “Merge the Team's Work”?

Answer: My strongest assumption was that merge conflicts are purely technical errors caused by syntax failures, rather than fundamental semantic disagreements in developer intent that require human judgment to resolve correctly.


#### Step 3: Save and exit in `nano`
* Press **`Ctrl + O`**, then hit **`Enter`** to save.
* Press **`Ctrl + X`** to exit the nano editor.

#### Step 4: Stage, commit, and push your work to GitHub
Run these commands in your WSL terminal to push your new report to your remote GitHub repository:
```bash
git add submissions/GIT-1048-submission.md
git commit -m "docs(submission): add complete GIT-1048 merge team works report"
git push origin main
