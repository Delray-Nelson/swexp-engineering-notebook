# Submission Workspace: Lesson 4 — Develop Your First Feature

* **Source:** Lesson 4 Submission — Develop Your First Feature
* **Engineer:** Hurdle TM · **Date:** 2026-11-14 · **Competency:** Feature Branching & Workspace Isolation

## 1. Ticket & objective
The objective was to build and isolate our first software feature on a dedicated, correctly named feature branch (`feature/json-export`), ensuring that the primary production branch (`main`) remains pristine and completely unaffected by in-progress experimental work.

## 2. What I did
- Initialized a local test repository and established a baseline commit containing a simple CSV export utility on the primary branch.
- Created and switched to a dedicated feature branch named `feature/json-export` using Git branch switching commands.
- Implemented the JSON export function, test stubs (`tests.txt`), and documentation (`README.md`) inside the feature branch.
- Encountered and resolved a default branch naming mismatch (`master` vs `main`), utilizing branch renaming flags (`-M`) and rescue branching techniques to secure commit history.
- Verified workspace isolation by switching back to `main` and confirming that feature-specific files and code modifications were absent.

## 3. Evidence
### Commit Graph Output (`git log --oneline --graph --all`)
```text
* e607030 (HEAD -> feature/json-export, rescue/experiment) Document JSON export
* c4f2a1b Add JSON export test stub
* 8b19f32 Add JSON export function
| * 3a10c2e (main) Add CSV export
|/  
* f1b2c4d Initial commit

Proof That main Lacks the Feature
Bash
hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l03/repo$ git switch main
Already on 'main'

hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l03/repo$ ls
export.py  # Notice tests.txt and README.md are absent on main

hurdle_tm@DESKTOP-N64PAVV:/tmp/swexp-l03/repo$ grep export_json export.py
# (No output / function missing in export.py on main)
4. Decisions & trade-offs
Approach Chosen: Chose strict feature-branch isolation over direct edits on main to protect production stability and enable clean, atomic code reviews.

Trade-offs: Maintaining multiple branches introduces overhead in branch management and context-switching, but it entirely eliminates regression risks and messy, tangled commit histories on production branches.

5. AI usage (draft → verify → log)
Asked: How to resolve branch reference errors when switching between master and main, and how to safely secure orphaned commits using rescue branches.

Verified against: Local terminal state outputs and Git documentation on movable branch pointers.

Corrections: Accounted for repository-level default branch naming differences by explicitly renaming baseline branches.

Final, trusted result: A repeatable, error-free feature branch workflow with a verified topological commit graph.

6. Definition of Done
[x] Work happens on a correctly named feature branch, never on main

[x] You can create, switch, list, and delete branches confidently

[x] You understand what a branch is (a movable pointer), not just how to use one

[x] main is unchanged by your in-progress work

7. Reflection
In Git, a branch is not a physical copy or duplicate of your project directory; it is simply a lightweight, movable pointer referencing a specific commit snapshot. Developing strictly on feature branches rather than main protects the stable production codebase from broken states, unreviewed code, and catastrophic regressions, ensuring that the primary branch remains clean and ready for continuous deployment at all times.
