#!/usr/bin/env bash
set -euo pipefail

DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET_FILE="$DOTFILES_DIR/.bash_custom"
LINK_NAME="$HOME/.bash_custom"

echo "[+] Installing dotfile symlinks..."
if [ -f "$TARGET_FILE" ]; then
    ln -sfn "$TARGET_FILE" "$LINK_NAME"
    echo "[+] Symlinked $LINK_NAME -> $TARGET_FILE"
else
    echo "[-] Error: Target file $TARGET_FILE not found."
    exit 1
fi
echo "[+] Dotfiles successfully installed."
