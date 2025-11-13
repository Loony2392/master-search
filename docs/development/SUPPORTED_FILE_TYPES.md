# Unterstützte Dateitypen - Master Search

## Übersicht

Master Search unterstützt **48 verschiedene Dateitypen** aus verschiedenen Kategorien. Die Dateitypen sind logisch organisiert und abgedecken alle gängigen Formate für Textdateien, Konfigurationen und Dokumente.

## 📊 Statistik

| Kategorie | Anzahl | Dateitypen |
|-----------|--------|-----------|
| Web & Markup | 4 | HTML, XML, JSON, etc. |
| Scripting & Programming | 17 | Python, JavaScript, TypeScript, Java, etc. |
| Styling | 4 | CSS, SCSS, SASS, LESS |
| Data & Configuration | 8 | CSV, YAML, TOML, SQL, INI, etc. |
| Documentation | 3 | TXT, Markdown, reStructuredText |
| Office Documents | 7 | Word, Excel, PowerShell, PDF, etc. |
| Sonstiges | 5 | Vue, Svelte, Log, Properties, etc. |
| **GESAMT** | **48** | - |

---

## 🔍 Detaillierte Liste

### 📁 Web & Markup (4 Dateitypen)
Für Web-Entwicklung und Datenformate:

| Dateityp | Beschreibung | Beispiel |
|----------|-------------|----------|
| `.html` | HyperText Markup Language | `index.html` |
| `.htm` | HyperText Markup Language (alt) | `page.htm` |
| `.xml` | Extensible Markup Language | `config.xml` |
| `.json` | JavaScript Object Notation | `data.json` |

---

### 🔤 Scripting & Programming (17 Dateitypen)
Für Programmiersprachen und Skripte:

| Dateityp | Sprache | Beispiel |
|----------|---------|----------|
| `.py` | Python | `script.py` |
| `.js` | JavaScript | `app.js` |
| `.jsx` | React JSX | `Component.jsx` |
| `.ts` | TypeScript | `types.ts` |
| `.tsx` | React TypeScript | `Component.tsx` |
| `.java` | Java | `Main.java` |
| `.cpp` | C++ | `program.cpp` |
| `.c` | C | `main.c` |
| `.h` | C/C++ Header | `header.h` |
| `.cs` | C# / CSharp | `Program.cs` |
| `.php` | PHP | `index.php` |
| `.rb` | Ruby | `script.rb` |
| `.go` | Go/Golang | `main.go` |
| `.rs` | Rust | `main.rs` |
| `.sh` | Bash Shell | `script.sh` |
| `.ps1` | PowerShell | `script.ps1` |
| `.bat` | Windows Batch | `run.bat` |

---

### 🎨 Styling (4 Dateitypen)
Für CSS und CSS-Präprozessoren:

| Dateityp | Beschreibung | Beispiel |
|----------|-------------|----------|
| `.css` | Cascading Style Sheets | `style.css` |
| `.scss` | SCSS (Sass Syntax) | `style.scss` |
| `.sass` | SASS (Indented Syntax) | `style.sass` |
| `.less` | LESS CSS | `style.less` |

---

### 📊 Data & Configuration (8 Dateitypen)
Für Konfigurationen und Datenformate:

| Dateityp | Beschreibung | Beispiel |
|----------|-------------|----------|
| `.csv` | Comma-Separated Values | `data.csv` |
| `.yml` | YAML Markup Language | `config.yml` |
| `.yaml` | YAML (verbose) | `config.yaml` |
| `.toml` | TOML Configuration | `config.toml` |
| `.ini` | INI Configuration | `settings.ini` |
| `.cfg` | Configuration File | `app.cfg` |
| `.conf` | Configuration File | `nginx.conf` |
| `.sql` | SQL Database | `query.sql` |

---

### 📝 Documentation (3 Dateitypen)
Für Dokumentation und Textdateien:

| Dateityp | Beschreibung | Beispiel |
|----------|-------------|----------|
| `.txt` | Plain Text | `README.txt` |
| `.md` | Markdown | `README.md` |
| `.rst` | reStructuredText | `index.rst` |

---

### 📄 Office Documents (7 Dateitypen)
Für Büro- und Dokumentenformate:

| Dateityp | Beschreibung | Beispiel |
|----------|-------------|----------|
| `.doc` | Microsoft Word (alt) | `document.doc` |
| `.docx` | Microsoft Word | `document.docx` |
| `.pdf` | Portable Document Format | `file.pdf` |
| `.xlsx` | Microsoft Excel | `spreadsheet.xlsx` |
| `.pptx` | Microsoft PowerPoint | `presentation.pptx` |
| `.odt` | OpenDocument Text | `document.odt` |
| `.rtf` | Rich Text Format | `document.rtf` |

---

### ⭐ Sonstiges (5 Dateitypen)
Für weitere Dateitypen:

| Dateityp | Beschreibung | Beispiel |
|----------|-------------|----------|
| `.log` | Log-Dateien | `app.log` |
| `.edcx` | EDCX-Spezialformat | `data.edcx` |
| `.vue` | Vue.js Component | `App.vue` |
| `.svelte` | Svelte Component | `Component.svelte` |
| `.properties` | Java Properties | `app.properties` |

---

## 🚀 Verwendung

### Alle Dateitypen durchsuchen
```bash
python cli_main.py -p C:\path\to\search -t "Suchtext"
```

### Nur bestimmte Dateitypen
```bash
# Nur Python-Dateien
python cli_main.py -p . -t "import" --pattern "*.py"

# Nur Konfigurationen
python cli_main.py -p . -t "database" --pattern "*.yml|*.yaml|*.ini|*.conf"

# Nur Dokumentation
python cli_main.py -p . -t "TODO" --pattern "*.md|*.txt|*.rst"
```

### GUI verwenden
```bash
python gui_main.py
```
Dann im GUI die gewünschten Dateitypen auswählen.

---

## 🔧 Konfiguration

### Neue Dateitypen hinzufügen

Editieren Sie `file_search_tool.py` und fügen Sie in der `supported_text_extensions`-Liste neue Einträge hinzu:

```python
self.supported_text_extensions = {
    # Bestehende Kategorien...
    # Neue Kategorie
    '.myformat',  # Mein spezielles Format
}
```

### Dateitypen aus Suche ausschließen

Modifizieren Sie die `supported_text_extensions`-Menge und entfernen Sie unerwünschte Typen:

```python
# Ein Dateityp entfernen:
self.supported_text_extensions.discard('.xml')

# Oder beim Initialisieren:
self.supported_text_extensions = self.supported_text_extensions - {'.pdf', '.doc'}
```

---

## 📋 Kompatibilität

### ✅ Vollständig unterstützt
- Alle Dateitypen können durchsucht werden
- Intelligente Encoding-Erkennung
- Unicode/UTF-8 Support
- Multi-Byte-Zeichen (CJK) unterstützt

### ⚠️ Einschränkungen
- **Binärdateien:** Werden automatisch übersprungen
- **Große Dateien:** >50MB werden aus Performance-Gründen übersprungen
- **PDF:** Text-Extraction nur mit zusätzlichen Bibliotheken
- **Office Docs:** Content-Suche erfordert zusätzliche Tools

### 🛠️ Erweiterbarkeit
Alle Dateitypen können durch Subklassing von `FileSearchTool` angepasst werden:

```python
class CustomFileSearchTool(FileSearchTool):
    def __init__(self):
        super().__init__()
        # Neue Typen hinzufügen
        self.supported_text_extensions.add('.custom')
```

---

## 📚 Weitere Ressourcen

- `file_search_tool.py` - Hauptimplementierung
- `check_extensions.py` - Überprüfungsskript für alle Dateitypen
- `FILE_TYPES_UPDATE.md` - History und Änderungen
- `FEATURE_MATRIX.md` - Feature-Übersicht nach Dateityp

---

## 📞 Support

Wenn Sie einen speziellen Dateityp benötigen, erstellen Sie bitte ein Issue oder kontaktieren Sie:
- **Email:** info@loony-tech.de
- **GitHub:** https://github.com/Loony2392/master-search

---

**Letzte Aktualisierung:** November 12, 2025  
**Version:** 2025.11.1
