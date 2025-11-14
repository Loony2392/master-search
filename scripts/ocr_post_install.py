#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - OCR Post-Installation Setup
============================================
Automatically initializes OCR models after MSI installation
Called by cx_Freeze setup scripts

This script:
1. Downloads and caches OCR models
2. Configures language support
3. Sets up OCR cache directories
4. Validates OCR installation

Author: Loony2392
Version: 1.0.0
"""

import sys
import os
import subprocess
from pathlib import Path

def setup_ocr_models():
    """Download and cache OCR models for faster first run."""
    
    print("[OCR] Master Search - OCR Setup")
    print("=" * 60)
    
    # Get cache directory
    cache_dir = Path.home() / ".master_search" / "ocr_cache"
    cache_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"[OCR] Cache directory: {cache_dir}")
    
    try:
        # Initialize EasyOCR
        print("\n[OCR] Initializing EasyOCR...")
        try:
            import easyocr
            reader = easyocr.Reader(
                ['de', 'en'],  # German and English by default
                gpu=False,  # Use CPU for broader compatibility
                model_storage_directory=str(cache_dir),
            )
            print("[OK] EasyOCR initialized successfully")
            print(f"     Languages: German, English")
        except Exception as e:
            print(f"[WARN] EasyOCR init failed: {e}")
        
        # Initialize PaddleOCR
        print("\n[OCR] Initializing PaddleOCR...")
        try:
            from paddleocr import PaddleOCR
            ocr = PaddleOCR(
                use_angle_cls=True,
                lang='de',  # German
                model_storage_directory=str(cache_dir),
            )
            print("[OK] PaddleOCR initialized successfully")
            print(f"     Languages: German")
        except Exception as e:
            print(f"[WARN] PaddleOCR init failed: {e}")
        
        print("\n" + "=" * 60)
        print("[OK] OCR setup completed!")
        print("\nNotes:")
        print("  - Models cached in: " + str(cache_dir))
        print("  - First search with OCR will be faster now")
        print("  - Additional languages can be downloaded on demand")
        
        return True
        
    except KeyboardInterrupt:
        print("\n[WARN] OCR setup cancelled by user")
        return False
    except Exception as e:
        print(f"\n[WARN] OCR setup error: {e}")
        print("     Master Search will still work, OCR will be set up on first use")
        return False

if __name__ == "__main__":
    success = setup_ocr_models()
    sys.exit(0 if success else 1)
