#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tooltip Widget for Tkinter
===========================
Provides cross-platform tooltip support for widgets.

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025
"""

import tkinter as tk
from tkinter import font as tkfont


class ToolTip:
    """
    Create a tooltip for a given widget
    
    Features:
    - Shows on hover
    - Auto-wraps long text
    - Platform-aware positioning
    """
    
    def __init__(self, widget, text: str = "", background: str = "#FFFFE0", relief: str = tk.SOLID, bd: int = 1):
        """
        Initialize tooltip
        
        Args:
            widget: The widget to attach tooltip to
            text: Tooltip text
            background: Tooltip background color (improved contrast: dark background)
            relief: Relief style (tk.SOLID, tk.RAISED, tk.SUNKEN)
            bd: Border width
        """
        self.widget = widget
        self.text = text
        # Improved background: dark with good contrast
        self.background = "#2D2D2D"  # Dark charcoal for better contrast
        self.foreground = "#FFFFFF"  # White text
        self.relief = relief
        self.bd = bd
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        
        # Bind events
        self.widget.bind("<Enter>", self.showtip, add=True)
        self.widget.bind("<Leave>", self.hidetip, add=True)
        self.widget.bind("<ButtonPress>", self.hidetip, add=True)
    
    def showtip(self, event=None):
        """Show tooltip with improved styling"""
        if self.tipwindow or not self.text:
            return
        
        x = self.widget.winfo_rootx() + self.widget.winfo_width()
        y = self.widget.winfo_rooty() - 5
        
        # Create toplevel window
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        
        # Create label with improved styling for better contrast
        label = tk.Label(
            tw,
            text=self.text,
            background=self.background,  # Dark background
            foreground=self.foreground,   # White text
            relief=tk.RAISED,
            bd=2,
            justify=tk.LEFT,
            font=("Segoe UI", 10, "bold"),  # Slightly larger, bold for readability
            wraplength=400,  # Wider wrapping for better text layout
            padx=10,  # More padding
            pady=8
        )
        label.pack(ipadx=1)
    
    def hidetip(self, event=None):
        """Hide tooltip"""
        if self.tipwindow:
            self.tipwindow.destroy()
            self.tipwindow = None
    
    def update_text(self, new_text: str):
        """Update tooltip text"""
        self.text = new_text


def add_tooltip(widget, text: str, **kwargs) -> ToolTip:
    """
    Convenience function to add tooltip to a widget
    
    Args:
        widget: Target widget
        text: Tooltip text
        **kwargs: Additional arguments for ToolTip
    
    Returns:
        ToolTip instance
    """
    return ToolTip(widget, text, **kwargs)
