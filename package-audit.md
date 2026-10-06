# Package Audit & Trusted Installation Policy Report

**Ticket Reference:** SEC-2150  
**Deliverable:** Package Audit & Supply Chain Hardening  
**Environment:** WSL2 / Ubuntu Host  

---

## 1. Package Inventory Counts (Before & After)
* **Initial Baseline Package Count (Before):** `552` installed packages (queried via `apt list --installed 2>/dev/null | wc -l`)
* **Final Audit Package Count (After):** `551` installed packages following cleanup, removal, and autoremoval cycles.

---

## 2. Security Updates & Patches Applied
The system package indices were refreshed (`sudo apt update`) and upgradable security packages were reviewed (`apt list --upgradable`) to patch known Common Vulnerabilities and Exposures (CVEs):
* Applied updates for base system libraries and critical runtime dependencies.
* Verified all repository metadata through detached GPG signatures (`Release.gpg`) to ensure cryptographic provenance.

---

## 3. Package Removal & System Hygiene
* **Package Removed:** `tree` (installed temporarily during Lab 12 inspection tasks).
* **Action Taken:** Executed `sudo apt remove --purge -y tree` followed by `sudo apt autoremove -y`.
* **Rationale:** Purging ensures that test utilities, temporary binaries, and their orphaned dependencies are completely wiped from disk, minimizing the system's attack surface and maintaining strict compliance with production footprint minimization.

---

## 4. Trusted Installation Policy (Replacing `curl | sudo bash`)
> **Standard Operating Procedure:** Direct streaming of unvetted remote scripts into unconstrained root shells (e.g., `curl https://untrusted-domain.com/install.sh | sudo bash`) is strictly prohibited across all environments. All third-party software, utilities, and dependencies must be provisioned exclusively through official, cryptographically signed package managers (`apt`), verified OCI container registries (`Docker` / `Podman`), or manually inspected source repositories accompanied by valid GPG commit/tag signatures. Any deviation requires a formal security review and documented architectural exception.
