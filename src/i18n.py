#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - i18n Module
============================
Simple JSON-based translation system with multi-language support.

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025
"""

import json
import locale
import os
from pathlib import Path
from typing import Dict

_LOCALES_CACHE = {}
_CURRENT_LANG = None
_VERSION = None

# Determine LOCALES_DIR - handle both normal Python and cx_Freeze
try:
    # Environment variable (highest priority)
    if 'MASTER_SEARCH_LOCALES' in os.environ:
        LOCALES_DIR = Path(os.environ['MASTER_SEARCH_LOCALES'])
    
    # Check if locales is in the same directory as i18n.py (source structure)
    elif (Path(__file__).parent / "locales").exists():
        LOCALES_DIR = Path(__file__).parent / "locales"
    
    # Check parent directory (new structure: src/ and locales/ are siblings)
    elif (Path(__file__).parent.parent / "locales").exists():
        LOCALES_DIR = Path(__file__).parent.parent / "locales"
    
    # For cx_Freeze frozen applications
    elif hasattr(sys, 'frozen'):
        import sys
        # Running as frozen EXE
        LOCALES_DIR = Path(sys.executable).parent / "locales"
    
    # Last resort: current working directory
    else:
        LOCALES_DIR = Path.cwd() / "locales"
        
    print(f"[i18n] Using locales directory: {LOCALES_DIR}")
    
except Exception as e:
    print(f"[WARNING] Error determining locales directory: {e}")
    LOCALES_DIR = Path.cwd() / "locales"


def _get_version():
    """Get version from version.py dynamically."""
    global _VERSION
    if _VERSION is not None:
        return _VERSION
    
    try:
        from version import VERSION
        _VERSION = VERSION
        return VERSION
    except ImportError:
        _VERSION = "unknown"
        return _VERSION


def _detect_system_lang():
    """Detect system language code (e.g., 'en', 'de')."""
    try:
        loc = locale.getdefaultlocale()[0]
        if loc:
            return loc.split("_")[0].lower()
    except:
        pass
    return "en"


def _load_locale(lang):
    """Load translation dictionary from JSON file."""
    if lang in _LOCALES_CACHE:
        return _LOCALES_CACHE[lang]
    
    lang_path = LOCALES_DIR / f"{lang}.json"
    if not lang_path.exists():
        lang_path = LOCALES_DIR / "en.json"
    
    try:
        with lang_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
            _LOCALES_CACHE[lang] = data
            return data
    except Exception as e:
        print(f"Could not load locale {lang}: {e}")
        return {}


def set_locale(lang):
    """Set the active language (e.g., 'en', 'de')."""
    global _CURRENT_LANG
    _CURRENT_LANG = lang


def tr(key, **kwargs):
    """Translate a key. Falls back to English, then key itself."""
    global _CURRENT_LANG
    
    if _CURRENT_LANG is None:
        _CURRENT_LANG = _detect_system_lang()
    
    data = _load_locale(_CURRENT_LANG)
    val = data.get(key)
    
    if val is None and _CURRENT_LANG != "en":
        data_en = _load_locale("en")
        val = data_en.get(key)
    
    if val is None:
        val = key
    
    # Replace {VERSION} placeholder with actual version
    val = val.replace("{VERSION}", _get_version())
    
    try:
        return val.format(**kwargs) if kwargs else val
    except:
        return val


# Auto-initialize
_CURRENT_LANG = _detect_system_lang()
