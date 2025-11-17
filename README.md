# 🔍 Master Search

![Master Search](https://raw.githubusercontent.com/Loony2392/master-search/main/media/master_search_icon_128x128.png)

> Professional file search tool with advanced features and German localization

![Version](https://img.shields.io/badge/version-2025.11.24-blue.svg)
![Python](https://img.shields.io/badge/python-3.11%2B-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

**Author:** [@Loony2392](https://github.com/Loony2392)  
**Email:** b.kolb@loony-tech.de  
**Company:** LOONY-TECH  
**GitHub:** https://github.com/Loony2392/master-search  
**Created:** November 2025

---

## 🚀 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Technical Architecture](#-technical-architecture)
- [Configuration](#-configuration)
- [Supported File Types](#-supported-file-types)
- [Internationalization](#-internationalization)
- [Troubleshooting](#-troubleshooting)
- [Testing & Quality Assurance](#-testing--quality-assurance)
- [Changelog](#-changelog)
- [Author](#-author)
- [License](#-license)

---

## ✨ Features

### Core Search Functionality
- **🔍 Filename Search**: Case-insensitive filename and directory name matching
- **📝 Content Search**: Full-text search inside files with line number tracking
- **🔄 Recursive Search**: Deep directory traversal with intelligent filtering
- **⚡ High Performance**: Multi-threaded processing with optimized algorithms
- **📄 Professional Reports**: Beautiful HTML reports with clickable links and statistics

### Modern User Interface
- **🎨 Colorful Console Output**: Rich terminal interface with emoji support
- **📊 Real-time Progress**: Live statistics and progress tracking
- **🌍 Multilingual Support**: Complete German localization (138+ UI elements)
- **🎯 Responsive Design**: HTML reports work perfectly on all devices
- **✨ Modern Animations**: Smooth 60 FPS loading animations with HorizontalPulseLoader

### Performance & Reliability
- **🚀 Intelligent Scaling**: Automatic worker optimization based on CPU/RAM
- **💾 Memory Efficient**: Smart batch processing for large file sets
- **🔒 Encoding Robust**: Fallback support for UTF-8, Latin-1, CP1252, and more
- **🛡️ Error Handling**: Graceful handling of permission errors and file corruption
- **📦 Large Files**: Automatic skipping of files >50MB to maintain performance

### Cross-Platform Support
- **🏠 Windows**: Native MSI installer with Start Menu integration
- **🍎 macOS**: Native app bundle with macOS-specific utilities
- **🐧 Linux**: Source installation with all dependencies included
- **⚙️ Universal**: Pure Python core works everywhere

---

## 📦 Installation

### Option 1: macOS DMG Package (Recommended for macOS)

1. Download the latest `Master_Search_v2025.11.13_FINAL.dmg` from [Releases](https://github.com/Loony2392/master-search/releases)
2. Double-click the DMG to mount it
3. Drag the "Master Search" app to your Applications folder
4. Launch from Applications or Spotlight (Cmd+Space)

**Benefits:** Native macOS app, optimized for Apple Silicon & Intel, no dependencies required

### Option 2: Windows MSI Installer (Recommended for Windows)

1. Download the latest `Master_Search-2025.11.24-win64.msi` from [Releases](https://github.com/Loony2392/master-search/releases)
2. Double-click the MSI and follow the installation wizard
3. **Shortcuts are created automatically:**
   - Start Menu: "Master Search" (GUI) and "Master Search CLI"
   - Desktop: "Master Search" (GUI) and "Master Search CLI"
4. Launch from Start Menu or Desktop

**Benefits:** No Python required, native shortcuts, clean Windows integration, automatic uninstaller, 6.3 MB lightweight install

### Option 3: Python Source (All Platforms)

**Requirements:**
- Python 3.12 or higher
- pip package manager

**Installation:**
```bash
# Clone the repository
git clone https://github.com/Loony2392/master-search.git
cd master-search

# Install dependencies
pip install -r requirements.txt

# Run the application
python gui_main.py
```

### Option 4: Build from Source

For developers who want to build custom versions:

```bash
# Install build dependencies
pip install -r requirements-dev.txt

# Build macOS DMG (macOS only)
python build_dmg.py

# Build Windows MSI (Windows only)
python build_msi.py

# Build documentation
python -m build --sdist
```

---

## 🎯 Usage

### Graphical Interface (Recommended)

```bash
# Start the modern GUI
python gui_main.py
```

1. **Enter search terms**: Type one or more search patterns (comma/semicolon separated)
2. **Select directory**: Browse or type the path to search
3. **Choose file types**: Select specific extensions or search all files
4. **Configure options**: Set case sensitivity, content search, etc.
5. **Start search**: Click "Search" and watch real-time progress
6. **View results**: HTML report opens automatically with detailed findings

### Command Line Interface

```bash
# Start CLI mode
python file_search_tool.py

# Example usage
python file_search_tool.py --search "config,settings" --path "/home/user/projects" --types ".json,.ini,.conf"
```

### Batch Processing

```bash
# Search multiple patterns across different directories
python cli_main.py --batch --config search_config.json
```

---

## 🛠️ Technical Architecture

### System Overview

```
Master Search Architecture
├── 🎨 User Interface Layer
│   ├── GUI (gui_main.py, gui_search_tool.py)
│   ├── CLI (cli_main.py, file_search_tool.py)
│   └── Animations (loading_animations.py)
├── 🔍 Core Search Engine
│   ├── File System Scanner
│   ├── Content Analyzer
│   ├── Pattern Matcher
│   └── Result Aggregator
├── 🌍 Internationalization
│   ├── Translation System (i18n.py)
│   ├── Language Configuration (language_config.py)
│   └── Locale Files (locales/*.json)
├── 📊 Reporting System
│   ├── HTML Template Engine
│   ├── Statistics Calculator
│   ├── Export Utilities
│   └── Report Generator (report_generator.py)
└── ⚙️ System Integration
    ├── Performance Configuration
    ├── Settings Management
    ├── Cross-Platform Utilities
    └── Build Scripts
```

### Search Algorithm

1. **Directory Traversal**: Recursive scanning with `os.walk()` optimization
2. **File Filtering**: Extension-based filtering with configurable patterns
3. **Content Analysis**: 
   - Intelligent encoding detection (UTF-8, Latin-1, CP1252)
   - Line-by-line processing for memory efficiency
   - Pattern matching with case-insensitive options
   - Line number tracking for precise result reporting
4. **Result Aggregation**: Structured data collection with metadata
5. **Report Generation**: Template-based HTML report creation

### Performance Optimizations

- **Lazy Loading**: Files are read only when necessary
- **Encoding Fallbacks**: Multiple encoding attempts for compatibility
- **Size Limits**: Large files (>50MB) are automatically skipped
- **Batch Processing**: Efficient processing in configurable chunks
- **Memory Management**: No full file loading into memory
- **Thread Pool**: Optimized worker threads based on system resources

---

## ⚙️ Configuration

### Performance Settings

Edit `performance_config.py`:

```python
PERFORMANCE_CONFIG = {
    'MAX_FILE_SIZE_MB': 50,           # Skip files larger than 50MB
    'BATCH_SIZE': 1000,               # Process files in batches
    'MAX_WORKERS': None,              # Auto-detect based on CPU cores
    'MEMORY_LIMIT_MB': 1024,          # Memory usage limit
    'TIMEOUT_SECONDS': 300            # Search timeout
}
```

### Language Settings

Edit `language_config.py`:

```python
LANGUAGE_CONFIG = {
    'default_language': 'en',         # Default to English
    'fallback_language': 'en',        # Fallback language
    'auto_detect': True,              # Auto-detect system language
    'available_languages': ['en', 'de', 'fr']
}
```

### Application Settings

Edit `settings_manager.py` for advanced configuration:

```python
SETTINGS = {
    'search': {
        'case_sensitive': False,
        'include_hidden_files': False,
        'max_results': 10000
    },
    'ui': {
        'theme': 'modern',
        'animations_enabled': True,
        'auto_open_reports': True
    }
}
```

---

## 📁 Supported File Types

Master Search intelligently handles various file types:

### Text Files (Content Search)
- **Documents**: `.txt`, `.md`, `.rst`, `.doc`, `.docx`
- **Source Code**: `.py`, `.js`, `.html`, `.css`, `.java`, `.cpp`, `.c`, `.h`
- **Configuration**: `.json`, `.xml`, `.yml`, `.yaml`, `.ini`, `.conf`, `.cfg`
- **Data Files**: `.csv`, `.tsv`, `.log`, `.sql`
- **Web Files**: `.php`, `.asp`, `.jsp`, `.tsx`, `.jsx`

### Binary Files (Filename Search Only)
- **Images**: `.jpg`, `.png`, `.gif`, `.bmp`, `.svg`, `.ico`
- **Archives**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`
- **Executables**: `.exe`, `.msi`, `.deb`, `.rpm`, `.dmg`
- **Media**: `.mp3`, `.mp4`, `.avi`, `.mkv`, `.wav`

### Custom File Type Configuration

Create a custom file type filter:

```python
CUSTOM_FILE_TYPES = {
    'source_code': ['.py', '.js', '.java', '.cpp'],
    'documents': ['.txt', '.md', '.doc', '.pdf'],
    'config_files': ['.json', '.xml', '.yml', '.ini']
}
```

---

## 🌍 Internationalization

Master Search features complete internationalization with professional translations.

### Supported Languages

- **🇺🇸 English (en)**: Default language, 138+ strings
- **🇩🇪 German (de)**: Complete localization, 138+ strings
- **🇫🇷 French (fr)**: Basic localization, 100+ strings

### Translation System

The i18n system uses JSON-based translations:

```python
# Usage in code
from i18n import _
print(_("search_started"))  # Auto-translates based on system locale
```

### Adding New Languages

1. Create `locales/{language_code}.json`
2. Copy structure from `locales/en.json`
3. Translate all strings
4. Test with `python test_realtime_display.py`

Example translation file structure:

```json
{
    "app_title": "Master Search",
    "search_button": "Search",
    "results_found": "{count} results found",
    "language_name": "English"
}
```

### Current Translation Coverage

| Language | Coverage | Status |
|----------|----------|---------|
| English  | 138/138  | ✅ Complete |
| German   | 138/138  | ✅ Complete |
| French   | 100/138  | 🔄 In Progress |

---

## 🔧 Troubleshooting

### Common Issues

#### 🐍 **ModuleNotFoundError: colorama**
```bash
# Solution 1 - Install via requirements
pip install -r requirements-minimal.txt

# Solution 2 - Direct installation
pip install colorama

# Solution 3 - Automatic installation
# The tool auto-installs colorama on first run
```

#### 🔒 **PermissionError: File Access Denied**
```
Error: [Errno 13] Permission denied: 'file.txt'
```
**Solutions:**
- Run as Administrator (Windows) or with sudo (Linux/macOS)
- Check file permissions: `chmod 644 file.txt`
- Verify antivirus software isn't blocking access

#### 🌐 **HTML Report Won't Open Automatically**
```
Could not automatically open browser
```
**Solutions:**
- Manually open the HTML file (path is displayed in console)
- Check default browser settings
- Try different browser: `firefox report.html`

#### 📦 **MSI Installation Issues**

**Problem:** "This app can't run on your PC"
```
Solution 1: Run MSI as Administrator
Solution 2: Temporarily disable Windows SmartScreen
Solution 3: Request digitally signed version
```

**Problem:** "Windows protected your PC" SmartScreen warning
```
Solution: Click "More info" → "Run anyway"
Note: This is normal for unsigned applications
```

**Problem:** MSI build fails
```bash
# Check dependencies
pip install cx_Freeze>=6.15.0

# Install Windows Build Tools
# Visual Studio Build Tools required

# Try updated build
python -m pip install --upgrade setuptools wheel
python build_msi.py
```

#### ⚡ **Performance Issues**

**Problem:** Very slow search
```
Solution 1: Test with smaller directories first
Solution 2: Install psutil for optimized worker count
Solution 3: Use SSD instead of HDD for better I/O
Solution 4: Exclude large binary files
```

**Problem:** High memory usage
```
Solution 1: Reduce batch size in performance_config.py
Solution 2: Configure fewer worker threads
Solution 3: Temporarily disable antivirus real-time scanning
Solution 4: Close other memory-intensive applications
```

#### 🔍 **No Results Found**
```
🚫 No results found
```
**Possible causes:**
- Search term doesn't exist in files
- Directory contains only binary files
- Encoding issues with text files
- Search path is incorrect
- File permissions prevent access

#### 🖥️ **Windows MSI Shortcuts Not Appearing**
```
Start Menu or Desktop shortcuts missing after installation
```
**Solution:**
- Shortcuts are created automatically during MSI installation via cx_Freeze
- If missing, they were not installed (uncommon issue)
- Manual workaround: Create shortcuts manually pointing to:
  - GUI: `C:\Program Files\Master Search\Master_Search.exe`
  - CLI: `C:\Program Files\Master Search\MasterSearch_CLI.exe`

### Debug Mode

Enable detailed logging for advanced troubleshooting:

```python
# Add to beginning of main() function
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

Or use environment variable:
```bash
# Windows
set DEBUG=1 && python gui_main.py

# Linux/macOS
DEBUG=1 python gui_main.py
```

---

## 🧪 Testing & Quality Assurance

Master Search includes comprehensive testing and quality assurance:

### Local Testing

```bash
# Simple test runner
python test_all.py

# Detailed unit tests
pytest tests/test_file_search_tool.py -v

# Integration tests
pytest tests/test_integration.py -v

# All tests with coverage report
pytest tests/ -v --cov=file_search_tool --cov-report=html
```

### Test Coverage

- ✅ **28 Unit Tests** - FileSearchTool functionality
- ✅ **35+ Integration Tests** - Module interactions
- ✅ **Syntax Checking** - py_compile validation
- ✅ **Linting** - Flake8, Pylint analysis
- ✅ **Security Scan** - Bandit security checks
- ✅ **Functional Tests** - End-to-end validation

### GitHub Actions Workflows

Automated testing on every push and pull request:

- 🔍 **test.yml** - Quality assurance pipeline with multi-platform testing
- 🚀 **release.yml** - Automated build and release on git tags
- 🔒 **security.yml** - Daily security audits and vulnerability scanning
- ⚡ **performance.yml** - Weekly performance monitoring and benchmarks

See [.github/workflows/README.md](.github/workflows/README.md) for detailed workflow documentation.

---

## 📝 Changelog

### 🎉 **Version 2025.11.24** (November 2025)
- **⚡ Native cx_Freeze Shortcuts**: Automatic Start Menu and Desktop shortcuts during installation
- **🚀 Optimized Build Process**: Build time reduced from 316s to 126s (60% faster)
- **🧹 Simplified Codebase**: Removed WiX/NSIS alternatives, streamlined to native cx_Freeze
- **📦 Lightweight MSI**: 6.3 MB base install without OCR dependencies
- **🔄 Automatic Version Management**: Version automatically pulled from version.py
- **✅ Production Ready**: Final optimized installer for distribution

### 🎉 **Version 2025.11.13** (November 2025)
- **🍎 macOS Native DMG Package**: Professional app bundle with Python 3.12 + tkinter
- **🔧 Release Organization**: Structured `releases/` folder for macOS, Windows, and Linux
- **✨ Build System Refactor**: Updated py2app, PyInstaller, and cx_Freeze configurations
- **🌍 Cross-Platform Config**: Platform-aware paths (macOS, Linux, Windows)
- **🧪 Test Infrastructure**: Pytest setup with conftest.py and import path resolution
- **🚀 Production Ready**: All build scripts configured for distribution

### 🔮 **Planned Features** (Version 2025.12.0)
- **🔍 Regex Search**: Advanced pattern matching with regular expressions
- **📁 Exclusion Filters**: Configurable file and directory exclusions
- **💾 Configuration Profiles**: Reusable search configurations
- **🔄 Batch Mode**: Automated scheduled searches
- **📧 Email Reports**: Scheduled report delivery
- **🌐 Web Interface**: Browser-based remote access

---

## 👨‍💻 Author

**Loony2392 ([@Loony2392](https://github.com/Loony2392))**
- 📧 **Email:** b.kolb@loony-tech.de
- 🏢 **Company:** LOONY-TECH
- 🌍 **Location:** Germany
- 💼 **Role:** Software Developer & IT Specialist
- 🐙 **GitHub:** [@Loony2392](https://github.com/Loony2392)

### 🚀 **About the Author**
Loony2392 is an experienced software developer at LOONY-TECH, specializing in Python applications and automation solutions. With extensive experience in developing tools for file management and data analysis, he creates practical solutions for everyday IT challenges.

### 🎯 **Project Motivation**
Master Search was developed at LOONY-TECH to provide IT professionals and developers with a powerful, user-friendly file search tool. The project combines enterprise functionality with an appealing user interface and professional reporting capabilities.

---

## 📜 License

```
MIT License

Copyright (c) 2025 LOONY-TECH - Loony2392 (@Loony2392)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

- **Python Community** for the excellent language and libraries
- **colorama developers** for cross-platform color support
- **LOONY-TECH** for development support and resources
- **Open Source Community** for inspiration and best practices
- **Contributors** for testing, feedback, and improvements

---

## 📞 Support & Contact

Questions, suggestions, or need support?

- 📧 **Email:** b.kolb@loony-tech.de
- 🐛 **Bug Reports:** [Create an issue](https://github.com/Loony2392/master-search/issues)
- 💡 **Feature Requests:** [Start a discussion](https://github.com/Loony2392/master-search/discussions)
- 📖 **Documentation:** This README is regularly updated
- 🌐 **Website:** [GitHub Pages](https://loony2392.github.io/master-search/)

---

<div align="center">

**⭐ If you like Master Search, give us a star! ⭐**

*Developed with ❤️ by Loony2392*

![GitHub Repo Stars](https://img.shields.io/github/stars/Loony2392/master-search?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Loony2392/master-search?style=social)
![GitHub Watchers](https://img.shields.io/github/watchers/Loony2392/master-search?style=social)

[📦 Download Latest Release](https://github.com/Loony2392/master-search/releases/latest) | 
[📖 View Documentation](https://loony2392.github.io/master-search/) | 
[🐛 Report Issues](https://github.com/Loony2392/master-search/issues) | 
[💬 Join Discussions](https://github.com/Loony2392/master-search/discussions)

</div>