#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Settings Manager
==================================
Manages application settings (search path, worker count, etc.)
Persists settings to user config directory

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional

# Config location
CONFIG_DIR = Path.home() / ".master_search"
SETTINGS_FILE = CONFIG_DIR / "settings.json"

# Default settings
DEFAULT_SETTINGS = {
    "search_path": str(Path.cwd()),
    "max_workers": 4,
    "search_mode": "AND",
    "case_sensitive": False,
    "use_regex": False,
    "include_content": True,
    "file_pattern": "*",
    "window_width": 900,
    "window_height": 700,
    "category_code": True,
    "category_markup": True,
    "category_documents": True,
    "category_spreadsheets": True,
    "category_presentations": True,
    "category_data": True,
    "category_databases": True,
    "category_logs": True,
    "category_config": True,
    "category_web": True,
    "category_media": True,
    "category_archives": True,
    "category_fonts": True,
    "category_text": True,
    "use_ocr": False,
}


class SettingsManager:
    """Manages application settings with file persistence"""
    
    def __init__(self):
        """Initialize settings manager"""
        self.config_dir = CONFIG_DIR
        self.settings_file = SETTINGS_FILE
        self.settings = self._load_settings()
    
    def _ensure_config_dir(self):
        """Ensure config directory exists"""
        try:
            self.config_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"⚠️  Could not create config directory: {e}")
    
    def _load_settings(self) -> Dict[str, Any]:
        """Load settings from file or return defaults"""
        try:
            if self.settings_file.exists():
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    loaded = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    settings = DEFAULT_SETTINGS.copy()
                    settings.update(loaded)
                    return settings
        except Exception as e:
            print(f"⚠️  Could not load settings: {e}")
        
        return DEFAULT_SETTINGS.copy()
    
    def save_settings(self, settings: Optional[Dict[str, Any]] = None):
        """Save settings to file"""
        try:
            self._ensure_config_dir()
            
            if settings:
                self.settings = DEFAULT_SETTINGS.copy()
                self.settings.update(settings)
            
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️  Could not save settings: {e}")
    
    def get(self, key: str, default=None):
        """Get a setting value"""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set a setting value"""
        self.settings[key] = value
    
    def update(self, settings_dict: Dict[str, Any]):
        """Update multiple settings at once"""
        self.settings.update(settings_dict)
    
    def get_all(self) -> Dict[str, Any]:
        """Get all settings"""
        return self.settings.copy()


# Global instance
_settings_manager = None


def get_settings_manager() -> SettingsManager:
    """Get or create the global settings manager"""
    global _settings_manager
    if _settings_manager is None:
        _settings_manager = SettingsManager()
    return _settings_manager
