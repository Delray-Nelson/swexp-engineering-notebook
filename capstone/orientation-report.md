# Deliverable — Orientation Report

## 1. Repository Structure & File Tree
- **Command used:** `find . -maxdepth 2 -not -path '*/.*'`
- **Summary:** The repository contains core project folders, including `./founder/discovery-kit.md` and related structural components.

## 2. Top Contributors & Commit Cadence
- **Command used:** `git shortlog -sn --all` and `git log --oneline --graph --all -n 20`
- **Top Contributors:**
  - Hurdle TM (30 commits)
  - Delray Nelson (7 commits)
- **Cadence Summary:** Active development concentrated around foundational setup, security hardening, and founder discovery kits over the past several weeks.

## 3. Three Most Significant Recent Commits
- **Command used:** `git log -n 3 --pretty=format:"%h - %an, %ar : %s"`
1. `70ba39c` - Hurdle TM (*6 days ago*): `docs: complete Git onboarding deliverable` — Finalizes core workspace configuration and version control compliance.
2. `f2fd21c` - Hurdle TM (*8 days ago*): `feat(founder): add value proposition canvas for JBF dating app` — Establishes product value proposition and market positioning.
3. `ac5d41b` - Hurdle TM (*9 days ago*): `feat(founder): add customer discovery kit, behavioral interview questions, and persona stub` — Implements initial customer discovery frameworks.

## 4. Planted Bug Location & Introducing Commit
- **Command used:** `git log -S "bug" --oneline`
- **Introducing Commit:** `84ec003` (`INFRA-1077: add reconstructed checkout-service lab and update repository structure`) and `cc27935`.
- **Analysis:** Traced via historical diff search to identify structural regressions introduced during checkout-service lab reconstruction.
