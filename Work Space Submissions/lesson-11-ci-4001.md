# Submission Workspace

**Source:** Lesson 11 Submission — CI-4001  
**Engineer:** Hurdle TM · **Date:** 2026-11-27 · **Competency:** Investigate a Failed CI Pipeline & Legitimate Remediation  

## 1. Ticket & objective
* **Ticket:** `CI-4001` (Priority: P1 · Type: CI/CD · Blocks Merge)
* **Objective:** Diagnose why the required CI check on the pull request is failing (blocking merge per the branch protection rules configured in `GOV-3001`), find the real root causes rather than disabling or bypassing the check, commit clean fixes, and verify the pipeline turns green legitimately.

## 2. What I did
1. Created `/tmp/swexp-l11` and ran `gen.sh` to initialize the sample repository with `.github/workflows/ci.yml`, `calc.py`, `test_calc.py`, and `local_ci.sh`.
2. Installed `python3-pip` and `python3-pytest` via `apt`, installed `ruff` (`0.17.6`) via `pip`, and added `$HOME/.local/bin` to `PATH` (persisted in `~/.bashrc`) so local checks mirrored the CI workflow.
3. Ran `pytest -q` and isolated the first test failure in `test_calc.py::test_add` (`AssertionError: assert 6 == 5` from `add(2, 3)` returning `6` due to the off-by-one bug `return a + b + 1`).
4. Fixed `calc.py` by removing unused `import os` and changing `return a + b + 1` to `return a + b`, committed that change (`34f13de`), ran `./local_ci.sh` where `ruff check .` caught `I001 [*] Import block is un-sorted or un-formatted` in `test_calc.py:1:1`, formatted `test_calc.py`, committed the fix, and verified `./local_ci.sh` passes (`ALL GREEN`).

~~~~bash
mkdir -p /tmp/swexp-l11 && cd /tmp/swexp-l11
bash gen.sh && cd repo
sudo apt update && sudo apt install -y python3-pip python3-pytest
pip install --break-system-packages ruff
export PATH="$HOME/.local/bin:$PATH"
./local_ci.sh
~~~~

## 3. Evidence

### Workflow file (`.github/workflows/ci.yml`)
~~~~yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install pytest ruff
      - run: ruff check .
      - run: pytest -q
~~~~

### Original failing logs (first error highlighted in each)

**Test failure (`pytest -q`):**
~~~~text
F                                                                        [100%]
=================================== FAILURES ===================================
___________________________________ test_add ___________________________________

    def test_add():
>       assert add(2, 3) == 5
E       assert 6 == 5        <-- FIRST ERROR: off-by-one bug in calc.add(2, 3)
E        +  where 6 = add(2, 3)

test_calc.py:3: AssertionError
=========================== short test summary info ============================
FAILED test_calc.py::test_add - assert 6 == 5
1 failed in 0.28s
~~~~

**Lint failure (`./local_ci.sh` -> `ruff check .`):**
~~~~text
== ruff ==
I001 [*] Import block is un-sorted or un-formatted   <-- FIRST ERROR: unformatted import block
 --> test_calc.py:1:1
  |
1 | from calc import add
  | ^^^^^^^^^^^^^^^^^^^^
2 | def test_add():
3 |     assert add(2, 3) == 5
  |
help: Organize imports
~~~~

### Fixes as commits & diffs
~~~~text
commit 34f13deaf4b1760003a58abfbb61487dd58253cf
Author: King of Games <nelsondelray26@gmail.com>
Date:   Fri Nov 27 16:10:15 2026 -0500

    fix(calc): remove unused import and fix off-by-one in add

diff --git a/calc.py b/calc.py
index df83424..4693ad3 100644
--- a/calc.py
+++ b/calc.py
@@ -1,3 +1,2 @@
-import os
 def add(a, b):
-    return a + b + 1
+    return a + b

commit ad291c3337f83537c57d5d6752016b243e0eba48
    Add calc + CI (currently red)
~~~~

### Passing run (`./local_ci.sh`)
~~~~text
== ruff ==
All checks passed!
== pytest ==
1 passed in 0.02s
ALL GREEN
~~~~

### What this CI protects `main` against
This CI pipeline guards `main` by running automated lint (`ruff check .`) and test (`pytest -q`) checks on every push and pull request before code is merged. It catches functional bugs (such as `add(2, 3)` returning `6` instead of `5`), lint and import formatting issues (such as unused imports and `I001` violations), and hidden environment differences between local shells and a clean runner. Paired with `GOV-3001` branch protection, keeping required checks enabled and fixing root causes keeps `main` healthy—whereas disabling or bypassing a check hides real defects and lets broken code reach `main`.

## 4. Decisions & trade-offs
* **Approach chosen:** Installed `pytest` and `ruff` in WSL to mirror `.github/workflows/ci.yml`, inspected the first error in each failure, and fixed the underlying code and import formatting in `calc.py` and `test_calc.py`.
* **Alternatives considered:** Disabling `ruff check .` or removing `test_add` to force a green check was rejected because it violates `CI-4001` and weakens branch protection.
* **Trade-offs:** Configuring `$HOME/.local/bin` on `PATH` and fixing both `ruff` issues took extra steps up front, but established a repeatable local verification check before pushing.

## 5. AI usage (draft -> verify -> log)
* **Asked:** How to diagnose the failing `CI-4001` pipeline, install missing `pytest` and `ruff` tools in WSL, fix both lint and test errors, and create the submission file.
* **Verified against:** Local terminal outputs from `pytest -q`, `ruff check .`, `git diff`, `git log -n 2 --stat`, and `./local_ci.sh`.
* **Corrections:** `pip` initially was not installed and `~/.local/bin` was not on `PATH`; installed the packages, updated `PATH`, and caught a follow-up `I001` import-formatting error in `test_calc.py` after fixing `calc.py`.
* **Final, trusted result:** Verified green `./local_ci.sh` run (`ALL GREEN`) with atomic fix commits and full failure-to-pass evidence.

## 6. Definition of Done
* [x] **Workflow file submitted:** `.github/workflows/ci.yml` included in Section 3.
* [x] **Original failing log with first error highlighted:** `pytest` `assert 6 == 5` and `ruff` `I001` first errors highlighted in Section 3.
* [x] **Fixes as commits:** `calc.py` fix (`34f13de`) and `test_calc.py` `I001` formatting fix committed without bypassing checks (Section 3).
* [x] **Passing run:** `./local_ci.sh` green run (`ALL GREEN`) recorded in Section 3.
* [x] **Paragraph on what CI protects `main` against:** Included in Section 3.

## 7. Reflection
Reading the first error in a clean runner environment makes CI debugging much faster and prevents guessing or turning off checks to force a pass. Working through missing `PATH` entries, a failing assertion in `test_add`, and a `ruff` `I001` import issue showed how automated checks catch defects before they land on `main`.
