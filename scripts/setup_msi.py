#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - MSI Builder Setup
==================================
cx_Freeze Setup für MSI-Erstellung

Developer: Loony2392
Company: LOONY-TECH  
Email: info@loony-tech.de
"""

import sys
import os
from pathlib import Path
from cx_Freeze import setup, Executable
from version import VERSION

# Build-Optionen
build_options = {
    'packages': [
        'os', 'sys', 're', 'html', 'pathlib', 'datetime', 'mimetypes', 'time', 
        'multiprocessing', 'concurrent.futures', 'threading', 'queue', 'subprocess',
        'tkinter', 'tkinter.ttk', 'tkinter.filedialog', 'tkinter.messagebox',
        'tkinter.scrolledtext', 'webbrowser', 'urllib', 'urllib.parse'
    ],
    'includes': ['colorama', 'psutil'],
    'excludes': [
        'unittest', 'pydoc', 'doctest', 'test', 'distutils',
        'email', 'http', 'xml', 'pdb', 'sqlite3', 'socketserver'
    ],
    'include_files': [
        ('README.md', 'README.md'),
        ('requirements.txt', 'requirements.txt'),
        ('requirements-minimal.txt', 'requirements-minimal.txt'),
        ('version.py', 'version.py'),
        ('performance_config.py', 'performance_config.py'),
        ('gui_search_tool.py', 'gui_search_tool.py'),
        ('file_search_tool.py', 'file_search_tool.py'),
        ('report_generator.py', 'report_generator.py'),
        ('i18n.py', 'i18n.py'),
        ('language_config.py', 'language_config.py'),
        ('update_notifier.py', 'update_notifier.py'),
        ('gui_main.py', 'gui_main.py'),
        ('cli_main.py', 'cli_main.py'),
        ('media/master_search_icon.ico', 'media/master_search_icon.ico'),
        ('media/loony_tech_logo.ico', 'media/loony_tech_logo.ico'),
        ('locales', 'locales'),  # Include translation files
    ],
    'zip_include_packages': ['encodings', 'importlib', 'collections'],
    'optimize': 2,
}

# MSI-Optionen
bdist_msi_options = {
    'upgrade_code': '{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}',  # Eindeutige GUID für Master Search
    'add_to_path': False,  # Nicht zu PATH hinzufügen
    'initial_target_dir': r'[ProgramFilesFolder]\Master Search',
    'install_icon': 'media/master_search_icon.ico',
    'all_users': True,  # Installation für alle Benutzer
}

# Beispiel: shortcut_table für Startmenü- und Desktop-Verknüpfungen
shortcut_table = [
    # Startmenü-Eintrag für GUI-EXE
    ("StartMenuShortcut_GUI",      # Shortcut Id
     "StartMenuFolder",            # Directory (Startmenü)
     "Master Search",              # Name
     "TARGETDIR",                  # Component_
     "[TARGETDIR]MasterSearch.exe",# Target (Relativer Pfad in TARGETDIR)
     None,                         # Arguments
     "Master Search - GUI",        # Description
     None, None, None, None, 'TARGETDIR'  # Hotkey, Icon, IconIndex, ShowCmd, WkDir
     ),
    # Startmenü-Eintrag für CLI-EXE
    ("StartMenuShortcut_CLI",
     "StartMenuFolder",
     "Master Search (CLI)",
     "TARGETDIR",
     "[TARGETDIR]MasterSearchCLI.exe",
     None,
     "Master Search - CLI",
     None, None, None, None, 'TARGETDIR'
     ),
    # Optional: Desktop-Shortcut für GUI
    ("DesktopShortcut_GUI",
     "DesktopFolder",
     "Master Search",
     "TARGETDIR",
     "[TARGETDIR]MasterSearch.exe",
     None,
     "Master Search - GUI",
     None, None, None, None, 'TARGETDIR'
     ),
]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options['data'] = msi_data

# Basis für Executable bestimmen
if sys.platform == "win32":
    base_gui = "Win32GUI"  # GUI-Anwendung ohne Konsole
    base_console = None    # Console-Anwendung
else:
    base_gui = None
    base_console = None

# Executables definieren
executables = [
    Executable(
        'gui_main.py',
        base=base_gui,
        target_name='MasterSearch.exe',
        icon='media/master_search_icon.ico',
        copyright='Copyright (C) 2025 LOONY-TECH - Loony2392',
    ),
    Executable(
        'cli_main.py',
        base=base_console,
        target_name='MasterSearchCLI.exe',
        icon='media/loony_tech_logo.ico',
        copyright='Copyright (C) 2025 LOONY-TECH - Loony2392',
    )
]

setup(
    name='Master Search',
    version=VERSION,
    description='Professional Multi-Term File Search Tool',
    long_description='A comprehensive file and content search utility with HTML reporting, multi-term support, regex capabilities, and high-performance parallel processing developed by LOONY-TECH.',
    author='Loony2392',
    author_email='info@loony-tech.de',
    url='https://github.com/Loony2392/master-search',
    license='MIT',
    options={
        'build_exe': build_options,
        'bdist_msi': bdist_msi_options,
    },
    executables=executables,
)