# 🔄 Update Notifier Integration Guide

## Wie du das Update-System in deine App einbindest

### 1️⃣ **Einfachste Variante - Console Output**

In deiner `gui_search_tool.py` (beim Start):

```python
from update_notifier import check_and_show_update

class MainWindow:
    def __init__(self, root):
        self.root = root
        # ... dein GUI-Code ...
        
        # Prüfe auf Updates beim Start (einmalig)
        check_and_show_update()
```

**Output:**
```
======================================================================
🎉 MASTER SEARCH - WILLKOMMEN ZUM UPDATE!
======================================================================

✅ Version 2025.11.0 ist jetzt installiert!

📝 ÄNDERUNGEN IN DIESER VERSION:

✨ Neu:
  • Windows Standard-App Integration für HTML-Reports
  • Erweiterte HTML-Report-Funktionalität
  • Umfassende Test-Suite (63+ Tests)

🔧 Verbessert:
  • Performance-Optimierungen (Multiprocessing)
  • Code-Qualität (Linting, Formatting)
  
🔒 Sicherheit:
  • Security Audit durchgeführt

======================================================================
💡 Tipp: Weitere Details findest du in CHANGELOG.md
======================================================================
```

---

### 2️⃣ **GUI Dialog Variante** (Empfohlen)

Wenn du einen GUI-Dialog mit einem Fenster möchtest:

```python
from update_notifier import check_and_show_update

class MainWindow:
    def __init__(self, root):
        self.root = root
        # ... dein GUI-Code ...
        
        # Prüfe auf Updates mit GUI Dialog
        check_and_show_update(self.root)
```

**Output:**
```
┌─────────────────────────────────────────────────────────────────┐
│  Master Search Update                              [_][=][X]     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Master Search v2025.11.0                                       │
│                                                                  │
│  ✅ Neues Update installiert!                                   │
│                                                                  │
│  📝 Was ist neu:                                                │
│                                                                  │
│  ✨ Neu:                                                         │
│    • Windows Standard-App Integration                            │
│    • Erweiterte HTML-Report-Funktionalität                      │
│    • Umfassende Test-Suite (63+ Tests)                          │
│                                                                  │
│  🔧 Verbessert:                                                 │
│    • Performance-Optimierungen (Multiprocessing)               │
│    • Code-Qualität (Linting, Formatting)                        │
│                                                                  │
│  ==================================================              │
│  Weitere Details in CHANGELOG.md                                │
│                                                                  │
│                                    [OK]                          │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3️⃣ **Manuelle Kontrolle**

Wenn du die Notification manuell kontrollieren willst:

```python
from update_notifier import UpdateNotifier

def check_updates():
    notifier = UpdateNotifier()
    
    # Prüfe ob Update gezeigt werden soll
    if notifier.should_show_update_notification():
        print(f"📢 Update erkannt: {notifier.current_version}")
        notifier.show_update_notification()
    else:
        print("✅ Keine neuen Updates")
```

---

## 📋 Wie es funktioniert

### **Ablauf:**

1. **Erste Installation** → Keine Notification (neue Version wird gespeichert)
2. **Nächster Start gleiche Version** → Keine Notification (schon gesehen)
3. **Update eingespielt (neue Version)** → **NOTIFICATION GEZEIGT!** (einmalig)
4. **Nächster Start** → Keine Notification (schon gesehen)

### **Speicherort:**

```
C:\Users\[USERNAME]\.master_search\
├── last_version.json
```

**Inhalt (Beispiel):**
```json
{
  "version": "2025.11.0",
  "last_updated": "C:\\Users\\b.kolb\\..."
}
```

---

## 🔧 Was wird automatisch gelesen?

Das System liest **automatisch** aus `CHANGELOG.md`:

```markdown
## [2025.11.0] - 12. November 2025

### ✨ Neu
- ...

### 🔧 Verbessert
- ...

### 🔒 Sicherheit
- ...
```

**→ Extrahiert automatisch alle Punkte und zeigt sie!**

---

## 💡 Tipps & Tricks

### **Nur einmalig beim Start prüfen:**
```python
# In __main__ oder beim GUI-Start
if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    
    # Update Notification (einmalig, da sofort nach Start)
    check_and_show_update(root)
    
    root.mainloop()
```

### **Update-Verlauf manuell zurücksetzen:**
```python
from pathlib import Path
import json

config_dir = Path.home() / ".master_search"
version_file = config_dir / "last_version.json"

# Löschen (nächster Start zeigt Notification wieder)
version_file.unlink(missing_ok=True)
```

### **Für Testing die Version temporär ändern:**
```python
from update_notifier import UpdateNotifier

# Test mit alter Version
notifier = UpdateNotifier(current_version="2.0.0")
notifier.show_update_notification()
```

---

## 🎨 Anpassungen

### **Andere Kategorien hinzufügen:**

In `update_notifier.py` → `get_changelog_summary()`:

```python
categories = {
    '✨ Neu': r"### ✨ Neu\n(.*?)(?=### |\Z)",
    '🔧 Verbessert': r"### 🔧 Verbessert\n(.*?)(?=### |\Z)",
    # Hier neue Kategorien hinzufügen:
    '🎯 Ziele': r"### 🎯 Ziele\n(.*?)(?=### |\Z)",
}
```

### **Max Items ändern:**

```python
# Standard: 10 Items pro Kategorie
check_and_show_update()  # 10 Items

# Nur 5 Items zeigen
notifier = UpdateNotifier()
summary = notifier.get_changelog_summary(
    notifier.current_version, 
    max_items=5  # Hier ändern
)
```

---

## ✅ Fertig!

Das ist alles was du brauchst. Die Integration ist sehr einfach:

```python
# 1 Zeile Code
from update_notifier import check_and_show_update
check_and_show_update()  # Das ist alles!
```

**Dann:**
- ✅ Liest CHANGELOG.md automatisch
- ✅ Zeigt Update nur einmalig
- ✅ Speichert gesehene Version
- ✅ Funktioniert Console + GUI
- ✅ Keine Nerv-Popups bei jedem Start

🚀 **Perfekt für Production!**
