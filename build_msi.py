#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - MSI Installer Builder
======================================
Creates native Windows MSI installers using cx_Freeze

Features:
  - Builds GUI and CLI executables
  - Packages as Windows MSI installer
  - Creates proper uninstaller
  - Registers in Add/Remove Programs
  - Professional installer wizard

Output: Master_Search-YYYY.MM.DD-win64.msi

Author: Loony2392
Company: LOONY-TECH
"""

import sys
import subprocess
import shutil
from pathlib import Path
from datetime import datetime
import re

class MSIBuilder:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.scripts_dir = self.project_root / 'scripts'
        self.dist_folder = self.project_root / 'dist'
        self.build_folder = self.project_root / 'build'
        self.msi_build_folder = self.project_root / 'msi_build'
        
        # Get version from version.py
        self.version = self._get_version()
        self.msi_filename = f"Master_Search-{self.version}-win64.msi"
        
    def _get_version(self):
        """Extract version from version.py"""
        version_file = self.project_root / 'version.py'
        if version_file.exists():
            with open(version_file, 'r', encoding='utf-8') as f:
                content = f.read()
                match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
                if match:
                    return match.group(1)
        # Fallback to current date
        return datetime.now().strftime('%Y.%m.%d')
    
    def print_status(self, message, prefix='[*]'):
        """Print status message with color."""
        colors = {
            '[*]': '\033[94m',      # Blue
            '[OK]': '\033[92m',     # Green
            '[ERROR]': '\033[91m',  # Red
            '[BUILD]': '\033[95m',  # Magenta
            '[WARNING]': '\033[93m' # Yellow
        }
        reset = '\033[0m'
        color = colors.get(prefix, '')
        print(f"{color}{prefix}{reset} {message}")
    
    def clean_build(self):
        """Clean previous builds."""
        self.print_status("Cleaning previous builds...", "[*]")
        for folder in [self.build_folder, self.dist_folder, self.msi_build_folder]:
            if folder.exists():
                shutil.rmtree(folder, ignore_errors=True)
                self.print_status(f"Removed {folder.name}/", "[OK]")
    
    def check_dependencies(self):
        """Check if required tools are installed."""
        self.print_status("Checking dependencies...", "[*]")
        
        # Check cx_Freeze
        try:
            import cx_Freeze
            self.print_status(f"cx_Freeze {cx_Freeze.__version__} found", "[OK]")
        except ImportError:
            self.print_status("cx_Freeze not installed. Installing...", "[WARNING]")
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'cx_Freeze>=7.0'], check=True)
        
        # Check PyInstaller (for fallback executables)
        try:
            import PyInstaller
            self.print_status(f"PyInstaller found", "[OK]")
        except ImportError:
            self.print_status("PyInstaller not installed. Installing...", "[WARNING]")
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'PyInstaller>=6.0'], check=True)
        
        return True
    
    def build_gui_exe(self):
        """Build GUI executable with cx_Freeze."""
        self.print_status("Building GUI executable with cx_Freeze...", "[*]")
        
        setup_file = self.scripts_dir / 'cx_freeze_gui_setup.py'
        
        # Create cx_Freeze setup script if it doesn't exist
        if not setup_file.exists():
            self._create_cx_freeze_gui_setup()
        
        try:
            result = subprocess.run(
                [sys.executable, str(setup_file), 'build'],
                cwd=str(self.project_root),
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                self.print_status("GUI executable built successfully", "[OK]")
                return True
            else:
                self.print_status(f"Error: {result.stderr}", "[ERROR]")
                return False
        except Exception as e:
            self.print_status(f"Error: {e}", "[ERROR]")
            return False
    
    def build_cli_exe(self):
        """Build CLI executable with cx_Freeze."""
        self.print_status("Building CLI executable with cx_Freeze...", "[*]")
        
        setup_file = self.scripts_dir / 'cx_freeze_cli_setup.py'
        
        # Create cx_Freeze setup script if it doesn't exist
        if not setup_file.exists():
            self._create_cx_freeze_cli_setup()
        
        try:
            result = subprocess.run(
                [sys.executable, str(setup_file), 'build'],
                cwd=str(self.project_root),
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                self.print_status("CLI executable built successfully", "[OK]")
                return True
            else:
                self.print_status(f"Error: {result.stderr}", "[ERROR]")
                return False
        except Exception as e:
            self.print_status(f"Error: {e}", "[ERROR]")
            return False
    
    def build_msi(self):
        """Build MSI installer with cx_Freeze."""
        self.print_status("Building MSI installer...", "[*]")
        
        setup_file = self.scripts_dir / 'cx_freeze_msi_setup.py'
        
        if not setup_file.exists():
            self._create_cx_freeze_msi_setup()
        
        try:
            result = subprocess.run(
                [sys.executable, str(setup_file), 'bdist_msi'],
                cwd=str(self.project_root),
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                self.print_status("MSI installer built successfully", "[OK]")
                return self._move_msi_to_dist()
            else:
                self.print_status(f"Error building MSI: {result.stderr}", "[ERROR]")
                self.print_status("Attempting fallback with PyInstaller...", "[WARNING]")
                return self._build_exe_fallback()
        except Exception as e:
            self.print_status(f"Error: {e}", "[ERROR]")
            return False
    
    def _move_msi_to_dist(self):
        """Move generated MSI to dist folder."""
        try:
            # cx_Freeze puts MSI in build/exe.win-amd64-3.x/
            msi_files = list(self.project_root.glob('build/**/*.msi'))
            
            if msi_files:
                self.dist_folder.mkdir(exist_ok=True)
                src = msi_files[0]
                dst = self.dist_folder / self.msi_filename
                shutil.move(str(src), str(dst))
                self.print_status(f"MSI moved to {dst.name}", "[OK]")
                return True
            
            # Try dist folder
            msi_files = list(self.dist_folder.glob('*.msi'))
            if msi_files:
                src = msi_files[0]
                dst = self.dist_folder / self.msi_filename
                if src != dst:
                    src.rename(dst)
                self.print_status(f"MSI renamed to {self.msi_filename}", "[OK]")
                return True
            
            self.print_status("No MSI file found after build", "[ERROR]")
            return False
        except Exception as e:
            self.print_status(f"Error moving MSI: {e}", "[ERROR]")
            return False
    
    def _build_exe_fallback(self):
        """Build EXE installers as fallback using PyInstaller."""
        self.print_status("Using PyInstaller as fallback...", "[WARNING]")
        
        try:
            # Build GUI
            result = subprocess.run(
                [sys.executable, '-m', 'PyInstaller', str(self.scripts_dir / 'gui.spec')],
                cwd=str(self.project_root),
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                self.print_status(f"GUI build failed: {result.stderr}", "[ERROR]")
                return False
            
            self.print_status("GUI executable created (fallback)", "[OK]")
            
            # Build CLI
            result = subprocess.run(
                [sys.executable, '-m', 'PyInstaller', str(self.scripts_dir / 'cli.spec')],
                cwd=str(self.project_root),
                capture_output=True,
                text=True
            )
            
            if result.returncode != 0:
                self.print_status(f"CLI build failed: {result.stderr}", "[ERROR]")
                return False
            
            self.print_status("CLI executable created (fallback)", "[OK]")
            return True
        except Exception as e:
            self.print_status(f"Fallback failed: {e}", "[ERROR]")
            return False
    
    def _create_cx_freeze_gui_setup(self):
        """Create cx_Freeze setup.py for GUI."""
        setup_content = '''"""cx_Freeze setup for GUI"""
from cx_Freeze import setup, Executable
import sys

setup(
    name="Master Search",
    version="${VERSION}",
    description="Advanced file search tool",
    executables=[
        Executable("gui_main.py", target_name="Master_Search.exe", icon="media/icon.ico" if exists("media/icon.ico") else None)
    ]
)
'''.replace('${VERSION}', self.version)
        
        setup_file = self.scripts_dir / 'cx_freeze_gui_setup.py'
        setup_file.write_text(setup_content, encoding='utf-8')
    
    def _create_cx_freeze_cli_setup(self):
        """Create cx_Freeze setup.py for CLI."""
        setup_content = '''"""cx_Freeze setup for CLI"""
from cx_Freeze import setup, Executable

setup(
    name="Master Search CLI",
    version="${VERSION}",
    description="Advanced file search tool (CLI)",
    executables=[
        Executable("cli_main.py", target_name="MasterSearch_CLI.exe")
    ]
)
'''.replace('${VERSION}', self.version)
        
        setup_file = self.scripts_dir / 'cx_freeze_cli_setup.py'
        setup_file.write_text(setup_content, encoding='utf-8')
    
    def _create_cx_freeze_msi_setup(self):
        """Create cx_Freeze setup.py for MSI."""
        setup_content = '''"""cx_Freeze setup for MSI installer"""
from cx_Freeze import setup, Executable
from pathlib import Path

project_root = Path(__file__).parent.parent

setup(
    name="Master Search",
    version="${VERSION}",
    author="Loony2392",
    author_email="contact@loony-tech.de",
    description="Advanced file search tool",
    long_description="Master Search - Professional file search utility with GUI and CLI",
    url="https://github.com/Loony2392/master-search",
    executables=[
        Executable(
            "gui_main.py",
            target_name="Master_Search.exe",
            icon=str(project_root / "media" / "icon.ico") if (project_root / "media" / "icon.ico").exists() else None
        ),
        Executable(
            "cli_main.py",
            target_name="MasterSearch_CLI.exe"
        )
    ],
    options={
        "bdist_msi": {
            "add_to_path": True,
            "upgrade_code": "{3F692526-948B-4B39-BF5F-1C3FD99FC7F4}",
            "initial_target_dir": "[ProgramFilesFolder]\\\\Master Search",
        }
    }
)
'''.replace('${VERSION}', self.version)
        
        setup_file = self.scripts_dir / 'cx_freeze_msi_setup.py'
        setup_file.write_text(setup_content, encoding='utf-8')
    
    def show_results(self):
        """Display build results."""
        print("\n" + "="*60)
        self.print_status("MSI BUILD COMPLETED", "[BUILD]")
        print("="*60 + "\n")
        
        if (self.dist_folder / self.msi_filename).exists():
            msi_size = (self.dist_folder / self.msi_filename).stat().st_size / (1024 * 1024)
            self.print_status(f"✅ {self.msi_filename} ({msi_size:.1f} MB)", "[OK]")
        
        exe_files = list(self.dist_folder.glob('*.exe'))
        if exe_files:
            self.print_status("Executables:", "[*]")
            for exe in exe_files:
                size_mb = exe.stat().st_size / (1024 * 1024)
                self.print_status(f"  {exe.name} ({size_mb:.1f} MB)", "[*]")
        
        self.print_status(f"Output folder: {self.dist_folder}", "[*]")
        print()
    
    def run(self):
        """Run the complete build process."""
        print("\n" + "="*60)
        self.print_status("MASTER SEARCH - MSI INSTALLER BUILDER", "[BUILD]")
        print(f"Version: {self.version}")
        print("="*60 + "\n")
        
        if not self.check_dependencies():
            return False
        
        print()
        self.clean_build()
        print()
        
        if not self.build_msi():
            return False
        
        print()
        self.show_results()
        return True

if __name__ == '__main__':
    builder = MSIBuilder()
    success = builder.run()
    sys.exit(0 if success else 1)
