# Submission Workspace

**Source:** Lesson 01 Submission — <FILL IN: Ticket ID>
**Engineer:** Delray Nelson · **Date:** 2026-11-05 · **Competency:** <FILL IN: from the lesson header>

## 1. Ticket & objective

The ticket asked me to get oriented in an unfamiliar, multi-author repository using only read-only Git history tools (`log`, `show`, `blame`, `diff`, `shortlog`), then find the commit that introduced a planted bug in `average()`. The deliverable is an orientation report in my notebook covering:

- repo structure
- top contributors
- the three most significant commits
- the bug's location, its introducing commit, and the commit message

All with the exact commands I used.

## 2. What I did

I generated the lab repo with `gen.sh` (Lab 01 — Investigate an Existing Repository). It produces 5 commits from 3 authors with one planted bug. Then I worked through it in passes:

1. **Orient:** surveyed history and contributors.
2. **Recent change:** inspected the latest commit.
3. **Find the bug:** blamed the broken line, then read the file's patch history.
4. **Confirm:** diffed the suspect commit against its parent and ran the pickaxe search.
5. **Explain:** wrote the findings to `capstone/orientation-report.md`.

```text
$ mkdir -p /tmp/swexp-l01 && cd /tmp/swexp-l01
$ bash gen.sh && cd repo
$ git log --oneline --graph --decorate
$ git shortlog -sn e97a189
$ git show HEAD
$ git blame calc.py
$ git log -p -- calc.py
$ git diff 96b8247~1 96b8247 -- calc.py
$ git log -S"len(values)" --oneline -- calc.py
$ python3 -c "from calc import average; print(average([1, 2, 3]))"
```

## 3. Evidence

**History survey:** 5 commits, linear, no merges.

```text
* e97a189 Add minimum()
* 368dcaf Add README
* 96b8247 Refactor average() for performance
* b8555e4 Add maximum()
* fbc0ae3 Add calc with add() and average()
```

**Contributors** (`git shortlog -sn e97a189`):

```text
     2  Ada
     2  Bjarne
     1  Grace
```

**Latest change** (`git show HEAD`): `e97a189` by Bjarne, "Add minimum()". It only added `minimum()` and left `average()` alone.

**Blame** points at the broken line:

```text
96b8247c (Grace 2026-11-05 06:28:43 -0500 5)     return sum(values) / 2
```

**Before/after** (`git diff 96b8247~1 96b8247 -- calc.py`):

```diff
 def average(values):
-    return sum(values) / len(values)
+    return sum(values) / 2
```

**Pickaxe** (`git log -S"len(values)" --oneline -- calc.py`):

```text
96b8247 Refactor average() for performance
fbc0ae3 Add calc with add() and average()
```

`fbc0ae3` added `len(values)`, and `96b8247` removed it.

**Behavior:** `average([1, 2, 3])` returns `3.0`; the correct answer is `2.0`.

**Bug finding:** `calc.py`, `average()`. Introduced in `96b8247` by Grace, "Refactor average() for performance."

## 4. Decisions & trade-offs

- **Blame first, then the patch log.** `git blame` answers "who last touched this line" instantly. `git log -p -- calc.py` confirmed that no later commit touched `average()`, which blame alone can't prove.
- **Pickaxe as independent confirmation.** Searching for the removal of `len(values)` reached the same commit by a different route, so the answer doesn't rest on one tool.
- **Used `shortlog -sn e97a189` instead of `HEAD`.** I had accidentally committed to the lab repo, so pinning the lab's last commit kept my own commit out of the contributor count.
- **Didn't regenerate the repo.** Rerunning `gen.sh` would create new timestamps and change every SHA, which would break the evidence I'd already collected.
- **Deferred:** fixing the bug. The ticket was investigation only, using read-only tools.

**Incident during submission.** I added my notebook's GitHub remote to the lab repo and force-pushed. That replaced the notebook's history on GitHub with the lab repo's.

To recover, I confirmed that my local notebook clone still had the real history at `7eed6be` and created a backup branch. I then force-pushed it back with `--force-with-lease`, pinned to the lab commit's full SHA. Finally, I verified the result with `git ls-remote origin main` and removed the remote from the lab repo.

Lesson learned: check `git
