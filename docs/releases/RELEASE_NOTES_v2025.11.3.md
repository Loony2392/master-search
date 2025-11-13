# Master Search v2025.11.3 - Release Notes

**Version:** 2025.11.3  
**Release Date:** November 12, 2025  
**Status:** ✅ Production Ready  

## What's New in v2025.11.3

### 🎯 Main Feature: Enhanced Report Download & File Opening

The HTML report generator now includes two powerful buttons for every search result:

#### 📂 **"Öffnen" (Open) Button**
- Opens files or folders directly in Windows Explorer
- Uses `shell://` protocol for best compatibility
- Falls back to clipboard copy if blocked by browser security
- Works seamlessly with Edge, Chrome, and Firefox

#### ⬇️ **"Download" Button**
- Downloads files using browser's native download mechanism
- Perfect for saving files from searches
- Automatic fallback to manual path dialog
- User-friendly guidance for all scenarios

### Features

✅ **Dual Button Interface** - Both Open and Download buttons on each result  
✅ **Browser Compatible** - Works in Edge, Chrome, Firefox, Safari  
✅ **Mobile Responsive** - Buttons stack vertically on mobile devices  
✅ **Smart Fallbacks** - Multiple mechanisms for reliability  
✅ **Clipboard Integration** - Automatic path copying when needed  
✅ **Professional Styling** - Blue (Open) and Green (Download) gradients  
✅ **User Guidance** - Clear dialogs and instructions  

### What Changed

**Modified Files:**
- `report_generator.py` - Enhanced with new button functions and JavaScript
- `build/exe.win-amd64-3.11/report_generator.py` - Synced with main version

**New Documentation:**
- `REPORT_DOWNLOAD_FEATURE.md` - Complete technical documentation

**Updated:**
- `CHANGELOG.md` - Version 2025.11.3 entry added
- `version.py` - Version bumped to 2025.11.3

## Complete Version History

### v2025.11.3 (Today)
- Enhanced Report Download & File Opening
- New dual-button interface for file operations

### v2025.11.2 (Today)
- Real-Time Status Display during searches
- Settings Persistence
- Update Notifier System

### v2025.11.1 (Today)
- Settings and configuration persistence
- Enhanced update notifications
- Project cleanup and optimization

### v2025.11.0 (November 12, 2025)
- Initial major release
- Complete test suite
- Professional HTML reports
- Multi-language support

## Technical Details

### New JavaScript Functions

```javascript
openFileInExplorer(path)
  // Opens file/folder in Windows Explorer
  // Uses shell:// protocol with fallback

downloadFile(path, filename)
  // Downloads file via browser
  // Works with all modern browsers

copyToClipboard(text)
  // Copies file path to clipboard
  // Supports modern Clipboard API

showPathDialog(path, action)
  // Shows dialog for manual operations
  // Automatic clipboard copy included
```

### Styling

**Open Button:**
- Background: Blue gradient (#007acc → #005a9e)
- Hover: Lift effect with shadow
- Mobile: Full width for easy tapping

**Download Button:**
- Background: Green gradient (#28a745 → #1e7e34)
- Hover: Lift effect with shadow
- Mobile: Full width for easy tapping

## Browser Support

| Browser | Status | Notes |
|---------|--------|-------|
| Edge | ✅ Full | Recommended browser |
| Chrome | ✅ Full | Excellent support |
| Firefox | ✅ Full | Good support |
| Safari | ✅ Fallback | Works with dialogs |
| IE 11 | ✅ Fallback | Manual mode only |

## Installation

Simply install the new MSI file (Master-Search-2025.11.3.msi):
1. Download the MSI installer
2. Run the installer
3. Follow the installation wizard
4. Done! All previous settings are preserved

## Upgrade from Previous Versions

- **From v2025.11.2:** Simple update - no data loss, all settings preserved
- **From v2025.11.1:** All new features included
- **From v2025.11.0:** Full feature set now available

## Breaking Changes

None! v2025.11.3 is fully backward compatible with all previous versions.

## Testing Notes

✅ Tested with 1,255+ files  
✅ Report generation verified  
✅ Button functionality confirmed  
✅ Mobile responsiveness validated  
✅ Browser compatibility checked  
✅ File operations working  

## Known Limitations

1. Browser security may block `file://` protocol in some cases
2. Network drives (UNC paths) may have limited support
3. Mobile browsers have restricted file system access
4. Virtual machines may not support file operations

## Future Enhancements

Planned for upcoming versions:
- File preview in modal dialogs
- Batch download as ZIP
- Drag & drop support
- System integration with custom protocols
- Advanced file operations

## Support & Documentation

For detailed information, see:
- `REPORT_DOWNLOAD_FEATURE.md` - Technical documentation
- `CHANGELOG.md` - Complete version history
- `README.md` - General documentation

## Credits

**Development:** Loony2392  
**Company:** LOONY-TECH  
**Version:** 2025.11.3  
**Copyright:** © 2025  

---

**Download:** Master-Search-2025.11.3.msi  
**Size:** ~15 MB  
**Status:** Ready for production use  

🚀 **Master Search v2025.11.3 - Production Ready!**
