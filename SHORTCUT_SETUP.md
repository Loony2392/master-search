# Master Search - Shortcut Installation Guide

## 🚀 Quick Start

Nach der MSI-Installation müssen Shortcuts manuell erstellt werden:

### **Option 1: Batch-Datei (Einfach)**
```
Double-click auf: Create_Shortcuts.bat
```

### **Option 2: Python-Skript**
```powershell
python scripts/create_shortcuts.py
```

### **Option 3: PowerShell (Mit Admin-Rechten)**
```powershell
python scripts/create_shortcuts.py
```

---

## 📋 Installation Schritt für Schritt

### 1️⃣ **Installieren**
```powershell
msiexec /i "Master_Search-2025.11.22-win64.msi"
```

### 2️⃣ **Shortcuts erstellen**
```powershell
# Wechsel in das Installationsverzeichnis
cd "C:\Program Files\Master Search"

# Oder von der Download-Lokation
python scripts/create_shortcuts.py
```

### 3️⃣ **Fertig!**
- ✅ Start-Menü: "Master Search" & "Master Search CLI"
- ✅ Desktop: "Master Search" Verknüpfung
- ✅ PATH aktualisiert

---

## 📍 Wo finde ich die Shortcuts?

| Ort | Datei |
|-----|-------|
| **Start-Menü** | `Start → Master Search` |
| **Desktop** | `Master Search.lnk` |
| **Programmverzeichnis** | `C:\Program Files\Master Search\` |

---

## 🔧 Vollautomatische Installation (Skript)

Erstelle `install_all.ps1`:

```powershell
# install_all.ps1 - Vollautomatische Installation

$msiFile = "Master_Search-2025.11.22-win64.msi"

# 1. MSI installieren
Write-Host "📦 Installiere Master Search..."
msiexec /i $msiFile /qn /norestart

# Warten
Start-Sleep -Seconds 5

# 2. Shortcuts erstellen
Write-Host "🔗 Erstelle Shortcuts..."
python scripts/create_shortcuts.py

Write-Host "✅ Installation abgeschlossen!"
```

Starten mit:
```powershell
.\install_all.ps1
```

---

## 🗑️ Deinstallation

### Nur Shortcuts entfernen:
```powershell
python scripts/create_shortcuts.py --remove
```

### Komplette Deinstallation:
```powershell
msiexec /x "Master_Search-2025.11.22-win64.msi"
```

---

## 🆘 Troubleshooting

### Shortcuts wurden nicht erstellt?

**Problem**: "access denied" oder "permission denied"
```powershell
# Mit Administrator-Rechten ausführen
python scripts/create_shortcuts.py
```

**Problem**: "Python nicht gefunden"
```powershell
# Vollständigen Python-Pfad verwenden
"C:\Program Files\Master Search\python.exe" scripts/create_shortcuts.py
```

**Problem**: Die EXE-Dateien sind nicht vorhanden
```powershell
# Prüfe, ob Master Search richtig installiert ist
dir "C:\Program Files\Master Search"
```

---

## ℹ️ Details

- **Installer Type**: Windows MSI
- **Architektur**: 64-bit
- **Installation Pfad**: `C:\Program Files\Master Search\`
- **MSI Größe**: 6,3 MB

---

**Version**: 2025.11.22  
**Company**: LOONY-TECH  
**Repository**: https://github.com/Loony2392/master-search
