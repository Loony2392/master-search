#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - macOS GUI Entry Point
=====================================
Platform-optimized entry point for macOS App Bundle

Author: Loony2392
Email: info@loony-tech.de
Version: 2025.11.9
"""

import sys
import os
from pathlib import Path

def setup_mac_environment():
    """Setup macOS-specific environment for App Bundle."""
    
    # Get the app bundle path
    if getattr(sys, 'frozen', False):
        # Running in py2app bundle
        bundle_dir = Path(sys.executable).parent
        resources_dir = bundle_dir / 'Resources'
        
        # Add Python path
        site_packages = bundle_dir / 'lib' / 'python3.11' / 'site-packages'
        if site_packages.exists():
            sys.path.insert(0, str(site_packages))
        
        # Add resources to path
        if resources_dir.exists():
            sys.path.insert(0, str(resources_dir))
            
        # Set environment for locales
        locales_dir = resources_dir / 'locales'
        if locales_dir.exists():
            os.environ['MASTER_SEARCH_LOCALES'] = str(locales_dir)
        
        print(f"🍎 Running from macOS App Bundle: {bundle_dir}")
    else:
        # Running in development mode
        project_root = Path(__file__).parent.parent
        src_dir = project_root / 'src'
        config_dir = project_root / 'config'
        
        # Add to Python path
        sys.path.insert(0, str(src_dir))
        sys.path.insert(0, str(config_dir))
        sys.path.insert(0, str(project_root))
        
        # Set environment for locales
        locales_dir = project_root / 'locales'
        if locales_dir.exists():
            os.environ['MASTER_SEARCH_LOCALES'] = str(locales_dir)
        
        print(f"🚀 Running in development mode from: {project_root}")


def main():
    """Main entry point for macOS."""
    try:
        # Setup macOS environment
        setup_mac_environment()
        
        # Import and run the GUI
        from .gui_search_tool import MasterSearchGUI
        
        # Create and run the application
        app = MasterSearchGUI()
        app.run()
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("This might be a missing dependency or path issue.")
        
        # Try to show a simple error dialog
        try:
            import tkinter as tk
            from tkinter import messagebox
            
            root = tk.Tk()
            root.withdraw()  # Hide main window
            
            messagebox.showerror(
                "Master Search - Import Error",
                f"Could not start Master Search:\n\n{e}\n\n"
                "Please check your installation."
            )
            
        except:
            # If even tkinter fails, just print error
            print("Could not display error dialog.")
        
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Error starting Master Search: {e}")
        
        # Try to show error dialog
        try:
            import tkinter as tk
            from tkinter import messagebox
            
            root = tk.Tk()
            root.withdraw()
            
            messagebox.showerror(
                "Master Search - Error",
                f"Unexpected error:\n\n{e}\n\n"
                "Please contact support if this persists."
            )
            
        except:
            print("Could not display error dialog.")
        
        sys.exit(1)


if __name__ == "__main__":
    main()