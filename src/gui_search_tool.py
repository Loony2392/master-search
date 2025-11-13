#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - GUI Version
===========================
Professional Multi-Term File Search Tool with GUI Interface

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.1 (with bug fixes)
Created: November 2025

Bug Fixes (v1.0.1):
- Fixed UI layout overlap (Category window, Button frame, Log frame repositioned)
- Added context-limited display in reports (5 words before/after search term)
- Verified category filter functionality
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import sys
import threading
import webbrowser
from pathlib import Path
import subprocess
import time
from datetime import datetime
import re
from queue import Queue

# Add config directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config'))

from .file_search_tool import FileSearchTool, DEFAULT_REPORT_DIR
from .report_generator import HTMLReportGenerator
# Note: performance_config is in config/, not src/
# Import it via sys.path manipulation
import sys
import os
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config')
if config_path not in sys.path:
    sys.path.insert(0, config_path)
from performance_config import (
    AUTO_WORKER_COUNT,
    MANUAL_WORKER_COUNT,
)
from .settings_manager import get_settings_manager
from . import i18n
from .platform_utils import PlatformUtils, get_temp_dir, open_folder
from .loading_animations import ModernProgressBar, ModernBounceLoader, LoadingOverlay, show_loading

# Create a simple config dict for compatibility
PERFORMANCE_CONFIG = {
    "max_workers": MANUAL_WORKER_COUNT if not AUTO_WORKER_COUNT else None,
}


def parse_search_terms(raw_text: str):
    """Split raw input into search terms using comma, semicolon or newline."""
    parts = re.split(r"[,\n;]+", raw_text)
    terms = [p.strip() for p in parts if p.strip()]
    return terms


class MasterSearchGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(i18n.tr("app_title"))
        self.root.geometry("900x700")
        self.root.minsize(800, 600)

        # try set icon
        try:
            icon_path = os.path.join(os.path.dirname(__file__), "media", "master_search_icon.ico")
            if os.path.exists(icon_path):
                self.root.iconbitmap(icon_path)
        except Exception as e:
            print(f"Icon could not be loaded: {e}")

        self.setup_variables()
        self.setup_ui()
        self.setup_bindings()

        self.last_report_path = None

    def setup_variables(self):
        self.search_path = tk.StringVar()
        self.search_terms = tk.StringVar()
        self.file_pattern = tk.StringVar(value="*")
        self.search_mode = tk.StringVar(value="AND")
        self.use_regex = tk.BooleanVar(value=False)
        self.case_sensitive = tk.BooleanVar(value=False)
        self.include_content = tk.BooleanVar(value=True)
        # Worker-Standard: 4 Kerne, oder aus Config wenn gesetzt
        worker_default = PERFORMANCE_CONFIG.get("max_workers") or 4
        self.max_workers = tk.IntVar(value=worker_default)

        # Lade Settings aus Config
        settings_mgr = get_settings_manager()
        self.search_path.set(settings_mgr.get("search_path", str(Path.cwd())))
        self.max_workers.set(settings_mgr.get("max_workers", 4))
        self.search_mode.set(settings_mgr.get("search_mode", "AND"))
        self.case_sensitive.set(settings_mgr.get("case_sensitive", False))
        self.use_regex.set(settings_mgr.get("use_regex", False))
        self.include_content.set(settings_mgr.get("include_content", True))
        self.file_pattern.set(settings_mgr.get("file_pattern", "*"))
        
        # Category selections for file filtering
        self.category_code = tk.BooleanVar(value=settings_mgr.get("category_code", True))
        self.category_documents = tk.BooleanVar(value=settings_mgr.get("category_documents", True))
        self.category_data = tk.BooleanVar(value=settings_mgr.get("category_data", True))
        self.category_logs = tk.BooleanVar(value=settings_mgr.get("category_logs", True))
        self.category_config = tk.BooleanVar(value=settings_mgr.get("category_config", True))
        self.category_web = tk.BooleanVar(value=settings_mgr.get("category_web", True))
        
        # File extension to category mapping
        self.CATEGORY_MAPPING = {
            # Code
            'py': 'code', 'java': 'code', 'js': 'code', 'jsx': 'code', 'ts': 'code', 'tsx': 'code',
            'cpp': 'code', 'c': 'code', 'h': 'code', 'hpp': 'code', 'cs': 'code', 'swift': 'code',
            'go': 'code', 'rs': 'code', 'rb': 'code', 'php': 'code', 'scala': 'code',
            'kt': 'code', 'sh': 'code', 'bash': 'code', 'ps1': 'code', 'bat': 'code',
            
            # Documents
            'pdf': 'documents', 'docx': 'documents', 'doc': 'documents', 'xlsx': 'documents',
            'xls': 'documents', 'pptx': 'documents', 'ppt': 'documents', 'odt': 'documents',
            'rtf': 'documents',
            
            # Data
            'csv': 'data', 'json': 'data', 'xml': 'data', 'sql': 'data', 'db': 'data',
            'sqlite': 'data', 'yaml': 'data', 'yml': 'data',
            
            # Logs
            'log': 'logs',
            
            # Config
            'cfg': 'config', 'conf': 'config', 'config': 'config', 'ini': 'config', 'toml': 'config',
            'properties': 'config', 'env': 'config',
            
            # Web (includes documentation markup)
            'html': 'web', 'htm': 'web', 'css': 'web', 'scss': 'web', 'sass': 'web', 'less': 'web',
            'vue': 'web', 'svelte': 'web', 'md': 'web', 'rst': 'web', 'edcx': 'web', 'txt': 'web',
        }
        
        # Real-time status display variables (initialized later in setup_ui)
        self.files_processed_var = None
        self.matches_found_var = None
        self.scan_speed_var = None
        self.excluded_files_var = None
        
        # Queue for real-time status updates from search thread
        self.status_queue = Queue()
        
        # Stop flag for search interruption
        self.stop_search_flag = False
        self.search_thread = None
        self.current_search_tool = None  # Reference to current search tool for stop propagation

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky="nsew")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(8, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, columnspan=3, pady=(0, 20), sticky="ew")

        title_label = ttk.Label(header_frame, text="🔍 Master Search", font=("Segoe UI", 18, "bold"))
        title_label.pack(side="left")

        company_label = ttk.Label(header_frame, text=i18n.tr("company_label"), font=("Segoe UI", 10), foreground="gray")
        company_label.pack(side="right", anchor="e")

        # Search path
        ttk.Label(main_frame, text=i18n.tr("label_search_path"), font=("Segoe UI", 10, "bold")).grid(row=1, column=0, sticky="w", pady=2)

        path_frame = ttk.Frame(main_frame)
        path_frame.grid(row=1, column=1, columnspan=2, sticky="ew", pady=2)
        path_frame.grid_columnconfigure(0, weight=1)

        self.path_entry = ttk.Entry(path_frame, textvariable=self.search_path, font=("Consolas", 10))
        self.path_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))

        ttk.Button(path_frame, text="📂", width=4, command=self.browse_folder).grid(row=0, column=1)

        # Search terms
        ttk.Label(main_frame, text=i18n.tr("label_search_terms"), font=("Segoe UI", 10, "bold")).grid(row=2, column=0, sticky="w", pady=2)

        self.terms_entry = ttk.Entry(main_frame, textvariable=self.search_terms, font=("Consolas", 10), width=50)
        self.terms_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=2)

        hint_label = ttk.Label(main_frame, text=i18n.tr("hint_multiple_terms"), font=("Segoe UI", 9), foreground="gray")
        hint_label.grid(row=3, column=1, columnspan=2, sticky="w", pady=(0, 6))

        ttk.Label(main_frame, text=i18n.tr("label_file_pattern"), font=("Segoe UI", 10, "bold")).grid(row=4, column=0, sticky="w", pady=2)

        self.pattern_entry = ttk.Entry(main_frame, textvariable=self.file_pattern, font=("Consolas", 10), width=20)
        self.pattern_entry.grid(row=4, column=1, sticky="w", pady=2)

        # Options
        options_frame = ttk.LabelFrame(main_frame, text=" " + i18n.tr("options_title") + " ", padding="10")
        options_frame.grid(row=5, column=0, columnspan=3, sticky="ew", pady=10)
        options_frame.grid_columnconfigure(2, weight=1)

        ttk.Label(options_frame, text=i18n.tr("label_mode")).grid(row=0, column=0, sticky="w", padx=(0, 10))
        mode_frame = ttk.Frame(options_frame)
        mode_frame.grid(row=0, column=1, sticky="w")

        ttk.Radiobutton(mode_frame, text=i18n.tr("mode_and"), variable=self.search_mode, value="AND").pack(side="left", padx=5)
        ttk.Radiobutton(mode_frame, text=i18n.tr("mode_or"), variable=self.search_mode, value="OR").pack(side="left", padx=5)

        check_frame = ttk.Frame(options_frame)
        check_frame.grid(row=1, column=0, columnspan=3, sticky="w", pady=(5, 0))

        ttk.Checkbutton(check_frame, text=i18n.tr("include_content"), variable=self.include_content).pack(side="left", padx=(0, 15))
        ttk.Checkbutton(check_frame, text=i18n.tr("case_sensitive"), variable=self.case_sensitive).pack(side="left", padx=(0, 15))
        ttk.Checkbutton(check_frame, text=i18n.tr("use_regex"), variable=self.use_regex).pack(side="left")

        perf_frame = ttk.Frame(options_frame)
        perf_frame.grid(row=2, column=0, columnspan=3, sticky="w", pady=(5, 0))

        ttk.Label(perf_frame, text=i18n.tr("label_cpu_cores")).pack(side="left")
        ttk.Spinbox(perf_frame, from_=1, to=os.cpu_count(), textvariable=self.max_workers, width=5, font=("Consolas", 10)).pack(side="left", padx=(5, 15))
        ttk.Label(perf_frame, text=f"(available: {os.cpu_count()})").pack(side="left")

        # File Categories Selection
        category_frame = ttk.LabelFrame(main_frame, text=" 📁 File Categories ", padding="10")
        category_frame.grid(row=6, column=0, columnspan=3, sticky="ew", pady=10)
        category_frame.grid_columnconfigure(1, weight=1)

        # First row of categories
        cat_row1 = ttk.Frame(category_frame)
        cat_row1.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 5))

        ttk.Checkbutton(cat_row1, text="💻 Code (.py, .java, .js, .cpp, etc.)", variable=self.category_code).pack(side="left", padx=(0, 20))
        ttk.Checkbutton(cat_row1, text="📄 Documents (.pdf, .docx, .xlsx, etc.)", variable=self.category_documents).pack(side="left", padx=(0, 20))
        ttk.Checkbutton(cat_row1, text="📊 Data (.csv, .json, .xml, .sql)", variable=self.category_data).pack(side="left")

        # Second row of categories
        cat_row2 = ttk.Frame(category_frame)
        cat_row2.grid(row=1, column=0, columnspan=3, sticky="w", pady=(0, 0))

        ttk.Checkbutton(cat_row2, text="📝 Logs (.log, .txt)", variable=self.category_logs).pack(side="left", padx=(0, 20))
        ttk.Checkbutton(cat_row2, text="⚙️  Config (.conf, .yaml, .ini, .toml)", variable=self.category_config).pack(side="left", padx=(0, 20))
        ttk.Checkbutton(cat_row2, text="🌐 Web (.html, .css, .vue, etc.)", variable=self.category_web).pack(side="left")

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=3, pady=10)

        self.search_btn = ttk.Button(button_frame, text=i18n.tr("btn_search"), command=self.start_search, style="Accent.TButton")
        self.search_btn.pack(side="left", padx=5)
        
        self.stop_btn = ttk.Button(button_frame, text=i18n.tr("btn_stop"), command=self.stop_search, state="disabled")
        self.stop_btn.pack(side="left", padx=5)

        self.report_btn = ttk.Button(button_frame, text=i18n.tr("btn_show_last_report"), command=self.open_last_report, state="disabled")
        self.report_btn.pack(side="left", padx=5)

        self.folder_btn = ttk.Button(button_frame, text=i18n.tr("btn_report_folder"), command=self.open_report_folder)
        self.folder_btn.pack(side="left", padx=5)

        ttk.Button(button_frame, text=i18n.tr("btn_info"), command=self.show_info).pack(side="right", padx=5)

        # Log frame
        log_frame = ttk.LabelFrame(main_frame, text=" 📋 Status & Log ", padding="5")
        log_frame.grid(row=8, column=0, columnspan=3, sticky="nsew", pady=(0, 0))
        log_frame.grid_rowconfigure(3, weight=1)
        log_frame.grid_columnconfigure(0, weight=1)

        # Modern progress bar instead of standard ttk
        self.progress = ModernProgressBar(log_frame, width=600, height=12, color="#00A8FF", style="neon-pulse")
        
        # Keep reference to the canvas for grid management
        self.progress.canvas.grid(row=0, column=0, sticky="ew", pady=(0, 5))

        self.status_var = tk.StringVar(value=i18n.tr("status_ready"))
        self.status_label = ttk.Label(log_frame, textvariable=self.status_var, font=("Segoe UI", 9))
        self.status_label.grid(row=1, column=0, sticky="w", pady=(0, 5))

        # Real-time stats frame
        stats_frame = ttk.Frame(log_frame)
        stats_frame.grid(row=2, column=0, sticky="ew", pady=(0, 5))
        stats_frame.grid_columnconfigure(1, weight=1)
        stats_frame.grid_columnconfigure(3, weight=1)

        self.files_processed_var = tk.StringVar(value="Files: 0/0")
        self.matches_found_var = tk.StringVar(value="Matches: 0")
        self.excluded_files_var = tk.StringVar(value="")
        self.scan_speed_var = tk.StringVar(value="Speed: 0 files/sec")

        ttk.Label(stats_frame, textvariable=self.files_processed_var, font=("Segoe UI", 9), foreground="blue").grid(row=0, column=0, sticky="w", padx=5)
        ttk.Label(stats_frame, textvariable=self.matches_found_var, font=("Segoe UI", 9), foreground="green").grid(row=0, column=2, sticky="w", padx=5)
        ttk.Label(stats_frame, textvariable=self.excluded_files_var, font=("Segoe UI", 9), foreground="red").grid(row=0, column=3, sticky="w", padx=5)
        ttk.Label(stats_frame, textvariable=self.scan_speed_var, font=("Segoe UI", 9), foreground="orange").grid(row=0, column=4, sticky="w", padx=5)

        self.log_text = scrolledtext.ScrolledText(log_frame, height=8, font=("Consolas", 9), wrap=tk.WORD)
        self.log_text.grid(row=3, column=0, sticky="nsew")

        # Initial log
        self.log(i18n.tr("log_start_search"))
        self.log(f"📂 {i18n.tr('label_search_path')} {self.search_path.get()}")
        self.log(f"⚡ Available CPU cores: {os.cpu_count()}")

    def setup_bindings(self):
        self.root.bind("<Return>", lambda e: self.start_search())
        self.root.bind("<F5>", lambda e: self.start_search())
        self.root.bind("<Control-o>", lambda e: self.browse_folder())
        self.root.bind("<Control-r>", lambda e: self.open_last_report())

    def browse_folder(self):
        folder = filedialog.askdirectory(title=i18n.tr("dlg_browse_title"), initialdir=self.search_path.get())
        if folder:
            self.search_path.set(folder)
            self.log(f"📁 {i18n.tr('label_search_path')} changed: {folder}")

    def is_file_in_selected_categories(self, filepath):
        """Prüft, ob eine Datei zu den ausgewählten Kategorien gehört."""
        file_ext = os.path.splitext(filepath)[1].lstrip('.').lower()
        
        # Get the category for this file extension
        file_category = self.CATEGORY_MAPPING.get(file_ext, None)
        
        # Check if selected categories include this file's category
        category_selected = {
            'code': self.category_code.get(),
            'documents': self.category_documents.get(),
            'data': self.category_data.get(),
            'logs': self.category_logs.get(),
            'config': self.category_config.get(),
            'web': self.category_web.get(),
        }
        
        # If extension is not in mapping, exclude it (only include known types)
        if file_category is None:
            return False
        
        return category_selected.get(file_category, False)

    def get_filtered_files(self, search_directory):
        """Sammelt alle Dateien der ausgewählten Kategorien aus dem Suchverzeichnis."""
        filtered_files = []
        try:
            for root, dirs, files in os.walk(search_directory):
                # Check if search was stopped
                if self.stop_search_flag:
                    break
                    
                for file in files:
                    filepath = os.path.join(root, file)
                    if self.is_file_in_selected_categories(filepath):
                        filtered_files.append(filepath)
        except Exception as e:
            self.log(f"⚠️ Error while filtering files: {str(e)}")
        
        return filtered_files

    def log(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        formatted_message = f"[{timestamp}] {message}\n"
        self.log_text.insert(tk.END, formatted_message)
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def update_status(self, message):
        self.status_var.set(message)
        self.root.update_idletasks()

    def validate_inputs(self):
        if not self.search_path.get().strip():
            messagebox.showerror(i18n.tr("error"), i18n.tr("error_no_search_path"))
            return False
        if not os.path.exists(self.search_path.get()):
            messagebox.showerror(i18n.tr("error"), i18n.tr("error_path_not_exist"))
            return False
        if not self.search_terms.get().strip():
            messagebox.showerror(i18n.tr("error"), i18n.tr("error_no_search_terms"))
            return False
        return True

    def start_search(self):
        if not self.validate_inputs():
            return
        # prepare UI
        self.stop_search_flag = False
        self.search_btn.config(state="disabled", text=i18n.tr("search_started"))
        self.stop_btn.config(state="normal")
        self.progress.start_indeterminate()
        self.log_text.delete(1.0, tk.END)
        
        # Reset stats
        self.files_processed_var.set("📁 Files: 0/0")
        self.matches_found_var.set("🎯 Matches: 0")
        self.excluded_files_var.set("")
        self.scan_speed_var.set("⚡ Progress: 0%")
        
        # Clear previous results
        self.last_report_path = None
        self.report_btn.config(state="disabled")
        self.search_thread = threading.Thread(target=self.perform_search)
        self.search_thread.daemon = True
        self.search_thread.start()
    
    def stop_search(self):
        """Stop the search and generate report with collected data."""
        self.stop_search_flag = True
        # Propagate stop to search tool if running
        if hasattr(self, 'current_search_tool') and self.current_search_tool:
            self.current_search_tool.stop_requested = True
        self.stop_btn.config(state="disabled")
        self.log(i18n.tr("search_stopped"))
        self.update_status(i18n.tr("search_stopped_msg"))

    def perform_search(self):
        try:
            search_params = {
                "directory": self.search_path.get(),
                "terms": parse_search_terms(self.search_terms.get()),
                "file_pattern": self.file_pattern.get() if self.file_pattern.get() else "*",
                "mode": self.search_mode.get(),
                "case_sensitive": self.case_sensitive.get(),
                "use_regex": self.use_regex.get(),
                "search_content": self.include_content.get(),
                "max_workers": self.max_workers.get(),
            }

            self.log(i18n.tr("log_start_search"))
            self.log(f"   📁 Path: {search_params['directory']}")
            self.log(f"   🔤 Terms: {', '.join(search_params['terms'])}")
            self.log(f"   📄 Pattern: {search_params['file_pattern']}")
            self.log(f"   🔧 Mode: {search_params['mode']}")
            self.log(f"   ⚡ Workers: {search_params['max_workers']} parallel processes for faster search")
            self.log("")

            # Save category selections to settings
            settings_mgr = get_settings_manager()
            settings_mgr.set("category_code", self.category_code.get())
            settings_mgr.set("category_documents", self.category_documents.get())
            settings_mgr.set("category_data", self.category_data.get())
            settings_mgr.set("category_logs", self.category_logs.get())
            settings_mgr.set("category_config", self.category_config.get())
            settings_mgr.set("category_web", self.category_web.get())
            
            # Log selected categories
            selected_cats = []
            if self.category_code.get(): selected_cats.append("💻 Code")
            if self.category_documents.get(): selected_cats.append("📄 Documents")
            if self.category_data.get(): selected_cats.append("📊 Data")
            if self.category_logs.get(): selected_cats.append("📝 Logs")
            if self.category_config.get(): selected_cats.append("⚙️ Config")
            if self.category_web.get(): selected_cats.append("🌐 Web")
            
            if selected_cats:
                self.log(f"   📁 Categories: {', '.join(selected_cats)}")
            
            self.update_status(i18n.tr("search_started"))

            # Create search tool instance (verbose=False to suppress console output)
            search_tool = FileSearchTool(verbose=False)
            self.current_search_tool = search_tool  # Store reference for stop propagation
            search_tool.search_path = search_params["directory"]
            search_tool.search_terms = search_params["terms"]
            search_tool.search_mode = search_params["mode"].lower() 
            search_tool.case_sensitive = search_params.get("case_sensitive", False)
            search_tool.use_regex = search_params.get("regex", False)
            search_tool.max_workers = search_params["max_workers"]
            # IMPORTANT: Disable multiprocessing in GUI context (prevents multiple window spawning)
            search_tool.use_multiprocessing = False
            
            # Set callback function for real-time status updates
            search_tool.status_callback = self.on_search_status_update
            
            # Start processing status updates from queue
            self.process_status_updates()
            
            # Run search with stop flag checking
            search_tool.search_files_and_folders()
            results = search_tool.results
            
            # Filter results by selected file categories
            excluded_count = 0
            if results:
                before_filter = len(results)
                results = [
                    result for result in results 
                    if self.is_file_in_selected_categories(result.get('path', ''))
                ]
                after_filter = len(results)
                excluded_count = before_filter - after_filter
                if excluded_count > 0:
                    self.log(f"📁 Filtered by categories: {before_filter} → {after_filter} results")
                    self.log(f"   🚫 Außerhalb des Filters: {excluded_count} Dateien")
                
                # Count filtered matches
                filtered_matches = sum(len(result.get('matches', [])) for result in results)
                self.matches_found_var.set(f"🎯 Matches: {filtered_matches:,}")
                self.files_processed_var.set(f"📁 Files: {after_filter:,}")
                if excluded_count > 0:
                    self.excluded_files_var.set(f"🚫 {excluded_count:,} ausgeschlossen")
            
            # Check if user stopped the search
            if self.stop_search_flag:
                self.log(i18n.tr("search_interrupted"))
                matches_count = len(results) if results else 0
                self.log(i18n.tr("collected_results", count=matches_count))
            else:
                matches_count = len(results) if results else 0
                self.log(i18n.tr("search_finished") + f": {matches_count} files")
                self.update_status(i18n.tr("search_finished") + f" - {matches_count} files")

            # Generate report with collected data (whether search was stopped or not)
            # Ensure report directory exists
            # Cross-platform default report directory
            report_dir = DEFAULT_REPORT_DIR or get_temp_dir()
            Path(report_dir).mkdir(parents=True, exist_ok=True)
            
            report_gen = HTMLReportGenerator(
                search_terms=search_params["terms"],
                search_path=search_params["directory"],
                case_sensitive=search_tool.case_sensitive,
                use_regex=search_tool.use_regex,
                output_dir=str(report_dir)
            )
            report_path = report_gen.generate(results=results)

            self.last_report_path = report_path
            if report_path:
                if self.stop_search_flag:
                    self.log(i18n.tr("report_partial", report=str(report_path)))
                    self.update_status(i18n.tr("report_partial", report=os.path.basename(report_path)))
                else:
                    self.log(i18n.tr("report_created", report=str(report_path)))
                    self.update_status(i18n.tr("report_created", report=str(report_path)))
                
                self.root.after(0, lambda: self.report_btn.config(state="normal"))
                
                if self.stop_search_flag:
                    self.root.after(0, lambda: messagebox.showinfo(i18n.tr("search_stopped_title"), i18n.tr("search_stopped_message", matches=matches_count, report=os.path.basename(report_path))))
                else:
                    self.root.after(0, lambda: messagebox.showinfo(i18n.tr("search_complete_title"), i18n.tr("search_complete_message", matches=matches_count, report=os.path.basename(report_path))))

        except Exception as e:
            error_msg = f"Error during search: {str(e)}"
            self.log(error_msg)
            self.update_status(i18n.tr("error") + ": " + str(e))
            self.root.after(0, lambda: messagebox.showerror(i18n.tr("error"), error_msg))

        finally:
            # Clean up search tool reference
            self.current_search_tool = None
            self.root.after(0, self.search_finished)

    def on_search_status_update(self, status_data):
        """Callback function from FileSearchTool to receive real-time status updates."""
        try:
            self.status_queue.put(status_data, block=False)
        except:
            pass  # Queue full, skip this update

    def process_status_updates(self):
        """Process real-time status updates from the queue and update GUI."""
        try:
            while True:
                status_data = self.status_queue.get_nowait()
                
                if status_data.get('type') == 'progress':
                    # Update progress bar and stats
                    processed = status_data.get('processed', 0)
                    total = status_data.get('total', 1)
                    matches = status_data.get('matches', 0)
                    percent = status_data.get('percent', 0)
                    
                    # Calculate speed (files per second)
                    if processed > 0:
                        speed = processed  # files processed so far
                    else:
                        speed = 0
                    
                    # Update display variables
                    self.files_processed_var.set(f"📁 Files: {processed:,}/{total:,}")
                    self.matches_found_var.set(f"🎯 Matches: {matches:,}")
                    
                    if processed > 0 and percent > 0:
                        self.scan_speed_var.set(f"⚡ Progress: {percent:.1f}%")
                    
                    self.root.update_idletasks()
                
                elif status_data.get('type') == 'complete':
                    # Final update
                    total = status_data.get('total', 0)
                    matches = status_data.get('matches', 0)
                    elapsed = status_data.get('elapsed_time', 0)
                    speed = status_data.get('speed', 0)
                    
                    self.files_processed_var.set(f"📁 Files: {total:,}/{total:,}")
                    self.matches_found_var.set(f"🎯 Matches: {matches:,}")
                    if elapsed > 0:
                        self.scan_speed_var.set(f"⚡ Speed: {speed:.0f} files/sec")
                    
        except:
            pass  # Queue empty or error
        
        # Schedule next update check
        if not self.stop_search_flag:
            self.root.after(100, self.process_status_updates)

    def search_finished(self):
        self.progress.stop_indeterminate()
        self.search_btn.config(state="normal", text=i18n.tr("btn_search"))
        self.stop_btn.config(state="disabled")
        self.stop_search_flag = False

    def open_last_report(self):
        if self.last_report_path and os.path.exists(self.last_report_path):
            try:
                webbrowser.open(f"file://{self.last_report_path}")
                self.log(f"🌐 Report opened: {os.path.basename(self.last_report_path)}")
            except Exception as e:
                self.log(f"Error opening report: {str(e)}")
                messagebox.showerror(i18n.tr("error"), f"Report could not be opened:\n{str(e)}")
        else:
            messagebox.showwarning(i18n.tr("no_report_warning_title"), i18n.tr("no_report_warning_msg"))

    def open_report_folder(self):
        try:
            report_dir = Path(DEFAULT_REPORT_DIR)
            report_dir.mkdir(parents=True, exist_ok=True)
            if not open_folder(str(report_dir)):
                messagebox.showinfo(i18n.tr("info"), f"Report folder: {report_dir}")
            else:
                self.log(f"📂 Report folder opened: {report_dir}")
        except Exception as e:
            self.log(f"Error opening folder: {str(e)}")
            messagebox.showerror(i18n.tr("error"), f"Could not open folder:\n{str(e)}")

    def show_info(self):
        try:
            from version import VERSION
            about_text = i18n.tr("about_text").format(VERSION)
            messagebox.showinfo(i18n.tr("about_title"), about_text)
        except ImportError:
            # Fallback wenn version.py nicht gefunden wird
            about_text = i18n.tr("about_text").format("2025.11.10")
            messagebox.showinfo(i18n.tr("about_title"), about_text)

    def show_release_notes(self):
        """Zeigt die Release Notes in einem separaten Fenster."""
        try:
            from version import VERSION
            
            # Prüfe ob diese Version bereits gezeigt wurde
            settings_mgr = get_settings_manager()
            last_version = settings_mgr.get("last_shown_version", "")
            
            # Zeige Release Notes wenn noch nicht gezeigt
            if VERSION != last_version:
                # Erstelle eigenständiges Release Notes Fenster
                notes_window = tk.Toplevel(self.root)
                notes_window.title(f"🆕 Master Search v{VERSION} - Release Notes")
                notes_window.geometry("700x600")
                notes_window.minsize(600, 400)
                
                # Header
                header_frame = ttk.Frame(notes_window)
                header_frame.pack(fill="x", padx=15, pady=15)
                
                version_label = ttk.Label(
                    header_frame, 
                    text=f"Master Search v{VERSION}",
                    font=("Segoe UI", 16, "bold")
                )
                version_label.pack(anchor="w")
                
                date_label = ttk.Label(
                    header_frame,
                    text=f"Released: November 12, 2025",
                    font=("Segoe UI", 10),
                    foreground="gray"
                )
                date_label.pack(anchor="w", pady=(5, 0))
                
                # Separator
                ttk.Separator(notes_window, orient="horizontal").pack(fill="x", padx=15, pady=10)
                
                # Content Frame mit Scrollbar
                content_frame = ttk.Frame(notes_window)
                content_frame.pack(fill="both", expand=True, padx=15, pady=10)
                
                # Text Widget mit Scrollbar
                scrollbar = ttk.Scrollbar(content_frame)
                scrollbar.pack(side="right", fill="y")
                
                text_widget = tk.Text(
                    content_frame,
                    wrap="word",
                    yscrollcommand=scrollbar.set,
                    font=("Segoe UI", 10),
                    relief="flat",
                    bg="#f5f5f5",
                    fg="#333333"
                )
                text_widget.pack(fill="both", expand=True)
                scrollbar.config(command=text_widget.yview)
                
                # Release Notes Content
                release_notes = f"""🎉 Master Search v{VERSION}

✨ NEUE FEATURES

📍 Zeilennummern in Suchergebnissen
   • Zeilennummern bei allen Dateitypen angezeigt
   • Unterstützung für: Text, Code, CSV, PDF, Office, Logs, HTML, XML
   • Konsistente Anzeige im Report: "Zeile N:"

📊 Unterstützte Dateitypen mit Zeilennummern
   • Textdateien: .txt, .md, .rst, .log
   • Code: .py, .js, .java, .cpp, .cs, .rb, .go, .rs, .sh, .ps1, .bat
   • Web & Markup: .html, .xml, .json, .css, .vue, .svelte
   • Daten: .csv, .sql, .yaml, .ini, .conf
   • Office: .docx, .doc, .pdf, .xlsx, .pptx, .odt, .rtf

🔧 VERBESSERTE EXTRAKTOREN

   ✅ DOCX - mit Paragraph-Nummern
   ✅ DOC - alte Word-Dateien
   ✅ PDF - mit PyPDF2
   ✅ PPTX - PowerPoint Slides
   ✅ ODT - OpenDocument Format
   ✅ RTF - Rich Text Format
   ✅ XLSX - Excel Spreadsheets
   ✅ CSV - mit Encoding-Unterstützung
   ✅ LOG - Log-Dateien
   ✅ Standard-Textdateien

🧪 TESTING

   • Umfangreiche Tests mit 13+ Dateitypen
   • Validierung aller Extraktoren
   • Performance optimiert

📥 REPORT-BUTTONS

   • "Öffnen" Button - Öffnet in Windows Explorer
   • "Download" Button - Download via Browser
   • Mobile-responsive Design
   • Automatisches Fallback zu Clipboard

⚡ PERFORMANCE

   • Echtzeit Status-Display während Suche
   • Datei-Counter, Match-Counter, Scan-Speed
   • Multi-Threading/Multi-Processing
   • Optimierte Batch-Verarbeitung

---

🚀 PRODUCTION READY
   Vollständig getestet und produktionsreif!

💡 TIPPS

   • Drücke ENTER um Suche zu starten
   • Drücke STRG+O um Ordner zu wählen
   • Drücke STRG+R um letzten Report zu öffnen
   • Verwende Regex für erweiterte Suche

---

Version {VERSION} © 2025 LOONY-TECH
www.loony-tech.de"""
                
                text_widget.insert("1.0", release_notes)
                text_widget.config(state="disabled")  # Readonly
                
                # Footer mit Close-Button
                footer_frame = ttk.Frame(notes_window)
                footer_frame.pack(fill="x", padx=15, pady=15)
                
                close_button = ttk.Button(
                    footer_frame,
                    text="✓ Verstanden",
                    command=lambda: (
                        settings_mgr.update({"last_shown_version": VERSION}),
                        notes_window.destroy()
                    )
                )
                close_button.pack(side="right")
                
                # Positioniere Fenster auf dem Bildschirm
                notes_window.transient(self.root)
                notes_window.grab_set()
                
                # Zentriere das Fenster über der Hauptanwendung
                self.root.update_idletasks()
                x = self.root.winfo_x() + (self.root.winfo_width() - 700) // 2
                y = self.root.winfo_y() + (self.root.winfo_height() - 600) // 2
                notes_window.geometry(f"+{max(0, x)}+{max(0, y)}")
                
                # Aktualisiere last_shown_version
                settings_mgr.update({"last_shown_version": VERSION})
                
        except Exception as e:
            pass  # Fehlerhafte Anzeige ist nicht kritisch

    def run(self):
        try:
            style = ttk.Style()
            style.theme_use("winnative")
        except Exception:
            pass

        self.log(i18n.tr("status_ready"))
        
        # Speichere Settings wenn Fenster geschlossen wird
        def on_closing():
            self.save_settings()
            self.root.destroy()
        
        self.root.protocol("WM_DELETE_WINDOW", on_closing)
        
        # Ensure window is visible and on top
        self.root.deiconify()
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        
        # Zeige Release Notes wenn neue Version vorhanden
        self.root.after(500, self.show_release_notes)
        
        self.root.mainloop()
    
    def save_settings(self):
        """Speichert aktuelle Einstellungen in die Config-Datei"""
        try:
            settings_mgr = get_settings_manager()
            settings_mgr.update({
                "search_path": self.search_path.get(),
                "max_workers": self.max_workers.get(),
                "search_mode": self.search_mode.get(),
                "case_sensitive": self.case_sensitive.get(),
                "use_regex": self.use_regex.get(),
                "include_content": self.include_content.get(),
                "file_pattern": self.file_pattern.get(),
            })
            settings_mgr.save_settings()
        except Exception as e:
            print(f"⚠️  Could not save settings: {e}")


# NOTE: Do NOT add any main() or if __name__ == "__main__" here!
# This is imported by gui_main.py which handles the entry point.