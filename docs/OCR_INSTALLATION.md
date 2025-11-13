# OCR Integration - Automatische Installation
===============================================

## Übersicht

Ab Version 2025.11.19 wird **EasyOCR** automatisch während des Build-Prozesses installiert und in den finalen Paketen (DMG/MSI) enthalten.

### Was ist neu?

- ✅ **Automatische OCR-Installation** während DMG/MSI-Build
- ✅ **Keine manuellen Schritte** für Benutzer nötig
- ✅ **Cross-Platform** (Windows, macOS, Linux)
- ✅ **Fallback-Systeme** falls Installation fehlschlägt
- ✅ **OCR standardmäßig DEAKTIVIERT** (Opt-In Nutzer-Entscheidung)

## Für Benutzer

### macOS (DMG)
1. DMG herunterladen: `Master_Search_v2025.11.19.dmg`
2. Datei doppelklicken
3. Master Search in Programme ziehen
4. Starten → OCR ist bereits installiert und einsatzbereit!

**Erste Verwendung:**
- Beim ersten OCR-Durchlauf werden Sprachmodelle heruntergeladen (~200MB)
- Danach verwendet OCR gecachte Modelle (sehr schnell)

### Windows (MSI)
1. MSI-Installer herunterladen: `Master_Search_v2025.11.19.msi`
2. Installer ausführen
3. Installation abschließen
4. Starten → OCR ist bereits installiert!

### Linux (optional)
- Für Linux-Systeme: `pip install easyocr` (oder PaddleOCR)
- Siehe: [Linux-Installation](#linux-installation)

## Für Entwickler

### Build-Prozess

#### macOS DMG
```bash
python build_dmg.py
```

Der Prozess führt automatisch aus:
1. Abhängigkeiten prüfen
2. `setup_ocr.py` ausführen (installiert EasyOCR + PaddleOCR)
3. py2app kompilieren
4. DMG erstellen

#### Windows MSI
```bash
python build_msi.py
```

Der Prozess:
1. Abhängigkeiten prüfen
2. `setup_ocr.py` ausführen
3. PyInstaller kompilieren
4. MSI erstellen

### OCR Setup-Skript

**Datei:** `scripts/setup_ocr.py`

```python
# Installiert automatisch:
- easyocr>=1.7.0      # Primär
- paddleocr>=2.7.0    # Fallback
```

**Funktionen:**
- ✅ Timeout-Handling (5 Min max pro Paket)
- ✅ Fehlerbehandlung (Build nicht unterbrochen)
- ✅ Progress-Ausgabe
- ✅ Platform-Erkennung

### OCR Dependencies

**Datei:** `requirements-ocr.txt`

```
easyocr>=1.7.0
paddleocr>=2.7.0
```

Diese werden **nicht** in `requirements.txt` eingebunden, um:
- Minimale Installation zu unterstützen
- Build-Zeit zu reduzieren
- Speicher sparen (optional)

### Manuelle Installation (Fallback)

Falls der automatische Build-Prozess OCR nicht installiert:

```bash
# Option 1: Nur Primary Engine
pip install easyocr

# Option 2: Mit Fallback
pip install easyocr paddleocr

# Option 3: Tesseract (optional, system-abhängig)
# Windows: https://github.com/UB-Mannheim/tesseract/releases
# macOS:   brew install tesseract
# Linux:   sudo apt install tesseract-ocr
```

## Technische Details

### Paketgröße

| Komponente | Größe |
|-----------|-------|
| Base App | ~50MB |
| EasyOCR | ~150MB |
| PaddleOCR | ~200MB |
| **Total Installed** | ~400MB |

**Hinweis:** Sprachmodelle werden beim ersten Durchlauf heruntergeladen (nicht enthalten)

### Abhängigkeiten

EasyOCR wird mit folgenden Abhängigkeiten installiert:
- numpy
- opencv-python
- torch
- PIL/Pillow
- andere Deep-Learning Deps

### Caching

- **Cache-Verzeichnis:** `~/.cache/master_search/ocr/`
- **Cache-Größe:** ~200MB für Standard-Sprachen
- **Automatische Cleanup:** Keine (manuell möglich)

### Performance

| Operation | Zeit |
|-----------|------|
| Erste OCR-Erkennung | 3-8 Sekunden |
| Nachfolgende (cached) | <100ms |
| Modell-Download | 2-5 Min (einmalig) |
| Batch-Verarbeitung (10 Bilder) | 5-10 Sekunden |

## Fehlerbehandlung

### Szenario 1: OCR-Installation schlägt fehl
- ✅ Build wird **nicht abgebrochen**
- ℹ️ Warnung angezeigt
- Benutzer kann manuell installieren: `pip install easyocr`

### Szenario 2: Kein OCR verfügbar
- OCR-Checkbox ist **deaktiviert** (grau)
- Tooltip zeigt: "OCR: Nicht installiert"
- Suche funktioniert normal (ohne OCR)

### Szenario 3: Modell-Download beim ersten Start
- Benutzer sieht Fortschrittsanzeige
- OCR-Fenster bleibt responsive
- Download kann abgebrochen werden

## Linux-Installation

### Debian/Ubuntu
```bash
sudo apt update
sudo apt install python3-pip
pip install easyocr
```

### Fedora/RHEL
```bash
sudo dnf install python3-pip
pip install easyocr
```

### Arch
```bash
sudo pacman -S python-pip
pip install easyocr
```

## Troubleshooting

### OCR-Checkbox ist grau/deaktiviert
**Grund:** EasyOCR nicht installiert
**Lösung:**
```bash
pip install easyocr
# Starten Sie die App neu
```

### "Out of Memory" Fehler beim ersten Durchlauf
**Grund:** Modelle laden mit größeren Mengen gleichzeitig
**Lösung:**
1. OCR für einzelne Dateien nutzen
2. Batch-Verarbeitung reduzieren
3. RAM freigeben bevor OCR startet

### Sehr langsam beim ersten Durchlauf
**Grund:** Sprachmodelle werden heruntergeladen
**Lösung:**
1. Geduldig warten (normal)
2. Aktive Verbindung prüfen
3. Größeres Timeout verwenden

### Timeout beim Modell-Download
**Grund:** Langsame/unterbrochene Verbindung
**Lösung:**
```bash
# Manuell herunterladen und cachen
python -c "import easyocr; reader = easyocr.Reader(['de'])"
# Dies lädt Modelle vor
```

## Version-Geschichte

### v2025.11.19 (Aktuell)
- ✅ Automatische OCR-Installation in DMG/MSI
- ✅ Kategorie-Tooltips mit Dateitypen
- ✅ Improved OCR fallback system
- ✅ Cross-platform support

### v2025.11.18
- Basis-OCR Integration
- Manual installation support

### v2025.11.17
- 1000+ Dateitypen
- 14 Kategorien

## FAQ

**F: Ist OCR wirklich vorinstalliert?**
A: Ja! Aber standardmäßig ausgeschaltet. Benutzer müssen es explizit in den Einstellungen aktivieren.

**F: Kann ich OCR deaktivieren/entfernen?**
A: Ja, via Einstellungen → OCR: Deaktiviert. Zu entfernen: `pip uninstall easyocr`

**F: Funktioniert OCR offline?**
A: Ja, nach dem ersten Durchlauf (wenn Modelle gecacht). Beim ersten Mal braucht es eine Verbindung.

**F: Welche Sprachen unterstützt OCR?**
A: 80+ Sprachen. Standard: Deutsch + Englisch. Weitere per Konfiguration.

**F: Kann ich PaddleOCR statt EasyOCR nutzen?**
A: Ja, beide können installiert sein. Das Beste wird automatisch gewählt.

**F: Ist OCR auf Apple Silicon (M1/M2) möglich?**
A: Ja, getestete und optimierte Version für ARM64.
