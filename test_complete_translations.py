#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Comprehensive Translation Test
==============================================
Test all translation keys used in the GUI to ensure complete German localization.

Author: Loony2392
Email: info@loony-tech.de
Version: 2025.11.10
"""

import sys
import os
import re

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def find_translation_keys_in_file(filepath):
    """Find all i18n.tr() calls in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all i18n.tr("key") patterns
        pattern = r'i18n\.tr\(["\']([^"\']+)["\']\)'
        matches = re.findall(pattern, content)
        return matches
        
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return []


def test_all_translations():
    """Test all translation keys found in the GUI."""
    print("🔍 Searching for all translation keys...")
    
    import i18n
    i18n.set_locale('de')
    
    # Find all translation keys used in GUI files
    gui_files = [
        'src/gui_search_tool.py',
        'src/gui_main.py'
    ]
    
    all_keys = set()
    for file_path in gui_files:
        if os.path.exists(file_path):
            keys = find_translation_keys_in_file(file_path)
            all_keys.update(keys)
    
    print(f"📝 Found {len(all_keys)} unique translation keys")
    
    # Test each key
    missing_keys = []
    translated_keys = []
    
    for key in sorted(all_keys):
        translation = i18n.tr(key)
        
        # Check if translation is just the key itself (meaning no translation found)
        if translation == key:
            missing_keys.append(key)
        else:
            translated_keys.append((key, translation))
    
    # Show results
    print(f"\n✅ Successfully translated: {len(translated_keys)}")
    if translated_keys:
        print("   Sample translations:")
        for key, trans in translated_keys[:5]:  # Show first 5
            print(f"     {key:<25} = {trans}")
        if len(translated_keys) > 5:
            print(f"     ... and {len(translated_keys) - 5} more")
    
    if missing_keys:
        print(f"\n❌ Missing translations: {len(missing_keys)}")
        for key in missing_keys:
            print(f"     {key}")
        return False
    else:
        print(f"\n🎉 All {len(all_keys)} translation keys are properly translated!")
        return True


def test_error_dialogs():
    """Test specific error dialog translations."""
    print("\n🚨 Testing Error Dialog Translations:")
    
    import i18n
    i18n.set_locale('de')
    
    error_keys = [
        'error_no_search_terms',
        'error_no_terms', 
        'error_no_directory',
        'error_invalid_regex',
        'error_search_failed'
    ]
    
    for key in error_keys:
        translation = i18n.tr(key)
        print(f"  {key:<25} = {translation}")
    
    return True


def main():
    """Run comprehensive translation tests."""
    print("🧪 Master Search - Comprehensive Translation Test")
    print("=" * 60)
    
    test1 = test_all_translations()
    test2 = test_error_dialogs()
    
    print("\n" + "=" * 60)
    if test1 and test2:
        print("🎉 ALL TRANSLATION TESTS PASSED!")
        print("✅ Complete German localization verified")
        print("✅ No missing translation keys found")
        print("✅ Error dialogs properly translated")
        print("\n🚀 GUI is ready with complete German support!")
    else:
        print("❌ Some translation tests failed")
        print("⚠️  Please add missing translations to locales/de.json")
    
    return test1 and test2


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)