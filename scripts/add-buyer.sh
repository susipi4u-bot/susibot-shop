#!/bin/bash
# Fügt Käufer nach Zahlung als Collaborator hinzu
# Usage: ./add-buyer.sh <github-username> <product-repo>

USERNAME="$1"
REPO="$2"
TOKEN="${GITHUB_TOKEN}"  # Set via env var for security

if [ -z "$USERNAME" ] || [ -z "$REPO" ]; then
  echo "Usage: $0 <github-username> <product-repo>"
  echo "Example: $0 johndoe healthcheck-script"
  exit 1
fi

echo "Lade $USERNAME zu $REPO ein..."

response=$(curl -s -X PUT "https://api.github.com/repos/susipi4u-bot/${REPO}/collaborators/${USERNAME}" \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  -d '{"permission":"pull"}')

if echo "$response" | grep -q '"id"'; then
  echo "✅ Erfolgreich! Einladung an $USERNAME gesendet."
  echo "Sie erhalten eine Email von GitHub."
else
  echo "❌ Fehler: $response"
fi
