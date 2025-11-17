# MSI Shortcuts Integration Guide

## Problem Description

Shortcuts in the Start Menu and on the Desktop were not being created during MSI installation.

**User requirement**: "das ging vorher aber über die msi installation" (shortcuts should be created during installation, not after)

## Solutions Implemented

### Solution 1: WiX Toolset (Recommended)

If WiX Toolset is installed on your system, the build script will automatically:

1. **Detect WiX**: Checks for `candle.exe` and `heat.exe`
2. **Generate WiX Configuration**: Creates `Master_Search_Shortcuts.wxs` with shortcut definitions
3. **Build MSI**: Uses WiX to compile a proper MSI with **native shortcut support**

**Features**:
- ✅ Shortcuts created automatically during installation
- ✅ Start Menu shortcuts (GUI + CLI)
- ✅ Desktop shortcuts
- ✅ Add to PATH environment variable
- ✅ Proper uninstall support

**Installation**: 
```bash
# Install WiX Toolset from: https://wixtoolset.org/
# Then the build script will use it automatically
```

### Solution 2: Automatic Post-Installation Hooks

If WiX is not available, the build script will use **cx_Freeze** with post-installation hooks:

1. **Build MSI**: Creates base Windows MSI with cx_Freeze
2. **Include Post-Install Script**: Adds `msi_post_install.py` to MSI package
3. **Create Shortcuts on First Launch**: Shortcuts created when application first runs

**Features**:
- ✅ Shortcuts created automatically on first launch
- ✅ No user action required
- ✅ Works without WiX installation

### Solution 3: Manual Shortcut Creation

Users can manually create shortcuts after installation:

```bash
python scripts/create_shortcuts.py
```

Or double-click:
```
Create_Shortcuts.bat
```

## Build Configuration

### `build_msi.py` - Build Process

The updated build script (`build_msi.py`) now includes:

```python
def check_dependencies(self):
    """Check for available installer tools"""
    # Detects: WiX Toolset, NSIS, cx_Freeze
    # Sets: self.use_wix, self.use_nsis flags
    
def build_with_wix(self):
    """Build MSI using WiX if available"""
    # Generates WiX config with shortcuts
    # Compiles with WiX Toolset
    # Returns proper MSI with native shortcuts

def build(self):
    """Main build process"""
    # 1. Checks dependencies
    # 2. Tries WiX build first (if available)
    # 3. Falls back to cx_Freeze if needed
    # 4. Creates checksums and reports
```

### `generate_wix_config.py` - WiX Configuration Generator

Creates `Master_Search_Shortcuts.wxs` with:

```xml
<Feature Id="ProductFeature" Title="Master Search">
    <ComponentRef Id="MainExecutable"/>
    <ComponentRef Id="ProgramMenuDir"/>    <!-- Start Menu -->
    <ComponentRef Id="DesktopShortcutGUI"/> <!-- Desktop -->
</Feature>

<!-- Start Menu shortcuts -->
<DirectoryRef Id="ApplicationProgramsFolder">
    <Shortcut Name="Master Search" Target="[INSTALLFOLDER]Master_Search.exe"/>
    <Shortcut Name="Master Search CLI" Target="[INSTALLFOLDER]MasterSearch_CLI.exe"/>
    <Shortcut Name="Uninstall Master Search" Target="msiexec.exe /x [ProductCode]"/>
</DirectoryRef>

<!-- Desktop shortcuts -->
<DirectoryRef Id="DesktopFolder">
    <Shortcut Name="Master Search" Target="[INSTALLFOLDER]Master_Search.exe"/>
    <Shortcut Name="Master Search CLI" Target="[INSTALLFOLDER]MasterSearch_CLI.exe"/>
</DirectoryRef>
```

### `msi_post_install.py` - Post-Installation Hook

Automatically runs after MSI installation to create shortcuts:

```python
def create_vbs_shortcut(link_path, target_path, description, work_dir, icon_path):
    """Create shortcuts using VBScript"""
    # Uses Windows built-in shortcut creation
    # Works on all Windows versions
    # No external dependencies

def main():
    """Create Start Menu and Desktop shortcuts"""
    # Gets installation directory from environment
    # Creates shortcuts in:
    #   - Start Menu: C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Master Search
    #   - Desktop: C:\Users\{user}\Desktop
```

## Installation Methods

### Method 1: Direct MSI with WiX (Best - Shortcuts Automatic)

```bash
# With WiX Toolset installed:
python build_msi.py

# Result: Master_Search-2025.11.22-win64.msi
# Installation: Double-click or msiexec /i <file.msi>
# Shortcuts: Automatically created during installation ✅
```

### Method 2: MSI with cx_Freeze (Good - Shortcuts on First Launch)

```bash
# Without WiX Toolset:
python build_msi.py

# Result: Master_Search-2025.11.22-win64.msi
# Installation: Double-click or msiexec /i <file.msi>
# Shortcuts: Created on first application launch ✅
```

### Method 3: Manual Shortcut Creation (Fallback)

```bash
# After MSI installation:
python scripts/create_shortcuts.py

# Or double-click:
Create_Shortcuts.bat
```

## Testing Shortcuts

After installation, verify shortcuts were created:

```bash
# Check Start Menu
dir "%appdata%\Microsoft\Windows\Start Menu\Programs\Master Search"

# Check Desktop
dir "%userprofile%\Desktop\Master*"

# Verify by launching
"C:\Program Files\Master Search\Master_Search.exe"
```

## Troubleshooting

### Shortcuts Not Created

1. **Check installation directory**:
   ```bash
   dir "C:\Program Files\Master Search"
   ```

2. **Manually create shortcuts**:
   ```bash
   python scripts/create_shortcuts.py
   ```

3. **Check Windows permissions**:
   - Run installer as Administrator
   - Ensure user has write permissions to Start Menu and Desktop

### WiX Integration Issues

1. **Verify WiX installation**:
   ```bash
   where candle
   where heat
   ```

2. **If WiX not found**:
   - Install from: https://wixtoolset.org/
   - Or use fallback method (cx_Freeze)

3. **WiX compilation errors**:
   - Check `scripts/Master_Search_Shortcuts.wxs` syntax
   - Ensure all referenced files exist

## Files Modified/Created

### Modified:
- `build_msi.py` - Added WiX detection and build support

### Created:
- `scripts/generate_wix_config.py` - WiX configuration generator
- `scripts/msi_post_install.py` - Post-installation hook
- `scripts/Master_Search_Shortcuts.wxs` - WiX MSI configuration
- `scripts/Master_Search.nsi` - NSIS alternative (future)

## Version History

### v2025.11.22
- ✅ Added WiX Toolset support with native shortcuts
- ✅ Implemented post-installation hooks for cx_Freeze fallback
- ✅ Created shortcut creation scripts
- ✅ Generated documentation

### v2025.11.21
- ✅ Fixed encoding errors (emoji → ASCII)
- ✅ Resolved directory locking issues
- ✅ Built functional MSI (6.3 MB)

## References

- **WiX Toolset**: https://wixtoolset.org/
- **cx_Freeze Documentation**: https://cx-freeze.readthedocs.io/
- **NSIS Documentation**: https://nsis.sourceforge.io/

## Support

For issues or questions:
- GitHub: https://github.com/Loony2392/master-search
- Email: info@loony-tech.de
