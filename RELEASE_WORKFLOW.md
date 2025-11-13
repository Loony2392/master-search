# 🚀 Release Workflow Documentation

**Last Updated**: 13 November 2025  
**Version**: 2025.11.13  

---

## Overview

Master Search has a fully automated GitHub Actions release workflow that:

1. ✅ **Validates the release** - Checks version format and existing tags
2. ✅ **Runs full test suite** - Ensures code quality before release
3. ✅ **Updates version** - Increments version.py automatically
4. ✅ **Builds artifacts** - Creates platform-specific installers:
   - Windows: Installer package (ZIP with executables)
   - macOS: DMG package
   - Linux: DEB package + portable archives
5. ✅ **Creates GitHub Release** - Uploads all artifacts as release assets
6. ✅ **Deploys documentation** - Updates GitHub Pages
7. ✅ **Sends notifications** - Confirms successful release

---

## How It Works

### Trigger Methods

#### 1. **Manual Release (via Workflow Dispatch)**
```bash
# Go to GitHub Actions > Release & Deploy > Run workflow
# Fill in:
# - Version: 2025.11.13
# - Release Type: patch/minor/major
# - Pre-release: true/false (optional)
# - Generate builds: true (default)
# - Deploy docs: true (default)
```

#### 2. **Automatic Release (via Git Tag Push)**
```bash
# Locally:
git tag -a v2025.11.13 -m "Master Search v2025.11.13"
git push origin v2025.11.13

# Automatically triggers release workflow
```

### Workflow Steps

#### Step 1: Validate Release
- ✅ Extracts version from tag or workflow input
- ✅ Validates version format: `YYYY.MM.DD` or `YYYY.MM.DD.PATCH`
- ✅ Checks for duplicate tags
- **Status**: `validate-release` job

#### Step 2: Run Tests
- ✅ Executes full test suite
- ✅ Ensures code quality
- **Status**: `run-full-tests` job (uses test.yml)

#### Step 3: Update Version (Manual Releases Only)
- ✅ Updates `version.py` with new version
- ✅ Generates changelog entry
- ✅ Commits and pushes changes
- **Status**: `update-version` job

#### Step 4: Build Artifacts
- ✅ **Windows**: Creates installer package via `scripts/create_installer_package.py`
- ✅ **macOS**: Creates DMG package
- ✅ **Linux**: Creates DEB and portable archives
- **Status**: `build-artifacts` job (matrix for multiple OS)

#### Step 5: Create GitHub Release
- ✅ Downloads all build artifacts
- ✅ Creates Git tag (for manual releases)
- ✅ Prepares release notes with platform-specific instructions
- ✅ Uploads all artifacts as release assets
- **Status**: `create-release` job

#### Step 6: Deploy Documentation
- ✅ Builds HTML documentation
- ✅ Deploys to GitHub Pages
- ✅ Creates landing page with links
- **Status**: `deploy-documentation` job

#### Step 7: Send Notification
- ✅ Confirms successful release
- ✅ Provides download links
- **Status**: `notification` job

---

## Windows Installer Package Details

### What Gets Built

The Windows build uses **PyInstaller** to create:

```
release_builds/
├── Master_Search_v2025.11.13_Windows.zip    [27.36 MB]
├── Master_Search_v2025.11.13_Windows.zip.sha256
└── MasterSearch_v2025.11.13/
    ├── bin/
    │   ├── MasterSearch.exe                 [13.94 MB - GUI]
    │   └── MasterSearchCLI.exe              [13.90 MB - CLI]
    ├── Launch-GUI.bat                       [Easy launcher]
    ├── Launch-CLI.bat                       [Easy launcher]
    └── README.txt                           [Installation guide]
```

### Build Process

1. **Install PyInstaller**
   ```bash
   pip install PyInstaller>=6.1.0
   ```

2. **Build GUI Executable**
   ```bash
   python -m PyInstaller scripts/gui.spec
   ```

3. **Build CLI Executable**
   ```bash
   python -m PyInstaller scripts/cli.spec
   ```

4. **Create Installer Package**
   ```bash
   python scripts/create_installer_package.py
   ```

5. **Generate Checksums**
   - SHA256 checksums for all files
   - Stored in `.sha256` file

### Why ZIP Instead of MSI?

- ✅ **No external dependencies** - Doesn't require WiX or Inno Setup
- ✅ **Faster builds** - PyInstaller + ZIP is quick
- ✅ **Full control** - Batch file launchers for easy access
- ✅ **User-friendly** - Extract and run, no installation needed
- ✅ **Portable** - Works from any folder (USB, network, etc.)

---

## Release Notes

### Automatic Generation

The release notes are generated in the `create-release` job:

```markdown
# 🎉 Master Search v2025.11.13

## 📋 Overview
[Multi-language description]

## 🚀 Key Features
[Feature list with emoji]

## 📦 Downloads
[Platform-specific download links with sizes]

## 🚀 Installation Instructions
[Platform-specific setup instructions]

...
```

### Manual Editing

You can edit release notes on GitHub:
1. Go to Releases
2. Click on the release
3. Click "Edit" button
4. Modify the description
5. Save changes

---

## Release Assets

### Downloaded by Users

When users visit the release page, they can download:

- `Master_Search_v2025.11.13_Windows.zip` (27.36 MB)
  - Contains all executables and launchers
  - Ready to extract and use
  - No Python required

- `Master_Search_v2025.11.13_macOS.dmg` (varies)
  - Standard macOS application bundle
  - Drag to Applications to install

- `Master_Search_v2025.11.13_Linux.deb` (varies)
  - Standard Debian package
  - Install via `dpkg -i`

- `Master_Search_v2025.11.13_Linux_Portable.tar.gz` (varies)
  - Portable source archive
  - Extract and run with Python

- Source archives (`.tar.gz`, `.zip`)
  - Full source code for developers

---

## How to Trigger a Release

### Option 1: Manual GitHub Actions (Recommended)

1. Go to: https://github.com/Loony2392/master-search
2. Click **Actions** tab
3. Select **🚀 Release & Deploy** workflow
4. Click **Run workflow**
5. Fill in:
   - **Version**: `2025.11.13` (YYYY.MM.DD format)
   - **Release Type**: `patch`, `minor`, or `major`
   - **Pre-release**: `false` (for production)
   - **Generate builds**: `true` (for release packages)
   - **Deploy docs**: `true` (for documentation)
6. Click **Run workflow**
7. Wait for all jobs to complete (usually 5-15 minutes)
8. Check: https://github.com/Loony2392/master-search/releases/latest

### Option 2: Git Tag Push (Fast)

```bash
# From your local repository:
git tag -a v2025.11.13 -m "Master Search v2025.11.13 - Release & Cleanup"
git push origin v2025.11.13

# Automatically triggers release workflow via 'push' event
# Skips version update step (already done locally)
```

### Option 3: Command Line (Local Development)

```bash
# Update version locally
python -c "
with open('version.py', 'r') as f:
    content = f.read()
content = content.replace('VERSION = \"2025.11.12\"', 'VERSION = \"2025.11.13\"')
with open('version.py', 'w') as f:
    f.write(content)
"

# Build locally
python build.py all
python scripts/create_installer_package.py

# Commit and push
git add version.py release_builds/
git commit -m "🚀 Release v2025.11.13"
git tag -a v2025.11.13 -m "Master Search v2025.11.13"
git push origin main v2025.11.13
```

---

## Monitoring Release Progress

### GitHub Actions UI

1. Go to: https://github.com/Loony2392/master-search/actions
2. Click on **🚀 Release & Deploy** workflow run
3. Watch job progress in real-time:
   - 🔍 Validate Release
   - 🧪 Full Test Suite
   - 📝 Update Version
   - 🏗️ Build Release Artifacts (Windows, macOS, Linux in parallel)
   - 🎉 Create GitHub Release
   - 📚 Deploy Documentation
   - 📧 Release Notification

### Expected Duration

- **Fast track** (tag push): 5-10 minutes
- **Full workflow** (manual): 10-15 minutes
  - Testing: 3-5 min
  - Building: 5-8 min
  - Release creation: 1-2 min

---

## Troubleshooting

### Issue: "Tag already exists"
**Solution**: Use a different version number or delete the tag:
```bash
git tag -d v2025.11.13
git push origin :refs/tags/v2025.11.13
```

### Issue: Build failed on Windows
**Likely cause**: Missing PyInstaller or spec files  
**Solution**: 
- Check `scripts/gui.spec` and `scripts/cli.spec` exist
- Run locally: `python build.py all`
- Check for errors in logs

### Issue: MSI/ZIP not in release assets
**Solution**:
- Workflow may still be running - refresh page
- Check Actions tab for errors
- Manually run: `python scripts/create_installer_package.py`
- Upload manually to release

### Issue: Documentation not deploying
**Solution**:
- Check GitHub Pages settings (should auto-publish from Actions)
- Check the `deploy-documentation` job logs
- Verify workflow has `pages` permissions

---

## Performance Metrics

### Build Times (Typical)

| Step | Time | Notes |
|------|------|-------|
| Validate | 30s | Quick validation |
| Tests | 3-5m | Full test suite |
| Version Update | 1m | Git commit + push |
| Windows Build | 3-5m | PyInstaller + ZIP |
| macOS Build | 3-5m | DMG creation |
| Linux Build | 2-4m | DEB + archives |
| Create Release | 2-3m | Upload artifacts |
| Deploy Docs | 1-2m | GitHub Pages |
| **Total** | **10-15m** | Entire workflow |

---

## Version Format

Master Search uses **calendar versioning**:

```
YYYY.MM.DD[.PATCH]

Examples:
- 2025.11.13     (13 November 2025)
- 2025.11.13.1   (13 November 2025, patch 1)
- 2025.11.13.2   (13 November 2025, patch 2)
```

**Rules**:
- ✅ Year: 4 digits
- ✅ Month: 1-2 digits (01-12)
- ✅ Day: 1-2 digits (01-31)
- ✅ Patch: optional, 1+ digits

---

## Workflow Files

### Main Files

- `.github/workflows/release.yml` - Main release workflow
- `.github/workflows/test.yml` - Test suite (called by release)
- `scripts/create_installer_package.py` - Windows installer builder
- `scripts/gui.spec` - PyInstaller spec for GUI
- `scripts/cli.spec` - PyInstaller spec for CLI
- `build.py` - Local build launcher

### Generated Files

During release, these are created:

- `version.py` - Updated version
- `CHANGELOG.md` - Updated changelog
- `release_builds/` - All release artifacts
- GitHub Release - With all assets

---

## Best Practices

1. **Always run tests first**
   - Local: `pytest`
   - GitHub: Full suite runs automatically

2. **Use semantic versioning**
   - PATCH: Bug fixes (2025.11.13.1 → 2025.11.13.2)
   - MINOR: Features (2025.11.13 → 2025.11.14 or 2025.12.01)
   - MAJOR: Breaking changes (2025.x.x → 2026.x.x)

3. **Write clear commit messages**
   - Release commits are tagged
   - Include what changed in the message

4. **Test on multiple platforms**
   - Windows: Before release
   - macOS: Check DMG can be mounted
   - Linux: Test DEB installation

5. **Update documentation**
   - Update README.md with new features
   - Add migration guides if needed
   - Update user guides in appropriate languages

6. **Monitor the release**
   - Check Actions tab for any failures
   - Verify all assets upload correctly
   - Test download links manually

---

## GitHub Pages Documentation

Documentation is automatically deployed to:
- https://loony2392.github.io/master-search/

### What's Included
- User guides (DE, EN, FR)
- README and changelog
- API documentation (if available)
- Release information

### Manual Trigger
```yaml
deploy_docs: true  # In workflow_dispatch inputs
```

---

## Contact & Support

- **Email**: b.kolb@loony-tech.de
- **GitHub**: https://github.com/Loony2392/master-search
- **Issues**: https://github.com/Loony2392/master-search/issues

---

**Status**: ✅ Fully Automated  
**Maintenance**: Active  
**Last Updated**: 13 November 2025
