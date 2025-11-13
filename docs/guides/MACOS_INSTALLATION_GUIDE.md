# Master Search für macOS - Installationsanleitung
====================================================

Master Search ist jetzt vollständig kompatibel mit macOS! Diese Anleitung hilft Ihnen bei Installation und Verwendung.

## 📋 Systemvoraussetzungen

- **macOS:** 10.12 Sierra oder neuer
- **Python:** 3.8 oder neuer (für Entwicklung)
- **Architektur:** Intel (x86_64) oder Apple Silicon (ARM64)

## 🚀 Installation

### Option 1: DMG Download (Empfohlen)
1. Laden Sie die neueste DMG-Datei herunter
2. Doppelklicken Sie auf die DMG-Datei zum Mounten
3. Ziehen Sie "Master Search.app" in den Applications-Ordner
4. Starten Sie über Spotlight oder den Applications-Ordner

### Option 2: Aus Quellcode bauen
```bash
# Repository klonen
git clone https://github.com/loony2392/master-search.git
cd master-search

# Abhängigkeiten installieren
pip install -r requirements-mac.txt

# DMG erstellen
python scripts/build_dmg.py
```

## 🎯 Verwendung

### GUI-Version
```bash
# Aus Applications-Ordner starten oder:
python src/gui_main_mac.py
```

### CLI-Version
```bash
# Terminal verwenden:
python src/cli_main_mac.py --search "Suchterm" --directory "/path/to/search"
```

## 🔧 macOS-spezifische Funktionen

### Plattform-Integration
- **Finder-Integration:** Dateien öffnen mit `open` Kommando
- **Spotlight-kompatibel:** App über Spotlight findbar
- **App Bundle:** Native .app-Struktur
- **Retina-Support:** High-DPI Display Unterstützung

### Dateisystem
- **HFS+ & APFS:** Vollständige Unterstützung
- **Case Sensitivity:** Automatische Erkennung
- **Extended Attributes:** Werden berücksichtigt
- **Symlinks:** Werden korrekt behandelt

### Standard-Verzeichnisse
- **Reports:** `~/Downloads/Master Search/`
- **Einstellungen:** `~/Library/Application Support/Master Search/`
- **Logs:** `~/Library/Logs/Master Search/`

## 🛠️ Entwicklung

### Entwicklungsumgebung einrichten
```bash
# Python-Umgebung erstellen
python3 -m venv venv_macos
source venv_macos/bin/activate

# Abhängigkeiten installieren
pip install -r requirements-mac.txt

# App im Entwicklungsmodus starten
python src/gui_main.py
```

### DMG erstellen
```bash
# Vollständiges DMG mit App Bundle
python scripts/build_dmg.py

# Nur App Bundle (ohne DMG)
python setup_dmg.py py2app
```

### Code Signing (Optional)
```bash
# App signieren für Distribution
codesign -s "Developer ID Application: Your Name" \
         --deep --force \
         "dist/Master Search.app"

# Signatur verifizieren
codesign -v "dist/Master Search.app"
```

## 📱 App Bundle Struktur
```
Master Search.app/
├── Contents/
│   ├── Info.plist          # App-Metadaten
│   ├── MacOS/
│   │   └── Master Search   # Hauptprogramm
│   ├── Resources/
│   │   ├── locales/        # Sprachdateien
│   │   ├── lib/            # Python-Bibliotheken
│   │   └── site-packages/  # Abhängigkeiten
│   └── Frameworks/         # Python-Framework
```

## ⚡ Performance-Optimierungen

### Für große Verzeichnisse
```python
# Optimale Einstellungen für macOS
MAX_WORKERS = 8  # Für Apple Silicon
CHUNK_SIZE = 1000
USE_SPOTLIGHT_INDEX = True  # Nutzt macOS Spotlight-Index
```

### Memory Management
```python
# macOS-spezifische Speicherverwaltung
USE_MMAP = True  # Für große Dateien
AUTO_GC = True   # Automatische Garbage Collection
```

## 🔍 Troubleshooting

### Häufige Probleme

#### "App kann nicht geöffnet werden" (Gatekeeper)
```bash
# App erlauben
sudo xattr -rd com.apple.quarantine "Master Search.app"

# Oder in Systemeinstellungen:
# Sicherheit & Datenschutz → "Trotzdem öffnen"
```

#### Python-Import-Fehler
```bash
# Python-Pfad prüfen
which python3
python3 --version

# Abhängigkeiten neu installieren
pip install --force-reinstall -r requirements-mac.txt
```

#### Berechtigungen für Dateizugriff
```bash
# Vollzugriff auf Festplatte erlauben:
# Systemeinstellungen → Sicherheit & Datenschutz → 
# Datenschutz → Vollzugriff auf Festplatte → Master Search hinzufügen
```

### Log-Dateien
```bash
# App-Logs anzeigen
tail -f ~/Library/Logs/Master Search/app.log

# System-Logs
log stream --predicate 'process == "Master Search"'
```

## 🌍 Lokalisierung

Master Search unterstützt mehrere Sprachen auf macOS:

- **Deutsch:** Standard für deutsche macOS-Installation
- **English:** Standard für englische macOS-Installation  
- **Français:** Standard für französische macOS-Installation

Sprache wird automatisch basierend auf System-Locale gewählt.

## 📄 Integration mit anderen Apps

### Finder-Integration
```applescript
# AppleScript für Finder-Integration
tell application "Finder"
    set selectedItems to selection
    repeat with anItem in selectedItems
        set itemPath to POSIX path of (anItem as alias)
        do shell script "python3 /path/to/src/gui_main.py --path " & quoted form of itemPath
    end repeat
end tell
```

### Terminal-Integration
```bash
# Alias für .zshrc oder .bash_profile
alias msearch='python3 /Applications/Master\ Search.app/Contents/Resources/cli_main.py'

# Verwendung
msearch --search "TODO" --directory ~/Documents
```

## ⚖️ Lizenz & Support

- **Lizenz:** Proprietär (© 2025 LOONY-TECH)
- **Support:** info@loony-tech.de
- **Updates:** Automatische Benachrichtigungen in der App

## 📊 Kompatibilitätsmatrix

| macOS Version | Unterstützung | Getestet |
|---------------|---------------|----------|
| 14.x Sonoma   | ✅ Vollständig | ✅      |
| 13.x Ventura  | ✅ Vollständig | ✅      |
| 12.x Monterey | ✅ Vollständig | ⚠️       |
| 11.x Big Sur  | ✅ Vollständig | ⚠️       |
| 10.15 Catalina| ✅ Vollständig | ❌      |
| 10.14 Mojave  | ⚠️ Eingeschränkt| ❌     |
| ≤ 10.13       | ❌ Nicht unterstützt | ❌ |

**Legende:**
- ✅ Vollständig getestet und funktional
- ⚠️ Sollte funktionieren, aber nicht vollständig getestet
- ❌ Nicht unterstützt oder getestet

---

*Vielen Dank für die Verwendung von Master Search auf macOS! 🍎*