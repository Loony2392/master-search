# Release Notes - Master Search v2025.11.13

**Release Date**: 13 November 2025  
**Version**: 2025.11.13  
**Status**: ✅ Production Ready

---

## 🎉 What's New

### ✨ Major Improvements

#### 1. **Complete Root Directory Cleanup**
- Removed duplicate `file_search_tool.py` from root directory
- All core modules now properly consolidated in `src/` folder
- Eliminated technical debt and namespace confusion

#### 2. **PyInstaller Migration Completed**
- Successfully migrated from cx_Freeze (which had OneDrive path issues)
- Clean, standalone executables without DLL path conflicts
- Updated all build dependencies in `requirements-dev.txt`

#### 3. **Enhanced Build System**
- Unified `build.py` launcher for all targets
- Support for both GUI and CLI executable generation
- Clean separation of concerns with spec files in `scripts/`

### 🎨 UI Enhancements

#### GUI Features
- ✅ Colorful emoji icons throughout the interface
- ✅ Professional button labels with visual indicators
- ✅ Enhanced stats display showing excluded files count
- ✅ Proper Release Notes display on startup

### 🌍 Complete Localization

All three languages fully supported with complete key coverage:

- **German (Deutsch)** - de.json
- **English** - en.json  
- **French (Français)** - fr.json

#### Translation Keys Added
- Button labels: `🚀 Suche starten`, `🛑 Stopp`, `📊 Report anzeigen`, etc.
- Report display: Professional search report with all metadata
- Stats labels: Files found, folders found, matches, execution time
- Options with emoji: `✅ UND`, `⭐ ODER`, `🔎 Dateiinhalt`, `⚙️ Regex`

### 🔧 Bug Fixes

#### Category Filter System - Critical Fixes
1. **Fixed Unknown File Type Logic**
   - Unknown file types now properly excluded instead of always included
   - Impact: Prevents unwanted files from appearing in results

2. **Fixed Filter Field Name Bug**
   - Corrected field name from `file_path` to `path` in filter check
   - Impact: Filters now work correctly with actual result structure

3. **Fixed Category Defaults**
   - Added all category defaults to `DEFAULT_SETTINGS`
   - All categories now default to `True` (enabled)
   - Impact: Sensible defaults on first launch

4. **Fixed .txt File Classification**
   - Moved `.txt` files from "logs" category to "web" category
   - Proper categorization based on file purpose
   - Impact: More intuitive categorization

#### Stats Display
- ✅ Filtered stats display accuracy improved
- ✅ Excluded files counter now properly displayed
- ✅ Stats reset on new search for clean state

#### Release Notes Display
- ✅ Fixed condition from `VERSION > last_version` to `VERSION != last_version`
- ✅ Release Notes now display correctly on first run
- ✅ Proper version tracking implementation

### 📦 Executables

Both production-ready executables generated:

```
dist/MasterSearch.exe        13.94 MB  [GUI Application]
dist/MasterSearchCLI.exe     13.9 MB   [Command Line Interface]
```

**Build Date**: 13 November 2025 17:10  
**Build Tool**: PyInstaller 6.16.0  
**Python Version**: 3.11.9  

---

## 🔄 Upgrade Notes

### From v2025.11.12

**Breaking Changes**: None

**Migration Required**: No action needed - all settings are backward compatible

**Recommendations**:
1. Delete old executables before installing new version
2. Update PyInstaller: `pip install PyInstaller>=6.1.0`
3. Remove cx_Freeze if installed: `pip uninstall cx_Freeze`

---

## 📋 Technical Details

### Build System Improvements

**Before**:
- Scattered build configurations
- Reliance on problematic cx_Freeze
- Inconsistent executable generation

**After**:
- Unified `build.py` launcher
- Clean PyInstaller specs in `scripts/`
- Reliable, reproducible builds

### Code Organization

```
Master Search/
├── build.py              # Master build launcher
├── version.py            # Version management
├── gui_main.py           # GUI entry point
├── cli_main.py           # CLI entry point
├── src/                  # Core modules
│   ├── gui_search_tool.py
│   ├── file_search_tool.py
│   ├── report_generator.py
│   └── ... (10+ modules)
├── scripts/              # Build & automation
│   ├── gui.spec
│   ├── cli.spec
│   └── ... (utilities)
├── locales/              # Translations (3 languages)
├── config/               # Configuration modules
└── dist/                 # Final executables
```

### Dependencies

**Production** (`requirements.txt`):
- colorama >= 0.4.6
- pillow >= 9.0.0
- psutil >= 5.9.0
- setuptools >= 68.0.0

**Build** (`requirements-dev.txt`):
- PyInstaller >= 6.1.0
- pytest, black, flake8, mypy (development)

---

## ✅ Verification Checklist

- ✅ Version number updated (2025.11.13)
- ✅ Root directory cleaned and organized
- ✅ All modules properly located
- ✅ Both executables built successfully
- ✅ No duplicate files or code
- ✅ All translations complete across 3 languages
- ✅ Category filters fully functional
- ✅ Stats display accurate
- ✅ Release Notes working correctly
- ✅ Build system reliable and clean
- ✅ No cx_Freeze dependencies remaining

---

## 🚀 Installation & Usage

### GUI Application
```powershell
# Run executable
.\MasterSearch.exe
```

### Command Line Interface
```powershell
# Run with arguments
.\MasterSearchCLI.exe --help
```

### From Source
```bash
# Build GUI
python build.py gui

# Build CLI
python build.py cli

# Build both
python build.py all

# Clean build artifacts
python build.py clean
```

---

## 📝 Known Limitations

- OneDrive paths with special characters require proper quoting
- Very large file searches (>1M files) may require increased RAM
- Some legacy file extensions not yet categorized

---

## 🙏 Contributors

- **Loony2392** - Creator and Maintainer
- **LOONY-TECH** - Company

---

## 📞 Support

For issues, feature requests, or suggestions:
- GitHub: https://github.com/Loony2392/master-search
- Email: info@loony-tech.de

---

## 📜 License

Master Search v2025.11.13  
(c) 2025 LOONY-TECH  
Author: Bastian Alexander Kolb

---

**Status**: ✅ Production Ready  
**Last Updated**: 13 November 2025 17:15 UTC
