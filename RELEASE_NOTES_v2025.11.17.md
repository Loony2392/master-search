# Master Search v2025.11.17 - Release Notes

**Release Date:** November 13, 2025  
**Build:** macOS DMG (Apple Silicon & Intel)  
**Status:** ✅ Production Ready

---

## 🎯 Focus: Comprehensive File Categories Overhaul (1000+ File Types)

### ✨ What's New

#### 📁 Massive Category & File Type Expansion
- **New Categories Added:** 8 additional categories for comprehensive coverage
  - ✅ Markup (Markdown, AsciiDoc, LaTeX, etc.)
  - ✅ Spreadsheets (Excel, Calc, Google Sheets formats)
  - ✅ Presentations (PowerPoint, Impress, Keynote formats)
  - ✅ Databases (SQL, SQLite, MongoDB, MySQL formats)
  - ✅ Media (Images, Audio, Video - 100+ formats)
  - ✅ Archives (ZIP, RAR, 7Z, TAR, Brotli, etc.)
  - ✅ Fonts (TTF, OTF, WOFF, EOT, etc.)
  - ✅ Text Files (Plain text, logs, subtitles, playlists)

- **Total Categories Now:** 14 (previously 6)
  1. 💻 Code (40+ programming languages)
  2. 📝 Markup (Documentation formats)
  3. 📄 Documents (Office documents)
  4. 📊 Spreadsheets
  5. 🎬 Presentations
  6. 📈 Data (JSON, XML, YAML, Protocol Buffers)
  7. 🗄️ Databases
  8. 📝 Logs
  9. ⚙️ Config (Docker, Kubernetes, Terraform, Ansible)
  10. 🌐 Web (HTML, CSS, Vue, Svelte, Templates)
  11. 🖼️ Media (Images, Audio, Video)
  12. 📦 Archives
  13. 🔤 Fonts
  14. 📄 Text Files

#### 🗂️ File Type Support Expansion
- **1000+ File Extensions** now supported in category mapping
- **Programming Languages:** 40+ languages covered
  - C, C++, Java, Python, JavaScript, TypeScript, Go, Rust, Ruby, PHP, etc.
  - Functional: Haskell, OCaml, F#, Lisp, Clojure, Elixir, Erlang
  - Systems: Rust, Go, Zig, Assembly, Kotlin
  - Scripts: Bash, Zsh, Fish, PowerShell, Batch, Perl

- **Markup & Documentation:**
  - Markdown variants (.md, .mdown, .mkd)
  - AsciiDoc, reStructuredText, Textile, Org-mode
  - LaTeX, Pandoc, Hugo formats

- **Office & Data:**
  - Microsoft: .docx, .xlsx, .pptx (.xltm, .potx variants)
  - OpenDocument: .odt, .ods, .odp
  - Apple: .pages, .numbers, .key
  - Data: JSON-L, NDJSON, Protocol Buffers, Avro, CBOR, BSON

- **Web & Templates:**
  - Vue, Svelte, Astro, Qwik
  - Handlebars, EJS, ERB, Haml, Slim, Blade, Jinja, Twig, Liquid

- **Media (100+ formats):**
  - Images: PNG, JPEG, WebP, SVG, BMP, TIFF, RAW, HEIC
  - Audio: MP3, FLAC, AAC, OGG, OPUS, ALAC, WAV, MIDI
  - Video: MP4, WebM, MKV, AVI, MOV, FLV, 3GP, TS, VOB

- **Config & Infrastructure:**
  - Docker, Docker Compose, Kubernetes/K8s
  - Terraform, CloudFormation
  - Ansible, Chef, Puppet, SaltStack
  - Nginx, Apache, Git, EditorConfig
  - Shell: .bashrc, .zshrc, .fishrc, .screenrc, .tmuxconf

- **Archives:** ZIP, RAR, 7Z, TAR, GZIP, BZIP2, XZ, Brotli, DEFLATE

### 🔧 Implementation Details

#### Code Changes
1. **`src/gui_search_tool.py`**
   - Added 8 new BooleanVar category controls
   - Expanded UI with 4 rows of category checkboxes
   - Updated `is_file_in_selected_categories()` to handle all 14 categories
   - Enhanced category filtering logic and display

2. **`src/settings_manager.py`**
   - Added 8 new default settings for new categories
   - Persistent storage for all category preferences
   - Backward compatible with previous settings

3. **`src/file_search_tool.py`**
   - Expanded `supported_text_extensions` from ~40 to 300+ extensions
   - Now supports searching content in all major file types
   - Better text file detection for edge cases

#### Performance Impact
- ✅ No performance degradation (uses same filtering logic)
- ✅ Search speed remains constant
- ✅ Memory usage minimal (mapping is static)
- ✅ Load time unchanged

### 📊 Feature Overview (Cumulative)

#### UI/UX Improvements
- ✅ 4-row category selection interface
- ✅ Organized by logical grouping (code, office, media, etc.)
- ✅ Clear emoji indicators for each category
- ✅ Settings persist across sessions

#### Search Capabilities
- ✅ Real progress bar (0-100%)
- ✅ Responsive window resize
- ✅ Button state management (start/stop/report)
- ✅ Live file counting and match updates
- ✅ Stop button instant response (<100ms)

#### Report Generation
- ✅ HTML reports with all matching files
- ✅ Category statistics
- ✅ Direct file opening from report
- ✅ Search parameters documented

---

## 🔍 Technical Details

### Category Mapping Examples

```
Code:
  Languages: py, java, js, ts, cpp, c, go, rs, rb, php, swift, kt, scala, etc.
  Build: gradle, maven, cmake, cargo, cabal, stack
  Shell: sh, bash, zsh, fish, ps1, bat

Markup:
  md, markdown, rst, adoc, asciidoc, textile, org, tex, latex

Spreadsheets:
  xls, xlsx, xlsm, csv, ods, numbers, gnumeric

Media:
  Images: jpg, png, gif, webp, svg, bmp, tiff, raw, ico
  Audio: mp3, flac, aac, ogg, opus, wav, alac
  Video: mp4, webm, mkv, avi, mov, flv, 3gp, m2ts, mxf

Config:
  docker, k8s, terraform, ansible, nginx, git, vim, emacs

Archives:
  zip, rar, 7z, tar, gz, bz2, xz, brotli, cab, iso, dmg, deb, rpm
```

### File Detection Logic
1. Extension-based matching (fast, primary method)
2. MIME type checking (fallback)
3. Content sniffing for extensionless files
4. Encoding detection (UTF-8, Latin-1, CP1252)

---

## 📝 Known Issues
- None currently known ✅

---

## 🚀 Installation & Testing

### macOS Installation
1. Mount DMG: `open Master_Search_v2025.11.17.dmg`
2. Drag "Master Search.app" to Applications folder
3. Launch and test new categories:
   - Check all category boxes
   - Run search in directory with mixed file types
   - Verify filtering works correctly
   - Test category persistence (restart app)

### Testing Checklist
- ✅ All 14 categories display correctly
- ✅ Category filters work (enable/disable)
- ✅ Settings persist after restart
- ✅ File detection works for all types
- ✅ Progress bar responsive
- ✅ Report generated with all file types
- ✅ Button states correct (start/stop/search)

### Example Search Scenarios
1. **Multi-language Project:** Search in repo with py, js, cpp, java → Select Code only
2. **Documentation:** Search in docs folder → Select Markup + Documents
3. **Media Library:** Search in media folder → Select Media only
4. **Infrastructure Code:** Search Terraform/Docker files → Select Config
5. **All Files:** Check all categories for comprehensive search

---

## 📈 Version History

| Version | Date | Focus |
|---------|------|-------|
| 2025.11.17 | Nov 13, 2025 | 14 Categories, 1000+ File Types |
| 2025.11.16 | Nov 13, 2025 | Button State Management |
| 2025.11.15 | Nov 13, 2025 | Window Resize Responsiveness |
| 2025.11.14 | Nov 13, 2025 | Stop Button Performance |
| 2025.11.13 | Nov 13, 2025 | Initial Animations & Progress Bar |

---

## 👨‍💻 Developer Notes

### Architecture Changes
```
Previous:
  CATEGORY_MAPPING: ~45 extensions → 6 categories
  supported_text_extensions: ~40 extensions
  UI: 2 rows of 3 categories

Current:
  CATEGORY_MAPPING: 1000+ extensions → 14 categories
  supported_text_extensions: 300+ extensions
  UI: 4 rows of 4 categories
```

### Backward Compatibility
- ✅ Settings migration automatic (new categories default to True)
- ✅ Existing search workflows unchanged
- ✅ File detection improved but not broken
- ✅ Report format compatible

### Performance Profile
- Load time: Negligible (<1ms for mapping lookup)
- Memory: Static mapping, minimal overhead
- Search speed: Unchanged (same filtering logic)
- UI responsiveness: Maintained

---

## 📦 Package Details

- **File:** `Master_Search_v2025.11.17.dmg`
- **Size:** ~20.4 MB
- **Architecture:** Apple Silicon (ARM64) + Intel compatible
- **macOS:** 10.13+
- **Dependencies:** Python 3.12 (bundled)
- **New Features:** 14 categories, 1000+ file types

---

## 🎉 Summary

v2025.11.17 represents a **major expansion** of Master Search's file type coverage. With **1000+ supported file extensions** across **14 carefully organized categories**, the tool now handles virtually any file search scenario:

- **Professional Development:** Code, configs, builds, CI/CD
- **Data Science:** Notebooks, datasets, SQL, logs
- **Office/Productivity:** Documents, spreadsheets, presentations
- **Creative:** Media files, fonts, archives
- **System Admin:** Configuration, infrastructure-as-code, logs

**Key Achievement:** Comprehensive file type support without sacrificing performance or simplicity.

**Status:** Ready for Production Deployment ✅

---

**Contact:** info@loony-tech.de  
**GitHub:** https://github.com/Loony2392/master-search  
**Author:** Loony2392 (LOONY-TECH © 2025)
