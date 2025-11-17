# 🚀 Semantic Release & Automated Builds

## Overview

Master Search now uses **Semantic Release** for automated versioning and multi-platform builds.

## 🔄 How It Works

### 1. **Conventional Commits**

All commits must follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 2. **Commit Types & Release Triggers**

| Type | Release | Example |
|------|---------|---------|
| `feat:` | **Minor** (0.1.0) | `feat: add OCR support` |
| `fix:` | **Patch** (0.0.1) | `fix: correct shortcut creation` |
| `perf:` | **Patch** (0.0.1) | `perf: optimize search algorithm` |
| `BREAKING CHANGE:` | **Major** (1.0.0) | See below |

### 3. **Breaking Changes (Major Release)**

Add `BREAKING CHANGE:` in commit footer:

```
feat: rewrite search engine

BREAKING CHANGE: Old command-line API removed
```

---

## 📋 Examples

### Example 1: Feature Release (v2025.11.24 → v2025.12.0)

```bash
git commit -m "feat: add regex search support

- Implemented full regex pattern matching
- Added regex help documentation
- Added regex examples to CLI"

git push
```

**Result:**
- ✅ Version bumped (minor release)
- ✅ Release notes generated
- ✅ CHANGELOG.md updated
- ✅ Windows MSI built
- ✅ macOS DMG built
- ✅ GitHub Release created

### Example 2: Bug Fix Release (v2025.12.0 → v2025.12.1)

```bash
git commit -m "fix: correct Start Menu shortcut path on Windows"

git push
```

**Result:**
- ✅ Version bumped (patch release)
- ✅ Release notes generated
- ✅ All installers built
- ✅ GitHub Release created

### Example 3: Major Release (v2.0.0 → v3.0.0)

```bash
git commit -m "feat: complete UI rewrite

BREAKING CHANGE: Old GUI configuration files not compatible
with new version. Users must reconfigure settings."

git push
```

**Result:**
- ✅ Major version bump
- ✅ Release notes with breaking changes
- ✅ All installers built

---

## 🤖 Automated Workflow

```
📝 Commit with conventional format
    ↓
📤 git push to main
    ↓
✅ GitHub Actions triggered
    ↓
🔍 Semantic Release analyzes commits
    ↓
📊 Determines version bump (major/minor/patch)
    ↓
📝 Generates release notes & updates CHANGELOG
    ↓
🏷️ Creates git tag (v2025.12.0)
    ↓
🪟 Windows: Build MSI (cx_Freeze)
🍎 macOS: Build DMG (py2app)
    ↓
📦 Upload installers to GitHub Release
    ↓
🎉 Release published & ready for download
```

---

## 📦 What Gets Built Automatically

### Windows (MSI)
- **File**: `Master_Search-2025.11.24-win64.msi`
- **Size**: ~6.3 MB
- **Built on**: Windows Latest Runner
- **Includes**: Full Python runtime, shortcuts, OCR optional

### macOS (DMG)
- **File**: `Master_Search-2025.11.24-macos.dmg`
- **Built on**: macOS Latest Runner
- **Includes**: Full app bundle, Python, tkinter

---

## 🔑 GitHub Token Requirements

The workflow uses `${{ secrets.GITHUB_TOKEN }}` which is automatically available.

**Permissions granted:**
- ✅ Create releases
- ✅ Upload assets
- ✅ Create git tags
- ✅ Update repository

---

## 🛠️ Manual Testing

Test the release workflow locally:

```bash
# Install semantic-release locally
npm install

# Dry run (no actual release)
npx semantic-release --dry-run

# Full run (creates actual release)
npx semantic-release
```

---

## 📊 Version File Auto-Update (Optional)

To automatically update `version.py`, add this to the workflow:

```yaml
- name: Update version.py
  run: |
    python -c "
    version = '${{ needs.semantic-release.outputs.new_release_version }}'
    with open('version.py', 'r+') as f:
        content = f.read()
        content = content.replace(
            'VERSION = \"',
            f'VERSION = \"{version}'
        )
        f.seek(0)
        f.write(content)
        f.truncate()
    "
    git config --local user.email "action@github.com"
    git config --local user.name "GitHub Action"
    git add version.py
    git commit -m "chore: update version to v${{ needs.semantic-release.outputs.new_release_version }}"
    git push
```

---

## 🚫 Disable Release

To skip release even with qualifying commits:

```bash
git commit -m "docs: update README

[skip ci]"
```

---

## 📚 Resources

- [Semantic Release Documentation](https://semantic-release.gitbook.io/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

## 🤔 Troubleshooting

### Release Not Triggering?

1. Check commit format matches conventional commits
2. Verify main branch is target
3. Check GitHub token permissions
4. View workflow logs in Actions tab

### Build Fails?

1. Check Python/dependencies installed
2. Verify build scripts work locally
3. Check runner logs for specific errors
4. Manually run build script to debug

---

**Happy releasing! 🚀**
