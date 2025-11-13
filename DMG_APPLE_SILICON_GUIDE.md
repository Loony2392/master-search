# Master Search DMG für macOS - Apple Silicon & Universal Binary Support

## Status

Das aktuelle `build_dmg.py` Script funktioniert auf beiden:
- ✅ Intel-Macs (x86_64)
- ✅ Apple Silicon Macs (ARM64/M1/M2/M3+)

**Aber:** Das gebaute App-Bundle läuft nur auf der gleichen Architektur wie Python selbst!

## Das Problem

Wenn du Python auf einem M1/M2 Mac installiert hast:
```bash
python3 --version
# Python 3.11.6

arch
# arm64  ← Das ist Apple Silicon!
```

Dann erstellt `build_dmg.py` ein ARM64-only App-Bundle.

Wenn jemand mit Intel-Mac die DMG öffnet → **funktioniert nicht!**

## Die Lösung: Universal Binaries

Wir brauchen **Universal Binaries**, die auf BEIDEN Architekturen laufen:

```
Master Search.app/
├── MacOS/
│   ├── master_search → Universal Binary (Intel + ARM64)
│   └── python3 → Universal Binary (Intel + ARM64)
└── ...
```

## Implementierung

### Option 1: Mit PyInstaller (Empfohlen)

PyInstaller kann direkt Universal Binaries bauen:

```bash
# Auf M1/M2 Mac mit Universal Python:
python3 -m PyInstaller --target-architecture universal2 scripts/gui.spec
```

### Option 2: Mit py2app (aktuell)

py2app hat eingeschränkte Universal-Binary-Unterstützung. Wir müssen folgendes tun:

```bash
# 1. Universal Python installieren (nicht nur ARM64!)
# Von https://www.python.org/downloads/ downloaden:
#    "macOS 64-bit universal2 installer"

# 2. Venv mit Universal Python erstellen:
/usr/local/bin/python3 -m venv venv_universal

# 3. In venv aktivieren:
source venv_universal/bin/activate

# 4. PyInstaller mit universal2 flag:
python3 -m PyInstaller --onedir --target-architecture universal2 \
    scripts/gui.spec
```

### Option 3: Mit Homebrew Python

```bash
# Universal Python via Homebrew:
brew install python@3.11-universal

# Oder check ob du Universal hast:
file /usr/local/bin/python3
# Mach64 universal binary with 2 architectures: [x86_64:Mach-O 64-bit executable x86_64]
```

## Wie man überprüft ob Universal Binary

```bash
# Check ob App Universal ist:
file Master\ Search.app/Contents/MacOS/Master_Search

# Sollte zeigen:
# Mach-O universal binary with 2 architectures: [x86_64:Mach-O 64-bit executable x86_64] 
# [arm64:Mach-O 64-bit executable arm64]
```

## Workflow für Universal DMG

### Lokal auf M1/M2 Mac bauen (Universal):

1. **Universal Python installieren:**
   ```bash
   # Option A: Homebrew
   brew install python@3.11-universal
   
   # Oder von python.org downloaden
   ```

2. **Venv mit Universal Python:**
   ```bash
   /usr/local/bin/python3 -m venv venv_universal
   source venv_universal/bin/activate
   pip install -r requirements.txt
   ```

3. **PyInstaller mit universal2:**
   ```bash
   python3 -m PyInstaller --onedir --target-architecture universal2 \
       scripts/gui.spec
   python3 -m PyInstaller --onedir --target-architecture universal2 \
       scripts/cli.spec
   ```

4. **DMG bauen:**
   ```bash
   python3 build_dmg.py
   ```

### GitHub Actions für Universal DMG:

Wir können GitHub Actions auf M1-Runner verwenden:

```yaml
macos-dmg:
  runs-on: macos-latest-xlarge  # M1 Mac
  steps:
    - uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        # Stellt sicher dass wir universal2 bekommen
    
    - run: |
        python3 -m PyInstaller --target-architecture universal2 \
            scripts/gui.spec
        python3 build_dmg.py
```

## Current Status für Master Search

**Aktuell:**
- `build_dmg.py` funktioniert auf M1/M2, erstellt aber ARM64-only DMG
- Funktioniert auf Intel-Macs, erstellt aber x86_64-only DMG

**Für Production:**
1. Universal Python nutzen
2. PyInstaller mit `--target-architecture universal2`
3. DMG baut dann automatisch Universal Binary App

## Verifizierung nach dem Build

```bash
# 1. Check ob DMG Universal ist:
file dist/Master_Search_vX.Y.Z.dmg

# 2. Mount DMG:
open dist/Master_Search_vX.Y.Z.dmg

# 3. Check ob App Universal ist:
file "/Volumes/Master Search/Master Search.app/Contents/MacOS/Master_Search"

# Sollte zeigen:
# Mach-O universal binary with 2 architectures: [x86_64:...] [arm64:...]
```

## Performance

Universal Binaries sind ca. 2x größer, aber:
- Nur ~15-20% größer bei kompression (DMG mit zlib-level=9)
- Kein Performance-Hit auf M1/M2 (der ARM64 Code läuft nativ)
- Intel-Macs nutzen Intel-Code (auch nativ)

## Nächste Schritte

1. **Kurz-Term:** Dokumentieren dass wir Apple Silicon unterstützen (ARM64)
2. **Mittel-Term:** Universal Python + PyInstaller unterstützen
3. **Lang-Term:** GitHub Actions mit M1-Runner für Universal DMG

## Referenzen

- [PyInstaller Universal Binary Support](https://pyinstaller.org/en/stable/usage.html#options-specific-to-macos)
- [Python Universal Binaries](https://docs.python.org/3/using/mac/python-on-mac.html)
- [Homebrew Python Universal](https://github.com/Homebrew/homebrew-core/pull/125399)
- [Apple Silicon App Development](https://developer.apple.com/documentation/apple-silicon)
