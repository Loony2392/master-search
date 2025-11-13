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

# WORKAROUND: Suppress cx_Freeze's DLL directory errors
# Patch ctypes.windll.kernel32.SetDllDirectory to not fail on permission errors
if sys.platform == 'win32':
    try:
        import ctypes
        original_set_dll = ctypes.windll.kernel32.SetDllDirectory
        def safe_set_dll_directory(path):
            try:
                return original_set_dll(path)
            except Exception:
                # Silently ignore DLL directory errors
                return 1  # Return success anyway
        ctypes.windll.kernel32.SetDllDirectory = safe_set_dll_directory
    except Exception:
        pass

# Add parent directory to sys.path to import version
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
from version import VERSION

# Change to project root for cx_Freeze build
os.chdir(str(project_root))

# Get Python installation directory for tkinter DLLs
# sys.executable = C:\Users\...\Python311\python.exe
# So parent = C:\Users\...\Python311\
python_base = os.path.dirname(sys.executable)  # C:\Users\...\Python311\
python_dlls = os.path.join(python_base, 'DLLs')  # C:\Users\...\Python311\DLLs\
python_tcltk = os.path.join(python_base, 'tcl')  # C:\Users\...\Python311\tcl\

# Build-Optionen
build_options = {
    'packages': [
        'os', 'sys', 're', 'html', 'pathlib', 'datetime', 'mimetypes', 'time', 
        'multiprocessing', 'concurrent.futures', 'threading', 'queue', 'subprocess',
        'ctypes', 'ctypes.util', 'tkinter', 'tkinter.ttk', 'tkinter.font', 'tkinter.messagebox'
    ],
    'includes': [
        'colorama', 'psutil', 'tkinter',
        # Explicitly include config and src as packages
        'config', 'config.language_config', 'config.performance_config',
        'src', 'src.file_search_tool', 'src.gui_search_tool', 'src.loading_animations',
        'src.i18n', 'src.report_generator', 'src.update_notifier', 'src.settings_manager',
        'src.platform_utils'
    ],
    'excludes': [
        'unittest', 'pydoc', 'doctest', 'test', 'distutils',
        'email', 'http', 'xml', 'pdb', 'sqlite3', 'socketserver'
    ],
    'include_files': [
        ('config', 'config'),      # Config module (language_config, performance_config)
        ('src', 'src'),            # Source modules
        ('locales', 'locales'),    # Translation files
        ('media', 'media'),        # Icons and images
        (str(project_root / 'init_dll_path.py'), 'init_dll_path.py'),  # DLL initialization
        # Include complete Python DLLs directory (contains tkinter DLLs)
        (python_dlls, 'lib/DLLs'),
        # Include tcl/tk library files
        (python_tcltk, 'tcl'),
    ],
    'zip_include_packages': [],  # Don't zip packages - include them as directories
    'zip_exclude_packages': '*',  # Exclude everything from zip
    'optimize': 0,  # Don't optimize - keep source as-is for debugging and proper imports
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
    base_gui = "Win32GUI"  # GUI application without console window
    base_console = None    # Console application
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