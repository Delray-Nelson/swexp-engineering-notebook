# Incident Postmortem: Lab 09

## Incident Summary
- **Offending Process:** burner.sh
- **Runaway PID:** 1284
- **CPU Utilization:** 8.4%
- **Termination Path:** SIGTERM (signal 15) sent to PID 1284; verified dead via kill -0.

## Diagnostics & Prevention
- **Process Identification:** Located using `ps aux --sort=-%cpu` and `pgrep -fl burner`.
- **Systemd Health:** Verified services under `systemctl status` to ensure system stability.
