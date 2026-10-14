#!/usr/bin/env bash
set -euo pipefail

LOG_FILE="/var/log/app/provision.log"

log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE" 2>/dev/null || echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

log "=== Starting Capstone Provisioning ==="

# Phase 1 Recap / Foundation Check
log "Checking system users and directories..."
sudo groupadd -f appgroup
if ! id -u appuser &>/dev/null; then
    sudo useradd -r -g appgroup -s /bin/false appuser
    log "Created service user: appuser"
else
    log "Service user appuser already exists."
fi

sudo mkdir -p /opt/app /var/log/app /var/backups/app
sudo chown -R appuser:appgroup /opt/app /var/log/app
sudo chmod 750 /opt/app /var/log/app
sudo chmod 700 /var/backups/app

# Phase 2: Baseline Packages & Updates
log "Updating package cache and installing baseline tools..."
sudo apt-get update -y
sudo apt-get install -y curl ufw fail2ban unattended-upgrades logrotate

log "=== Phase 2 Automation Completed Successfully ==="
