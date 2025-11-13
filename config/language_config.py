#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Language Configuration Manager
==============================================
Manages user language preference and provides language selection dialog

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025
"""

import json
import os
from pathlib import Path
import locale
import sys

# Config file location - use temp/appdata for portability
def get_config_dir():
    """Get user config directory - platform-aware (Windows/macOS/Linux)"""
    try:
        if sys.platform == 'win32':
            # Windows: use %APPDATA%
            config_dir = Path(os.path.expandvars(r'%APPDATA%\Master Search'))
        elif sys.platform == 'darwin':
            # macOS: use ~/Library/Application Support
            config_dir = Path.home() / 'Library' / 'Application Support' / 'Master Search'
        else:
            # Linux: use ~/.config
            config_dir = Path.home() / '.config' / 'Master Search'
    except Exception:
        # Fallback: use system temp directory
        import tempfile
        config_dir = Path(tempfile.gettempdir()) / 'Master Search'
    
    try:
        config_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        # If we can't create (e.g., read-only FS), use temp as fallback
        import tempfile
        config_dir = Path(tempfile.gettempdir()) / 'Master Search'
        config_dir.mkdir(parents=True, exist_ok=True)
    
    return config_dir

CONFIG_FILE = get_config_dir() / "language.json"

def get_saved_language():
    """Load saved language preference"""
    try:
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('language', None)
    except:
        pass
    return None

def save_language(lang):
    """Save language preference"""
    try:
        config_dir = CONFIG_FILE.parent
        config_dir.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump({'language': lang}, f, indent=2)
        return True
    except Exception as e:
        print(f"Could not save language: {e}")
        return False

def get_system_language():
    """Detect system language"""
    try:
        loc = locale.getdefaultlocale()[0]
        if loc:
            lang = loc.split("_")[0].lower()
            # Only return if we support it
            if lang in ['de', 'en', 'fr']:
                return lang
    except:
        pass
    return 'en'

def get_active_language():
    """Get the active language - saved > system > default"""
    saved = get_saved_language()
    if saved:
        return saved
    
    system_lang = get_system_language()
    if system_lang:
        return system_lang
    
    return 'en'

def show_language_dialog():
    """Show language selection dialog using tkinter"""
    try:
        import tkinter as tk
        from tkinter import simpledialog
        
        # Create a minimal root window (not visible)
        root = tk.Tk()
        root.withdraw()  # Hide immediately
        root.geometry("1x1+0+0")  # Minimal size and position
        
        # Create the dialog
        dialog = tk.Toplevel(root)
        dialog.title("Master Search - Language Selection")
        dialog.geometry("350x200")
        dialog.resizable(False, False)
        dialog.grab_set()  # Make it modal
        dialog.transient(root)  # Associate with root
        
        # Center window on screen
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        selected_lang = tk.StringVar(value=get_active_language())
        result = [None]  # Store result
        
        # Title
        title = tk.Label(dialog, text="🌐 Select Language", font=("Segoe UI", 14, "bold"))
        title.pack(pady=15)
        
        # Subtitle
        subtitle = tk.Label(dialog, text="Wähle deine Sprache / Choose your language", 
                           font=("Segoe UI", 9), foreground="gray")
        subtitle.pack()
        
        # Radio buttons
        frame = tk.Frame(dialog)
        frame.pack(pady=20)
        
        tk.Radiobutton(frame, text="🇬🇧 English", variable=selected_lang, value="en",
                      font=("Segoe UI", 11)).pack(anchor="w", pady=8)
        tk.Radiobutton(frame, text="🇩🇪 Deutsch", variable=selected_lang, value="de",
                      font=("Segoe UI", 11)).pack(anchor="w", pady=8)
        tk.Radiobutton(frame, text="🇫🇷 Français", variable=selected_lang, value="fr",
                      font=("Segoe UI", 11)).pack(anchor="w", pady=8)
        
        # Button frame
        button_frame = tk.Frame(dialog)
        button_frame.pack(pady=20)
        
        def on_ok():
            result[0] = selected_lang.get()
            save_language(result[0])
            dialog.destroy()
        
        def on_close():
            if result[0] is None:
                result[0] = selected_lang.get()
            dialog.destroy()
        
        ok_btn = tk.Button(button_frame, text="✓ OK", command=on_ok, width=15, font=("Segoe UI", 10))
        ok_btn.pack()
        
        # Bind Enter key to OK button
        dialog.bind('<Return>', lambda e: on_ok())
        
        # Handle window close button
        dialog.protocol("WM_DELETE_WINDOW", on_close)
        
        # Ensure button gets focus
        ok_btn.focus()
        
        # Show dialog and wait
        root.deiconify()
        root.wait_window(dialog)
        root.destroy()
        
        return result[0] if result[0] else selected_lang.get()
        
    except Exception as e:
        print(f"Could not show language dialog: {e}")
        return get_active_language()
