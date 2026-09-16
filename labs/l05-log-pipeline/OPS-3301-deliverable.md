# OPS-3301 — Investigate a Production Outage Using Log Files Deliverable

## Summary
OPS-3301 required isolating the root cause, duration, affected endpoint, and total impact of a Checkout API production outage using raw terminal log pipelines. By analyzing `access.log` and `app.log`, I determined the outage ran from 14:00:00 to 14:25:59 UTC, impacted the `/api/checkout` endpoint across ~380 requests, and was caused by connection pool exhaustion (`PaymentGateway timeout: connection pool exhausted (max=10)`).

## Evidence
- `awk '{print $9}' access.log | sort | uniq -c | sort -rn`: Identified HTTP 500 error count (~380 occurrences).
- `grep ' 500 ' access.log | head -1`: Established outage start time (`14:00:00`).
- `grep ' 500 ' access.log | tail -1`: Established outage end time (`14:25:59`).
- `grep ' 500 ' access.log | awk '{print $7}' | sort | uniq -c`: Isolated `/api/checkout` as the sole failing endpoint.
- `grep -i error app.log`: Extracted root cause (`ERROR PaymentGateway timeout: connection pool exhausted`).

## Predict → run → explain
- **Prediction before key command(s):** Filtering `access.log` by status code 500 and URL path will highlight the exact failing endpoint.
- **What actually happened:** Running the pipeline confirmed `/api/checkout` was responsible for 100% of the 500 errors during the 25-minute window.
- **Plain-Language Explanation:** Web logs track access receipts while app logs track execution exceptions. Correlating both pinpointed the exact connection pool bottleneck.
- **How I verified it:** Cross-referenced app log timeline timestamps with access log error spikes.

## Decisions & tradeoffs
I relied on modular CLI pipelines (`grep`, `awk`, `sort`, `uniq`) rather than transferring logs to a local environment. This tradeoff prioritized rapid incident response on remote boxes lacking UI log aggregators.

## AI workflow
- **Asked:** How to construct log pipeline commands and interpret AWK generator syntax.
- **Right:** Shell pipeline sequences for extracting status codes and timestamps.
- **Wrong/corrected:** Identified that multi-line AWK generator scripts hang in Bash if pasted line-by-line rather than executed as a single block.
- **Verified with:** Terminal pipeline execution outputs on generated lab log files.

## Definition of Done
- [x] Identified outage start and end timestamps.
- [x] Isolated failing API endpoint and total affected request count.
- [x] Correlated root cause error in application log.
- [x] Documented incident timeline in deliverable.

## Reflection
Sorting before `uniq -c` is mandatory because `uniq` only checks adjacent lines. Terminal pipelines provide instant diagnostic capability during production outages without external log tool dependencies.
