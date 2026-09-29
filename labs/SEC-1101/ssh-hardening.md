# SSH Hardening & Cryptographic Identity Rollout

**Ticket Reference:** SEC-1101  
**Deliverable:** Lab 11 — SSH Hardening  
**Target:** Ubuntu / WSL2 Environment  

---

## 1. Cryptographic Keypair Generation
- **Algorithm:** Ed25519 (256-bit elliptic-curve)
- **Identity Label:** `swexp`
- **Private Key Path:** ~~/.ssh/swexp_ed25519` (Mode `600`)
- **Public Key Path:** `~~/.ssh/swexp_ed25519.pub`

## 2. Ingress & Authorization Baseline
- Appended public key to `~~/.ssh/authorized_keys` with strict `chmod 600` permissions.
- Verified parent directory `~~/.ssh` is isolated to `chmod 700`.
- Verified loopback connectivity via `ssh -i ~/.ssh/swexp_ed25519 localhost 'echo key-login-ok'`.

## 3. Client Automation (`~~/.ssh/config`)
Configured Host entry for persistent, flagless ingress:
```text
Host lab-local
    HostName 127.0.0.1
    User hurdle_tm
    IdentityFile ~~/.ssh/swexp_ed25519
```

## 4. Daemon Hardening Policy
Deployed configuration overrides to `/etc/ssh/sshd_config.d/99-hardened.conf`:
- `PermitRootLogin no` (Neutralizes direct superuser network ingress)
- `PasswordAuthentication no` (Eliminates interactive password and dictionary attacks)
- `PubkeyAuthentication yes` (Enforces asymmetric cryptographic challenge verification)

## 5. Verification & Rollout Audit
1. **Pre-flight Syntax Audit:** Ran `sudo sshd -tFwith return code `0`.
2. **Dynamic Reload:** Applied policies via `sudo systemctl reload ssh` without dropping active sessions.
3. **Negative Fallback Check:** Executed `ssh -o PubkeyAuthentication=no lab-local`, receiving expected `Permission denied (pubkey)`.
4. **Positive Key Check:** Executed `ssh lab-local`, successfully establishing session with zero interactive password prompts.