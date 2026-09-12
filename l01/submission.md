# INFRA-1042 — System Survey Deliverable

## Summary
Investigated an unfamiliar Linux host environment to inventory core system metrics (OS, CPU, RAM, disk allocation) and identify storage risks without modifying system state. Produced a survey document (`survey.md`) and flagged host drive capacity as the top operational risk.

## Evidence
- Commands run: `uname -r`, `cat /etc/os-release`, `free -h`, `df -h`, `du -sh /var/* 2>/dev/null`
- Key output:

## Predict → run → explain
- Prediction before key command: Expected `/var/log` to contain the highest disk usage within `/var`.
- What actually happened: `/var/log` held 185M, confirming it was the largest single folder in `/var`.
- Plain-language explanation: Log files accumulate continuously during system operation, making them the primary consumer of space in `/var`.
- How I verified it: Ran `du -sh /var/* 2>/dev/null | sort -rh | head -n 3`.

## Decisions & tradeoffs
Chose read-only inspection commands (`df`, `du`, `stat`) over active modifying scripts to guarantee zero accidental impact on the server during survey.

## AI workflow
Asked AI to summarize `df -h` and `du -sh /var/*` outputs. AI correctly identified top `/var` directories, but manual verification of `df -h` proved the host Windows mount (`/mnt/c` at 97%) was the actual main storage bottleneck, not `/var`.

## Definition of Done
- [x] `survey.md` committed with OS, kernel, CPU/RAM, and disk data.
- [x] Three flagged findings documented.
- [x] No files on the system were modified during investigation.

## Reflection
Inspecting virtual filesystems and observing disk thresholds provides deterministic facts before attempting system changes.text
/dev/sdd       1007G  2.5G  954G   1% /
C:\            107G   102G  4.3G  97% /mnt/c
185M  /var/log
176M  /var/cache 
