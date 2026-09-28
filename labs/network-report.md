# Network Diagnostic & Surface Audit Report

**Ticket Reference:** NET-4001
**Deliverable:** Lab 10 — Networking Audit
**Environment:** WSL2 / Ubuntu Host

---

## 1. Network Interfaces & Routing Table

### Active Interfaces (`ip -br addr show`)
| Interface | State | IPv4 Address / CIDR | Role |
| :--- | :--- | :--- | :--- |
| `lo` | UNKNOWN | `127.0.0.1/8` | Loopback adapter (inter-process isolation) |
| `eth0` | UP | `172.17.30.79/20` | Primary routable interface (egress/ingress) |

### Default Gateway (`ip route show default`)
```text
default via 172.17.16.1 dev eth0 proto kernel
