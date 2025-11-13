# Master Search - Windows MSI Build Instructions

## Prerequisites

To build the Windows MSI installer, you need to run this on **Windows** or use **Windows Subsystem for Linux (WSL)**.

### Required Tools:
1. **Python 3.12+** (from python.org)
2. **WiX Toolset 3.11+** - Required for MSI creation
   - Download: https://github.com/wixtoolset/wix3/releases/tag/wix311rtm
   - Install to default location

3. **Visual C++ Build Tools** - For cx_Freeze compilation
   - Download: https://visualstudio.microsoft.com/visual-cpp-build-tools/

### Setup on Windows:

```bash
# 1. Clone/navigate to master-search directory
cd path\to\master-search

# 2. Create Python virtual environment
python -m venv .venv_build

# 3. Activate virtual environment
.venv_build\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
pip install cx_Freeze>=7.0

# 5. Build the MSI
python build_msi.py
```

### Output:
The MSI installer will be created at:
```
releases/windows/Master_Search_v2025.11.13.msi
```

## Troubleshooting

### "WiX Toolset not found"
- Ensure WiX is installed to: `C:\Program Files (x86)\WiX Toolset v3.11\`
- Or set `WIX` environment variable

### "cx_Freeze error"
- Ensure Visual C++ Build Tools are installed
- Try: `pip install --upgrade cx_Freeze`

### "Python version error"
- Build requires Python 3.8+
- For best results, use Python 3.12+

## Alternative: Use Existing Build on macOS

If building on macOS is difficult, you can:
1. Ask a Windows user to build the MSI
2. Or provide manual installation instructions for Windows users

---

For help, contact: info@loony-tech.de
