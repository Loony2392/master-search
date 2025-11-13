#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Cross-Platform GUI Entry Point
==============================================
Universal GUI entry point that works on Windows, macOS, and Linux

Author: Loony2392
Email: info@loony-tech.de
Version: 2025.11.9
"""

import sys
import os
from pathlib import Path

def setup_cross_platform_environment():
    """Setup cross-platform environment."""
    
    # Determine the script location
    if getattr(sys, 'frozen', False):
        # Running in frozen executable
        app_dir = Path(sys.executable).parent
        print(f"🔧 Running from executable: {app_dir}")
    else:
        # Running from source
        app_dir = Path(__file__).parent.parent
        print(f"🚀 Running from source: {app_dir}")
    
    # Add source directories to Python path
    src_dir = app_dir / 'src'
    config_dir = app_dir / 'config'
    
    if src_dir.exists():
        sys.path.insert(0, str(src_dir))
    if config_dir.exists():
        sys.path.insert(0, str(config_dir))
    
    sys.path.insert(0, str(app_dir))
    
    # Set locale environment
    locales_dir = app_dir / 'locales'
    if locales_dir.exists():
        os.environ['MASTER_SEARCH_LOCALES'] = str(locales_dir)
    
    # Import platform utilities to initialize cross-platform support
    try:
        import platform_utils
        platform = platform_utils.get_platform()
        print(f"🔍 Detected platform: {platform}")
    except ImportError:
        print("⚠️  Platform utilities not available, using defaults")


def main():
    """Main GUI entry point."""
    try:
        # Setup environment
        setup_cross_platform_environment()
        
        # Import and start GUI
        print("🎨 Starting Master Search GUI...")
        from .gui_search_tool import MasterSearchGUI
        
        # Create and run the application
        app = MasterSearchGUI()
        app.run()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        error_msg = f"Could not start Master Search GUI:\n\n{e}\n\nPlease check your installation."
        
        # Try to show error dialog
        try:
            import tkinter as tk
            from tkinter import messagebox
            
            root = tk.Tk()
            root.withdraw()
            
            messagebox.showerror("Master Search - Import Error", error_msg)
            
        except Exception:
            print("Could not display error dialog.")
            print(error_msg)
        
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Error starting Master Search: {e}")
        error_msg = f"Unexpected error:\n\n{e}\n\nPlease contact support."
        
        try:
            import tkinter as tk
            from tkinter import messagebox
            
            root = tk.Tk()
            root.withdraw()
            
            messagebox.showerror("Master Search - Error", error_msg)
            
        except Exception:
            print("Could not display error dialog.")
            print(error_msg)
        
        sys.exit(1)


if __name__ == "__main__":
    main()