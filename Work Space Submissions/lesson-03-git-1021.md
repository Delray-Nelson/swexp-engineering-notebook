# Submission Workspace: Lesson 3 — GIT-1021

- **Source:** Lesson 3 Submission — GIT-1021
- **Engineer:** Hurdle TM · **Date:** 2026-11-14 · **Competency:** Save Your First Feature & Clean Commit History

## 1. Ticket & objective
The ticket **GIT-1021** (Priority: P2) required taking a newly written customer-export utility (`export.py`), its configuration file (`config.yaml`), and development notes, and landing them into the repository as clean, well-described, atomic commits rather than one giant, unstructured "stuff" commit. The staging area had to be utilized deliberately to separate unrelated code edits.

## 2. What I did
- Initialized a controlled test environment and generated baseline files (`export.py`, `config.yaml`, `secrets.env`, and build artifacts) using the lab automation script.
- Created and configured a `.gitignore` file to ensure sensitive configuration files (`secrets.env`) and build directories (`build/`) are strictly excluded from version control tracking.
- Utilized interactive patch staging (`git add -p`) to inspect modifications hunk-by-hunk, isolating distinct functional changes (such as separating core CSV export logic from future expansion templates) into separate logical units before committing.

## 3. Evidence
```bash
hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l02/repo$ printf "secrets.env\nbuild/\n__pycache__/\n" > .gitignore
hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l02/repo$ git status   
On branch master
Untracked files:
        .gitignore
        config.yaml
        export.py

hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l02/repo$ git add -p export.py
hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l02/repo$ git commit -m "Implement CSV export"

## 4. Decisions & trade-offs
- **Approach Chosen:** Selected interactive hunk staging (`git add -p`) and explicit `.gitignore` rules to maintain atomic commit boundaries and prevent accidental security leaks (such as committing `.env` credentials).
- **Trade-offs:** Taking extra care to split edits and craft clean commit messages adds upfront friction compared to a quick `git add . && git commit -m "update"`, but it eliminates review bottlenecks and makes debugging production issues significantly easier downstream.

## 5. AI usage (draft → verify → log)
- **Asked:** How to execute granular hunk-by-hunk staging and maintain proper `.gitignore` safety for configuration and secret files.
- **Verified against:** Local lab terminal outputs and Git interactive patch manual behaviors (`git add -p`).
- **Corrections:** Ensured precise distinction between workspace modifications and staging index states.
- **Final, trusted result:** A reproducible Git workflow satisfying professional atomic commit standards.

## 6. Definition of Done
- [x] Changes are committed as logically separable commits
- [x] The staging area is used deliberately (including partial staging)
- [x] Commit messages follow the team's convention
- [x] A `.gitignore` excludes generated/secret files

## 7. Reflection
Mastering selective staging shifts version control from a simple file-saving chore into an active communication tool for engineering teams. Writing clear, imperative commit messages and isolating changes ensures that teammates and code reviewers can understand intent instantly without needing to decipher a tangled web of unrelated modifications.
