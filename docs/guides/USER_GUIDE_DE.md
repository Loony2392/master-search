# Master Search - Benutzeranleitung

**Version:** 2025.11.7  
**Letztes Update:** November 12, 2025  
**Sprachen:** Deutsch · English · Français

---

## 📑 Inhaltsverzeichnis

1. [Überblick](#überblick)
2. [Installation](#installation)
3. [Grundlagen](#grundlagen)
4. [Hauptfunktionen](#hauptfunktionen)
5. [Suchtechniken](#suchtechniken)
6. [HTML-Berichte](#html-berichte)
7. [Einstellungen](#einstellungen)
8. [Tipps & Tricks](#tipps--tricks)
9. [Häufig gestellte Fragen](#häufig-gestellte-fragen)
10. [Fehlerbehebung](#fehlerbehebung)

---

## Überblick

**Master Search** ist ein leistungsstarkes Desktop-Tool zur Volltextsuche über Dateisysteme. Es ermöglicht schnelle und effiziente Suchen in Dateien und Ordnern mit erweiterten Filteroptionen und schönen HTML-Berichten.

### Was kann Master Search?

✅ **Schnelle Dateisuche** - Durchsucht Millionen von Dateien in Sekunden  
✅ **Volltextsuche** - Sucht Inhalte innerhalb von Dateien  
✅ **Regex-Unterstützung** - Regex-Pattern für komplexe Suchen  
✅ **HTML-Berichte** - Automatische Generierung schöner Berichte mit Animationen  
✅ **59+ Dateitypen** - Unterstützt Code, Dokumente, Archiven und mehr  
✅ **Mehrsprachig** - Deutsch, Englisch, Französisch  
✅ **Echtzeit-Anzeige** - Sehen Sie Suchergebnisse während der Suche  
✅ **Clipboard-Integration** - Ein-Klick Kopieren von Dateipfaden  

---

## Installation

### Windows MSI Installer (Empfohlen)

1. **Download** der neuesten MSI-Datei von der Release-Seite
2. **Doppelklick** auf `Master_Search_Setup_v2025.11.7.msi`
3. **Setup-Assistent** folgen:
   - Installationsordner auswählen (Standard: `C:\Program Files\Master Search`)
   - Startmenü-Verknüpfung erstellen (optional)
   - Desktop-Verknüpfung erstellen (optional)
4. **Fertigstellen** - Master Search ist sofort einsatzbereit

### Portable Version

1. **Download** der portablen ZIP-Datei
2. **Entpacken** in gewünschtes Verzeichnis
3. **master_search.exe** ausführen (kein Setup erforderlich)
4. **Optional:** Verknüpfung auf Desktop erstellen

### Systemanforderungen

| Anforderung | Version |
|-------------|---------|
| **Windows** | 7 SP1 oder neuer |
| **Speicher** | 512 MB RAM minimum |
| **Festplatte** | 100 MB freier Speicherplatz |
| **Browser** | Moderner Browser für HTML-Berichte |

---

## Grundlagen

### Benutzeroberfläche

Die Master Search GUI besteht aus vier Hauptbereichen:

```
┌─────────────────────────────────────────────────────────┐
│  Master Search v2025.11.7                         [_][□][X]│
├─────────────────────────────────────────────────────────┤
│  SUCHBEREICH                                            │
│  ┌────────────────────────────────────────────────────┐ │
│  │ Suchbegriff:        [________________]              │ │
│  │ Dateityp-Filter:    [Alle] [nur Code] [Dokumente]  │ │
│  │ Suchort:            [C:\]  [Durchsuchen...]         │ │
│  │ ☐ In Dateien suchen  ☐ Groß/Kleinschreibung        │ │
│  │ ☐ Reguläre Ausdrücke ☐ HTML-Report generieren      │ │
│  │                     [SUCHE STARTEN]                 │ │
│  └────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│  ECHTZEIT-ERGEBNISSE                                    │
│  ┌────────────────────────────────────────────────────┐ │
│  │ 💾 C:\Projects\README.md         [📋] [📂] [🗑️]   │ │
│  │ 💾 C:\Projects\config.json       [📋] [📂] [🗑️]   │ │
│  │ 📄 C:\Docs\report.docx           [📋] [📂] [🗑️]   │ │
│  │ Suche läuft... 145 Ergebnisse gefunden             │ │
│  └────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ ✓ Fertig! 247 Dateien durchsucht, 12 Treffer gefunden   │
└─────────────────────────────────────────────────────────┘
```

### Elemente erklären

| Element | Beschreibung |
|---------|-------------|
| **Suchbegriff** | Das Wort oder die Phrase, die Sie suchen |
| **Dateityp-Filter** | Auf bestimmte Dateitypen beschränken (optional) |
| **Suchort** | Verzeichnis, das durchsucht werden soll |
| **In Dateien suchen** | Inhalt von Dateien durchsuchen (nicht nur Namen) |
| **Groß/Kleinschreibung** | Unterscheidung zwischen Groß- und Kleinbuchstaben |
| **Reguläre Ausdrücke** | Regex-Pattern statt einfacher Text |
| **HTML-Report** | Automatischer Report nach der Suche |

---

## Hauptfunktionen

### 1. Einfache Dateisuche

**Szenario:** Sie suchen alle Python-Dateien mit Namen `test`

**Schritte:**
1. **Suchbegriff:** `test` eingeben
2. **Dateityp-Filter:** "Code" wählen
3. **Suchort:** Root-Verzeichnis oder `C:\` wählen
4. **[SUCHE STARTEN]** klicken

**Ergebnis:**
- Alle `.py`, `.js`, `.ts` usw. mit "test" im Namen werden angezeigt
- Ergebnisse erscheinen in Echtzeit
- Nach Abschluss: Statistik (z.B. "247 Dateien durchsucht, 12 Treffer")

### 2. Volltextsuche in Dateien

**Szenario:** Sie suchen nach einer bestimmten Funktion in allen Code-Dateien

**Schritte:**
1. **Suchbegriff:** z.B. `def calculate_total` eingeben
2. **Dateityp-Filter:** "Code" wählen
3. ☑️ **"In Dateien suchen"** aktivieren (wichtig!)
4. **Suchort:** Projekt-Verzeichnis wählen
5. **[SUCHE STARTEN]** klicken

**Ergebnis:**
- Es werden nur Dateien gezeigt, die den Text enthalten
- Der Suchbegriff wird im Report farblich hervorgehoben
- Zeilenummern zeigen exakte Position des Textes

### 3. Regex-Suche (Fortgeschrittene Benutzer)

**Szenario:** Sie suchen alle E-Mail-Adressen in Dateien

**Schritte:**
1. **Suchbegriff:** `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` eingeben
2. ☑️ **"Reguläre Ausdrücke"** aktivieren
3. ☑️ **"In Dateien suchen"** aktivieren
4. **Dateityp-Filter:** "Alle" (um alle Dateitypen zu durchsuchen)
5. **[SUCHE STARTEN]** klicken

**Beliebte Regex-Pattern:**
```regex
# E-Mail-Adressen
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

# Telefonnummern (German)
(\+49|0)[0-9]{2,4}[-\s]?[0-9]{3,9}

# Dateigrößen (bytes, KB, MB, GB)
\d+\s*(B|KB|MB|GB|TB)

# IP-Adressen
\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}

# URLs
https?://[^\s]+

# Dateigrößen im JSON
"size"\s*:\s*(\d+)
```

### 4. Groß- und Kleinschreibung

**Standardverhalten:** Suche ignoriert Groß/Kleinschreibung
- `test` findet: Test, TEST, tEsT

**Mit Aktivierung:** Berücksichtigung von Groß/Kleinschreibung
- `Test` findet nur: Test (nicht test oder TEST)

**Wann verwenden:**
- Code-Variablen: `myVariable` vs `myVariable`
- Dateinamen: `README` vs `readme`
- Konfigurationen: Oft case-sensitive!

---

## Suchtechniken

### Mehrere Suchbegriffe

Master Search unterstützt mehrere Suchbegriffe mit Leerzeichen trennen:

```
Suchbegriff: function main utils
```

Dies findet Dateien, die **alle** dieser Begriffe enthalten:
- ✅ `function main(utils)`
- ✅ `Utils class with main function`
- ❌ `function main` (fehlt "utils")

### Dateityp-Filter

Vordefinierte Kategorien:

| Filter | Dateitypen |
|--------|-----------|
| **Code** | `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.c#`, `.go`, `.rs` usw. |
| **Web** | `.html`, `.css`, `.php`, `.js`, `.vue`, `.jsx` usw. |
| **Daten** | `.json`, `.xml`, `.yaml`, `.csv`, `.sql`, `.db` usw. |
| **Dokumente** | `.pdf`, `.docx`, `.xlsx`, `.pptx`, `.md`, `.txt` usw. |
| **Konfiguration** | `.ini`, `.cfg`, `.conf`, `.env`, `.properties` usw. |
| **Archive** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` usw. |

### Suchort-Auswahl

**Schnelle Auswahl:**
- `C:\` - Ganze Festplatte
- `C:\Users\` - Nur Benutzerdateien
- `C:\Program Files\` - Nur Programme

**Custom Pfad:**
1. **[Durchsuchen...]** klicken
2. Gewünschtes Verzeichnis auswählen
3. **OK** bestätigen

**Tipps:**
- ⚡ Engere Verzeichnisse sind schneller
- 🔒 Systemordner (Windows, System32) sind oft schreibgeschützt
- 🚫 Netzwerk-Pfade können langsam sein

---

## HTML-Berichte

### Was sind HTML-Berichte?

Automatisch generierte Berichte mit:
- 📊 **Statistiken** - Anzahl Treffer, durchsuchte Dateien
- 📁 **Kategorien** - Übersicht nach Dateitypen
- ✨ **Animationen** - Professionelle Fade-In-Effekte
- 🔗 **Interaktive Links** - Dateien direkt öffnen
- 📋 **Clipboard-Funktion** - Pfade kopieren
- 🎨 **Responsive Design** - Funktioniert auf allen Geräten

### Report erstellen

**Automatisch bei Suche:**
1. ☑️ **"HTML-Report generieren"** aktivieren
2. Suche wie normal ausführen
3. Nach Abschluss: Report öffnet sich automatisch

**Speicherort:**
```
C:\Users\<YourUsername>\AppData\Local\Master Search\Reports\
  ├── search_results_20251112_153249.html
  ├── search_results_20251112_153418.html
  └── search_results_20251112_154523.html
```

### Report-Features

#### 📋 Clipboard-Kopieren
- Klicken Sie auf einen Dateipfad im Report
- Pfad wird automatisch in Zwischenablage kopiert
- Benachrichtigung bestätigt erfolgreiche Kopie

#### 📂 Ordner öffnen
- Klicken Sie auf das Ordner-Symbol neben einer Datei
- Öffnet den Ordner mit der Datei im Explorer

#### 🔍 Highlighting
Suchbegriffe werden farblich hervorgehoben:
- **Orange** - Gefundene Suchbegriffe
- **Zeile X** - Exakte Position im Text

#### 📊 Kategorie-Übersicht
Automatische Analyse:
```
📁 Dateitypen
┌─────────────────────┐
│ Python        145   │
│ JSON           89   │
│ Markdown       54   │
│ YAML           28   │
│ XML            12   │
└─────────────────────┘
```

#### ✨ Animationen
- Report lädt mit leerem Hintergrund
- Elemente faden sich nacheinander ein
- Professioneller, polierter Eindruck
- Keine Performance-Auswirkungen

---

## Einstellungen

### Sprachauswahl

Master Search erkennt automatisch Systemsprache:
- 🇩🇪 **Deutsch** - Windows auf Deutsch
- 🇬🇧 **English** - Windows auf Englisch
- 🇫🇷 **Français** - Windows auf Französisch

**Manuelle Auswahl:**
In vielen Masken auf "Sprache" klicken um zu wechseln.

### Performance-Einstellungen

**Standard-Einstellungen (optimal):**
- Multi-Processing aktiv
- Maximale CPU-Auslastung
- Schnellste Suche

**Für langsame PCs:**
- Hardware-Anforderungen senken
- Weniger Worker-Threads
- Längere Suche, aber stabiler

### Fehlerbehandlung

Master Search ignoriert automatisch:
- 🔒 **Schreibgeschützte Dateien** - Keine Berechtigung
- ⚠️ **Beschädigte Dateien** - Können nicht gelesen werden
- 🔁 **Symbole/Junctions** - Endlosschleifen vermeiden
- 🌐 **Netzwerk-Fehler** - Offline Laufwerke

---

## Tipps & Tricks

### ⚡ Schnellere Suchen

1. **Engere Verzeichnisse wählen**
   - Nicht `C:\` durchsuchen, sondern `C:\Projects\`
   - 10x schneller!

2. **Dateityp-Filter nutzen**
   - Statt "Alle Dateien" - nur "Code" oder "Dokumente"
   - Reduziert zu durchsuchende Dateien um 70%

3. **Spezifischere Suchbegriffe**
   - `function main` statt `main`
   - Weniger Treffer = schnellere Verarbeitung

### 🎯 Genauere Suchen

1. **Groß/Kleinschreibung aktivieren**
   - Wenn Sie exakte Übereinstimmung brauchen

2. **Regex für komplexe Pattern**
   - `^import.*os$` - Nur `import os` Zeilen
   - `def\s+\w+\(` - Alle Funktionsdefinitionen

3. **In Dateien suchen aktivieren**
   - Um Dateiinhalte statt nur Namen zu durchsuchen

### 📊 Report-Analyse

1. **Nach Dateitypen sortieren**
   - Kategorien im Report zeigen Verteilung
   - Nützlich für Projektstruktur-Analyse

2. **Mehrsprachige Suche**
   - Deutsch: `Ñame`, `Größe`
   - Englisch: `Name`, `Size`
   - Ein Report für alle!

3. **Trend-Analyse**
   - Speichern Sie mehrere Reports
   - Vergleichen Sie Dateimengen im Zeitverlauf

### 🛠️ Für Entwickler

**Python-Projekte durchsuchen:**
```
Suchbegriff: TODO
Filter: Code
In Dateien: ☑️
```

**Alle Imports finden:**
```
Suchbegriff: ^import
Regex: ☑️
Filter: Code
```

**Config-Dateien finden:**
```
Suchbegriff: api_key
Filter: Konfiguration
In Dateien: ☑️
```

---

## Häufig gestellte Fragen

### F: Wie lange dauert eine Suche?

**A:** Abhängig von:
- **Verzeichnisgröße:** 1000 Dateien ≈ 1 Sekunde
- **Suchort:** Lokale Festplatte vs. Netzwerk
- **Dateityp-Filter:** Mit Filter ist es schneller
- **In Dateien suchen:** Langsamer als nur Namen

**Beispiele:**
- `C:\Projects\` (10.000 Dateien): ~10 Sekunden
- `C:\` (500.000 Dateien): ~5 Minuten
- Mit Filter: 2-3x schneller

### F: Wo werden die Reports gespeichert?

**A:** 
```
Windows 7/8/10/11:
C:\Users\<YourUsername>\AppData\Local\Master Search\Reports\
```

**Ordner öffnen:**
1. GUI öffnen → Rechtsklick auf Report
2. "Ordner öffnen" klicken
3. Alle Reports sehen

### F: Kann ich die Suche abbrechen?

**A:** Ja! 
- Während Suche läuft: **[ABBRECHEN]** Button wird angezeigt
- Klick darauf stoppt sofort die Suche
- Bisherige Ergebnisse bleiben erhalten

### F: Was ist der Unterschied zwischen "In Dateien suchen" und normalem Filter?

**A:**
```
OHNE "In Dateien suchen":
  Sucht nur Dateinamen
  test.py ✅
  testing.txt ✅
  mytestfile.py ✅
  
MIT "In Dateien suchen":
  Sucht auch Dateiinhalte
  file_mit_test_im_inhalt.py ✅
  + alles von oben auch
```

### F: Unterstützt Master Search Wildcards?

**A:**
- **Normale Suche:** Nein (aber Sie können Regex nutzen)
- **Mit Regex:** Ja!
  - `test.*\.py` - test123.py, testfile.py, etc.
  - `\.log$` - Nur .log Dateien am Ende

### F: Kann ich Netzwerk-Laufwerke durchsuchen?

**A:** Ja, aber:
- ✅ SMB/CIFS Netzwerk-Freigaben funktionieren
- ⚠️ Kann langsam sein (Netzwerk-Latenz)
- 🔒 Benötigt Zugriffsberechtigung
- 💡 **Tipp:** Netzwerk-Laufwerk lokal "mounten" für bessere Performance

### F: Wie kann ich einen Report drucken?

**A:** 
1. Report im Browser öffnen
2. **Strg+P** drücken (oder Datei → Drucken)
3. Drucker wählen
4. ✓ Als PDF speichern auch möglich!

### F: Welche Dateitypen werden unterstützt?

**A:** 59+ Dateitypen:
- **Code:** Python, JavaScript, Java, C++, C#, Go, Rust, PHP, Ruby, etc.
- **Web:** HTML, CSS, SCSS, Vue, React, Angular, etc.
- **Daten:** JSON, XML, YAML, CSV, SQL, etc.
- **Dokumente:** PDF, DOCX, XLSX, PPTX, Markdown, TXT, etc.
- **Config:** INI, CONF, ENV, Properties, etc.
- **Archive:** ZIP, RAR, 7Z, TAR, GZ, etc.

Vollständige Liste: [SUPPORTED_FILE_TYPES.md](../SUPPORTED_FILE_TYPES.md)

### F: Brauche ich Internet für Master Search?

**A:** Nein!
- ✅ Vollständig offline funktionsfähig
- ✅ Keine Daten-Übertragung
- ✅ Datenschutz gewährleistet
- ℹ️ Browser-Update der HTML-Reports ist optional

---

## Fehlerbehebung

### Problem: Suche ist sehr langsam

**Lösungen:**
1. Engeres Verzeichnis wählen
   - Statt `C:\` → `C:\Projects\`
2. Dateityp-Filter nutzen
   - Statt "Alle" → "Code"
3. "In Dateien suchen" deaktivieren
   - Wenn Sie nur Dateinamen brauchen
4. Spezifischere Suchbegriffe
   - `main.py` statt `main`

### Problem: "Zugriff verweigert" Fehler

**Ursachen & Lösungen:**
1. Administratorrechte erforderlich
   - GUI mit Rechtsklick → "Als Administrator ausführen"
2. Datei wird gerade verwendet
   - Andere Programme schließen
3. Antivirus blockiert Zugriff
   - Master Search zur Whitelist hinzufügen

### Problem: Report öffnet sich nicht

**Lösungen:**
1. Browser-Einstellungen prüfen
   - Lokale Dateien öffnen zulassen?
2. Popup-Blocker deaktivieren
   - Report wird in neuem Tab geöffnet
3. Default-Browser umschalten
   - Unter Windows-Einstellungen ändern
4. HTML-Datei manuell öffnen
   - Reports-Ordner öffnen, HTML-Datei doppelklicken

### Problem: Bestimmte Dateitypen werden ignoriert

**Ursachen:**
1. Dateityp-Filter ist zu restriktiv
   - Auf "Alle" einstellen
2. Dateiendung ist nicht in Whitelist
   - Technische Details: siehe SUPPORTED_FILE_TYPES.md

### Problem: Regex funktioniert nicht

**Häufige Fehler:**
1. Regex-Option nicht aktiviert
   - ☑️ "Reguläre Ausdrücke" Checkbox
2. Syntax-Fehler in Regex
   - Zu viele `(` ohne Schließung
   - Ungültige Escape-Sequenzen
3. Pattern-Variationen
   - `\d` nur in Raw-Strings ✅
   - `\\d` (doppelter Backslash) auch möglich

**Test-Tools:**
- [regex101.com](https://regex101.com) - Online Regex-Tester
- Dort Pattern testen bevor Sie in Master Search eingeben

### Problem: Master Search antwortet nicht

**Lösungen:**
1. Suche abbrechen
   - [ABBRECHEN] Button klicken
2. Mit Strg+Z Fenster schließen
3. Neu starten
   - Sollte normalerweise 1-2 Sekunden dauern

---

## Erweiterte Themen

### Befehlszeilen-Interface (CLI)

Master Search kann auch über Kommandozeile verwendet werden:

```powershell
# Grundlegende Suche
python cli_main.py --search test --path C:\Projects

# Mit Optionen
python cli_main.py --search main --path C:\src --in-files --regex

# Report generieren
python cli_main.py --search TODO --path . --report

# Alle Optionen
python cli_main.py --help
```

### Integration mit anderen Tools

**Beispiel: PowerShell-Pipeline**
```powershell
# Suche + Report-Verarbeitung
master_search.exe --search error --path C:\Logs | Process-SearchResults
```

**Beispiel: Windows-Scheduler**
```
Scheduled Task → Master Search → täglich um 22:00 Uhr
Report wird automatisch generiert und emailed
```

---

## Support & Kontakt

**Probleme gefunden?**
- 📧 Email: info@loony-tech.de
- 🐛 Bug Report: [GitHub Issues](https://github.com/Loony2392/master-search)
- 💬 Fragen: Community Forum (coming soon)

**Version Information:**
- **Aktuelle Version:** 2025.11.7
- **Letztes Update:** November 12, 2025
- **Autor:** Loony2392
- **Lizenz:** Proprietär

---

## Lizenz & Rechtliches

Master Search™ - Professional File Search Tool
© 2025 Loony2392 & LOONY-TECH. Alle Rechte vorbehalten.

**Datenschutz:**
- ✅ Keine Daten-Sammlung
- ✅ Keine Telemetrie
- ✅ Vollständig offline
- ✅ Lokale Verarbeitung nur

---

**Viel Erfolg bei der Suche! 🚀**

*Master Search - Professionelle Dateisuche mit schönen Berichten*
