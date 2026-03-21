#!/bin/bash
# Session-Cleanup: Löscht alte Sessions, behält die 10 neuesten
SESSION_DIR="/home/susi/.openclaw/agents/main/sessions"

count=$(find "$SESSION_DIR" -type f 2>/dev/null | wc -l)

if [ "$count" -gt 10 ]; then
  find "$SESSION_DIR" -type f -printf '%T@ %p\n' | sort -rn | tail -n +11 | cut -d' ' -f2- | xargs -r rm -f
  echo "$(date): Cleanup gelöscht, behalte 10 neueste von $count Dateien"
else
  echo "$(date): Nur $count Dateien, nichts zu löschen"
fi