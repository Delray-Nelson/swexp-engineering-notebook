# SEC-2031 — Permission Denied Deliverable

## Summary
Ticket SEC-2031 required resolving deployment write failures on `/opt/app/releases` and read failures on `/etc/app/secrets.env`. A previous engineer attempted a unsafe `chmod 777` override. I audited the system permissions using `ls -l` and `find`, restored least-privilege permissions (`750` for directories, `640` for secrets), and validated that runtime services execute without world-writable risks.

## Evidence
- `ls -l secrets.env`: Identified over-permissive `666` (`-rw-rw-rw-`) mode exposing sensitive keys.
- `find ~/swexp-lab/l03 -perm -002 -type f`: Located all dangerous world-writable files in the environment.
- `chmod 640 secrets.env`: Secured secrets to owner read/write and group read.
- `chmod 750 releases`: Configured release folder for owner access and group execution/traversal.
- `stat -c "%a %U:%G %n" secrets.env`: Confirmed octal `640` enforcement.

## Predict → run → explain
- **Prediction before key command:** Changing permissions from `666` to `640` will remove world-writable access while keeping the file readable for the runtime group.
- **What actually happened:** `ls -l` shifted output from `-rw-rw-rw-` to `-rw-r-----`. Re-running the `find` world-writable check returned zero paths.
- **Plain-language explanation:** Octal `640` restricts file mutations strictly to the owner while permitting process groups to read runtime values into memory.
- **How I verified it:** Re-executed `find -perm -002` and confirmed no world-writable files remained.

## Decisions & tradeoffs
- **Chose:** Applied octal `640` for secrets and `750` for directories with explicit `chown` group assignments.
- **Reason:** Guarantees least privilege and satisfies security auditing rules.
- **Rejected:** Reaching for `chmod 777`, which introduces critical security vulnerabilities and grants unnecessary world execution bits.

## AI workflow
Asked: How to fix terminal heredoc blocks and structure permission deliverables. | Right: Identified terminal waiting on `EOF` keyword and generated standard workspace schema. | Wrong/corrected: Attempted to paste raw markdown text into active shell causing syntax parsing errors. | Verified with: Terminal execution of `stat` and `git push`.

## Definition of Done
- [x] Identified world-writable file risks with `find -perm -002`.
- [x] Restored least privilege on secret files (`640`) and directories (`750`).
- [x] Verified deployment access without using `chmod 777`.

## Reflection
`chmod 777` is an unsafe quick fix that exposes system files to lateral movement during security breaches. Least-privilege models (`640`/`750`) protect production assets while maintaining operational function.
