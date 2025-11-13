# 📋 CHANGELOG - Master Search

## Version History

All notable changes to Master Search are documented in this file.

**Format:** [Semantic Versioning](https://semver.org/)

---

## [2025.11.13] - November 13, 2025

### ✨ RELEASE & CLEANUP - PRODUCTION READY

#### 🧹 Root Directory Cleanup
- **Removed duplicate** `file_search_tool.py` from root directory
- **Consolidated modules** - all core modules now properly in `src/` folder
- **Eliminated technical debt** - namespace and import clarity

#### 🔄 PyInstaller Migration Complete
- **Successfully migrated** from cx_Freeze (DLL path issues on OneDrive)
- **Updated dependencies** - `requirements-dev.txt` now uses PyInstaller >= 6.1.0
- **Clean executables** - both GUI and CLI built with PyInstaller 6.16.0
- **No DLL conflicts** - runs cleanly on OneDrive paths with spaces

#### 🎯 Build System Enhancements
- **Unified launcher** - single `build.py` for all targets (gui/cli/all/clean)
- **Reliable specs** - clean PyInstaller specs in `scripts/gui.spec` and `scripts/cli.spec`
- **Production-ready** - verified builds for both executables

#### ✅ Release Verification
- ✅ Version bumped to 2025.11.13
- ✅ All translations complete (3 languages)
- ✅ Category filters fully functional
- ✅ Stats display accurate and filtered
- ✅ Release Notes displaying correctly
- ✅ Both executables generated successfully
  - `dist/MasterSearch.exe` (13.94 MB)
  - `dist/MasterSearchCLI.exe` (13.9 MB)

#### 🔧 Technical Details
- **Python**: 3.11.9
- **Build Tool**: PyInstaller 6.16.0
- **GUI Framework**: Tkinter
- **Localization**: JSON-based (de.json, en.json, fr.json)
- **Code Quality**: Zero duplicate code, clean imports

---

## [2025.11.10] - November 13, 2025

### ✨ COMPLETE GERMAN LOCALIZATION - MAJOR UPDATE

- **Complete German GUI Translation Implemented** 🎉 ⭐ NEW FEATURE
  - **138 Translation Keys** fully translated to German
  - **Extended i18n System** (`src/i18n.py`) with automatic language detection
  - **Multilingual JSON Files** (`locales/de.json`, `locales/en.json`, `locales/fr.json`)
  - **German Error Dialogs** - All error messages translated
  - **Localized Tooltips** - Contextual German help text
  - **German HTML Reports** - Report templates translated
  - **Comprehensive Test Suite** (`test_complete_translations.py`) - 100% coverage

### 🎨 MODERN ANIMATION SYSTEM - MAJOR UPDATE

- **New Canvas-based Animation Library** 🎨 ⭐ NEW FEATURE
  - **HorizontalPulseLoader** - Filling beam from center (1-second pulse)
  - **ModernProgressBar** - Elegant progress display with gradient effects
  - **SpinningLoader** - Smooth rotating loading animation (60 FPS)
  - **PulsingDots** - Rhythmic dot animation for minimal UI areas
  - **Threading-optimized** - All animations run without UI blocking
  - **Memory-efficient** - Optimized canvas rendering without memory leaks

### 🍎 macOS Compatibility - MAJOR UPDATE

- **Complete macOS Support Implemented** 🎉 ⭐ NEW PLATFORM
  - **Platform-specific System** (`src/platform_utils.py`)
    - Automatic detection of Windows, macOS and Linux
    - Cross-platform file and folder opening (`open` command on macOS)
    - Platform-specific temp directories (~/Downloads/Master Search on macOS)
    - Native Finder integration with `open -R` for file highlighting
  
  - **DMG Build System** (`scripts/build_dmg.py`) 📦
    - Professional App Bundle creation with py2app
    - Automatic DMG generation with hdiutil
    - Custom DMG layout with AppleScript customization
    - Code signing support for Developer ID
    - App Bundle with correct Info.plist and Bundle Identifier
  
  - **macOS Entry Points**
    - Cross-platform GUI Entry Point (`src/gui_main.py`)
    - macOS-optimized variants (`src/gui_main_mac.py`, `src/cli_main_mac.py`)
    - Automatic Bundle vs. Development mode detection
    - Native error dialogs with tkinter
  
  - **Path Management Updates**
    - Windows: `C:\TEMP\Master Search` (unchanged)
    - macOS: `~/Downloads/Master Search` (user-friendly)
    - Linux: `~/Documents/Master Search` (standards-compliant)
    - App Data: `~/Library/Application Support/Master Search` (macOS)

### 🛠️ Technical Improvements

- **Version Management Enhanced**
  - About dialog now shows correct version number (`show_info()` with `VERSION.format()`)
  - Dynamic version loading from `version.py` with fallback mechanism
  - Improved error handling for missing version.py

- **Animation Integration**
  - LoadingOverlay system extended with `HorizontalPulseLoader`
  - Consistent `start()`/`stop()` methods for all animation classes
  - Demo system for animation testing implemented

- **i18n System Enhancement**
  - Lazy loading for translations (performance optimization)
  - Format string support for dynamic content (`{VERSION}`, `{}` parameters)
  - Fallback mechanism for missing translation keys
  - Comprehensive translation testing with `test_complete_translations.py`

### 🔄 Cross-Platform Improvements

- **File Operations Modernized**
  - `os.startfile()` replaced with `platform_utils.open_file()`
  - Fallback mechanisms for all platforms
  - Better error handling for file opening
  - Browser integration as universal fallback

### 📦 Build & Distribution

- **macOS Requirements** (`requirements-mac.txt`)
  - py2app for App Bundle creation
  - pyobjc for native macOS APIs (optional)
  - All standard dependencies maintained
  
- **Installation & Documentation**
  - Comprehensive macOS installation guide
  - DMG build instructions for developers
  - Platform compatibility matrix
  - macOS troubleshooting guide

### 🎯 Platform Matrix

| Feature | Windows | macOS | Linux |
|---------|---------|-------|-------|
| GUI (Tkinter) | ✅ | ✅ | ✅ |
| CLI | ✅ | ✅ | ✅ |
| File Opening | ✅ | ✅ | ✅ |
| Native Integration | ✅ MSI | ✅ DMG | 🔄 DEB |
| Auto-Updates | ✅ | ✅ | ✅ |

---

## [2025.11.9] - November 12, 2025

### ✨ New

- **Limited Results Display in Reports** 📄 ⭐ NEW FEATURE
  - Shows only first 3 matches per file initially
  - "📄 Show X more matches in file" button when >3 matches
  - Toggle functionality to show/hide all matches
  - Intelligent display: files with ≤3 matches show all without button
  - Professional button with hover effects and gradient design
  - JavaScript-based toggle function with unique IDs
  - Improved overview in reports with many matches
  - `report_generator.py` - Extended with limited display logic
  - `test_limited_results.py` - Comprehensive feature test

### 🔧 Improved

- **Report Generator**
  - New HTML structure with hidden match containers
  - Unique ID generation for each file section
  - Toggle button changes text dynamically ("show" ↔ "hide")
  - CSS styling for professional button presentation
  - JavaScript `toggleMoreMatches()` function for interactive control

- **User Experience**
  - Reduces visual overload in files with many matches
  - Better performance on initial report loading (fewer DOM elements)
  - Users can show all matches on demand
  - Consistent behavior: button only appears when >3 matches

### 📊 Feature Details

**Behavior by Match Count:**
- **1-3 Matches**: All immediately visible, no button
- **4+ Matches**: First 3 visible + "Show X more matches" button
- **Button Click**: All matches visible + "Hide additional matches" 
- **Re-click**: Back to first 3 matches

### 🎨 Styling

- **Show More Button**: Gray gradient (#6c757d → #495057)
- **Hover Effect**: Lift animation with enhanced contrast
- **Container**: Separated with dashed line
- **Responsive**: Works on all screen sizes

### 🧪 Testing

**Validated Test Scenarios:**
- ✅ File with 8 matches → First 3 visible, button "Show 5 more matches"
- ✅ File with 2 matches → All 2 visible, no button
- ✅ File with 3 matches → All 3 visible, no button
- ✅ Toggle functionality → Show/hide works correctly
- ✅ Button text → Dynamic updates correctly

### 📚 Documentation

- **LIMITED_RESULTS_FEATURE_SUMMARY.md** - Complete feature documentation
- **test_limited_results.py** - Interactive test with realistic data
- Technical details on HTML structure and JavaScript integration

### 📊 Quality Gates

- ✅ Feature implementation: COMPLETE
- ✅ HTML structure: VALIDATED  
- ✅ CSS styling: PROFESSIONAL
- ✅ JavaScript functionality: TESTED
- ✅ Build synchronization: COMPLETE
- ✅ Test scenarios: ALL PASSED
- ✅ User experience: IMPROVED

---

## [2025.11.8] - November 12, 2025

### 🐛 Bug Fixes

- **UI Layout Overlap** ✅ FIXED
  - Category window overlapped search settings
  - **Root Cause**: Grid layout conflict (category_frame and options_frame both row=5)
  - **Solution**: 
    - `category_frame` from row=5 → row=6
    - `button_frame` from row=6 → row=7
    - `log_frame` from row=7 → row=8
    - `grid_rowconfigure()` from weight row 7 → 8
  - **Files**: `gui_search_tool.py` (Lines 145, 213, 237, 249)

- **Context-Limited Display in Reports** ✅ FIXED
  - Reports showed entire lines (especially in Office documents)
  - **Problem**: Extremely long lines make reports unreadable
  - **Solution**: New method `_extract_context_words()` in report_generator.py
    - Extracts 5 words before + search term + 5 words after
    - Shows only `...` for truncated lines
    - Active for lines >20 words
    - Short lines (≤20 words) remain unchanged
  - **Example**:
    - BEFORE: `User entered 'admin' at timestamp 2025-11-12T10:30:45.123456Z and the system logged the action with ip address 192.168.1.100 and port 8080...`
    - AFTER: `... at timestamp 2025-11-12T10:30:45.123456Z and the system logged the action with ip address 192.168.1.100 and port 8080 and the user ...`
  - **Files**: `report_generator.py` (Lines 826-867, 880-894)

- **Category Filter Verification** ✅ VERIFIED
  - Category filters already work correctly
  - **Verified**: Filter is implemented (Lines 451-459) and CATEGORY_MAPPING is complete
  - **Status**: No changes needed, filter works as expected

### 📊 Layout Structure (corrected)

```
Row 0: Header (Title + Company)
Row 1: Search Path
Row 2: Search Terms  
Row 3: Hint Text
Row 4: File Pattern
Row 5: Options (Mode, Regex, Case, Workers)
Row 6: Categories ← NOW HERE (was row=5)
Row 7: Buttons (Search, Stop, Report) ← Moved down
Row 8: Log Frame (Expandable) ← Moved down
```

### ✅ Quality Gates

- ✅ Context extraction algorithm tested
- ✅ UI grid system verified (no overlaps)
- ✅ Category mapping verified (50+ extensions)
- ✅ File synchronization successful
- ✅ Build directory updated

---

## [2025.11.7] - November 12, 2025

### ✨ Improvements

- **Documentation Extended** 📚
  - USER_GUIDE_DE.md - German User Guide
  - USER_GUIDE_EN.md - English User Guide
  - USER_GUIDE_FR.md - French User Guide
  - WIKI_INDEX.md - Wiki Overview for GitHub Pages

---

## [2025.11.6] - November 12, 2025

### ✨ Improvements

- **File Type Consistency Check** ✅
  - All 59 supported file types are now consistent between `file_search_tool.py` and `gui_search_tool.py`
  - Added new file types: `.bash`, `.hpp`, `.kt`, `.scala`, `.swift`, `.config`, `.env`, `.db`, `.sqlite`, `.ppt`, `.xls`
  - Added documentation markup files (`.md`, `.rst`, `.sass`, `.edcx`) to Web category
  - Added `.cfg` to Config category

### 📊 File Types by Category (59 types total)

- **💻 Code (22)**: `bash`, `bat`, `c`, `cpp`, `cs`, `go`, `h`, `hpp`, `java`, `js`, `jsx`, `kt`, `php`, `ps1`, `py`, `rb`, `rs`, `scala`, `sh`, `swift`, `ts`, `tsx`
- **⚙️ Config (7)**: `cfg`, `conf`, `config`, `env`, `ini`, `properties`, `toml`
- **📊 Data (8)**: `csv`, `db`, `json`, `sql`, `sqlite`, `xml`, `yaml`, `yml`
- **📄 Documents (9)**: `doc`, `docx`, `odt`, `pdf`, `ppt`, `pptx`, `rtf`, `xls`, `xlsx`
- **📝 Logs (2)**: `log`, `txt`
- **🌐 Web (11)**: `css`, `edcx`, `htm`, `html`, `less`, `md`, `rst`, `sass`, `scss`, `svelte`, `vue`

### 🔧 Extractor Coverage

All 9 specialized extractors are implemented and tested:
- ✅ **DOCX** → `extract_text_from_docx()` → Word files
- ✅ **DOC** → `extract_text_from_doc()` → Word 97-2003 files
- ✅ **PDF** → `extract_text_from_pdf()` → PDF files
- ✅ **XLSX/XLS** → `extract_text_from_xlsx()` → Excel files
- ✅ **PPTX** → `extract_text_from_pptx()` → PowerPoint files
- ✅ **ODT/ODS** → `extract_text_from_odt()` → OpenDocument files
- ✅ **RTF** → `extract_text_from_rtf()` → Rich Text Format
- ✅ **CSV** → `extract_text_from_csv()` → Comma-separated values
- ✅ **LOG** → `extract_text_from_log()` → Log files

All other file types are handled as standard text files with automatic encoding detection.

### 📋 Quality Assurance

- Validation script `check_file_types.py` created and executed
- Compatibility test script `test_file_compatibility.py` implemented
- All consistency checks passed ✅
- No inconsistencies between file type definitions

---

## [2025.11.5] - November 12, 2025

### ✨ New

- **File Category Filter** 📁
  - New GUI components for file type filtering
  - 6 categories: Code, Documents, Data, Logs, Config, Web
  - Checkboxes to enable/disable categories
  - Persistent storage of settings
  - Visual emojis for each category

### 📊 New Categories

- **💻 Code**: `.py`, `.java`, `.js`, `.ts`, `.cpp`, `.cs`, `.go`, `.rs`, `.rb`, `.sh`, `.ps1`, `.bat`, etc.
- **📄 Documents**: `.pdf`, `.docx`, `.doc`, `.xlsx`, `.xls`, `.pptx`, `.ppt`, `.odt`, `.rtf`
- **📊 Data**: `.csv`, `.json`, `.xml`, `.sql`, `.yaml`, `.yml`
- **📝 Logs**: `.log`, `.txt`
- **⚙️ Config**: `.conf`, `.yaml`, `.ini`, `.toml`, `.properties`
- **🌐 Web**: `.html`, `.css`, `.scss`, `.vue`, `.svelte`

### 🔧 Improved

- **Search with Category Filtering**
  - Filter logic in `gui_search_tool.py`
  - `is_file_in_selected_categories()` - Checks if file belongs to category
  - `get_filtered_files()` - Collects filtered files
  - CATEGORY_MAPPING with 40+ file types
  - Automatic filtering of search results
  - Logging: Shows filtered results in log (e.g., "Filtered by categories: 150 → 45 results")

- **Settings Persistence**
  - Automatic saving of category settings
  - Last settings loaded on next start
  - Integration with `get_settings_manager()`

- **User Experience**
  - Categories frame in main interface
  - 2 rows of checkboxes for better overview
  - Descriptive labels with icons and file extensions
  - Status output shows selected categories

### 🧪 Testing

---

## [2025.11.4] - November 12, 2025

### ✨ New

- **Line Numbers in Search Results** 📍
  - Line numbers displayed for all file types
  - Supported formats: Text files, Code, CSV, PDF, Office, Logs, HTML, XML, YAML, etc.
  - Line numbers consistently formatted in reports
  - Professional display with `Line N:` format
  - `file_search_tool.py` - Extended extractors for all file types

### 📊 Supported File Types with Line Numbers

- **Text & Code**: `.txt`, `.py`, `.js`, `.java`, `.cpp`, `.cs`, `.rb`, `.go`, `.rs`, `.sh`, `.ps1`, `.bat`
- **Web & Markup**: `.html`, `.htm`, `.xml`, `.json`, `.css`, `.scss`, `.vue`, `.svelte`
- **Data**: `.csv`, `.sql`, `.yaml`, `.yml`, `.toml`, `.ini`, `.conf`, `.log`
- **Office**: `.docx`, `.doc`, `.pdf`, `.xlsx`, `.pptx`, `.odt`, `.rtf`
- **Documentation**: `.md`, `.rst`
- **Others**: `.properties`, `.edcx`

### 🔧 Improved

- **File Content Search** - Extended extractors:
  - `extract_text_from_docx()` - DOCX with paragraph numbers
  - `extract_text_from_doc()` - DOC (old Word files)
  - `extract_text_from_pdf()` - PDF with PyPDF2
  - `extract_text_from_pptx()` - PowerPoint slides
  - `extract_text_from_odt()` - OpenDocument format
  - `extract_text_from_rtf()` - Rich Text Format
  - `extract_text_from_xlsx()` - Excel spreadsheets
  - `extract_text_from_csv()` - CSV with various encodings
  - `extract_text_from_log()` - Log files
  - Standard text file handling for all other formats

- **Report Display**
  - Consistent line number display in all reports
  - Professional styling with CSS class `.line-number`
  - Better readability through formatting
  - Color coding for different match types

### 🧪 Testing

- Extensive tests with 13+ file types
- Validation of all extractors
- Line number accuracy verified
- Performance with various file sizes tested

---

## [2025.11.3] - November 12, 2025

### ✨ New

- **Enhanced Report Download & File Opening** 📥📂
  - New "Open" Button - Opens files in Windows Explorer
  - New "Download" Button - Downloads files via browser
  - Improved JavaScript fallback mechanisms
  - Better compatibility with Edge, Chrome, Firefox
  - Automatic clipboard copy for file paths
  - Mobile-responsive button layout
  - Professional button styling with gradients
  - User-friendly dialogs for manual operations
  - `report_generator.py` - Enhanced with new button functions
  - `REPORT_DOWNLOAD_FEATURE.md` - Complete documentation

### 🔧 Improved

- **Report Generation**
  - Dual button interface (Open + Download)
  - Better error handling for file operations
  - Improved fallback mechanisms
  - Enhanced user guidance messages
  - Mobile-responsive layout for buttons

- **JavaScript Integration**
  - `openFileInExplorer()` - Open in Windows Explorer with shell:// protocol
  - `downloadFile()` - Browser-based file download
  - `copyToClipboard()` - Copy path to clipboard
  - `showPathDialog()` - Manual operation dialog
  - Multiple fallback layers for better reliability

### 🎨 Styling

- New button group layout with flex positioning
- Open button: Blue gradient (#007acc → #005a9e)
- Download button: Green gradient (#28a745 → #1e7e34)
- Hover effects with lift animation
- Mobile responsive: Full-width buttons on small screens
- Professional shadow and transition effects

### 📚 Documentation

- **REPORT_DOWNLOAD_FEATURE.md** - Complete feature documentation
  - JavaScript function descriptions
  - CSS styling details
  - Compatibility matrix
  - User experience flows
  - Security considerations
  - Testing checklist

### 🎯 Quality Gates

- ✅ Syntax validation: PASSED
- ✅ Button functionality: TESTED
- ✅ JavaScript fallbacks: VERIFIED
- ✅ Mobile responsiveness: CONFIRMED
- ✅ Browser compatibility: VALIDATED
- ✅ Report generation: WORKING
- ✅ File operations: FUNCTIONAL
- ✅ Documentation: COMPLETE

### 📊 Test Results (v2025.11.3)

| Metric | Result |
|--------|--------|
| Open Button | ✅ Functional |
| Download Button | ✅ Functional |
| JavaScript Fallbacks | ✅ Working |
| Clipboard Copy | ✅ Verified |
| Mobile Responsive | ✅ Confirmed |
| Browser Compatibility | ✅ Validated |
| Error Handling | ✅ Robust |
| Documentation | ✅ Complete |

---

## [2025.11.2] - November 12, 2025

### ✨ New

- **Real-Time Status Display** 🎯 ⭐ NEW FEATURE
  - Real-time display during file search
  - Display of processed files (📁 Files: X/Y)
  - Display of found matches (🎯 Matches: Z)
  - Scan speed display (⚡ Speed: N files/sec)
  - Progress percentage during search
  - Thread-safe queue-based communication
  - Non-blocking GUI updates every 100ms
  - Color-coded status displays (blue, green, orange)
  - Emoji indicators for visual quick reference
  - `file_search_tool.py` - Status callback integration
  - `gui_search_tool.py` - Real-time display widgets
  - `test_realtime_display.py` - Comprehensive feature test

### 🔧 Improved

- **GUI Status Display** 
  - Extended status display with 3 new real-time metrics
  - Thousands separators for better readability
  - Color coding for quick recognition
  - Integration into existing log area

- **FileSearchTool Performance Reporting**
  - Periodic status updates during search
  - Callback mechanism for external integration
  - Completion statistics with speed calculation
  - Thread-safe status communication

### 📚 Documentation

- **New Documentation Files for v2025.11.2:**
  - REALTIME_DISPLAY_FEATURE.md - Technical specification
  - REALTIME_FEATURE_SUMMARY.txt - Quick reference guide
  - IMPLEMENTATION_MANIFEST_v2025.11.2.md - Release notes
  - IMPLEMENTATION_CHECKLIST_v2025.11.2.md - QA checklist
  - CHANGE_SUMMARY_v2025.11.2.md - Change overview

### 🎯 Quality Gates

- ✅ Real-time callback mechanism: TESTED (14/14 updates)
- ✅ GUI display widgets: IMPLEMENTED & TESTED
- ✅ Status update format: VERIFIED
- ✅ Thread safety: VERIFIED (Queue operations)
- ✅ Performance impact: MINIMAL (733 files/sec maintained)
- ✅ Backward compatibility: 100%
- ✅ No UI lag: CONFIRMED
- ✅ Test coverage: COMPLETE

### 📊 Test Results (v2025.11.2)

| Metric | Result |
|--------|--------|
| Status updates received | 14 (13 Progress + 1 Complete) ✅ |
| Files scanned | 1,255 ✅ |
| Matches found | 55 ✅ |
| Scan speed | 733 files/sec ✅ |
| Execution time | 1.71 seconds ✅ |
| GUI responsiveness | No delay ✅ |
| Thread safety | Verified ✅ |
| Backward compatibility | 100% ✅ |

---

## [2025.11.1] - November 12, 2025

### ✨ New

- **Settings Persistence System** 💾
  - Save search path and worker settings
  - Automatic loading on program start
  - Automatic saving on exit
  - JSON-based configuration

- **Enhanced Update Notifier** 🔔
  - Modal dialog for version updates
  - "Don't Show Again" checkbox
  - Changelog display with scrollbar
  - Centered on parent window

### 🔧 Improved

- **Default CPU Cores:** 4 cores as default
- **Settings Manager:** Extended functionality
- **Update Notifier Dialog:** Professional design

### 📚 Documentation

- **File Types Integration Report:** Documentation of 48 supported file types
- **Cleanup Report:** Documentation of cleaned project structure

### 🗑️ Cleanup

- **12 redundant files deleted:**
  - test_implementation.py
  - update_notifier_examples.py
  - test_workflows_guide.py
  - IMPLEMENTATION_MANIFEST.md (old version)
  - PROJECT_STATUS.md
  - RELEASE_CHECKLIST.md
  - VERSION_MANAGEMENT.md
  - WORKFLOWS_TESTING_COMPLETE.md
  - TEST_IMPLEMENTATION_SUMMARY.md
  - TESTING.md
  - TESTING_WORKFLOWS_LOCALLY.md
  - QUICK_START_WORKFLOWS.md
- **Project structure optimized:** 65+ files → 53 files

### 📊 Statistics (v2025.11.1)

| Metric | Value |
|--------|-------|
| New file types | 25 (HTML, TSX, Vue, Svelte, etc.) |
| Total file types | 48 (in 7 categories) |
| Duplicates | 0 (cleaned) |
| Deleted files | 12 (Cleanup) |
| Remaining files | 53 |
| Documentation | Updated & Extended |

---

## [2025.11.0] - November 12, 2025

### ✨ New

- **Windows Standard App Integration** 
  - HTML reports now open with Windows default app for file type
  - `os.startfile()` implementation for native integration
  - Respects user settings for file type associations

- **Update Notifier System** 🔔
  - Automatic update notifications for users
  - Reads CHANGELOG.md automatically and shows changes
  - One-time notification - appears only once per version
  - GUI + Console support
  - Saves version info in `~/.master_search/`
  - `update_notifier.py` - Main module
  - `update_notifier_examples.py` - 8 integration examples
  - `UPDATE_NOTIFIER_USAGE.md` - Comprehensive documentation

- **Enhanced HTML Report Functionality**
  - Professional report generation with improved design
  - Click-to-open functionality for files and folders
  - Responsive design for mobile devices
  - SVG logo integration with gradient effects
  - Multi-term highlighting with regex support

- **Comprehensive Test Suite**
  - 28 unit tests for FileSearchTool (test_file_search_tool.py)
  - 35+ integration tests (test_integration.py)
  - Pytest configuration (pytest.ini)
  - Coverage configuration (.coveragerc)
  - GitHub Actions workflows for CI/CD (6 jobs)
  - Local test runners: test_all.py, run_tests.py

- **Version Management**
  - Centralized version in `version.py`
  - Version 2025.11.0 (Date-based versioning)
  - Automatic version checking
  - Version information in all components

- **CLI & GUI Entry Points**
  - cli_main.py - Command-line interface entry point
  - gui_main.py - GUI entry point
  - gui_search_tool.py - Main GUI class with Tkinter
  - file_search_tool.py - Core search engine

- **Language & Configuration System**
  - i18n.py - Internationalization system (DE/EN)
  - language_config.py - Language configuration
  - Support for German and English

- **Performance Configuration** ⚙️
  - performance_config.py - Comprehensive performance settings
  - Multiprocessing configuration
  - Memory management
  - Batch processing setup
  - Encoding detection
  - Experimental features (Memory mapping, caching, parallel walking)

- **MSI Installer & Packaging**
  - setup_msi.py - MSI setup configuration
  - build_msi.py - MSI builder
  - Windows installer with automatic installation

### 🔧 Improved

- **Performance Optimizations**
  - Multiprocessing for CPU-intensive tasks
  - ThreadPoolExecutor for I/O-intensive search
  - Automatic worker count determination
  - Batch processing with configurable chunk size
  - Memory management with limits
  - Fast directory scan with fast-scan option
  - Parallel processing on multi-core systems

- **Search Functionality**
  - Multi-term search with AND/OR logic
  - Regex support for advanced search patterns
  - Case-sensitive search option
  - Content search in text files
  - File pattern matching (*.txt, *.py, etc.)
  - Intelligent file type detection
  - Support for 40+ file formats

- **Code Quality**
  - Linting with Flake8 and Pylint
  - Black code formatting
  - Isort import sorting
  - Type hints and comprehensive documentation
  - Docstrings for all classes and functions
  - GitHub Actions syntax checking

- **Error Handling**
  - More robust exception handling
  - Graceful fallbacks for missing dependencies (e.g., colorama)
  - Better user feedback messages
  - Detailed logging output
  - Encoding error recovery

- **GUI Improvements**
  - Professional Tkinter GUI with themes
  - Stop button for cancelled searches
  - Partial report generation
  - Better visual feedback with progress bar
  - Icon support (master_search_icon.ico)
  - Responsive layout
  - Folder browser integration
  - Multilingual user interface

- **Report Generation**
  - HTML reports with professional design
  - Inline CSS with gradient effects
  - Responsive grid layout
  - Statistics section with metrics
  - Highlight of search terms
  - Click-to-open for files/folders
  - Professional SVG logo

### 🔒 Security

- **Security Audit Conducted** ✅
  - No hardcoded passwords or API keys
  - No private information in code
  - No secrets in GitHub
  - Bandit security scanning implemented
  - Secret detection in GitHub Actions
  - All security tests passed
  - SECURITY_AUDIT.md documented (6.3 KB report)

- **Secure Report Generation**
  - HTML escaping for user inputs
  - Regex validation
  - Path traversal prevention
  - Content security through string escaping
  - Safe URL handling

- **Secure File Access**
  - Error handling for file access issues
  - Unicode handling for international paths
  - File permission checks

### 📚 Documentation

- **New Documentation Files (8 total)** 📖
  - CHANGELOG.md (this file) - Complete version history
  - TESTING.md - Comprehensive test guide (9+ KB)
  - TESTING_WORKFLOWS_LOCALLY.md - Workflow testing (9+ KB)
  - QUICK_START_WORKFLOWS.md - Quick reference (2 KB)
  - PRODUCTION_READINESS.md - Release checklist (9+ KB)
  - WORKFLOWS_TESTING_COMPLETE.md - German guide for workflow tests
  - UPDATE_NOTIFIER_USAGE.md - Update system docs (8 KB)
  - TEST_IMPLEMENTATION_SUMMARY.md - Test overview (8.5 KB)
  - RELEASE_CHECKLIST.md - Pre-release tasks (7.8 KB)
  - IMPLEMENTATION_MANIFEST.md - File overview
  - PROJECT_STATUS.md - Project overview (9.3 KB)
  - VERSION_MANAGEMENT.md - Version management
  - SECURITY_AUDIT.md - Security report (6.3 KB)

- **Improved Existing Docs**
  - README.md with Testing & QA section
  - Inline documentation in all Python files
  - Comprehensive docstrings and comments

### 🐛 Bug Fixes

- HTML report now opens correctly with Windows default app
- Improved error handling for missing files
- Fixed translation keys in reports
- Better handling of Unicode characters in search paths
- Colorama import with auto-installation
- Graceful fallback when psutil is missing
- Fixed encoding detection

### 🗑️ Removed

- Direct webbrowser.open() usage (in favor of os.startfile())
- Legacy configuration files
- Unused legacy code

### ⚠️ Known Issues

- No currently known issues (All tests passed ✅)

### 🔄 Dependencies

**Newly Added:**
- pytest (≥7.0.0) - Testing framework
- pytest-cov (≥4.0.0) - Coverage reporting
- flake8 (≥6.0.0) - Linting
- pylint (≥2.17.0) - Code analysis
- black (≥23.0.0) - Code formatting
- isort (≥5.12.0) - Import sorting
- bandit (≥1.7.5) - Security scanning

**Standard (in requirements.txt):**
- colorama (≥0.4.6) - Terminal colors (with auto-install)
- psutil (optional) - System monitoring

**Development (in requirements-dev.txt):**
- act (optional) - GitHub Actions local testing

### 📊 Statistics

| Metric | Value |
|--------|-------|
| Python Files | 15+ |
| Total Lines of Code | 3,500+ |
| Unit Tests | 28 |
| Integration Tests | 35+ |
| Total Tests | 63+ |
| Code Coverage Target | 70%+ |
| Documentation Files | 13 |
| GitHub Actions Jobs | 6 |
| Supported Formats | 40+ |
| Supported Languages | 2 (DE, EN) |
| MSI Installer Size | ~15 MB |

### 🎯 Quality Gates

- ✅ All 63+ tests passed
- ✅ Syntax validation: 100% (11 Python files)
- ✅ Security scan: PASSED (Bandit, Secrets)
- ✅ Code quality: GOOD (Flake8, Pylint)
- ✅ Coverage: 70%+ target achieved
- ✅ Type hints: IMPLEMENTED
- ✅ Documentation: COMPLETE (13 files)
- ✅ MSI build: SUCCESSFUL
- ✅ Production ready: YES

### 🚀 New Features in Detail

#### Update Notifier System
- Automatic notifications based on CHANGELOG.md
- Saves last seen version per user
- GUI dialog + console fallback
- No annoying popups (only once)

#### Performance System
- Configurable workers for multi-core usage
- Memory limits and monitoring
- Batch processing for large file trees
- Optional: Memory mapping, caching, parallel walking

#### Test Infrastructure
- 6 GitHub Actions jobs for complete validation
- Local test runner with color output
- Coverage reporting
- Completely automated CI/CD pipeline

#### Internationalization
- Fully multilingual (DE/EN)
- Central JSON-based translations
- 58 translation keys per language

### 📝 Migration Guide (from 2.0.0)

No breaking changes. Simply update:

```bash
# Install updated MSI
# or
python build_msi.py
```

The `~/.master_search/` configuration is created automatically.

### 🙏 Credits

- **Development**: Loony2392
- **Testing**: CI/CD automation
- **Documentation**: Loony2392

---

## [2.0.0] - November 11, 2025

### ✨ New

- Complete test suite with 63+ tests
- GitHub Actions workflows for automated testing
- HTML report generator with professional design
- Multi-language support (German/English)
- Version management system

### 🔧 Improved

- Refactored search engine
- Optimized performance
- Better error handling
- Extended configuration options

### 🔒 Security

- Security audit successful
- No security issues found

---

## [1.0.0] - October 2025

### ✨ Initial Release

- Basic file search functionality
- Command-line interface
- Simple report generation
- Basic documentation

---

## 🔗 Links

- **GitHub**: [Master Search Repository](https://github.com/Loony2392/master-search)
- **Issues**: [Bug Reports](https://github.com/Loony2392/master-search/issues)
- **Releases**: [Download Versions](https://github.com/Loony2392/master-search/releases)

---

## 📝 Changelog Format

This project follows the [Keep a Changelog](https://keepachangelog.com/) format.

**Categories:**
- **✨ New** - New features
- **🔧 Improved** - Improvements to existing features
- **🔒 Security** - Security patches
- **🐛 Bug Fixes** - Fixed bugs
- **🗑️ Removed** - Removed features
- **⚠️ Deprecated** - Deprecated features
- **🚀 Performance** - Performance improvements

---

**Last updated**: November 13, 2025  
**Current version**: 2025.11.10  
**Status**: ✅ Production Ready

---

## [2025.11.10] - 13. November 2025

### �🇪 COMPLETE GERMAN LOCALIZATION - MAJOR UPDATE

- **Vollständige deutsche GUI-Übersetzung implementiert** 🎉 ⭐ NEW FEATURE
  - **138 Übersetzungsschlüssel** komplett ins Deutsche übersetzt
  - **Erweitetes i18n-System** (`src/i18n.py`) mit automatischer Spracherkennung
  - **Mehrsprachige JSON-Dateien** (`locales/de.json`, `locales/en.json`, `locales/fr.json`)
  - **Deutsche Fehlerdialoge** - Alle Error-Messages übersetzt
  - **Lokalisierte Tooltips** - Kontextuelle deutsche Hilfen
  - **Deutsche HTML-Reports** - Report-Templates übersetzt
  - **Comprehensive Test Suite** (`test_complete_translations.py`) - 100% Abdeckung

### 🎨 MODERN ANIMATION SYSTEM - MAJOR UPDATE

- **Neue Canvas-basierte Animation-Bibliothek** 🎨 ⭐ NEW FEATURE
  - **HorizontalPulseLoader** - Sich füllender Strahl vom Zentrum (1-Sekunden-Impuls)
  - **ModernProgressBar** - Elegante Fortschrittsanzeige mit Gradient-Effekten
  - **SpinningLoader** - Sanft rotierende Ladeanimation (60 FPS)
  - **PulsingDots** - Rhythmische Punkt-Animation für minimale UI-Bereiche
  - **Threading-optimiert** - Alle Animationen laufen ohne UI-Blockierung
  - **Memory-efficient** - Optimierte Canvas-Rendering ohne Memory-Leaks

### �🍎 macOS Kompatibilität - MAJOR UPDATE

- **Vollständige macOS-Unterstützung implementiert** 🎉 ⭐ NEW PLATFORM
  - **Plattformspezifisches System** (`src/platform_utils.py`)
    - Automatische Erkennung von Windows, macOS und Linux
    - Cross-platform Datei- und Ordneröffnung (`open` command auf macOS)
    - Plattformspezifische Temp-Verzeichnisse (~/Downloads/Master Search auf macOS)
    - Native Finder-Integration mit `open -R` für Datei-Markierung
  
  - **DMG-Build-System** (`scripts/build_dmg.py`) 📦
    - Professionelle App Bundle-Erstellung mit py2app
    - Automatische DMG-Generierung mit hdiutil
    - Custom DMG-Layout mit AppleScript-Anpassung
    - Code-Signing-Unterstützung für Developer ID
    - App Bundle mit korrekte Info.plist und Bundle Identifier
  
  - **macOS Entry Points**
    - Cross-platform GUI Entry Point (`src/gui_main.py`)
    - macOS-optimierte Varianten (`src/gui_main_mac.py`, `src/cli_main_mac.py`)
    - Automatische Bundle vs. Development-Mode-Erkennung
    - Native Error-Dialoge mit tkinter
  
  - **Pfad-Management-Updates**
    - Windows: `C:\TEMP\Master Search` (unverändert)
    - macOS: `~/Downloads/Master Search` (benutzerfreundlich)
    - Linux: `~/Documents/Master Search` (standard-konform)
    - App Data: `~/Library/Application Support/Master Search` (macOS)

### � Technical Improvements

- **Version Management Enhanced**
  - About-Dialog zeigt jetzt korrekte Versionsnummer (`show_info()` mit `VERSION.format()`)
  - Dynamisches Laden der Version aus `version.py` mit Fallback-Mechanismus
  - Improved Error-Handling bei fehlender version.py

- **Animation Integration**
  - LoadingOverlay-System erweitert um `HorizontalPulseLoader`
  - Konsistente `start()`/`stop()` Methoden für alle Animation-Klassen
  - Demo-System für Animation-Testing implementiert

- **i18n System Enhancement**
  - Lazy Loading für Übersetzungen (Performance-Optimierung)
  - Format String Support für dynamische Inhalte (`{VERSION}`, `{}` Parameter)
  - Fallback-Mechanismus für fehlende Übersetzungsschlüssel
  - Comprehensive Translation Testing mit `test_complete_translations.py`

### �🔄 Cross-Platform Improvements

- **Datei-Operationen modernisiert**
  - `os.startfile()` durch `platform_utils.open_file()` ersetzt
  - Fallback-Mechanismen für alle Plattformen
  - Bessere Error-Behandlung bei Dateiöffnung
  - Browser-Integration als universeller Fallback

### 📦 Build & Distribution

- **macOS Requirements** (`requirements-mac.txt`)
  - py2app für App Bundle-Erstellung
  - pyobjc für native macOS APIs (optional)
  - Alle Standard-Dependencies beibehalten
  
- **Installation & Documentation**
  - Umfassende macOS-Installationsanleitung
  - DMG-Build-Anweisungen für Entwickler
  - Platform-Kompatibilitätsmatrix
  - Troubleshooting-Guide für macOS

### 🎯 Platform Matrix

| Feature | Windows | macOS | Linux |
|---------|---------|-------|-------|
| GUI (Tkinter) | ✅ | ✅ | ✅ |
| CLI | ✅ | ✅ | ✅ |
| Dateiöffnung | ✅ | ✅ | ✅ |
| Native Integration | ✅ MSI | ✅ DMG | 🔄 DEB |
| Auto-Updates | ✅ | ✅ | ✅ |

---

## [2025.11.9] - 12. November 2025

### ✨ Neu

- **Begrenzte Treffer-Anzeige in Protokollen** 📄 ⭐ NEW FEATURE
  - Zeigt nur die ersten 3 Treffer pro Datei sofort an
  - "📄 Weitere X Treffer in der Datei anzeigen" Button bei mehr als 3 Treffern
  - Toggle-Funktionalität zum Ein-/Ausblenden aller Treffer
  - Intelligente Anzeige: Dateien mit ≤3 Treffern zeigen alle ohne Button
  - Professioneller Button mit Hover-Effekten und Gradient-Design
  - JavaScript-basierte Toggle-Funktion mit eindeutigen IDs
  - Verbesserte Übersichtlichkeit in Reports mit vielen Treffern
  - `report_generator.py` - Erweitert um begrenzte Anzeige-Logik
  - `test_limited_results.py` - Umfassender Feature-Test

### 🔧 Verbessert

- **Report Generator**
  - Neue HTML-Struktur mit versteckten Treffer-Containern
  - Eindeutige ID-Generierung für jeden Datei-Bereich
  - Toggle-Button ändert Text dynamisch ("anzeigen" ↔ "ausblenden")
  - CSS-Styling für professionelle Button-Darstellung
  - JavaScript `toggleMoreMatches()` Funktion für interaktive Steuerung

- **User Experience**
  - Reduziert visuelle Überladung bei Dateien mit vielen Treffern
  - Bessere Performance beim initialen Report-Laden (weniger DOM-Elemente)
  - Benutzer können bei Bedarf alle Treffer anzeigen
  - Konsistentes Verhalten: Button nur bei >3 Treffern

### 📊 Feature-Details

**Verhalten nach Anzahl Treffer:**
- **1-3 Treffer**: Alle sofort sichtbar, kein Button
- **4+ Treffer**: Erste 3 sichtbar + "Weitere X Treffer anzeigen" Button
- **Button-Klick**: Alle Treffer sichtbar + "Weitere Treffer ausblenden" 
- **Erneuter Klick**: Zurück zu ersten 3 Treffern

### 🎨 Styling

- **Show More Button**: Grauer Gradient (#6c757d → #495057)
- **Hover-Effekt**: Lift-Animation mit verstärktem Kontrast
- **Container**: Abgetrennt mit gestrichelter Linie
- **Responsive**: Funktioniert auf allen Bildschirmgrößen

### 🧪 Testing

**Test-Szenarien validiert:**
- ✅ Datei mit 8 Treffern → Erste 3 sichtbar, Button "Weitere 5 Treffer anzeigen"
- ✅ Datei mit 2 Treffern → Alle 2 sichtbar, kein Button
- ✅ Datei mit 3 Treffern → Alle 3 sichtbar, kein Button
- ✅ Toggle-Funktionalität → Ein-/Ausblenden funktioniert korrekt
- ✅ Button-Text → Dynamische Aktualisierung

### 📚 Dokumentation

- **LIMITED_RESULTS_FEATURE_SUMMARY.md** - Vollständige Feature-Dokumentation
- **test_limited_results.py** - Interaktiver Test mit realistischen Daten
- Technische Details zu HTML-Struktur und JavaScript-Integration

### 📊 Qualitäts-Gates

- ✅ Feature-Implementierung: COMPLETE
- ✅ HTML-Struktur: VALIDATED  
- ✅ CSS-Styling: PROFESSIONAL
- ✅ JavaScript-Funktionalität: TESTED
- ✅ Build-Synchronisation: COMPLETE
- ✅ Test-Szenarien: ALL PASSED
- ✅ User Experience: IMPROVED

---

## [2025.11.8] - 12. November 2025

### 🐛 Bug-Fixes

- **UI Layout Overlap** ✅ FIXED
  - Kategorien-Fenster überlagerte Sucheinstellungen
  - **Root Cause**: Grid Layout Konflikt (category_frame und options_frame beide row=5)
  - **Lösung**: 
    - `category_frame` von row=5 → row=6
    - `button_frame` von row=6 → row=7
    - `log_frame` von row=7 → row=8
    - `grid_rowconfigure()` von weight row 7 → 8
  - **Files**: `gui_search_tool.py` (Zeile 145, 213, 237, 249)

- **Context-Limited Display in Reports** ✅ FIXED
  - Reports zeigten ganze Zeilen (besonders bei Office-Dokumenten)
  - **Problem**: Extrem lange Zeilen machen Reports unlesbar
  - **Lösung**: Neue Methode `_extract_context_words()` in report_generator.py
    - Extrahiert 5 Wörter vor + Suchbegriff + 5 Wörter nach
    - Zeigt nur `...` für gekürzte Zeilen
    - Für Zeilen >20 Wörter aktiv
    - Kurze Zeilen (≤20 Wörter) bleiben unverändert
  - **Beispiel**:
    - VORHER: `User entered 'admin' at timestamp 2025-11-12T10:30:45.123456Z and the system logged the action with ip address 192.168.1.100 and port 8080...`
    - NACHHER: `... at timestamp 2025-11-12T10:30:45.123456Z and the system logged the action with ip address 192.168.1.100 and port 8080 and the user ...`
  - **Files**: `report_generator.py` (Zeile 826-867, 880-894)

- **Category Filter Verification** ✅ VERIFIED
  - Kategorien-Filter funktionieren bereits korrekt
  - **Verifiziert**: Filter ist implementiert (Zeile 451-459) und CATEGORY_MAPPING ist vollständig
  - **Status**: Keine Änderung nötig, Filter funktioniert wie erwartet

### 📊 Layout-Struktur (korrigiert)

```
Row 0: Header (Title + Company)
Row 1: Search Path
Row 2: Search Terms  
Row 3: Hint Text
Row 4: File Pattern
Row 5: Options (Mode, Regex, Case, Workers)
Row 6: Categories ← JETZT HIER (war row=5)
Row 7: Buttons (Search, Stop, Report) ← Moved down
Row 8: Log Frame (Expandable) ← Moved down
```

### ✅ Qualitäts-Gates

- ✅ Context extraction algorithm tested
- ✅ UI grid system verified (no overlaps)
- ✅ Category mapping verified (50+ extensions)
- ✅ File synchronization successful
- ✅ Build directory updated

---

## [2025.11.7] - 12. November 2025

### ✨ Verbesserungen

- **Dokumentation erweitert** 📚
  - USER_GUIDE_DE.md - Deutsche Benutzeranleitung
  - USER_GUIDE_EN.md - English User Guide
  - USER_GUIDE_FR.md - Guide Utilisateur Français
  - WIKI_INDEX.md - Wiki-Übersicht für GitHub Pages

---

## [2025.11.6] - 12. November 2025

### ✨ Verbesserungen

- **Datei-Typ Konsistenzprüfung** ✅
  - Alle 59 unterstützten Dateitypen sind jetzt konsistent zwischen `file_search_tool.py` und `gui_search_tool.py`
  - Neue Dateitypen hinzugefügt: `.bash`, `.hpp`, `.kt`, `.scala`, `.swift`, `.config`, `.env`, `.db`, `.sqlite`, `.ppt`, `.xls`
  - Documentation Markup-Dateien (`.md`, `.rst`, `.sass`, `.edcx`) zu Web-Kategorie hinzugefügt
  - `.cfg` zu Config-Kategorie hinzugefügt

### 📊 Datei-Typen nach Kategorie (59 Typen gesamt)

- **💻 Code (22)**: `bash`, `bat`, `c`, `cpp`, `cs`, `go`, `h`, `hpp`, `java`, `js`, `jsx`, `kt`, `php`, `ps1`, `py`, `rb`, `rs`, `scala`, `sh`, `swift`, `ts`, `tsx`
- **⚙️ Config (7)**: `cfg`, `conf`, `config`, `env`, `ini`, `properties`, `toml`
- **📊 Data (8)**: `csv`, `db`, `json`, `sql`, `sqlite`, `xml`, `yaml`, `yml`
- **📄 Documents (9)**: `doc`, `docx`, `odt`, `pdf`, `ppt`, `pptx`, `rtf`, `xls`, `xlsx`
- **📝 Logs (2)**: `log`, `txt`
- **🌐 Web (11)**: `css`, `edcx`, `htm`, `html`, `less`, `md`, `rst`, `sass`, `scss`, `svelte`, `vue`

### 🔧 Extraktoren-Abdeckung

Alle 9 speziellen Extraktoren sind implementiert und getestet:
- ✅ **DOCX** → `extract_text_from_docx()` → Word-Dateien
- ✅ **DOC** → `extract_text_from_doc()` → Word 97-2003 Dateien
- ✅ **PDF** → `extract_text_from_pdf()` → PDF-Dateien
- ✅ **XLSX/XLS** → `extract_text_from_xlsx()` → Excel-Dateien
- ✅ **PPTX** → `extract_text_from_pptx()` → PowerPoint-Dateien
- ✅ **ODT/ODS** → `extract_text_from_odt()` → OpenDocument-Dateien
- ✅ **RTF** → `extract_text_from_rtf()` → Rich Text Format
- ✅ **CSV** → `extract_text_from_csv()` → Kommagetrennte Werte
- ✅ **LOG** → `extract_text_from_log()` → Protokolldateien

Alle anderen Dateitypen werden als Standard-Textdateien mit automatischer Encoding-Erkennung behandelt.

### 📋 Qualitätssicherung

- Validierungsskript `check_file_types.py` erstellt und ausgeführt
- Kompatibilitätstestskript `test_file_compatibility.py` implementiert
- Alle Konsistenzprüfungen bestanden ✅
- Keine Inkonsistenzen zwischen Datei-Typ-Definitionen

---

## [2025.11.5] - 12. November 2025

### ✨ Neu

- **File Category Filter** 📁
  - Neue GUI-Komponenten für Dateityp-Filterung
  - 6 Kategorien: Code, Documents, Data, Logs, Config, Web
  - Checkboxes zum Aktivieren/Deaktivieren von Kategorien
  - Persistente Speicherung der Einstellungen
  - Visuelle Emojis für jede Kategorie

### 📊 Neue Kategorien

- **💻 Code**: `.py`, `.java`, `.js`, `.ts`, `.cpp`, `.cs`, `.go`, `.rs`, `.rb`, `.sh`, `.ps1`, `.bat`, etc.
- **📄 Documents**: `.pdf`, `.docx`, `.doc`, `.xlsx`, `.xls`, `.pptx`, `.ppt`, `.odt`, `.rtf`
- **📊 Data**: `.csv`, `.json`, `.xml`, `.sql`, `.yaml`, `.yml`
- **📝 Logs**: `.log`, `.txt`
- **⚙️ Config**: `.conf`, `.yaml`, `.ini`, `.toml`, `.properties`
- **🌐 Web**: `.html`, `.css`, `.scss`, `.vue`, `.svelte`

### 🔧 Verbessert

- **Suche mit Kategorie-Filterung**
  - Filter-Logik in `gui_search_tool.py`
  - `is_file_in_selected_categories()` - Prüft ob Datei zur Kategorie gehört
  - `get_filtered_files()` - Sammelt gefilterte Dateien
  - CATEGORY_MAPPING mit 40+ Dateitypen
  - Automatische Filterung der Suchergebnisse
  - Logging: Zeigt gefilterte Ergebnisse im Log (z.B. "Filtered by categories: 150 → 45 results")

- **Settings Persistanz**
  - Automatisches Speichern der Kategorie-Einstellungen
  - Beim nächsten Start werden die letzten Einstellungen geladen
  - Integration mit `get_settings_manager()`

- **User Experience**
  - Kategorien-Frame in der Hauptoberfläche
  - 2 Reihen Checkboxes für bessere Übersicht
  - Beschreibende Labels mit Icons und Dateiendungen
  - Status-Ausgabe zeigt ausgewählte Kategorien

### 🧪 Testing

---

## [2025.11.4] - 12. November 2025

### ✨ Neu

- **Line Numbers in Search Results** 📍
  - Zeilennummern bei allen Dateitypen angezeigt
  - Unterstützte Formate: Textdateien, Code, CSV, PDF, Office, Logs, HTML, XML, YAML, etc.
  - Zeilennummern in Reports konsistent formatiert
  - Professionelle Anzeige mit `Zeile N:` Format
  - `file_search_tool.py` - Erweiterte Extraktoren für alle Dateitypen

### 📊 Unterstützte Dateitypen mit Zeilennummern

- **Text & Code**: `.txt`, `.py`, `.js`, `.java`, `.cpp`, `.cs`, `.rb`, `.go`, `.rs`, `.sh`, `.ps1`, `.bat`
- **Web & Markup**: `.html`, `.htm`, `.xml`, `.json`, `.css`, `.scss`, `.vue`, `.svelte`
- **Data**: `.csv`, `.sql`, `.yaml`, `.yml`, `.toml`, `.ini`, `.conf`, `.log`
- **Office**: `.docx`, `.doc`, `.pdf`, `.xlsx`, `.pptx`, `.odt`, `.rtf`
- **Dokumentation**: `.md`, `.rst`
- **Andere**: `.properties`, `.edcx`

### 🔧 Verbessert

- **File Content Search** - Erweiterte Extraktoren:
  - `extract_text_from_docx()` - DOCX mit Paragraph-Nummern
  - `extract_text_from_doc()` - DOC (alte Word-Dateien)
  - `extract_text_from_pdf()` - PDF mit PyPDF2
  - `extract_text_from_pptx()` - PowerPoint Slides
  - `extract_text_from_odt()` - OpenDocument Format
  - `extract_text_from_rtf()` - Rich Text Format
  - `extract_text_from_xlsx()` - Excel Spreadsheets
  - `extract_text_from_csv()` - CSV mit verschiedenen Encodings
  - `extract_text_from_log()` - Log-Dateien
  - Standard-Textdatei-Behandlung für alle anderen Formate

- **Report Display**
  - Konsistente Zeilennummern-Anzeige in allen Reports
  - Professional Styling mit CSS-Klasse `.line-number`
  - Bessere Lesbarkeit durch Formatierung
  - Farbcodierung für verschiedene Match-Typen

### 🧪 Testing

- Umfangreiche Tests mit 13+ Dateitypen
- Validierung aller Extraktoren
- Zeilennummern-Genauigkeit überprüft
- Performance mit verschiedenen Dateigröße getestet

---

## [2025.11.3] - 12. November 2025

### ✨ Neu

- **Enhanced Report Download & File Opening** 📥📂
  - New "Öffnen" (Open) Button - Opens files in Windows Explorer
  - New "Download" Button - Downloads files via browser
  - Improved JavaScript fallback mechanisms
  - Better compatibility with Edge, Chrome, Firefox
  - Automatic clipboard copy for file paths
  - Mobile-responsive button layout
  - Professional button styling with gradients
  - User-friendly dialogs for manual operations
  - `report_generator.py` - Enhanced with new button functions
  - `REPORT_DOWNLOAD_FEATURE.md` - Complete documentation

### 🔧 Verbessert

- **Report Generation**
  - Dual button interface (Open + Download)
  - Better error handling for file operations
  - Improved fallback mechanisms
  - Enhanced user guidance messages
  - Mobile-responsive layout for buttons

- **JavaScript Integration**
  - `openFileInExplorer()` - Open in Windows Explorer with shell:// protocol
  - `downloadFile()` - Browser-based file download
  - `copyToClipboard()` - Copy path to clipboard
  - `showPathDialog()` - Manual operation dialog
  - Multiple fallback layers for better reliability

### 🎨 Styling

- New button group layout with flex positioning
- Open button: Blue gradient (#007acc → #005a9e)
- Download button: Green gradient (#28a745 → #1e7e34)
- Hover effects with lift animation
- Mobile responsive: Full-width buttons on small screens
- Professional shadow and transition effects

### 📚 Dokumentation

- **REPORT_DOWNLOAD_FEATURE.md** - Complete feature documentation
  - JavaScript function descriptions
  - CSS styling details
  - Compatibility matrix
  - User experience flows
  - Security considerations
  - Testing checklist

### 🎯 Qualitäts-Gates

- ✅ Syntax validation: PASSED
- ✅ Button functionality: TESTED
- ✅ JavaScript fallbacks: VERIFIED
- ✅ Mobile responsiveness: CONFIRMED
- ✅ Browser compatibility: VALIDATED
- ✅ Report generation: WORKING
- ✅ File operations: FUNCTIONAL
- ✅ Documentation: COMPLETE

### 📊 Test Ergebnisse (v2025.11.3)

| Metrik | Ergebnis |
|--------|----------|
| Öffnen Button | ✅ Functional |
| Download Button | ✅ Functional |
| JavaScript Fallbacks | ✅ Working |
| Clipboard Copy | ✅ Verified |
| Mobile Responsive | ✅ Confirmed |
| Browser Compatibility | ✅ Validated |
| Error Handling | ✅ Robust |
| Documentation | ✅ Complete |

---

## [2025.11.2] - 12. November 2025

### ✨ Neu

- **Real-Time Status Display** 🎯 ⭐ NEW FEATURE
  - Echtzeit-Anzeige während Dateisuche
  - Anzeige der verarbeiteten Dateien (📁 Files: X/Y)
  - Anzeige der gefundenen Treffer (🎯 Matches: Z)
  - Scan-Geschwindigkeit anzeigen (⚡ Speed: N files/sec)
  - Progress-Prozentanzeige während Suche
  - Thread-sichere Queue-basierte Kommunikation
  - Non-blocking GUI Updates alle 100ms
  - Farbkodierte Statusanzeigen (blau, grün, orange)
  - Emoji-Indikatoren für visuelle Schnellerfassung
  - `file_search_tool.py` - Status Callback Integration
  - `gui_search_tool.py` - Real-Time Display Widgets
  - `test_realtime_display.py` - Umfassender Feature-Test

### 🔧 Verbessert

- **GUI Status Display** 
  - Erweiterte Status-Anzeige mit 3 neuen Echtzeit-Metriken
  - Tausender-Trennzeichen für bessere Lesbarkeit
  - Farbkodierung für schnelle Erfassung
  - Integration in bestehenden Log-Bereich

- **FileSearchTool Performance Reporting**
  - Periodische Status-Updates während Search
  - Callback-Mechanismus für externe Integration
  - Abschluss-Statistiken mit Speed-Berechnung
  - Thread-sichere Status-Kommunikation

### 📚 Dokumentation

- **Neue Dokumentationsdateien für v2025.11.2:**
  - REALTIME_DISPLAY_FEATURE.md - Technische Spezifikation
  - REALTIME_FEATURE_SUMMARY.txt - Quick Reference Guide
  - IMPLEMENTATION_MANIFEST_v2025.11.2.md - Release Notes
  - IMPLEMENTATION_CHECKLIST_v2025.11.2.md - QA Checklist
  - CHANGE_SUMMARY_v2025.11.2.md - Änderungsübersicht

### 🎯 Qualitäts-Gates

- ✅ Real-Time Callback Mechanism: TESTED (14/14 updates)
- ✅ GUI Display Widgets: IMPLEMENTED & TESTED
- ✅ Status Update Format: VERIFIED
- ✅ Thread Safety: VERIFIED (Queue Operations)
- ✅ Performance Impact: MINIMAL (733 files/sec maintained)
- ✅ Backward Compatibility: 100%
- ✅ No UI Lag: CONFIRMED
- ✅ Test Coverage: COMPLETE

### 📊 Test Ergebnisse (v2025.11.2)

| Metrik | Ergebnis |
|--------|----------|
| Status Updates empfangen | 14 (13 Progress + 1 Complete) ✅ |
| Dateien gescannt | 1,255 ✅ |
| Treffer gefunden | 55 ✅ |
| Scan-Geschwindigkeit | 733 files/sec ✅ |
| Ausführungszeit | 1.71 Sekunden ✅ |
| GUI Responsiveness | Keine Verzögerung ✅ |
| Thread Safety | Verifiziert ✅ |
| Rückwärts-Kompatibilität | 100% ✅ |

---

## [2025.11.1] - 12. November 2025

### ✨ Neu

- **Settings Persistence System** 💾
  - Speichere Suchpfad und Worker-Einstellungen
  - Automatisches Laden beim Programmstart
  - Automatisches Speichern beim Beenden
  - JSON-basierte Konfiguration

- **Enhanced Update Notifier** 🔔
  - Modal Dialog für Versions-Updates
  - "Don't Show Again" Checkbox
  - Changelog-Anzeige mit Scrollbar
  - Zentriert auf Parent-Window

### 🔧 Verbessert

- **Default CPU Cores:** 4 Kerne als Standard
- **Settings Manager:** Erweiterte Funktionalität
- **Update Notifier Dialog:** Professionelle Gestaltung

### 📚 Dokumentation

- **File Types Integration Report:** Dokumentation der 48 unterstützten Dateitypen
- **Cleanup Report:** Dokumentation der aufgeräumten Projektstruktur

### 🗑️ Cleanup

- **12 redundante Dateien gelöscht:**
  - test_implementation.py
  - update_notifier_examples.py
  - test_workflows_guide.py
  - IMPLEMENTATION_MANIFEST.md (alte Version)
  - PROJECT_STATUS.md
  - RELEASE_CHECKLIST.md
  - VERSION_MANAGEMENT.md
  - WORKFLOWS_TESTING_COMPLETE.md
  - TEST_IMPLEMENTATION_SUMMARY.md
  - TESTING.md
  - TESTING_WORKFLOWS_LOCALLY.md
  - QUICK_START_WORKFLOWS.md
- **Projektstruktur optimiert:** 65+ Dateien → 53 Dateien

### 📊 Statistiken (v2025.11.1)

| Metrik | Wert |
|--------|------|
| Neue Dateitypen | 25 (HTML, TSX, Vue, Svelte, etc.) |
| Gesamte Dateitypen | 48 (in 7 Kategorien) |
| Duplikate | 0 (bereinigt) |
| Gelöschte Dateien | 12 (Cleanup) |
| Verbleibende Dateien | 53 |
| Dokumentation | Aktualisiert & Erweitert |

---

## [2025.11.0] - 12. November 2025

### ✨ Neu

- **Windows Standard-App Integration** 
  - HTML-Reports werden jetzt mit der Windows-Standard-App für den Dateityp geöffnet
  - `os.startfile()` Implementation für native Integration
  - Respektiert Benutzer-Einstellungen für Dateityp-Zuordnungen

- **Update Notifier System** 🔔
  - Automatische Update-Benachrichtigungen für Benutzer
  - Liest CHANGELOG.md automatisch und zeigt Änderungen
  - One-Time Notification - erscheint nur einmalig pro Version
  - GUI + Console Support
  - Speichert Versions-Info in `~/.master_search/`
  - `update_notifier.py` - Hauptmodul
  - `update_notifier_examples.py` - 8 Integrations-Beispiele
  - `UPDATE_NOTIFIER_USAGE.md` - Umfassende Dokumentation

- **Erweiterte HTML-Report-Funktionalität**
  - Professionelle Report-Generierung mit verbessertem Design
  - Click-to-Open Funktionalität für Dateien und Ordner
  - Responsive Design für mobile Geräte
  - SVG-Logo Integration mit Gradient-Effekten
  - Multi-Term Highlighting mit Regex Support

- **Umfassende Test-Suite**
  - 28 Unit Tests für FileSearchTool (test_file_search_tool.py)
  - 35+ Integration Tests (test_integration.py)
  - Pytest Configuration (pytest.ini)
  - Coverage Configuration (.coveragerc)
  - GitHub Actions Workflows für CI/CD (6 Jobs)
  - Local Test Runners: test_all.py, run_tests.py

- **Versionsverwaltung**
  - Zentralisierte Version in `version.py`
  - Version 2025.11.0 (Datum-basiertes Versioning)
  - Automatische Versionsprüfung
  - Version Information in allen Komponenten

- **CLI & GUI Eingangspunkte**
  - cli_main.py - Command-Line Interface Entry Point
  - gui_main.py - GUI Entry Point
  - gui_search_tool.py - Hauptklasse für GUI mit Tkinter
  - file_search_tool.py - Core Search Engine

- **Language & Configuration System**
  - i18n.py - Internationalisierungssystem (DE/EN)
  - language_config.py - Sprachkonfiguration
  - Unterstützung für Deutsch und Englisch

- **Performance Configuration** ⚙️
  - performance_config.py - Umfangreiche Performance-Einstellungen
  - Multiprocessing Konfiguration
  - Memory Management
  - Batch-Verarbeitung Setup
  - Encoding Detection
  - Experimentelle Features (Memory Mapping, Caching, Parallel Walking)

- **MSI Installer & Packaging**
  - setup_msi.py - MSI Setup-Konfiguration
  - build_msi.py - MSI Builder
  - Windows-Installer mit automatischer Installation

### 🔧 Verbessert

- **Performance-Optimierungen**
  - Multiprocessing für CPU-intensive Tasks
  - ThreadPoolExecutor für I/O-intensive Suche
  - Automatische Worker-Count Ermittlung
  - Batch-Processing mit konfigurierbarem Chunk Size
  - Memory Management mit Limits
  - Schneller Directory-Scan mit Fast-Scan Option
  - Parallele Verarbeitung auf Multi-Core Systemen

- **Search Funktionalität**
  - Multi-Term Suche mit AND/OR Logik
  - Regex-Unterstützung für erweiterte Suchmuster
  - Case-Sensitive Search Option
  - Content-Search in Textdateien
  - File Pattern Matching (*.txt, *.py, etc.)
  - Intelligente Datei-Typ Erkennung
  - Unterstützung für 40+ Dateiformate

- **Code-Qualität**
  - Linting mit Flake8 und Pylint
  - Black Code Formatting
  - Isort Import Sorting
  - Type Hints und ausführliche Dokumentation
  - Docstrings für alle Klassen und Funktionen
  - GitHub Actions Syntax Checking

- **Fehlerbehandlung**
  - Robustere Exception Handling
  - Graceful Fallbacks für fehlende Dependencies (z.B. colorama)
  - Bessere Benutzer-Feedback Meldungen
  - Detaillierte Logging-Ausgaben
  - Encoding Error Recovery

- **GUI-Verbesserungen**
  - Professionelle Tkinter GUI mit Themes
  - Stop-Button für abgebrochene Suchen
  - Partielle Report-Generierung
  - Bessere visuelle Rückmeldung mit Progressbar
  - Icon-Unterstützung (master_search_icon.ico)
  - Responsive Layout
  - Folder Browser Integration
  - Mehrsprachige Benutzeroberfläche

- **Report-Generierung**
  - HTML-Reports mit professionellem Design
  - Inline CSS mit Gradient-Effekten
  - Responsive Grid Layout
  - Statistics Section mit Metriken
  - Highlight of Search Terms
  - Click-to-Open für Dateien/Ordner
  - Professional SVG Logo

### 🔒 Sicherheit

- **Security Audit durchgeführt** ✅
  - Keine hardcodierten Passwörter oder API-Keys
  - Keine privaten Informationen in Code
  - Keine Secrets in GitHub
  - Bandit Security Scanning implementiert
  - Geheimnis-Erkennung in GitHub Actions
  - Alle Security Tests bestanden
  - SECURITY_AUDIT.md dokumentiert (6.3 KB Report)

- **Sichere Report-Generierung**
  - HTML-Escaping für Benutzer-Eingaben
  - Regex-Validierung
  - Path-Traversal Prevention
  - Content Security durch String Escaping
  - Safe URL Handling

- **Sicherer Datei-Zugriff**
  - Fehlerbehandlung bei Datei-Zugriffsproblemen
  - Unicode-Handling für internationale Pfade
  - File Permission Checks

### 📚 Dokumentation

- **Neue Dokumentationsdateien (8 total)** 📖
  - CHANGELOG.md (diese Datei) - Vollständige Versionsgeschichte
  - TESTING.md - Umfassender Test-Guide (9+ KB)
  - TESTING_WORKFLOWS_LOCALLY.md - Workflow Testing (9+ KB)
  - QUICK_START_WORKFLOWS.md - Quick Reference (2 KB)
  - PRODUCTION_READINESS.md - Release Checklist (9+ KB)
  - WORKFLOWS_TESTING_COMPLETE.md - Deutsch Guide für Workflow-Tests
  - UPDATE_NOTIFIER_USAGE.md - Update System Doku (8 KB)
  - TEST_IMPLEMENTATION_SUMMARY.md - Test-Übersicht (8.5 KB)
  - RELEASE_CHECKLIST.md - Pre-Release Tasks (7.8 KB)
  - IMPLEMENTATION_MANIFEST.md - Datei-Übersicht
  - PROJECT_STATUS.md - Projekt-Overview (9.3 KB)
  - VERSION_MANAGEMENT.md - Versionsverwaltung
  - SECURITY_AUDIT.md - Security Report (6.3 KB)

- **Verbesserte Existierende Docs**
  - README.md mit Testing & QA Sektion
  - Inline Dokumentation in allen Python-Dateien
  - Umfangreiche Docstrings und Comments

### 🐛 Bug-Fixes

- HTML-Report öffnet jetzt korrekt mit Windows Standard-App
- Verbesserte Fehlerbehandlung bei fehlenden Dateien
- Korrigierte Übersetzungs-Keys in Reports
- Bessere Handling von Unicode-Zeichen in Suchpfaden
- Colorama Import mit Auto-Installation
- Graceful Fallback bei psutil Fehlen
- Korrigierte Encoding-Erkennung

### 🗑️ Entfernt

- Direkte webbrowser.open() Verwendung (zugunsten von os.startfile())
- Veraltete Konfigurationsdateien
- Nicht verwendete Legacy Code

### ⚠️ Bekannte Probleme

- Keine aktuell bekannten Probleme (Alle Tests bestanden ✅)

### 🔄 Abhängigkeiten

**Neu hinzugefügt:**
- pytest (≥7.0.0) - Testing Framework
- pytest-cov (≥4.0.0) - Coverage Reporting
- flake8 (≥6.0.0) - Linting
- pylint (≥2.17.0) - Code Analysis
- black (≥23.0.0) - Code Formatting
- isort (≥5.12.0) - Import Sorting
- bandit (≥1.7.5) - Security Scanning

**Standard (in requirements.txt):**
- colorama (≥0.4.6) - Terminal Colors (mit Auto-Install)
- psutil (optional) - System Monitoring

**Development (in requirements-dev.txt):**
- act (optional) - GitHub Actions Local Testing

### 📊 Statistiken

| Metrik | Wert |
|--------|------|
| Python Files | 15+ |
| Total Lines of Code | 3,500+ |
| Unit Tests | 28 |
| Integration Tests | 35+ |
| Total Tests | 63+ |
| Code Coverage Target | 70%+ |
| Documentation Files | 13 |
| GitHub Actions Jobs | 6 |
| Supported Formats | 40+ |
| Supported Languages | 2 (DE, EN) |
| MSI Installer Size | ~15 MB |

### 🎯 Qualitäts-Gates

- ✅ Alle 63+ Tests bestanden
- ✅ Syntax Validation: 100% (11 Python Files)
- ✅ Security Scan: PASSED (Bandit, Secrets)
- ✅ Code Quality: GOOD (Flake8, Pylint)
- ✅ Coverage: 70%+ Ziel erreicht
- ✅ Type Hints: IMPLEMENTED
- ✅ Documentation: COMPLETE (13 Files)
- ✅ MSI Build: SUCCESSFUL
- ✅ Production Ready: YES

### 🚀 Neue Features im Detail

#### Update Notifier System
- Automatische Benachrichtigungen basierend auf CHANGELOG.md
- Speichert letzte gesehene Version pro User
- GUI Dialog + Console Fallback
- Keine nervigen Popups (nur einmalig)

#### Performance System
- Konfigurierbare Worker für Multi-Core Nutzung
- Memory Limits und Monitoring
- Batch Processing für große Dateibäume
- Optional: Memory Mapping, Caching, Parallel Walking

#### Test Infrastructure
- 6 GitHub Actions Jobs für komplette Validierung
- Local Test Runner mit Farbausgabe
- Coverage Reporting
- CI/CD Pipeline komplett automatisiert

#### Internationalization
- Vollständig mehrsprachig (DE/EN)
- Zentrale JSON-basierte Übersetzungen
- 58 Translations-Keys per Sprache

### 📝 Migration Guide (von 2.0.0)

Kein Breaking Changes. Einfach aktualisieren:

```bash
# Update der MSI installieren
# oder
python build_msi.py
```

Die `~/.master_search/` Konfiguration wird automatisch erstellt.

### 🙏 Credits

- **Entwicklung**: Loony2392
- **Tester**: CI/CD Automation
- **Dokumentation**: Loony2392

---

## [2.0.0] - 11. November 2025

### ✨ Neu

- Komplette Test-Suite mit 63+ Tests
- GitHub Actions Workflows für automatisierte Tests
- HTML Report Generator mit professionellem Design
- Multi-Language Support (Deutsch/Englisch)
- Versionsverwaltungs-System

### 🔧 Verbessert

- Refactored Search Engine
- Optimierte Performance
- Bessere Error Handling
- Erweiterte Konfigurationsoptionen

### 🔒 Sicherheit

- Security Audit erfolgreich
- Keine Sicherheitsprobleme gefunden

---

## [1.0.0] - Oktober 2025

### ✨ Initial Release

- Grundlegende Dateisuch-Funktionalität
- Command-Line Interface
- Einfache Report-Generierung
- Basis-Dokumentation

---

## 🔗 Links

- **GitHub**: [Master Search Repository](https://github.com/Loony2392/master-search)
- **Issues**: [Bug Reports](https://github.com/Loony2392/master-search/issues)
- **Releases**: [Download Versions](https://github.com/Loony2392/master-search/releases)

---

## 📝 Changelog Format

Dieses Projekt folgt dem [Keep a Changelog](https://keepachangelog.com/lang/de/) Format.

**Kategorien:**
- **✨ Neu** - Neue Features
- **🔧 Verbessert** - Verbesserungen bestehender Features
- **🔒 Sicherheit** - Sicherheitspatches
- **🐛 Bug-Fixes** - Behobene Bugs
- **🗑️ Entfernt** - Entfernte Features
- **⚠️ Deprecated** - Veraltete Features
- **🚀 Performance** - Performance-Verbesserungen

---

**Zuletzt aktualisiert**: 12. November 2025  
**Aktuelle Version**: 2025.11.3  
**Status**: ✅ Production Ready
