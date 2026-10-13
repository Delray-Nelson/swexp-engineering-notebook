#!/usr/bin/env bash
set -euo pipefail

echo "[+] Starting Phase 1: Foundation & FHS Layout..."

# 1. Create dedicated system group and user
sudo groupadd -f appgroup
if ! id -u appuser &>/dev/null; then
    sudo useradd -r -g appgroup -s /bin/false appuser
    echo "[+] Created service user: appuser"
else
    echo "[+] Service user appuser already exists."
fi

# 2. Establish FHS-compliant directory layout
sudo mkdir -p /opt/app
sudo mkdir -p /var/log/app
sudo mkdir -p /var/backups/app

# 3. Lock down ownership and permissions
sudo chown -R appuser:appgroup /opt/app
sudo chown -R appuser:appgroup /var/log/app
sudo chmod 750 /opt/app
sudo chmod 750 /var/log/app
sudo chmod 700 /var/backups/app

echo "[+] Phase 1 Foundation successfully applied."
