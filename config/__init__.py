#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Config Package
==============================
Configuration modules for Master Search

Author: Loony2392
Email: info@loony-tech.de
"""

# Make config modules importable
from .language_config import (
    get_config_dir,
    get_saved_language,
    save_language,
    get_active_language,
    show_language_dialog
)

__all__ = [
    'get_config_dir',
    'get_saved_language',
    'save_language',
    'get_active_language',
    'show_language_dialog'
]
