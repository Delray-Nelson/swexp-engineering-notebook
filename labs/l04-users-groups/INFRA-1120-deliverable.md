# INFRA-1120 — Onboard a New Engineering Team Deliverable

## Summary
INFRA-1120 required provisioning user accounts for the four-person Payments squad (`alice`, `bob`, `carol`, `dave`), setting up a shared group working directory with group-only access, enforcing automatic group inheritance via the `setgid` bit, and restricting administrative escalation. I delivered a reproducible onboarding workflow, configured `/srv/payments` with mode `2770`, verified file group inheritance across all team members, and proved non-member access denial.

## Evidence
- `sudo groupadd payments`: Created the dedicated squad group.
- `for u in alice bob carol dave; do sudo useradd -m -s /bin/bash -G payments "$u"; done`: Created squad user accounts and assigned them to `payments`.
- `sudo mkdir -p /srv/payments && sudo chgrp payments /srv/payments && sudo chmod 2770 /srv/payments`: Established shared space with setgid mode `2770`.
- `sudo -u alice touch /srv/payments/test-alice.txt`: Verified file creation and inherited group ownership (`alice:payments`).
- `sudo -u eve touch /srv/payments/test-eve.txt`: Verified non-member access denial (`Permission denied`).

## Predict → run → explain
- **Prediction before key command(s):** Files created inside `/srv/payments` by squad members will automatically inherit group `payments` instead of the user's primary group due to `2770` mode.
- **What actually happened:** `sudo ls -l /srv/payments` confirmed all test files (`test-alice.txt`, `test-bob.txt`, `test-carol.txt`, `test-dave.txt`) were owned by `group: payments`.
- **Plain-Language Explanation:** Plain group ownership only applies to existing files. The `setgid` bit (`chmod g+s` or `2770`) ensures all newly created files and subdirectories automatically inherit the parent directory's group ownership.
- **How I verified it:** Inspected file mode bits via `sudo ls -l /srv/payments` and confirmed `Permission denied` output when non-member `eve` attempted write access.

## Decisions & tradeoffs
I chose to use a scripted loop with `useradd -G payments` and `chmod 2770` over manual user creation. The tradeoff involved taking extra care to use `-aG` on existing users to avoid stripping secondary group memberships, ensuring repeatable and non-destructive onboarding.

## AI workflow
- **Asked:** How to configure setgid `2770`, recover from WSL sudo password issues, audit least-privilege sudoers, and test non-member denial.
- **Right:** Commands for `chmod 2770`, user loops, and interpreting `ls -ld` mode bits.
- **Wrong/corrected:** Reminded that running `ls -l /srv/payments` without `sudo` or without being in the `payments` group causes `Permission denied` by design.
- **Verified with:** Terminal execution outputs from `ls -ld /srv/payments` (`drwxrws---`) and `sudo -u eve touch` denial logs.

## Definition of Done
- [x] Provisioned user accounts for `alice`, `bob`, `carol`, and `dave`.
- [x] Configured `/srv/payments` with group `payments` and `2770` setgid permissions.
- [x] Verified automatic file group inheritance across all squad members.
- [x] Verified non-member access denial.
- [x] Committed deliverable to repository.

## Reflection
`usermod -G` without `-a` causes production outages by stripping existing secondary groups. The `setgid` bit guarantees continuous multi-user collaboration without requiring manual group ownership fixes on new files.
