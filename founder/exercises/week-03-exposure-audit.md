# Week 3 Lab — Actual Exposure Audit (JBF Dating)

## 1. AI Surface History Scan (`key`, `token`, `password`, `Bearer`, Customer/Domain Names)
- **Surfaces checked:** `[TODO — list every chat app, CLI agent session log, and IDE assistant transcript checked this month]`
- **Pattern scan command / search method:** Checked local/workspace files and transcripts for `key`, `token`, `password`, `Bearer`, and project/customer terms (avoiding printing raw secret values).
- **Hits found:** `[TODO — record each hit's surface, file/session reference, pattern matched, and exact line/context summary without pasting live secrets]`

## 2. Hit Classification (`never-prompt` / `with-care` / `fine`)
- `[TODO — for each hit from Step 1, assign never-prompt, with-care, or fine and explain why under founder/ai-llm-policy.md]`
  - Example format:
    - Hit #1 (`[surface / artifact]`): `fine` | `with-care` | `never-prompt` — `[reason]`.

## 3. Tool Settings & Data-Handling Verification (From Official UI & Docs Only)
- **Tool & plan inspected:** `[TODO — e.g., ChatGPT / Claude / Cursor / Copilot + exact plan name]`
- **Used for model training on your plan?** `[TODO — record exact answer from official settings & privacy docs, plus date checked]`
- **Data retention policy:** `[TODO — record exact retention behavior/windows from official docs]`
- **Transcript sync location:** `[TODO — record where chats/transcripts/logs sync or are stored per official UI/docs]`

## 4. Credential Rotation Log (Actual Rotation & Time Taken)
- **Credentials rotated:** `[TODO — list any exposed or precautionary keys/tokens rotated; write "None required after audit" only if truly verified]`
- **Time taken to rotate:** `[TODO — record actual minutes taken, e.g., "14 minutes" — this is your empirical argument for the secrets rule in founder/ai-llm-policy.md]`

## 5. Repository Secret Scan & Remediation
- **Scanner used:** `[TODO — e.g., gitleaks, trufflehog, detect-secrets, or read-only regex pattern scan over tracked/untracked files]`
- **Findings & fixes before agent access:** `[TODO — list any suspicious strings or untracked scratch files found, how they were removed/ignored/rotated, and confirm clean scan status]`
