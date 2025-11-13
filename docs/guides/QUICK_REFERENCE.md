# Master Search - Quick Reference Guide

## What's New in This Update

### ✅ 1. Settings Are Now Saved Automatically
- **What:** Your search path, worker count, and other preferences are saved
- **Where:** `C:\Users\YourName\.master_search\settings.json`
- **How:** Settings save automatically when you close the app
- **Example:** Change to 8 workers → Close app → Open app → Still shows 8 workers ✓

### ✅ 2. Update Notifications Show as a Modal Dialog
- **What:** A professional dialog appears when there's a new version
- **How:** Dialog shows changes and you can choose "Don't show again"
- **Location:** Pops up centered on your main window
- **Version Tracking:** `C:\Users\YourName\.master_search\last_version.json`

### ✅ 3. Default is Now 4 CPU Cores
- **Old:** 0 or 16 cores
- **New:** 4 cores (balanced for most computers)
- **Can Change:** Use the spinbox in the GUI to adjust

### ✅ 4. French Language Added
- **Languages:** English, Deutsch (German), Français (French)
- **Auto-Detect:** Uses your system language preference
- **Manual Selection:** Choose in the language dialog on first run

---

## File Locations (Important)

### Settings Directory
```
C:\Users\<YourUsername>\.master_search\
├── settings.json           ← Your saved preferences
├── last_version.json       ← Which version you last saw
└── language.json           ← Your language choice
```

### Config Files (App Directory)
```
Master Search/
├── locales/
│   ├── de.json            ← German translations
│   ├── en.json            ← English translations
│   └── fr.json            ← French translations (NEW)
├── CHANGELOG.md           ← Shows in update dialog
├── version.py             ← Current version number
└── settings_manager.py    ← Settings handling (NEW)
```

---

## Troubleshooting

### Problem: Settings not saving
**Solution:** Make sure you close the app normally (click X button)
**Check:** Does `C:\Users\<YourName>\.master_search\settings.json` exist?

### Problem: Update notification doesn't appear
**Solution:** Delete `C:\Users\<YourName>\.master_search\last_version.json`
**Restart:** App will check for updates again

### Problem: Wrong language appears
**Solution:** Delete `C:\Users\<YourName>\.master_search\language.json`
**Restart:** Language selection dialog will appear again

### Problem: Settings show defaults instead of my preferences
**Solution:** Check if `settings.json` is being created in the right folder:
```
C:\Users\<YourName>\.master_search\settings.json
```

---

## How to Manually Edit Settings

If needed, you can edit `settings.json` directly:

```json
{
  "search_path": "C:\\Users\\b.kolb\\Documents",
  "max_workers": 4,
  "search_mode": "AND",
  "case_sensitive": false,
  "use_regex": false,
  "include_content": true,
  "file_pattern": "*",
  "window_width": 900,
  "window_height": 700
}
```

**Valid values:**
- `max_workers`: 1-16 (number of CPU cores)
- `search_mode`: "AND" or "OR"
- `case_sensitive`: true or false
- `use_regex`: true or false
- `include_content`: true or false
- `file_pattern`: "*" or "*.txt" or "*.py" etc.

---

## Developer Notes

### Testing Settings Persistence
1. Start the app
2. Change search path and worker count
3. Close the app (normal close, not force kill)
4. Check `settings.json` file created
5. Restart app - settings should be restored

### Testing Update Notification
1. Delete `~/.master_search/last_version.json`
2. Start the app
3. Modal dialog should appear with changelog
4. Check "Don't show again" checkbox
5. Click OK
6. Restart app - dialog should not appear

### Adding New Settings
1. Add to `DEFAULT_SETTINGS` dict in `settings_manager.py`
2. Add to `save_settings()` method in `gui_search_tool.py`
3. Add to `setup_variables()` method to load on startup

---

## Version Information
- **Current Version:** 2025.11.1
- **Release Date:** November 2025
- **Developer:** Loony2392
- **Config Directory:** `~/.master_search/`

---

## Key Files Changed
- ✏️ `gui_search_tool.py` - Added settings load/save
- ✏️ `update_notifier.py` - New modal dialog with checkbox
- ✏️ `gui_main.py` - Calls update notifier on startup
- ✏️ `language_config.py` - French language support
- ✏️ `performance_config.py` - Default 4 cores
- ✏️ `i18n.py` - Dynamic version replacement
- ✏️ `locales/*.json` - Version placeholder & French
- 🆕 `settings_manager.py` - NEW: Settings persistence
- 🆕 `locales/fr.json` - NEW: French translations

---

## Contact & Support
- **Developer:** Loony2392
- **Email:** info@loony-tech.de
- **Company:** LOONY-TECH
