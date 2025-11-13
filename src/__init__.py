#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Source Package
==============================
Main application modules

Author: Loony2392
Email: info@loony-tech.de
"""

# Only import the most critical modules
# Other modules are imported on-demand to avoid startup issues
from .i18n import set_locale

__all__ = [
    'set_locale'
]
