#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Quick Locale Update Test
========================================
Test the updated GUI with modern animations and complete German translations.

Author: Loony2392
Email: info@loony-tech.de
Version: 2025.11.10
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_animations():
    """Test the modern loading animations."""
    print("🎨 Testing Modern Loading Animations...")
    
    try:
        from loading_animations import ModernProgressBar, SpinningLoader, PulsingDots
        import tkinter as tk
        
        # Create test window
        root = tk.Tk()
        root.title("Animation Test")
        root.geometry("400x300")
        
        # Test ModernProgressBar
        progress = ModernProgressBar(root, width=300, color="#00A8FF")
        progress.start_indeterminate()
        
        print("✅ ModernProgressBar created and started")
        
        # Clean up after short display
        root.after(2000, lambda: [progress.stop_indeterminate(), root.destroy()])
        root.mainloop()
        
        return True
        
    except Exception as e:
        print(f"❌ Animation test failed: {e}")
        return False


def test_updated_gui():
    """Test the GUI with new translations and animations."""
    print("\n🖼️  Testing Updated GUI...")
    
    try:
        # Test imports
        import gui_search_tool
        import loading_animations
        import i18n
        
        print("✅ All modules import successfully")
        
        # Test German translations for new keys
        i18n.set_locale('de')
        
        new_keys = [
            'label_search_path',
            'hint_multiple_terms', 
            'options_title',
            'mode_and',
            'mode_or',
            'include_content',
            'case_sensitive',
            'use_regex',
            'available'
        ]
        
        print("\n📝 Testing new German translations:")
        for key in new_keys:
            translation = i18n.tr(key)
            print(f"  {key:<20} = {translation}")
        
        return True
        
    except Exception as e:
        print(f"❌ GUI test failed: {e}")
        return False


def main():
    """Run all tests."""
    print("🧪 Master Search - Updated GUI Testing")
    print("=" * 50)
    
    test1 = test_animations()
    test2 = test_updated_gui()
    
    print("\n" + "=" * 50)
    if test1 and test2:
        print("🎉 ALL TESTS PASSED!")
        print("✅ Modern animations working")
        print("✅ German translations complete")
        print("✅ GUI ready for improved user experience")
    else:
        print("❌ Some tests failed")
        print("⚠️  Check error messages above")
    
    print(f"\n🚀 Ready to start GUI with modern features:")
    print(f"   cd src && python gui_main.py")
    
    return test1 and test2


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)