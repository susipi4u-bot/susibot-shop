# passgen-script

Sicherer Passwort-Generator für die Kommandozeile.

## Features

- 🎲 **Längenwahl** – Passwörter von 4 bis 64 Zeichen
- 🔣 **Special Characters** – Optional: !@#$%^&*()_+-=[]{}|;:,.<>?
- 📋 **Copy-to-Clipboard** – Direkt in die Zwischenablage kopieren
- 🔒 **Sicher** – Mindestens ein Zeichen aus jeder Kategorie

## Installation

### Option 1: Direkt ausführen

```bash
# Clone oder Download dieses Repos
git clone https://github.com/susipi4u/passgen-script.git
cd passgen-script

# Ausführen
python3 passgen.py
```

### Option 2: Systemweit installieren

```bash
# Script ausführbar machen
chmod +x passgen.py

# Nach /usr/local/bin kopieren (oder ~/.local/bin/)
sudo cp passgen.py /usr/local/bin/passgen

# Jetzt überall aufrufbar
passgen
```

### Option 3: Als Python-Paket installieren (mit pip)

```bash
pip install .
# Oder
pipx install .
```

## Verwendung

### Grundbefehle

```bash
# Standard: 16 Zeichen mit Special Characters
passgen

# Eigene Länge
passgen -l 24
passgen --length 32

# Ohne Special Characters
passgen --no-special

# In Zwischenablage kopieren
passgen -c
passgen --clipboard

# Nur Passwort ausgeben (für Skripte)
passgen -q
```

### Alle Optionen

| Option | Beschreibung |
|--------|--------------|
| `-l, --length` | Passwortlänge (Standard: 16) |
| `--no-special` | Keine Special Characters verwenden |
| `-c, --clipboard` | In Zwischenablage kopieren |
| `-q, --quiet` | Nur Passwort ausgeben |

### Beispiele

```bash
# 12 Zeichen, kein Special
passgen -l 12 --no-special

# 20 Zeichen, in Zwischenablage
passgen -l 20 -c

# Für Scripts: Passwort in Variable speichern
PASS=$(passgen -q -l 20)
echo "$PASS"
```

## Anforderungen

- Python 3.7+

### Clipboard-Tools (optional)

- **Linux:** `xclip` oder `xsel`
- **macOS:** Standard vorhanden
- **Windows:** Standard vorhanden

```bash
# xclip installieren (Ubuntu/Debian)
sudo apt install xclip
```

## Lizenz

MIT License