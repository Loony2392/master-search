#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - PyInstaller Build Script
==========================================
Automated executable creation using PyInstaller

Author: Loony2392
Company: LOONY-TECH
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path

class PyInstallerBuilder:
    def __init__(self):
        self.project_root = Path(__file__).parent.parent  # Parent of scripts folder
        self.scripts_dir = self.project_root / 'scripts'
        self.dist_folder = self.project_root / 'dist'
        self.build_folder = self.project_root / 'build'
        
    def print_status(self, message, prefix='[*]'):
        """Print status message."""
        print(f"{prefix} {message}")
    
    def clean_build(self):
        """Clean previous builds."""
        self.print_status("Cleaning previous builds...", "[*]")
        for folder in [self.build_folder, self.dist_folder, self.project_root / '__pycache__']:
            if folder.exists():
                shutil.rmtree(folder, ignore_errors=True)
                self.print_status(f"Removed {folder.name}", "[OK]")
    
    def build_gui(self):
        """Build GUI executable."""
        self.print_status("Building GUI executable...", "[*]")
        try:
            result = subprocess.run(
                [
                    sys.executable, '-m', 'PyInstaller',
                    '--onefile',
                    str(self.scripts_dir / 'gui.spec'),
                ],
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
            self.print_status(f"Error building GUI: {e}", "[ERROR]")
            return False
    
    def build_cli(self):
        """Build CLI executable."""
        self.print_status("Building CLI executable...", "[*]")
        try:
            result = subprocess.run(
                [
                    sys.executable, '-m', 'PyInstaller',
                    '--onefile',
                    str(self.scripts_dir / 'cli.spec'),
                ],
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
            self.print_status(f"Error building CLI: {e}", "[ERROR]")
            return False
    
    def show_results(self):
        """Display build results."""
        print("\n" + "="*60)
        self.print_status("BUILD COMPLETED SUCCESSFULLY", "[SUCCESS]")
        print("="*60 + "\n")
        
        exe_files = list(self.dist_folder.glob('*.exe'))
        if exe_files:
            self.print_status("Generated Executables:", "[*]")
            for exe in exe_files:
                size_mb = exe.stat().st_size / (1024 * 1024)
                self.print_status(f"  {exe.name} ({size_mb:.1f} MB)", "[*]")
        
        self.print_status(f"Location: {self.dist_folder}", "[*]")
        self.print_status("Ready to distribute or install!", "[OK]")
    
    def run(self):
        """Run the complete build process."""
        print("\n" + "="*60)
        self.print_status("MASTER SEARCH - PyInstaller BUILD", "[BUILD]")
        print("="*60 + "\n")
        
        self.clean_build()
        print()
        
        if not self.build_gui():
            return False
        print()
        
        if not self.build_cli():
            return False
        print()
        
        self.show_results()
        return True

if __name__ == '__main__':
    builder = PyInstallerBuilder()
    success = builder.run()
    sys.exit(0 if success else 1)
