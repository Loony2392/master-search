# Master Search - User Guide

**Version:** 2025.11.7  
**Last Updated:** November 12, 2025  
**Languages:** English · Deutsch · Français

---

## 📑 Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Basics](#basics)
4. [Main Features](#main-features)
5. [Search Techniques](#search-techniques)
6. [HTML Reports](#html-reports)
7. [Settings](#settings)
8. [Tips & Tricks](#tips--tricks)
9. [FAQ](#faq)
10. [Troubleshooting](#troubleshooting)

---

## Overview

**Master Search** is a powerful desktop tool for full-text file system search. It enables fast and efficient searching in files and folders with advanced filtering options and beautiful HTML reports.

### What can Master Search do?

✅ **Fast file search** - Searches millions of files in seconds  
✅ **Full-text search** - Searches file contents  
✅ **Regex support** - Regular expressions for complex patterns  
✅ **HTML Reports** - Automatic generation of beautiful reports with animations  
✅ **59+ file types** - Supports code, documents, archives and more  
✅ **Multilingual** - German, English, French  
✅ **Real-time display** - See search results as they appear  
✅ **Clipboard integration** - One-click copy of file paths  

---

## Installation

### Windows MSI Installer (Recommended)

1. **Download** the latest MSI file from the release page
2. **Double-click** `Master_Search_Setup_v2025.11.7.msi`
3. **Follow Setup Wizard:**
   - Choose installation folder (default: `C:\Program Files\Master Search`)
   - Create Start Menu shortcut (optional)
   - Create Desktop shortcut (optional)
4. **Finish** - Master Search is ready to use immediately

### Portable Version

1. **Download** the portable ZIP file
2. **Extract** to desired directory
3. **Run** `master_search.exe` (no setup required)
4. **Optional:** Create desktop shortcut

### System Requirements

| Requirement | Version |
|-------------|---------|
| **Windows** | 7 SP1 or newer |
| **Memory** | 512 MB RAM minimum |
| **Disk Space** | 100 MB free space |
| **Browser** | Modern browser for HTML reports |

---

## Basics

### User Interface

The Master Search GUI consists of four main areas:

```
┌─────────────────────────────────────────────────────────┐
│  Master Search v2025.11.7                         [_][□][X]│
├─────────────────────────────────────────────────────────┤
│  SEARCH AREA                                            │
│  ┌────────────────────────────────────────────────────┐ │
│  │ Search Term:        [________________]              │ │
│  │ File Type Filter:   [All] [Code only] [Documents]  │ │
│  │ Search Location:    [C:\]  [Browse...]             │ │
│  │ ☐ Search in files  ☐ Case sensitive                │ │
│  │ ☐ Regular expressions ☐ Generate HTML report      │ │
│  │                     [START SEARCH]                  │ │
│  └────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│  REAL-TIME RESULTS                                      │
│  ┌────────────────────────────────────────────────────┐ │
│  │ 💾 C:\Projects\README.md         [📋] [📂] [🗑️]   │ │
│  │ 💾 C:\Projects\config.json       [📋] [📂] [🗑️]   │ │
│  │ 📄 C:\Docs\report.docx           [📋] [📂] [🗑️]   │ │
│  │ Searching... 145 results found                      │ │
│  └────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ ✓ Done! 247 files searched, 12 matches found           │
└─────────────────────────────────────────────────────────┘
```

### Interface Elements

| Element | Description |
|---------|-------------|
| **Search Term** | The word or phrase you're looking for |
| **File Type Filter** | Restrict to specific file types (optional) |
| **Search Location** | Directory to search in |
| **Search in files** | Search file contents (not just names) |
| **Case sensitive** | Distinguish between uppercase and lowercase |
| **Regular expressions** | Use regex pattern instead of plain text |
| **Generate HTML report** | Auto-generate report after search |

---

## Main Features

### 1. Simple File Search

**Scenario:** You want to find all Python files named `test`

**Steps:**
1. **Search Term:** Enter `test`
2. **File Type Filter:** Choose "Code"
3. **Search Location:** Choose root directory or `C:\`
4. **Click [START SEARCH]**

**Result:**
- All `.py`, `.js`, `.ts` etc. with "test" in name are displayed
- Results appear in real-time
- After completion: Statistics (e.g., "247 files searched, 12 matches")

### 2. Full-Text Search in Files

**Scenario:** You want to find a specific function in all code files

**Steps:**
1. **Search Term:** e.g., `def calculate_total` 
2. **File Type Filter:** Choose "Code"
3. ☑️ **"Search in files"** enable (important!)
4. **Search Location:** Choose project directory
5. **Click [START SEARCH]**

**Result:**
- Only files containing the text are shown
- Search term is highlighted in report
- Line numbers show exact position of text

### 3. Regex Search (Advanced Users)

**Scenario:** You want to find all email addresses in files

**Steps:**
1. **Search Term:** `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}` 
2. ☑️ **"Regular expressions"** enable
3. ☑️ **"Search in files"** enable
4. **File Type Filter:** "All" (to search all file types)
5. **Click [START SEARCH]**

**Popular Regex Patterns:**
```regex
# Email addresses
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

# Phone numbers (US)
(\+1|1)?[-.\s]?\(?[0-9]{3}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}

# File sizes (bytes, KB, MB, GB)
\d+\s*(B|KB|MB|GB|TB)

# IP addresses
\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}

# URLs
https?://[^\s]+

# JSON file sizes
"size"\s*:\s*(\d+)
```

### 4. Case Sensitivity

**Default behavior:** Search ignores case
- `test` finds: Test, TEST, tEsT

**When enabled:** Considers uppercase/lowercase
- `Test` finds only: Test (not test or TEST)

**When to use:**
- Code variables: `myVariable` vs `myVariable`
- Filenames: `README` vs `readme`
- Configurations: Often case-sensitive!

---

## Search Techniques

### Multiple Search Terms

Master Search supports multiple search terms separated by spaces:

```
Search Term: function main utils
```

This finds files containing **all** of these terms:
- ✅ `function main(utils)`
- ✅ `Utils class with main function`
- ❌ `function main` (missing "utils")

### File Type Filters

Predefined categories:

| Filter | File Types |
|--------|-----------|
| **Code** | `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.c#`, `.go`, `.rs` etc. |
| **Web** | `.html`, `.css`, `.php`, `.js`, `.vue`, `.jsx` etc. |
| **Data** | `.json`, `.xml`, `.yaml`, `.csv`, `.sql`, `.db` etc. |
| **Documents** | `.pdf`, `.docx`, `.xlsx`, `.pptx`, `.md`, `.txt` etc. |
| **Configuration** | `.ini`, `.cfg`, `.conf`, `.env`, `.properties` etc. |
| **Archives** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` etc. |

### Search Location Selection

**Quick Selection:**
- `C:\` - Entire hard drive
- `C:\Users\` - User files only
- `C:\Program Files\` - Programs only

**Custom Path:**
1. Click **[Browse...]**
2. Select desired directory
3. Click **OK**

**Tips:**
- ⚡ Narrower directories are faster
- 🔒 System folders (Windows, System32) are often read-only
- 🚫 Network paths can be slow

---

## HTML Reports

### What are HTML Reports?

Automatically generated reports with:
- 📊 **Statistics** - Number of matches, files searched
- 📁 **Categories** - Overview by file types
- ✨ **Animations** - Professional fade-in effects
- 🔗 **Interactive links** - Open files directly
- 📋 **Clipboard function** - Copy paths
- 🎨 **Responsive design** - Works on all devices

### Creating a Report

**Automatically during search:**
1. ☑️ **"Generate HTML report"** enable
2. Run search normally
3. After completion: Report opens automatically

**Storage Location:**
```
C:\Users\<YourUsername>\AppData\Local\Master Search\Reports\
  ├── search_results_20251112_153249.html
  ├── search_results_20251112_153418.html
  └── search_results_20251112_154523.html
```

### Report Features

#### 📋 Copy to Clipboard
- Click on a file path in the report
- Path automatically copied to clipboard
- Notification confirms successful copy

#### 📂 Open Folder
- Click the folder icon next to a file
- Opens the folder with the file in Explorer

#### 🔍 Highlighting
Search terms are color-highlighted:
- **Orange** - Found search terms
- **Line X** - Exact position in text

#### 📊 Category Overview
Automatic analysis:
```
📁 File Types
┌─────────────────────┐
│ Python        145   │
│ JSON           89   │
│ Markdown       54   │
│ YAML           28   │
│ XML            12   │
└─────────────────────┘
```

#### ✨ Animations
- Report loads with blank background
- Elements fade in sequentially
- Professional, polished appearance
- No performance impact

---

## Settings

### Language Selection

Master Search automatically detects system language:
- 🇬🇧 **English** - Windows in English
- 🇩🇪 **Deutsch** - Windows in German
- 🇫🇷 **Français** - Windows in French

**Manual Selection:**
In most dialogs, click "Language" to switch.

### Performance Settings

**Default settings (optimal):**
- Multi-processing active
- Maximum CPU utilization
- Fastest search

**For slower PCs:**
- Reduce hardware demands
- Fewer worker threads
- Longer search, but more stable

### Error Handling

Master Search automatically ignores:
- 🔒 **Read-only files** - No permission
- ⚠️ **Corrupted files** - Cannot be read
- 🔁 **Symbolic links/Junctions** - Prevent infinite loops
- 🌐 **Network errors** - Offline drives

---

## Tips & Tricks

### ⚡ Faster Searches

1. **Choose narrower directories**
   - Instead of `C:\` → use `C:\Projects\`
   - 10x faster!

2. **Use file type filters**
   - Instead of "All" → only "Code" or "Documents"
   - Reduces files to search by 70%

3. **Use specific search terms**
   - `function main` instead of `main`
   - Fewer matches = faster processing

### 🎯 More Accurate Searches

1. **Enable case sensitivity**
   - When you need exact matches

2. **Use regex for complex patterns**
   - `^import.*os$` - Only `import os` lines
   - `def\s+\w+\(` - All function definitions

3. **Enable "Search in files"**
   - To search file contents instead of just names

### 📊 Report Analysis

1. **Sort by file types**
   - Categories in report show distribution
   - Useful for project structure analysis

2. **Multilingual search**
   - German: `Ñame`, `Größe`
   - English: `Name`, `Size`
   - One report for all!

3. **Trend analysis**
   - Save multiple reports
   - Compare file counts over time

### 🛠️ For Developers

**Search Python projects:**
```
Search Term: TODO
Filter: Code
Search in files: ☑️
```

**Find all imports:**
```
Search Term: ^import
Regex: ☑️
Filter: Code
```

**Find config files:**
```
Search Term: api_key
Filter: Configuration
Search in files: ☑️
```

---

## FAQ

### Q: How long does a search take?

**A:** Depends on:
- **Directory size:** 1000 files ≈ 1 second
- **Search location:** Local drive vs. network
- **File type filter:** Faster with filter
- **Search in files:** Slower than name-only search

**Examples:**
- `C:\Projects\` (10,000 files): ~10 seconds
- `C:\` (500,000 files): ~5 minutes
- With filter: 2-3x faster

### Q: Where are reports stored?

**A:**
```
Windows 7/8/10/11:
C:\Users\<YourUsername>\AppData\Local\Master Search\Reports\
```

**Open folder:**
1. Open GUI → Right-click on report
2. Click "Open folder"
3. See all reports

### Q: Can I cancel a search?

**A:** Yes!
- While search is running: **[CANCEL]** button appears
- Click it to stop immediately
- Previous results are retained

### Q: What's the difference between "Search in files" and normal filter?

**A:**
```
WITHOUT "Search in files":
  Searches file names only
  test.py ✅
  testing.txt ✅
  mytestfile.py ✅
  
WITH "Search in files":
  Searches file contents too
  file_with_test_in_content.py ✅
  + all of above also
```

### Q: Does Master Search support wildcards?

**A:**
- **Normal search:** No (but you can use regex)
- **With regex:** Yes!
  - `test.*\.py` - test123.py, testfile.py, etc.
  - `\.log$` - Only .log files at end

### Q: Can I search network drives?

**A:** Yes, but:
- ✅ SMB/CIFS network shares work
- ⚠️ Can be slow (network latency)
- 🔒 Requires access permission
- 💡 **Tip:** Locally "mount" network drive for better performance

### Q: How can I print a report?

**A:**
1. Open report in browser
2. Press **Ctrl+P** (or File → Print)
3. Choose printer
4. ✓ Can also save as PDF!

### Q: Which file types are supported?

**A:** 59+ file types:
- **Code:** Python, JavaScript, Java, C++, C#, Go, Rust, PHP, Ruby, etc.
- **Web:** HTML, CSS, SCSS, Vue, React, Angular, etc.
- **Data:** JSON, XML, YAML, CSV, SQL, etc.
- **Documents:** PDF, DOCX, XLSX, PPTX, Markdown, TXT, etc.
- **Config:** INI, CONF, ENV, Properties, etc.
- **Archives:** ZIP, RAR, 7Z, TAR, GZ, etc.

Full list: [SUPPORTED_FILE_TYPES.md](../SUPPORTED_FILE_TYPES.md)

### Q: Do I need the internet for Master Search?

**A:** No!
- ✅ Fully functional offline
- ✅ No data transmission
- ✅ Privacy guaranteed
- ℹ️ Browser update for HTML reports is optional

---

## Troubleshooting

### Problem: Search is very slow

**Solutions:**
1. Choose narrower directory
   - Instead of `C:\` → `C:\Projects\`
2. Use file type filter
   - Instead of "All" → "Code"
3. Disable "Search in files"
   - If you only need file names
4. Use more specific search terms
   - `main.py` instead of `main`

### Problem: "Access denied" error

**Causes & Solutions:**
1. Administrator rights required
   - Open GUI with right-click → "Run as Administrator"
2. File in use
   - Close other programs
3. Antivirus blocking access
   - Add Master Search to whitelist

### Problem: Report doesn't open

**Solutions:**
1. Check browser settings
   - Allow opening local files?
2. Disable popup blocker
   - Report opens in new tab
3. Switch default browser
   - Change in Windows settings
4. Open HTML file manually
   - Open Reports folder, double-click HTML file

### Problem: Certain file types are ignored

**Causes:**
1. File type filter too restrictive
   - Set to "All"
2. File extension not in whitelist
   - See SUPPORTED_FILE_TYPES.md for details

### Problem: Regex doesn't work

**Common mistakes:**
1. Regex option not enabled
   - ☑️ "Regular expressions" checkbox
2. Syntax error in regex
   - Too many `(` without closing
   - Invalid escape sequences
3. Pattern variations
   - `\d` in raw strings ✅
   - `\\d` (double backslash) also possible

**Test tools:**
- [regex101.com](https://regex101.com) - Online regex tester
- Test pattern there before using in Master Search

### Problem: Master Search doesn't respond

**Solutions:**
1. Cancel search
   - Click [CANCEL] button
2. Close with Ctrl+Z
3. Restart
   - Should take 1-2 seconds normally

---

## Advanced Topics

### Command-Line Interface (CLI)

Master Search can also be used from command line:

```powershell
# Basic search
python cli_main.py --search test --path C:\Projects

# With options
python cli_main.py --search main --path C:\src --in-files --regex

# Generate report
python cli_main.py --search TODO --path . --report

# All options
python cli_main.py --help
```

### Integration with Other Tools

**Example: PowerShell Pipeline**
```powershell
# Search + Report processing
master_search.exe --search error --path C:\Logs | Process-SearchResults
```

**Example: Windows Scheduler**
```
Scheduled Task → Master Search → daily at 22:00
Report automatically generated and emailed
```

---

## Support & Contact

**Found issues?**
- 📧 Email: info@loony-tech.de
- 🐛 Bug Report: [GitHub Issues](https://github.com/Loony2392/master-search)
- 💬 Questions: Community Forum (coming soon)

**Version Information:**
- **Current Version:** 2025.11.7
- **Last Update:** November 12, 2025
- **Author:** Loony2392
- **License:** Proprietary

---

## License & Legal

Master Search™ - Professional File Search Tool
© 2025 Loony2392 & LOONY-TECH. All rights reserved.

**Privacy:**
- ✅ No data collection
- ✅ No telemetry
- ✅ Fully offline
- ✅ Local processing only

---

**Happy searching! 🚀**

*Master Search - Professional File Search with Beautiful Reports*
