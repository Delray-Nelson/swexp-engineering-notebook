#!/usr/bin/env bash
set -euo pipefail

log() { printf '[%s] %s\n' "$(date +\%T)" "$*"; }
fail() { printf 'ERROR: %s\n' "$*" >&2; exit 1; }

ERRORS=0

log "Starting developer onboarding setup..."

# 1. Prerequisite check
log "Checking required CLI tools..."
for c in git curl jq; do
  if ! command -v "$c" >/dev/null 2>&1; then
    log "Missing required command: $c"
    ((ERRORS++))
  fi
done

if [ "$ERRORS" -gt 0 ]; then
  fail "Prerequisite check failed with $ERRORS missing tool(s)."
fi

# 2. Idempotent workspace directory setup
TARGET_DIR="$HOME/projects/dev-onboarding-test"
log "Ensuring target directory exists: $TARGET_DIR"
mkdir -p "$TARGET_DIR"

# 3. Idempotent git clone logic
REPO_URL="https://github.com/Delray-Nelson/swexp-engineering-notebook.git"
CLONE_PATH="$TARGET_DIR/swexp-engineering-notebook"

if [ -d "$CLONE_PATH/.git" ]; then
  log "Repository already cloned at $CLONE_PATH. Skipping clone."
else
  log "Cloning repository $REPO_URL into$CLONE_PATH..."
  git clone "$REPO_URL" "$CLONE_PATH"
fi

log "Developer onboarding completed successfully!"
