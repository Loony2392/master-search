#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Update Notifier
================================
Shows users what changed in a new version (only once per update)

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025

Features:
    - Reads CHANGELOG.md automatically
    - Shows changes only once per version
    - Stores last seen version
    - Pretty formatted output
    - Multi-language support
"""

import os
import json
import re
from pathlib import Path
from typing import Optional, Dict, List
from version import VERSION

# Config
CONFIG_DIR = Path.home() / ".master_search"
VERSION_FILE = CONFIG_DIR / "last_version.json"
CHANGELOG_PATH = Path(__file__).parent / "CHANGELOG.md"


class UpdateNotifier:
    """Handles update notifications for users."""
    
    def __init__(self, current_version: str = VERSION):
        """
        Initialize the update notifier.
        
        Args:
            current_version: Current application version
        """
        self.current_version = current_version
        self.config_dir = CONFIG_DIR
        self.version_file = VERSION_FILE
        self.changelog_path = CHANGELOG_PATH
        
        # Ensure config directory exists
        self.config_dir.mkdir(parents=True, exist_ok=True)
    
    def should_show_update_notification(self) -> bool:
        """
        Check if update notification should be shown.
        
        Returns:
            True if notification should be shown, False otherwise
        """
        # If no version file exists, this is first run
        if not self.version_file.exists():
            self._save_version()
            return False
        
        try:
            with open(self.version_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                last_version = data.get('version')
                
                # Compare versions
                if last_version != self.current_version:
                    self._save_version()
                    return True
                    
        except Exception:
            # If error reading, show notification
            self._save_version()
            return True
        
        return False
    
    def _save_version(self):
        """Save current version to config file."""
        try:
            data = {
                'version': self.current_version,
                'last_updated': str(Path.cwd())
            }
            with open(self.version_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️  Could not save version info: {e}")
    
    def get_changelog_entry(self, version: str) -> Optional[str]:
        """
        Extract changelog entry for specific version.
        
        Args:
            version: Version to extract (e.g., "2025.11.0")
            
        Returns:
            Formatted changelog entry or None
        """
        if not self.changelog_path.exists():
            return None
        
        try:
            with open(self.changelog_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find version section
            pattern = rf"##\s+\[{re.escape(version)}\].*?(?=##\s+\[|\Z)"
            match = re.search(pattern, content, re.DOTALL)
            
            if match:
                return match.group(0)
            
        except Exception as e:
            print(f"⚠️  Could not read changelog: {e}")
        
        return None
    
    def get_changelog_summary(self, version: str, max_items: int = 10) -> List[str]:
        """
        Extract summary of changes from changelog.
        
        Args:
            version: Version to extract
            max_items: Maximum items to show from each category
            
        Returns:
            List of formatted change descriptions
        """
        changelog = self.get_changelog_entry(version)
        if not changelog:
            return []
        
        changes = []
        
        # Extract categories with items
        categories = {
            '✨ Neu': r"### ✨ Neu\n(.*?)(?=### |\Z)",
            '🔧 Verbessert': r"### 🔧 Verbessert\n(.*?)(?=### |\Z)",
            '🔒 Sicherheit': r"### 🔒 Sicherheit\n(.*?)(?=### |\Z)",
            '🐛 Bug-Fixes': r"### 🐛 Bug-Fixes\n(.*?)(?=### |\Z)",
            '🚀 Performance': r"### 🚀 Performance\n(.*?)(?=### |\Z)",
        }
        
        for category, pattern in categories.items():
            match = re.search(pattern, changelog, re.DOTALL)
            if match:
                items_text = match.group(1)
                # Extract bullet points
                items = re.findall(r"- (.+?)(?:\n|$)", items_text)
                
                if items:
                    changes.append(f"\n{category}:")
                    for item in items[:max_items]:
                        changes.append(f"  • {item}")
                    
                    if len(items) > max_items:
                        changes.append(f"  ... und {len(items) - max_items} weitere")
        
        return changes
    
    def show_update_notification(self, interactive: bool = True) -> bool:
        """
        Show update notification to user (formatted).
        
        Args:
            interactive: Whether to show interactive dialog or just print
            
        Returns:
            True if notification was shown
        """
        if not self.should_show_update_notification():
            return False
        
        # Get changelog
        summary = self.get_changelog_summary(self.current_version)
        
        if not summary:
            return False
        
        # Format output
        print("\n" + "=" * 70)
        print("🎉 MASTER SEARCH - WILLKOMMEN ZUM UPDATE!")
        print("=" * 70)
        print(f"\n✅ Version {self.current_version} ist jetzt installiert!\n")
        
        print("📝 ÄNDERUNGEN IN DIESER VERSION:")
        for line in summary:
            print(line)
        
        print("\n" + "=" * 70)
        print("💡 Tipp: Weitere Details findest du in CHANGELOG.md")
        print("=" * 70 + "\n")
        
        return True
    
    def show_update_dialog_gui(self, parent=None):
        """
        Show update notification in GUI (tkinter) with modal dialog and "don't show again" checkbox.
        
        Args:
            parent: Parent tkinter window (optional)
        """
        if not self.should_show_update_notification():
            return
        
        try:
            import tkinter as tk
            from tkinter import ttk
            
            # Get changelog summary
            summary = self.get_changelog_summary(self.current_version, max_items=5)
            
            if not summary:
                return
            
            # Create modal dialog
            dialog = tk.Toplevel(parent) if parent else tk.Tk()
            dialog.title("🎉 Master Search Update")
            dialog.geometry("550x400")
            dialog.resizable(False, False)
            
            # Make modal
            if parent:
                dialog.transient(parent)
                dialog.grab_set()
            
            # Try to set icon
            try:
                icon_path = Path(__file__).parent / "gui" / "icons" / "logo.ico"
                if icon_path.exists():
                    dialog.iconbitmap(str(icon_path))
            except Exception:
                pass
            
            # Main frame
            main_frame = ttk.Frame(dialog, padding="20")
            main_frame.pack(fill=tk.BOTH, expand=True)
            
            # Title
            title_label = ttk.Label(
                main_frame,
                text=f"🎉 Master Search v{self.current_version}",
                font=("Segoe UI", 12, "bold")
            )
            title_label.pack(anchor=tk.W, pady=(0, 5))
            
            # Subtitle
            subtitle_label = ttk.Label(
                main_frame,
                text="✅ Neues Update installiert!",
                font=("Segoe UI", 10),
                foreground="#0078d4"
            )
            subtitle_label.pack(anchor=tk.W, pady=(0, 10))
            
            # Changelog text frame with scrollbar
            text_frame = ttk.Frame(main_frame)
            text_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
            
            scrollbar = ttk.Scrollbar(text_frame)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            
            changelog_text = tk.Text(
                text_frame,
                height=12,
                width=60,
                yscrollcommand=scrollbar.set,
                font=("Courier New", 9),
                bg="#f5f5f5",
                borderwidth=1,
                relief=tk.SOLID
            )
            changelog_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.config(command=changelog_text.yview)
            
            # Insert changelog content
            changelog_text.insert("1.0", "📝 Was ist neu:\n\n")
            for line in summary:
                changelog_text.insert(tk.END, line + "\n")
            changelog_text.insert(tk.END, "\n" + "="*50)
            changelog_text.insert(tk.END, "\nWeitere Details in CHANGELOG.md")
            
            changelog_text.config(state=tk.DISABLED)
            
            # Checkbox for "don't show again"
            dont_show_var = tk.BooleanVar(value=False)
            checkbox = ttk.Checkbutton(
                main_frame,
                text="Nicht wieder anzeigen für diese Version",
                variable=dont_show_var
            )
            checkbox.pack(anchor=tk.W, pady=(0, 10))
            
            # Button frame
            button_frame = ttk.Frame(main_frame)
            button_frame.pack(fill=tk.X, pady=(5, 0))
            
            def on_ok():
                # Mark as seen if checkbox is checked
                if dont_show_var.get():
                    self._save_version()
                dialog.destroy()
                if not parent:
                    dialog.quit()
            
            ok_button = ttk.Button(
                button_frame,
                text="✅ OK",
                command=on_ok,
                width=20
            )
            ok_button.pack(side=tk.RIGHT)
            
            # Center dialog on parent if exists
            if parent:
                dialog.update_idletasks()
                parent_x = parent.winfo_x()
                parent_y = parent.winfo_y()
                parent_width = parent.winfo_width()
                parent_height = parent.winfo_height()
                
                x = parent_x + (parent_width - 550) // 2
                y = parent_y + (parent_height - 400) // 2
                dialog.geometry(f"+{max(0, x)}+{max(0, y)}")
            else:
                # Center on screen
                dialog.update_idletasks()
                x = (dialog.winfo_screenwidth() - 550) // 2
                y = (dialog.winfo_screenheight() - 400) // 2
                dialog.geometry(f"+{x}+{y}")
            
            dialog.mainloop()
                
        except ImportError:
            # Fallback to console
            self.show_update_notification()


def check_and_show_update(parent_window=None) -> bool:
    """
    Convenience function to check and show update notification.
    
    Args:
        parent_window: Parent tkinter window for GUI dialog (optional)
        
    Returns:
        True if notification was shown
    """
    notifier = UpdateNotifier()
    
    # Try GUI first if parent window provided
    if parent_window:
        try:
            notifier.show_update_dialog_gui(parent_window)
            return True
        except Exception as e:
            print(f"⚠️  GUI dialog failed: {e}")
            # Fall through to console notification
    
    # Fallback to console or show console notification
    return notifier.show_update_notification()


if __name__ == "__main__":
    # Test the notifier
    print("🧪 Testing Update Notifier...\n")
    
    notifier = UpdateNotifier()
    
    print(f"Current version: {notifier.current_version}")
    print(f"Config file: {notifier.version_file}")
    print(f"Changelog path: {notifier.changelog_path}")
    print()
    
    # Show notification
    if notifier.show_update_notification():
        print("✅ Update notification was shown!")
    else:
        print("ℹ️  No update notification needed (version already seen)")
    
    # Show changelog entry
    print("\n" + "=" * 70)
    print("📋 FULL CHANGELOG ENTRY:")
    print("=" * 70)
    changelog = notifier.get_changelog_entry(notifier.current_version)
    if changelog:
        print(changelog)
