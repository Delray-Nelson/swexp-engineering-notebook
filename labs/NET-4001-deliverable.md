# NET-4001 — Secure Remote Infrastructure Deliverable

## Summary
Ticket NET-4001 tasked us with diagnosing why a freshly provisioned app server could reach the external internet but failed to connect to its backend database. Additionally, security requested a comprehensive network exposure audit. I audited all listening sockets and active connections, diagnosed the transport/routing failure preventing database reachability, produced a security remediation plan, and verified the hardened boundary.

## Evidence
- Commands run:
  - `sudo ss -tulpn` — Audited all listening TCP/UDP endpoints, process names, and bound addresses.
  - `sudo ss -ton state established` — Inspected all active outbound connections.
  - `sudo ufw status verbose` — Evaluated the current host packet filtering policy.
  - `ping -c 3 <DB_PRIVATE_IP>` — Verified network-layer connectivity.
  - `nc -zv -w 3 <DB_PRIVATE_IP> 5432` — Tested transport-layer socket reachability on the PostgreSQL port.
- Key output:
  - App server showed port 22 (`sshd`) listening on `0.0.0.0:22` and application process listening on `0.0.0.0:3000`.
  - Database ping succeeded (`0% packet loss`), but `nc -zv` returned `nc: connect to <DB_PRIVATE_IP> port 5432 timed out`.
- Before/after state:
  - Before: App server was exposed on unneeded debug ports; database traffic was silently dropped by perimeter rules.
  - After: Local default-deny firewall (`ufw`) enabled with explicit ingress allowances; database ingress rules updated to permit traffic from the app server private IP.

## Predict → run → explain
- Prediction before key command(s): Running `nc -zv` against the database port would hang and timeout rather than refuse immediately, proving an intermediate firewall drop rather than a closed port.
- What actually happened: The connection attempt timed out after 3 seconds with zero response packets.
- Plain-language explanation: An IP gets packets to the correct machine, but the port directs packets to the correct application. A timeout means a security group or firewall silently discarded the request before the database daemon ever saw it.
- How I verified it: Added the app server's internal IP to the database security group allowlist and re-ran `nc -zv`, confirming an immediate `Connection to <DB_PRIVATE_IP> 5432 port [tcp/postgresql] succeeded!`.

## Decisions & tradeoffs
- Chose host-level `ufw` enforcement over relying solely on cloud provider security groups to provide defense-in-depth against lateral network movement.
- Rejected binding internal services to `0.0.0.0` for convenience; strictly bound non-public services to loopback (`127.0.0.1`) to eliminate remote attack surfaces.

## AI workflow
- Asked: How to differentiate between a closed port and a firewall drop using netcat and socket state inspection tools.
- Right: Correctly identified that `Connection refused` indicates an unbound/closed port, while a hang/timeout indicates a packet filter or firewall drop.
- Wrong/corrected: Suggested checking raw iptables chains manually first; corrected workflow to use modern `ss` and `ufw status` for cleaner triage.
- Verified with: Official Ubuntu Server firewall documentation and live testing in the coding terminal.

## Definition of Done
- [x] Full listening socket audit produced with all listening ports and interfaces cataloged.
- [x] Root cause of database reachability failure isolated and documented.
- [x] Host-level firewall posture hardened to default-deny incoming.
- [x] Triage steps and findings validated through live command execution.

## Reflection
1. Difference between an IP address and a port: An IP address identifies the specific host on a network, while a port identifies the specific process or service running on that host that should handle the connection.
2. Why a service can be running but unreachable: The service may be bound strictly to the loopback interface (`127.0.0.1`), a local or upstream firewall is dropping incoming packets, or the process is hung in an uninterruptible sleep state (`D`) unable to accept incoming socket handshakes.
