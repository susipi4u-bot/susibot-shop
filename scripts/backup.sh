#!/bin/bash
# Nachtsicherung - Backup wichtiger Daten
BACKUP_DIR="/home/susi/backups"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p $BACKUP_DIR

# Backup workspace
tar -czf $BACKUP_DIR/workspace_$DATE.tar.gz /home/susi/.openclaw/workspace/ 2>/dev/null

# Backup payment state
cp /home/susi/.openclaw/workspace/.payment_state $BACKUP_DIR/payment_state_$DATE.json 2>/dev/null

# Alte Backups aufräumen (älter als 7 Tage)
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete 2>/dev/null

echo "Backup erstellt: $DATE"