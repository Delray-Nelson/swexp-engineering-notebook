# INFRA-1077 — Recover the Lost Project Deliverable

## Summary
The ticket required reconstructing a scattered, unorganized fake project dump into a standardized checkout-service project directory (`src/`, `config/`, `docs/`) without data loss or unverified assumptions. I inspected the files, built the clean directory structure, verified identical files using SHA-256/MD5 checksums, created a `MANIFEST.md` documenting all file origins, built a compressed `.tar.gz` restore point excluding hidden Git metadata, and tracked the work in version control.

## Evidence
- `mkdir -p checkout-service/{src,config,docs}`: Created target layout before moving files.
- `find ~/swexp-lab/l02/dump -type f | sort`: Located all project fragments including stray files.
- `md5sum ~/swexp-lab/l02/dump/main.py ~/swexp-lab/l02/dump/main_COPY.py`: Proved byte-level duplicate identity (`main_COPY.py` matched `main.py`).
- `cp -a`: Copied files preserving permissions and modification timestamps.
- `tar --exclude='.git' -czf checkout-service.tar.gz checkout-service`: Built a clean compressed restore point.
- `tar -tzf checkout-service.tar.gz`: Verified archive contents before deployment.

## Predict → run → explain
- **Prediction before key command(s):** Running `md5sum` on `main.py` and `main_COPY.py` will yield identical 32-character hashes if the files contain identical contents.
- **What actually happened:** Both lines printed the exact same MD5 hash string.
- **Plain-language explanation:** File names can differ, but cryptographic hashing checks raw internal byte contents. Identical hashes mathematically guarantee identical content.
- **How I verified it:** Inspected stdout from `md5sum` and confirmed hash alignment before choosing to omit `main_COPY.py` from the final `src/` directory.

## Decisions & tradeoffs
- **Chose:** Copying files with `cp -a` instead of `mv`.
- **Reason:** Leaving the original source dump untouched preserved original evidence for auditing.
- **Rejected:** Blindly copying all `*.py` files into `src/`. That would have introduced unverified duplicate code (`main_COPY.py`).

## AI workflow
Asked: How to fix a 403 Git push error and clean up `.git` from a tar archive. | Right: Identified PAT permission scope missing and `.git` folder bloat in `tar`. | Wrong/corrected: Attempted to paste raw Markdown directly into terminal prompt causing bash syntax errors. | Verified with: Terminal execution of `cat << 'EOF'` and `tar -tzf`.

## Definition of Done
- [x] Target folder tree created (`src/`, `config/`, `docs/`).
- [x] Recovery manifest (`MANIFEST.md`) created mapping origins and decisions.
- [x] Compressed restore point (`.tar.gz`) built and verified cleanly.

## Reflection
The `find` preview command combined with `cp -a` made recovery safest by allowing me to audit source paths before modification. Copying every `*.py` file without previewing would have introduced unverified duplicate files into production and broken clean environment setup.
