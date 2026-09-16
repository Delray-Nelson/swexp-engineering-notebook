#!/usr/bin/env bash
set -euo pipefail

INPUT="${1:-/dev/stdin}"

echo "=== NIGHTLY LOG REPORT ==="
echo ""
echo "--- Total Requests ---"
wc -l < "$INPUT"

echo ""
echo "--- Status Breakdown ---"
awk '{print $9}' "$INPUT" | sort | uniq -c | sort -rn

echo ""
echo "--- Top Endpoints ---"
awk '{print $7}' "$INPUT" | sort | uniq -c | sort -rn | head -n 10

echo ""
echo "--- Top Client IPs ---"
awk '{print $1}' "$INPUT" | sort | uniq -c | sort -rn | head -n 10

echo ""
echo "--- 5xx Errors Saved ---"
grep -E ' 5[0-9][0-9] ' "$INPUT" | tee errors.log | wc -l
