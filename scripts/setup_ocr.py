#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR Setup Script for Build Bundles
===================================
Installs OCR engines into bundled Python environment
Called during DMG/MSI build process

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025
"""

import sys
import subprocess
import os
from pathlib import Path


def install_ocr_dependencies():
    """Install OCR dependencies into current Python environment"""
    
    print("🎨 Installing OCR Dependencies...")
    print("=" * 60)
    
    # List of OCR packages to install
    packages = [
        "easyocr>=1.7.0",      # Primary OCR engine
        "paddleocr>=2.7.0",    # Alternative OCR engine
    ]
    
    for package in packages:
        print(f"\n📦 Installing {package}...")
        try:
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", "--quiet", package],
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            if result.returncode == 0:
                print(f"✅ {package} installed successfully")
            else:
                print(f"⚠️  {package} installation had issues:")
                if result.stderr:
                    print(result.stderr[:200])  # Print first 200 chars of error
        except subprocess.TimeoutExpired:
            print(f"⏱️  {package} installation timed out (skipping)")
        except Exception as e:
            print(f"⚠️  Failed to install {package}: {e}")
    
    print("\n" + "=" * 60)
    print("✅ OCR dependency installation complete!")
    print("\nNotes:")
    print("  - First OCR use will download language models (~200MB)")
    print("  - Models are cached locally for fast subsequent runs")
    print("  - Requires ~1.5GB disk space for full OCR support")
    print("=" * 60)


if __name__ == "__main__":
    try:
        install_ocr_dependencies()
    except KeyboardInterrupt:
        print("\n\n⚠️  Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Installation failed: {e}")
        sys.exit(1)
