#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR Installation Dialog
=======================
User-friendly dialog for installing OCR engines automatically.

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
from typing import Callable, Optional

from .ocr_installer import OCRInstaller


class OCRInstallationDialog:
    """Dialog window for automatic OCR engine installation"""
    
    def __init__(self, parent_window, on_complete: Optional[Callable[[bool], None]] = None):
        """
        Initialize OCR installation dialog
        
        Args:
            parent_window: Parent tkinter window
            on_complete: Callback when installation completes (success: bool)
        """
        self.parent = parent_window
        self.on_complete = on_complete
        self.installer = OCRInstaller(callback=self._log_message)
        self.is_running = False
        
        # Create dialog window
        self.window = tk.Toplevel(parent_window)
        self.window.title("🖼️ OCR Engine Installation")
        self.window.geometry("600x500")
        self.window.minsize(500, 400)
        self.window.resizable(True, True)
        
        # Prevent closing during installation
        self.window.protocol("WM_DELETE_WINDOW", self._on_closing)
        
        self._setup_ui()
    
    def _setup_ui(self):
        """Setup the dialog UI"""
        # Header
        header_frame = ttk.Frame(self.window, padding="10")
        header_frame.pack(fill="x", expand=False)
        
        ttk.Label(
            header_frame,
            text="🖼️ Automatic OCR Engine Installation",
            font=("Segoe UI", 14, "bold")
        ).pack(side="left")
        
        # Information frame
        info_frame = ttk.LabelFrame(self.window, text=" Information ", padding="10")
        info_frame.pack(fill="x", padx="10", pady="5")
        
        info_text = """OCR (Optical Character Recognition) allows you to search for text within images.

This installer will automatically:
1. Detect your operating system (Windows, macOS, Linux)
2. Install the best available OCR engine
3. Configure it for use with Master Search

Supported engines:
• EasyOCR (recommended) - Pure Python, works everywhere
• PaddleOCR - Alternative, high accuracy
• Tesseract - Classic OCR, system-specific
"""
        
        ttk.Label(info_frame, text=info_text, justify="left").pack(fill="x")
        
        # Log frame
        log_frame = ttk.LabelFrame(self.window, text=" Installation Progress ", padding="5")
        log_frame.pack(fill="both", expand=True, padx="10", pady="5")
        log_frame.grid_rowconfigure(0, weight=1)
        log_frame.grid_columnconfigure(0, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=12,
            font=("Consolas", 9),
            wrap=tk.WORD,
            state="disabled"
        )
        self.log_text.grid(row=0, column=0, sticky="nsew")
        
        # Progress bar
        progress_frame = ttk.Frame(self.window)
        progress_frame.pack(fill="x", padx="10", pady="5")
        
        self.progress = ttk.Progressbar(
            progress_frame,
            mode="indeterminate"
        )
        self.progress.pack(fill="x")
        
        # Button frame
        button_frame = ttk.Frame(self.window, padding="10")
        button_frame.pack(fill="x")
        
        self.install_btn = ttk.Button(
            button_frame,
            text="⬇️ Start Installation",
            command=self._start_installation
        )
        self.install_btn.pack(side="left", padx="5")
        
        self.cancel_btn = ttk.Button(
            button_frame,
            text="✖️ Close",
            command=self._on_closing
        )
        self.cancel_btn.pack(side="left", padx="5")
        
        # Status label
        self.status_var = tk.StringVar(value="Ready to install")
        ttk.Label(button_frame, textvariable=self.status_var, foreground="blue").pack(side="right", padx="5")
        
        # Center on parent
        self.window.transient(self.parent)
        self.window.grab_set()
    
    def _log_message(self, message: str):
        """Log a message to the text widget"""
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")
        self.window.update_idletasks()
    
    def _start_installation(self):
        """Start the installation process in background thread"""
        if self.is_running:
            return
        
        self.is_running = True
        self.install_btn.config(state="disabled")
        self.cancel_btn.config(state="disabled")
        self.progress.start()
        self.status_var.set("Installing... (this may take a few minutes)")
        
        # Run installation in background
        thread = threading.Thread(target=self._install_worker)
        thread.daemon = True
        thread.start()
    
    def _install_worker(self):
        """Background worker for installation"""
        try:
            self._log_message("=" * 50)
            self._log_message("🚀 Starting OCR Engine Installation")
            self._log_message("=" * 50)
            self._log_message("")
            
            # Run installation
            success = self.installer.auto_install_ocr(background=False)
            
            self._log_message("")
            self._log_message("=" * 50)
            if success:
                self._log_message("✅ Installation completed successfully!")
                self._log_message("You can now enable OCR in Master Search")
                self.status_var.set("✅ Installation successful!")
                self.window.after(0, self._on_installation_complete, True)
            else:
                self._log_message("❌ Installation encountered issues")
                self._log_message("Please check the log above for details")
                self.status_var.set("⚠️ Installation incomplete - see log")
                self.window.after(0, self._on_installation_complete, False)
            
            self._log_message("=" * 50)
        
        except Exception as e:
            self._log_message(f"❌ Installation error: {str(e)}")
            self.status_var.set("❌ Installation failed")
            self.window.after(0, self._on_installation_complete, False)
        
        finally:
            self.progress.stop()
            self.install_btn.config(state="normal")
            self.cancel_btn.config(state="normal", text="✖️ Close")
            self.is_running = False
    
    def _on_installation_complete(self, success: bool):
        """Called when installation completes"""
        if self.on_complete:
            self.on_complete(success)
        
        if success:
            messagebox.showinfo(
                "🎉 Success",
                "OCR installation completed!\n\n" +
                "Please restart Master Search to use OCR for image searching."
            )
    
    def _on_closing(self):
        """Handle window closing"""
        if self.is_running:
            messagebox.showwarning(
                "Installation in Progress",
                "Installation is still running.\n\n" +
                "Please wait for it to complete."
            )
            return
        
        self.window.destroy()


def show_ocr_installation_dialog(parent_window, on_complete: Optional[Callable[[bool], None]] = None) -> OCRInstallationDialog:
    """
    Show OCR installation dialog
    
    Args:
        parent_window: Parent tkinter window
        on_complete: Optional callback for when installation completes
    
    Returns:
        OCRInstallationDialog instance
    """
    return OCRInstallationDialog(parent_window, on_complete)
