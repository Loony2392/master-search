#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Locale Test Script
==================================
Test script to verify that German localization is working properly.

Author: Loony2392
Email: info@loony-tech.de
Version: 2025.11.10
"""

import sys
import os
from pathlib import Path

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_german_locales():
    """Test German locale functionality."""
    
    print("🧪 Master Search - Locale Testing")
    print("=" * 50)
    
    try:
        import i18n
        
        # Test current language detection
        print(f"📍 Current language: {i18n._CURRENT_LANG}")
        print(f"🗂️  Locales directory: {i18n.LOCALES_DIR}")
        print(f"✅ Directory exists: {i18n.LOCALES_DIR.exists()}")
        
        # Test German translations
        print("\n🇩🇪 German Translations:")
        print("-" * 25)
        i18n.set_locale('de')
        
        # Test key UI elements
        test_keys = [
            'app_title',
            'btn_search',
            'btn_browse',
            'label_search_terms',
            'label_search_directory',
            'search_mode_and',
            'search_mode_or',
            'checkbox_case_sensitive',
            'status_ready',
            'error',
            'about_title'
        ]
        
        for key in test_keys:
            translation = i18n.tr(key)
            print(f"  {key:<25} = {translation}")
        
        # Test English for comparison
        print("\n🇬🇧 English Translations:")
        print("-" * 25)
        i18n.set_locale('en')
        
        for key in test_keys[:5]:  # Just show first 5 for comparison
            translation = i18n.tr(key)
            print(f"  {key:<25} = {translation}")
        
        # Test French
        print("\n🇫🇷 French Translations:")
        print("-" * 23)
        i18n.set_locale('fr')
        
        for key in test_keys[:3]:  # Just show first 3 for comparison
            translation = i18n.tr(key)
            print(f"  {key:<25} = {translation}")
        
        # Reset to German
        i18n.set_locale('de')
        
        print(f"\n✅ All locales working correctly!")
        print(f"🎯 Current language set to: {i18n._CURRENT_LANG}")
        
        return True
        
    except Exception as e:
        print(f"❌ Locale test failed: {e}")
        return False


def test_gui_integration():
    """Test GUI integration with locales."""
    
    print("\n🖼️  GUI Integration Test:")
    print("-" * 25)
    
    try:
        import gui_search_tool
        
        print("✅ GUI module imports successfully")
        
        # Test if GUI can access translations
        import i18n
        i18n.set_locale('de')
        
        # These should work without errors
        test_translations = [
            i18n.tr('app_title'),
            i18n.tr('btn_search'),
            i18n.tr('status_ready')
        ]
        
        print("✅ GUI can access German translations:")
        for trans in test_translations:
            print(f"  • {trans}")
        
        return True
        
    except Exception as e:
        print(f"❌ GUI integration test failed: {e}")
        return False


def main():
    """Run all locale tests."""
    
    test1 = test_german_locales()
    test2 = test_gui_integration()
    
    print("\n" + "=" * 50)
    if test1 and test2:
        print("🎉 ALL LOCALE TESTS PASSED!")
        print("✅ German localization is working correctly")
        print("✅ GUI integration is working correctly")
    else:
        print("❌ Some locale tests failed")
        print("⚠️  Check the error messages above")
    
    print("\n📋 Summary:")
    print(f"  • Locale system: {'✅ OK' if test1 else '❌ FAILED'}")
    print(f"  • GUI integration: {'✅ OK' if test2 else '❌ FAILED'}")
    
    return test1 and test2


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)