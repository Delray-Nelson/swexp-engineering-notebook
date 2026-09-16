# OPS-3344 — Build a Production Log Processing Pipeline Deliverable

## Summary
OPS-3344 required creating a reusable log processing script (`logreport.sh`) capable of reading from a file argument or standard input (`stdin`). The script outputs total request counts, status code breakdowns, top 10 endpoints, top 10 client IPs, and uses `tee` to isolate 5xx errors into `errors.log`.

## Evidence
- Stream routing verification: `ls /nope /etc > out.txt 2> err.txt` separated errors from valid output.
- Pipeline execution: `grep -E ' 5[0-9][0-9] ' access.log | tee errors.log | wc -l` captured 5xx lines while returning counts.
- `diff report-file.txt report-stdin.txt` returned zero differences, proving dual file and `stdin` compatibility.

## Predict → run → explain
- **Prediction:** Using `${1:-/dev/stdin}` allows the script to process direct files or piped streams seamlessly.
- **What actually happened:** Running `./logreport.sh access.log` and `cat access.log | ./logreport.sh` generated identical metrics outputs.
- **Plain-Language Explanation:** Setting standard input as the fallback input stream allows shell tools to participate cleanly in Unix command chains.
- **How I verified it:** Verified output equality using `diff`.

## Decisions & tradeoffs
I selected `${1:-/dev/stdin}` to avoid conditional `if/else` file checks, prioritizing simplicity and adherence to the Unix pipe philosophy.

## AI workflow
- **Asked:** How stream routing, `tee`, and `stdin` variable assignment operate in Bash.
- **Right:** Shell syntax patterns for stream redirection and pipeline creation.
- **Wrong/corrected:** N/A.
- **Verified with:** Executing script diff checks in terminal.

## Definition of Done
- [x] Stream routing verified (`stdout` vs `stderr`).
- [x] Implemented `tee` to extract 5xx lines to `errors.log`.
- [x] Built `logreport.sh` supporting direct file arguments and `stdin` pipes.
- [x] Saved sample output to `report-sample.md`.

## Reflection
`2>&1` order matters because redirections execute left-to-right. Pipe-capable scripts ensure log tools scale without requiring direct file modifications.
