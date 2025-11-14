# Master Search MSI Installer - Shortcuts & Installation

## ✅ Automatisch erstellte Verknüpfungen

Wenn Sie den MSI-Installer installieren, werden folgende Verknüpfungen **automatisch** erstellt:

### 1. **Start-Menü Verknüpfungen** (Always Created)
   - `Start Menü → Master Search → Master_Search.exe`
   - Location: `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Master Search\`

### 2. **Desktop Verknüpfungen** (Optional, kann during installation gewählt werden)
   - Optional: `Master Search` auf dem Desktop
   - Diese können während der Installation aktiviert werden

### 3. **Add/Remove Programs Eintrag**
   - Control Panel → Programs and Features → Master Search
   - Erlaubt einfaches Deinstallieren

### 4. **PATH-Umgebungsvariable**
   - Master Search wird zu PATH hinzugefügt
   - Ermöglicht CLI-Nutzung von überall aus

---

## 🔧 Installation durchführen

### Normale Installation (GUI):
```powershell
msiexec /i "Master_Search-2025.11.20-win64.msi"
```

### Silent Installation (ohne Dialog):
```powershell
msiexec /i "Master_Search-2025.11.20-win64.msi" /quiet
```

### Installation mit Log:
```powershell
msiexec /i "Master_Search-2025.11.20-win64.msi" /l*v install.log
```

---

## 📍 Nach der Installation zu finden:

| Ort | Was | Pfad |
|-----|-----|------|
| Start-Menü | Master Search | `%AppData%\Microsoft\Windows\Start Menu\Programs\Master Search\` |
| Programme | Master_Search.exe | `C:\Program Files\Master Search\` |
| Add/Remove | Master Search v2025.11.20 | Control Panel → Programs |
| PATH | Kommandozeile | `C:\Program Files\Master Search\` |

---

## 🗑️ Deinstallation

### Über Control Panel:
1. Control Panel → Programs and Features
2. Suchen Sie "Master Search"
3. Klicken Sie auf "Uninstall"

### Über Kommandozeile:
```powershell
msiexec /x "Master_Search-2025.11.20-win64.msi"
```

### Silent Uninstall:
```powershell
msiexec /x "Master_Search-2025.11.20-win64.msi" /quiet
```

---

## ℹ️ Technische Details

- **Installer Type**: Windows MSI (cx_Freeze)
- **Architektur**: 64-bit (win64)
- **Installation Pfad**: `C:\Program Files\Master Search\`
- **Upgrade Code**: `{3F692526-948B-4B39-BF5F-1C3FD99FC7F4}`
- **Größe**: ~6.3 MB

---

## ✓ Verifikation nach Installation

Nach der Installation können Sie verifizieren, dass alles funktioniert:

```powershell
# GUI starten
& "C:\Program Files\Master Search\Master_Search.exe"

# CLI testen (falls PATH aktualisiert wurde)
MasterSearch_CLI.exe --help

# Oder mit vollständigem Pfad
& "C:\Program Files\Master Search\MasterSearch_CLI.exe" --help
```

---

**Version**: 2025.11.20
**Company**: LOONY-TECH
**Support**: https://github.com/Loony2392/master-search
