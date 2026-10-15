# OPS-3600 Postmortem

## Issue
Disk usage on `/mnt/c` reached high utilization levels (95%), creating risk for system instability and execution halts.

## Findings
- **Root Cause**: Unmanaged test files and accumulated local application caches (`.cursor` and `.claude`).
- **Diagnostic Commands Used**: `df -h /mnt/c`, `free -h`

## Recovery Actions
- Removed extraneous test files.
- Cleared stale cache footprints to reclaim immediate head room.

## Before / After Metrics
- **Before**: 107G total, 101G used, 6.0G available (95% utilization)
- **After**: Validated via `df -h` that disk space usage dropped below the critical threshold.

## Prevention & Guardrails
- Added an automated alias/check to monitor storage headroom and alert if usage creeps above critical limits.
