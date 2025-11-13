# GitHub Workflows Documentation

## Übersicht

Dieses Projekt verwendet GitHub Actions für automatisierte Tests und Release-Management.

## 🧪 Test Workflow (test.yml)

**Auslöser:**
- Push zu `main` oder `develop` Branch
- Pull Requests zu `main` oder `develop`

**Was wird geprüft:**
- ✅ Python Syntax Validierung (py_compile)
- ✅ Linting mit pylint (Mindestpunkte: 7.0)
- ✅ Unit Tests mit pytest und Coverage
- ✅ Version Konsistenz (version.py)
- ✅ Cross-platform Testing (Ubuntu, Windows, macOS)
- ✅ Python 3.9, 3.10, 3.11 Kompatibilität

**Status Badge:**
```markdown
![Tests](https://github.com/[user]/Master-Search/actions/workflows/test.yml/badge.svg)
```

## 🚀 Release Workflow (release.yml)

### Automatischer Release (Tag-basiert)

**Auslöser:** Neuer Git Tag mit Format `v*` (z.B. `v1.0.0`)

```bash
git tag v1.0.0
git push origin v1.0.0
```

**Was passiert:**
1. Windows-Umgebung wird vorbereitet
2. Abhängigkeiten installiert (inkl. cx_Freeze)
3. MSI-Installer wird mit `build_msi.py` gebaut
4. GitHub Release wird erstellt
5. MSI-Datei wird als Release Asset hochgeladen
6. Artifact wird 30 Tage aufbewahrt

### Manueller Release (Workflow Dispatch)

**Auslöser:** Manual über GitHub UI

1. Gehe zu "Actions" Tab
2. Wähle "Build & Release"
3. Klicke "Run workflow"
4. Gib Version ein (z.B. `1.0.0`)
5. Klicke "Run workflow"

**Version wird automatisch:**
- In `version.py` aktualisiert
- Im MSI-Dateinamen verwendet
- Als Release-Tag verwendet

## 📋 Versionsverwaltung

Die Workflows verwenden `version.py` als zentrale Versionsverwaltung:

```python
# version.py
VERSION = "1.0.0"
AUTHOR = "Loony2392"
EMAIL = "info@loony-tech.de"
```

**Eine Stelle für alle:**
- MSI-Installer Version
- CLI-Output
- GUI-Info
- Release-Nummern

## ✨ Workflow Features

### Test Workflow Features:
- 🔄 Multi-Platform Testing (Windows, Linux, macOS)
- 🐍 Multi-Version Testing (Python 3.9, 3.10, 3.11)
- 📊 Coverage Reports (Code Coverage Tracking)
- 🔍 Linting & Quality Checks
- 📦 Dependency Validation

### Release Workflow Features:
- 🏗️ Automatischer Build-Prozess
- 📝 Release Notes Generation
- 📦 MSI-Artifact Upload
- 🔄 Version Auto-Update (Manual)
- ⏱️ 30-Tage Artifact Retention

## 🔧 Konfiguration

### Requirements.txt
Stelle sicher, dass `requirements.txt` alle Abhängigkeiten enthält:

```
# requirements.txt
cx_Freeze>=6.15.0
```

### Branches
Standard-Branches für Workflows:
- `main` - Production
- `develop` - Development

Ändere diese in den Workflow-Dateien falls nötig.

## 📊 Workflow Status

Status deiner Workflows anzeigen:

```markdown
| Workflow | Status |
|----------|--------|
| Test & Quality Check | ![Tests](https://github.com/[USER]/Master-Search/actions/workflows/test.yml/badge.svg) |
| Build & Release | ![Release](https://github.com/[USER]/Master-Search/actions/workflows/release.yml/badge.svg) |
```

## 🐛 Troubleshooting

### MSI nicht gefunden
- Überprüfe `build_msi.py` - Output-Pfad muss `build/` sein
- Logs in Workflow ansehen

### Version-Mismatch
- Stelle sicher, dass `version.py` korrekt ist
- Für manuellen Release: Gib korrekte Version ein

### Python-Version Problem
- Mindestanforderung: Python 3.9+
- Recommended: Python 3.11+

## 📝 Release Beispiel

### Vorbereitung:
```bash
# Version in version.py updaten
# ODER manuell im Workflow eingeben

# Tag erstellen
git tag v1.1.0
git push origin v1.1.0
```

### Ergebnis:
- ✅ GitHub Release erstellt
- ✅ MSI-Datei herunterladbar
- ✅ Release Notes auto-generiert
- ✅ Artifact für 30 Tage verfügbar

## 🔐 Secrets & Permissions

Erforderliche Permissions:
- `contents: write` - Release erstellen
- `actions: read` - Workflow Status

`GITHUB_TOKEN` wird automatisch bereitgestellt.

## 📚 Weitere Ressourcen

- [GitHub Actions Dokumentation](https://docs.github.com/en/actions)
- [cx_Freeze Dokumentation](https://cx-freeze.readthedocs.io)
- [pytest Dokumentation](https://docs.pytest.org)
