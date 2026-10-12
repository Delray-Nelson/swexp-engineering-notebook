# OPS-3600 Postmortem

## Issue
Disk usage on /mnt/c hit 95% capacity, causing system instability.

## Findings
- Primary source: 1GB test file in root.
- Secondary source: Bloated .cursor and .claude plugin caches.

## Recovery
- Removed 1GB test file.
- Purged plugin cache directories.

## Metrics (Before/After)
- Before: 95% usage
- After: <85% usage

## Prevention
- Added disk pressure monitor alias to .bashrc.