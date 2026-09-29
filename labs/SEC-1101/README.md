# SEC-1101 — Secure SSH Like a Professional Deliverable

## Summary
The ticket requested generating an Ed25519 cryptographic keypair, configuring passwordless loopback access, establishing client configuration aliases, and hardening the OpenSSH daemon against password and root ingress. I generated `swexp_ed25519`, authorized it locally under strict `chmod 600` permissions, configured `~/.ssh/config` for the `lab-local` alias, and enforced `PasswordAuthentication no` and `PermitRootLogin no` in the SSH daemon without lockout.

## Evidence
- Key generation: `ssh-keygen -t ed25519 -C "swexp" -f ~/.ssh/swexp_ed25519`
- Permission masking: `chmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys`
- Ingress verification: `ssh -i ~/.ssh/swexp_ed25519 localhost 'echo key-login-ok'` returned `key-login-ok`.
- Pre-flight syntax validation: `sudo sshd -t` returned exit code `0`.
- Daemon reload: `sudo systemctl reload ssh` applied directives dynamically.
- Negative test: `ssh -o PubkeyAuthentication=no lab-local` returned `Permission denied (publickey)`.

## Predict → Run → Explain
- **Prediction before key command:** Executing `ssh -o PubkeyAuthentication=no lab-local` will be rejected by the server rather than presenting an interactive password prompt.
- **What actually happened:** The connection dropped immediately with `Permission denied (publickey)`.
- **Plain-language explanation:** Ripping the number pad off the door (`PasswordAuthentication no`) means the guard rejects anyone without a key rather than asking for a secret word.
- **How I verified it:** Ran `ssh lab-local` in a secondary terminal session to confirm cryptographic authentication succeeds without prompt.

## Decisions & Tradeoffs
- **Ed25519 over RSA-4096:** Chosen for superior collision resistance, smaller 256-bit key length, and resistance to side-channel timing attacks.
- **`systemctl reload` over `restart`:** Chosen to update daemon memory tables with `SIGHUP` without terminating active administrative sessions, mitigating lockout risks.

## AI Workflow
- **Asked:** How to structure asymmetric authentication, test negative fallbacks, and prevent daemon lockout during configuration updates.
- **Right:** Ed25519 key generation syntax, strict-mode permission requirements (`700`/`600`), and `sshd -t` pre-flight checks.
- **Wrong/Corrected:** Terminal buffer truncation during large heredoc pastes caused dropped commands; corrected using base64 decoding and safe atomic file creation.
- **Verified with:** `sshd -t`, `ls -la`, and live loopback `ssh` handshakes.

## Definition of Done
- [x] Ed25519 keypair generated and permissioned to `600`/`700`
- [x] Public key authorized and loopback verified
- [x] `~/.ssh/config` alias configured for flagless connection
- [x] OpenSSH daemon hardened (`PermitRootLogin no`, `PasswordAuthentication no`)
- [x] Syntax pre-checked with `sshd -t` and reloaded safely
- [x] Negative fallback verified with public-key disabled
- [x] Deliverable documented and pushed referencing `SEC-1101`
