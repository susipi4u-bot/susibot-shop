#!/usr/bin/env python3
"""
Passwort-Generator
Kommandozeilen-Tool zum Generieren sicherer Passwörter
"""

import argparse
import random
import string
import sys

# Zeichensätze
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SPECIAL = "!@#$%^&*()_+-=[]{}|;:,.<>?"

def generate_password(length: int, use_special: bool = True) -> str:
    """Generiert ein Passwort mit wählbarer Länge und Special Characters."""
    chars = LOWERCASE + UPPERCASE + DIGITS
    if use_special:
        chars += SPECIAL
    
    # Mindestens ein Zeichen aus jeder gewählten Kategorie
    password = []
    password.append(random.choice(LOWERCASE))
    password.append(random.choice(UPPERCASE))
    password.append(random.choice(DIGITS))
    if use_special:
        password.append(random.choice(SPECIAL))
    
    # Rest mit zufälligen Zeichen auffüllen
    for _ in range(length - len(password)):
        password.append(random.choice(chars))
    
    # Mischen
    random.shuffle(password)
    return ''.join(password)

def copy_to_clipboard(text: str) -> bool:
    """Kopiert Text in die Zwischenablage."""
    try:
        # Linux/Unix
        import subprocess
        subprocess.run(['xclip', '-selection', 'clipboard'], 
                      input=text.encode(), check=True)
        return True
    except FileNotFoundError:
        try:
            # Alternative für Linux
            subprocess.run(['xsel', '--clipboard', '--input'], 
                          input=text.encode(), check=True)
            return True
        except FileNotFoundError:
            pass
    
    try:
        # macOS
        import subprocess
        subprocess.run(['pbcopy'], input=text.encode(), check=True)
        return True
    except FileNotFoundError:
        pass
    
    try:
        # Windows
        import subprocess
        subprocess.run(['clip'], input=text.encode(), check=True)
        return True
    except FileNotFoundError:
        pass
    
    return False

def main():
    parser = argparse.ArgumentParser(
        description='Sicherer Passwort-Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Beispiele:
  %(prog)s                      # 16 Zeichen, mit Special Characters
  %(prog)s -l 24                # 24 Zeichen Passwort
  %(prog)s -l 12 --no-special   # 12 Zeichen ohne Special Characters
  %(prog)s -c                   # In Zwischenablage kopieren
        '''
    )
    parser.add_argument('-l', '--length', type=int, default=16,
                       help='Passwortlänge (Standard: 16)')
    parser.add_argument('--no-special', action='store_true',
                       help='Keine Special Characters verwenden')
    parser.add_argument('-c', '--clipboard', action='store_true',
                       help='In Zwischenablage kopieren')
    parser.add_argument('-q', '--quiet', action='store_true',
                       help='Nur das Passwort ausgeben')
    
    args = parser.parse_args()
    
    if args.length < 4:
        print("Fehler: Passwortlänge muss mindestens 4 Zeichen sein.", 
              file=sys.stderr)
        sys.exit(1)
    
    password = generate_password(args.length, not args.no_special)
    
    if args.quiet:
        print(password)
    else:
        print(f"🔐 Passwort ({len(password)} Zeichen):")
        print(f"   {password}")
    
    if args.clipboard:
        if copy_to_clipboard(password):
            print("✓ In Zwischenablage kopiert!")
        else:
            print("✗ Kopieren fehlgeschlagen (kein Clipboard-Tool gefunden)",
                  file=sys.stderr)
            sys.exit(1)

if __name__ == '__main__':
    main()