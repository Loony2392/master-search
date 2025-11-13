# 🔍 Master Search

> Professional file search with extended features

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Author:** [@Loony2392](https://github.com/Loony2392)  
**Email:** info@loony-tech.de
**Company:** LOONY-TECH
**GitHub:** https://github.com/Loony2392/master-search  
**Created:** November 2025

---

## Table of Contents

- Features
- Installation
- Usage
- Screenshots
- Configuration
- Supported file types
- Technical details
- Troubleshooting
- Changelog
- Author

---

## Features

- Filename search (case-insensitive)
- Folder-name search
- Content search inside text files
- Recursive search
- Fast parallel processing (threading / multiprocessing)
- HTML report generation with clickable links

UI & reporting:
- Color console output (colorama)
- Emoji support for readability
- Real-time progress and stats
- Responsive HTML results with highlights

Performance & stability:
- Intelligent worker scaling using CPU/RAM (optional `psutil`)
- Batch processing and memory-friendly file handling
- Encoding fallbacks for mixed-encoding repositories

---

## Installation

### Option 1 — MSI Installer (Windows, recommended)

1. Download the latest `master-search-x.x.x.msi` from the Releases page.
2. Double-click the MSI and follow the installer.
3. Launch from Start Menu → "Master Search" or run `master-search` from a terminal.

Pros: no Python required on target machine, clean Windows integration and an uninstaller.

### Option 2 — Python (developer / advanced users)

Requirements:
- Python 3.7+

Clone and install:

```bash
git clone <repository-url>
cd master-search
pip install -r requirements.txt
```

Run locally:

```bash
python file_search_tool.py
```

### Option 3 — Build MSI yourself

Install dev dependencies and run the build script:

```bash
pip install -r requirements-dev.txt
python build_msi.py
```

The resulting MSI will be in `dist/`.

---

## Usage

Start the GUI (`gui_search_tool.py`) or the CLI (`file_search_tool.py`).

Basic CLI example:

```bash
python file_search_tool.py
```

Enter one or more search terms (comma/semicolon/newline separated) and a path to scan.

After completion an HTML report is generated and opened automatically when possible.

---

## Internationalization (i18n)

The GUI uses a simple i18n module (`i18n.py`) and `locales/` JSON files. By default the app uses the system locale and falls back to English. Add or edit `locales/<lang>.json` to provide translations.

Master Search — English README
==============================

Quick start
-----------
1. Install requirements:
```bash
pip install -r requirements.txt
```

Internationalization (i18n)
--------------------------
This project uses a gettext-based approach for localization. A small bootstrap module is provided: [Master Search/i18n.py](Master Search/i18n.py). Usage in your start scripts:

```py
from i18n import setup_i18n
_ = setup_i18n(domain="master_search", localedir="locales")
# use _("Some string") throughout your code
```

By default, English strings should be used in the source. Translations live under the `locales/` folder (standard gettext structure). You can extract messages with common tools (xgettext / msgfmt / babel) and provide `.po`/.mo files there.

GUI and CLI
-----------
Keep the GUI strings wrapped with `_()` to allow runtime translation depending on the system locale. The GUI will load translations based on the system language at startup.

MSI / Packaging (Windows)
-------------------------
We provide a helper script to build the EXE and MSI on Windows:
- [Master Search/setup_msi.py](Master Search/setup_msi.py)
- [Master Search/build_msi.py](Master Search/build_msi.py)

Build steps (Windows):
```powershell
# inside the project root
pip install -r requirements-dev.txt
python build_msi.py
```

Notes
-----
- Source strings and README are in English by default.
- Translation files should be placed in `locales/<lang>/LC_MESSAGES/master_search.mo`.
- See [Master Search/setup.py](Master Search/setup.py) for packaging configuration.

---

## Troubleshooting

- ModuleNotFoundError: colorama — install via `pip install -r requirements-minimal.txt` or `pip install colorama`.
- PermissionError — run as Administrator or check file permissions.
- MSI issues — ensure Visual Studio Build Tools are available when building on Windows.

---

## Author

Loony2392 — LOONY-TECH

Contact: info@loony-tech.de

- **Große Dateien** (>50MB) werden automatisch übersprungen

---

## 🛠️ Technische Details

### 🏗️ **Architektur**

```
Master Search
├── 🔍 FileSearchTool (Hauptklasse)
│   ├── 🎨 Farb-System (colorama)
│   ├── 📊 Fortschritts-Tracking
│   ├── 🔍 Such-Engine
│   └── 📄 HTML-Generator
├── 🎯 Such-Algorithmen
│   ├── Dateiname-Suche
│   ├── Ordnername-Suche
│   └── Inhalt-Suche
└── 📋 Bericht-Generator
    ├── HTML-Template
    ├── CSS-Styling
    └── JavaScript-Funktionen
```

### 🔍 **Such-Algorithmus**

1. **Verzeichnis-Traversierung**: Rekursive Durchsuchung mit `os.walk()`
2. **Dateiname-Matching**: Case-insensitive String-Vergleich
3. **Content-Analyse**: 
   - Intelligente Encoding-Erkennung (UTF-8, Latin-1, CP1252)
   - Zeilen-für-Zeilen-Verarbeitung
   - Treffer-Sammlung mit Zeilennummern
4. **Ergebnis-Aggregation**: Strukturierte Datensammlung
5. **HTML-Export**: Template-basierte Berichtgenerierung

### 📊 **Performance-Optimierungen**

- **Lazy Loading**: Dateien werden nur bei Bedarf gelesen
- **Encoding-Fallbacks**: Mehrere Encoding-Versuche für Kompatibilität
- **Größen-Limits**: Große Dateien werden übersprungen
- **Batch-Processing**: Effiziente Verarbeitung in Stapeln
- **Memory Management**: Keine vollständige Datei-Ladung in den Speicher

---

## 🔧 Troubleshooting

### ❓ **Häufige Probleme**

#### 🐍 **ModuleNotFoundError: colorama**
```bash
# Lösung 1 - Über requirements:
pip install -r requirements-minimal.txt

# Lösung 2 - Direkt:
pip install colorama

# Lösung 3 - Automatisch:
# Das Tool installiert colorama automatisch beim ersten Start
```

#### 🔒 **PermissionError beim Dateizugriff**
```
Fehler: [Errno 13] Permission denied: 'datei.txt'
```
**Lösung:** Script als Administrator ausführen oder Dateiberechtigungen prüfen

#### 🌐 **HTML-Datei öffnet sich nicht automatisch**
```
Browser konnte nicht automatisch geöffnet werden
```
**Lösung:** HTML-Datei manuell im Browser öffnen (Pfad wird angezeigt)

#### 📦 **MSI-Installation Probleme**

**Problem:** "Diese App kann auf Ihrem PC nicht ausgeführt werden"
```
Lösung 1: MSI als Administrator ausführen
Lösung 2: Windows SmartScreen temporär deaktivieren
Lösung 3: Digital signierte Version anfordern
```

**Problem:** "Windows protected your PC" / SmartScreen-Warnung
```
Lösung: "More info" → "Run anyway" klicken
Hinweis: Dies ist normal bei nicht-signierten Anwendungen
```

**Problem:** MSI-Build schlägt fehl
```bash
# Abhängigkeiten prüfen:
pip install cx_Freeze>=6.15.0

# Windows Build Tools installieren:
# Visual Studio Build Tools erforderlich

# Versuchen Sie:
python -m pip install --upgrade setuptools wheel
python build_msi.py
```

#### ⚡ **Performance-Probleme**

**Problem:** Sehr langsame Suche
```
Lösung 1: Verzeichnis mit weniger Dateien testen
Lösung 2: psutil installieren für optimierte Worker-Anzahl
Lösung 3: SSD statt HDD verwenden
```

**Problem:** Hoher RAM-Verbrauch  
```
Lösung 1: Kleinere Batch-Größen in performance_config.py
Lösung 2: Weniger Worker-Threads konfigurieren
Lösung 3: Antivirus-Software temporär deaktivieren
```

#### 🔍 **Keine Treffer gefunden**
```
🚫 Keine Ergebnisse gefunden
```
**Mögliche Ursachen:**
- Suchwort ist nicht vorhanden
- Pfad enthält nur Binärdateien
- Encoding-Probleme bei Textdateien

#### ⚡ **Langsame Performance**
**Optimierungen:**
- Kleinere Verzeichnisse wählen
- Große Dateien ausschließen
- SSD verwenden für bessere I/O-Performance

### 🛠️ **Debug-Modus**

Für erweiterte Fehlerdiagnose können Sie Debug-Informationen aktivieren:

```python
# Am Anfang der main() Funktion hinzufügen:
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 📝 Changelog

### 🎉 **Version 1.0.0** (November 2025)
- **🎉 Erstveröffentlichung** von Master Search
- **🔍 Kern-Suchfunktionalität** implementiert
- **🎨 Farbige Konsolen-UI** mit Emoji-Support
- **📄 HTML-Berichterstattung** mit responsive Design
- **📊 Fortschritts-Tracking** und Echtzeit-Statistiken
- **🛠️ Cross-Platform-Unterstützung** (Windows, Linux, macOS)
- **⚡ Performance-Optimierungen** für große Verzeichnisse
- **🔧 Fehlerbehandlung** und graceful fallbacks

### 🔮 **Geplante Features** (Version 1.1.0)
- **🔍 Regex-Suche** für erweiterte Muster
- **📁 Ausschluss-Filter** für Dateien und Ordner
- **💾 Konfigurationsdateien** für wiederverwendbare Einstellungen
- **🔄 Batch-Modus** für automatisierte Suchen
- **📧 Email-Berichte** für geplante Suchen
- **🌐 Web-Interface** für Remote-Zugriff

---

## 👨‍💻 Autor

**Loony2392 ([@Loony2392](https://github.com/Loony2392))**
- 📧 **Email:** info@loony-tech.de
- 🏢 **Unternehmen:** LOONY-TECH
- 🌍 **Standort:** Deutschland
- 💼 **Position:** Software Developer & IT Specialist
- 🐙 **GitHub:** [@Loony2392](https://github.com/Loony2392)

### 🚀 **Über den Autor**
Loony2392 ([@Loony2392](https://github.com/Loony2392)) ist ein erfahrener Software-Entwickler bei der LOONY-TECH mit Spezialisierung auf Python-Anwendungen und Automatisierungslösungen. Mit langjähriger Erfahrung in der Entwicklung von Tools für Dateiverwaltung und -analyse bringt er praktische Lösungen für alltägliche IT-Herausforderungen.

### 🎯 **Motivation**
Master Search wurde bei LOONY-TECH entwickelt, um IT-Professionals und Entwicklern ein mächtiges, benutzerfreundliches Tool für die Dateisuche zur Verfügung zu stellen. Das Tool kombiniert Enterprise-Funktionalität mit einer ansprechenden Benutzeroberfläche und professioneller Berichterstattung.

---

## 📜 License

```
MIT License

Copyright (c) 2025 LOONY-TECH - Loony2392 (@Loony2392)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Danksagungen

- **Python Community** für die excellente Sprache und Bibliotheken
- **colorama** Entwickler für die Cross-Platform-Farbunterstützung
- **LOONY-TECH** für die Unterstützung bei der Entwicklung
- **Open Source Community** für Inspiration und Best Practices

---

## 🧪 Testing & Quality Assurance

Master Search wird mit umfassenden Tests und Qualitätsprüfungen ausgeliefert:

### Lokale Tests ausführen

```bash
# Einfacher Test-Runner
python test_all.py

# Unit Tests detailliert
pytest tests/test_file_search_tool.py -v

# Integration Tests
pytest tests/test_integration.py -v

# Alle Tests mit Coverage Report
pytest tests/ -v --cov=file_search_tool --cov-report=html
```

### Test-Coverage

- ✅ **28 Unit Tests** - FileSearchTool Funktionalität
- ✅ **35+ Integration Tests** - Modul-Zusammenspiel
- ✅ **Syntax Checking** - py_compile Validierung
- ✅ **Linting** - Flake8, Pylint Analyse
- ✅ **Security Scan** - Bandit Security Check
- ✅ **Functional Tests** - End-to-End Validierung

### GitHub Actions Workflows

Automatische Tests bei jedem Push und Pull Request:

- 🔍 **test.yml** - Syntax, Linting, Unit Tests, Integration Tests, Security, Build
- 🚀 **release.yml** - Automatischer Build und Release bei git tag

Siehe [TESTING.md](TESTING.md) und [PRODUCTION_READINESS.md](PRODUCTION_READINESS.md) für Details.

---

## 📞 Support & Kontakt

Haben Sie Fragen, Verbesserungsvorschläge oder benötigen Support?

- 📧 **Email:** info@loony-tech.de
- 🐛 **Bug Reports:** Erstellen Sie ein Issue im Repository
- 💡 **Feature Requests:** Senden Sie Ihre Ideen per Email
- 📖 **Dokumentation:** Diese README.md wird regelmäßig aktualisiert

---

<div align="center">

**⭐ Wenn Ihnen Master Search gefällt, geben Sie uns einen Star! ⭐**

*Entwickelt mit ❤️ von Loony2392*

</div>