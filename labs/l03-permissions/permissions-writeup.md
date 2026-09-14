# SEC-2031 — Lab 03: Permissions & Least Privilege Deliverable

## Summary
In this lab, I reproduced permission security failures, diagnosed world-writable file risks, remediated open permissions on sensitive application secrets, and established strict least-privilege access rules without resorting to dangerous chmod 777 overrides.

## Evidence & Verification
### 1. Initial Lab Setup & Vulnerability Identification
Created the working environment and created secrets.env with intentionally over-permissive 666 mode.
- Command Run: ls -l secrets.env
- Before State Output: -rw-rw-rw- 1 hurdle_tm hurdle_tm 13 Sep 13 11:30 secrets.env

### 2. Least-Privilege Remediation
Remediated secrets.env by applying octal mode 640.
- Command Run: chmod 640 secrets.env
- After State Output: -rw-r----- 1 hurdle_tm hurdle_tm 13 Sep 13 11:32 secrets.env

## Why 640 is Correct (and Why 777 is Dangerous)
- Dangerous 777: Grants read/write/execute permissions to all users on the system, creating severe security risks.
- Correct 640: Enforces least privilege by granting read/write to owner, read-only to group, and zero access to world/others.

