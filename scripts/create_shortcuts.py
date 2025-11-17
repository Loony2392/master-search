#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Shortcut Creation Script
==========================================
Creates Start Menu and Desktop shortcuts after MSI installation

Run this script after installation to set up shortcuts
Or it can be called automatically by the MSI post-install phase

Author: Loony2392
Version: 1.0.0
"""

import sys
import os
from pathlib import Path
import json

def create_shortcuts():
    """Create Start Menu and Desktop shortcuts."""
    
    try:
        import win32com.client
        from win32com.client import Dispatch
    except ImportError:
        print("[ERROR] pywin32 not found. Installing...")
        os.system(f"{sys.executable} -m pip install pywin32 -q")
        import win32com.client
        from win32com.client import Dispatch
    
    print("[SHORTCUTS] Creating Master Search shortcuts...")
    print("=" * 60)
    
    # Installation directory
    install_dir = Path(os.environ.get('PROGRAMFILES', 'C:\\Program Files')) / 'Master Search'
    
    if not install_dir.exists():
        print(f"[ERROR] Installation directory not found: {install_dir}")
        print("        Please install Master Search first")
        return False
    
    gui_exe = install_dir / 'Master_Search.exe'
    cli_exe = install_dir / 'MasterSearch_CLI.exe'
    
    if not gui_exe.exists() or not cli_exe.exists():
        print(f"[ERROR] Executables not found in {install_dir}")
        return False
    
    # Shell object for creating shortcuts
    shell = Dispatch("WScript.Shell")
    
    # Start Menu paths
    start_menu_dir = Path(os.environ.get('APPDATA')) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Master Search'
    start_menu_dir.mkdir(parents=True, exist_ok=True)
    
    # Desktop path
    desktop_dir = Path(os.environ.get('USERPROFILE')) / 'Desktop'
    
    try:
        # Create Start Menu - GUI shortcut
        print("\n[SHORTCUT] Creating Start Menu → Master Search...")
        gui_start_menu = str(start_menu_dir / 'Master Search.lnk')
        shortcut = shell.CreateShortCut(gui_start_menu)
        shortcut.TargetPath = str(gui_exe)
        shortcut.WorkingDirectory = str(install_dir)
        shortcut.Description = "Professional file search tool"
        shortcut.IconLocation = str(gui_exe)
        shortcut.save()
        print(f"[OK] Created: {gui_start_menu}")
        
        # Create Start Menu - CLI shortcut
        print("\n[SHORTCUT] Creating Start Menu → Master Search CLI...")
        cli_start_menu = str(start_menu_dir / 'Master Search CLI.lnk')
        shortcut = shell.CreateShortCut(cli_start_menu)
        shortcut.TargetPath = str(cli_exe)
        shortcut.WorkingDirectory = str(install_dir)
        shortcut.Description = "Command-line search tool"
        shortcut.IconLocation = str(cli_exe)
        shortcut.save()
        print(f"[OK] Created: {cli_start_menu}")
        
        # Create Desktop - GUI shortcut
        print("\n[SHORTCUT] Creating Desktop → Master Search...")
        gui_desktop = str(desktop_dir / 'Master Search.lnk')
        shortcut = shell.CreateShortCut(gui_desktop)
        shortcut.TargetPath = str(gui_exe)
        shortcut.WorkingDirectory = str(install_dir)
        shortcut.Description = "Professional file search tool"
        shortcut.IconLocation = str(gui_exe)
        shortcut.save()
        print(f"[OK] Created: {gui_desktop}")
        
        # Create Desktop - CLI shortcut (optional)
        print("\n[SHORTCUT] Creating Desktop → Master Search CLI...")
        cli_desktop = str(desktop_dir / 'Master Search CLI.lnk')
        shortcut = shell.CreateShortCut(cli_desktop)
        shortcut.TargetPath = str(cli_exe)
        shortcut.WorkingDirectory = str(install_dir)
        shortcut.Description = "Command-line search tool"
        shortcut.IconLocation = str(cli_exe)
        shortcut.save()
        print(f"[OK] Created: {cli_desktop}")
        
        print("\n" + "=" * 60)
        print("[OK] All shortcuts created successfully!")
        print("\n✓ Start Menu shortcuts:")
        print("  • Master Search (GUI)")
        print("  • Master Search CLI")
        print("\n✓ Desktop shortcuts:")
        print("  • Master Search (GUI)")
        print("  • Master Search CLI")
        
        return True
        
    except Exception as e:
        print(f"\n[ERROR] Failed to create shortcuts: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure Master Search is installed")
        print("2. Run this script with Administrator privileges")
        print("3. Check that the installation directory exists")
        return False

def remove_shortcuts():
    """Remove previously created shortcuts."""
    print("[SHORTCUTS] Removing Master Search shortcuts...")
    print("=" * 60)
    
    try:
        # Start Menu paths
        start_menu_dir = Path(os.environ.get('APPDATA')) / 'Microsoft' / 'Windows' / 'Start Menu' / 'Programs' / 'Master Search'
        
        # Desktop path
        desktop_dir = Path(os.environ.get('USERPROFILE')) / 'Desktop'
        
        shortcuts = [
            start_menu_dir / 'Master Search.lnk',
            start_menu_dir / 'Master Search CLI.lnk',
            desktop_dir / 'Master Search.lnk',
            desktop_dir / 'Master Search CLI.lnk',
        ]
        
        for shortcut in shortcuts:
            if shortcut.exists():
                shortcut.unlink()
                print(f"[OK] Removed: {shortcut}")
        
        # Remove Start Menu folder if empty
        if start_menu_dir.exists() and not any(start_menu_dir.iterdir()):
            start_menu_dir.rmdir()
            print(f"[OK] Removed directory: {start_menu_dir}")
        
        print("\n[OK] All shortcuts removed")
        return True
        
    except Exception as e:
        print(f"[ERROR] Failed to remove shortcuts: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--remove':
        success = remove_shortcuts()
    else:
        success = create_shortcuts()
    
    sys.exit(0 if success else 1)
