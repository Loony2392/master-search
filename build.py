#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Build Launcher
===============================
Central build script that coordinates all build tasks

Usage:
    python build.py gui          - Build GUI executable only
    python build.py cli          - Build CLI executable only
    python build.py all          - Build both GUI and CLI (default)
    python build.py clean        - Clean build artifacts

Author: Loony2392
Company: LOONY-TECH
"""

import sys
import subprocess
from pathlib import Path

class BuildLauncher:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.scripts_dir = self.project_root / 'scripts'
    
    def run_command(self, cmd, description):
        """Run a command and report status."""
        print(f"\n{'='*60}")
        print(f"[*] {description}")
        print(f"{'='*60}\n")
        
        result = subprocess.run(
            cmd,
            cwd=str(self.project_root)
        )
        return result.returncode == 0
    
    def build_gui(self):
        """Build GUI executable."""
        return self.run_command(
            [sys.executable, '-m', 'PyInstaller', str(self.scripts_dir / 'gui.spec')],
            "Building Master Search GUI with PyInstaller"
        )
    
    def build_cli(self):
        """Build CLI executable."""
        return self.run_command(
            [sys.executable, '-m', 'PyInstaller', str(self.scripts_dir / 'cli.spec')],
            "Building Master Search CLI with PyInstaller"
        )
    
    def clean(self):
        """Clean build artifacts."""
        import shutil
        print(f"\n{'='*60}")
        print("[*] Cleaning build artifacts")
        print(f"{'='*60}\n")
        
        for folder in ['build', 'dist', '__pycache__']:
            path = self.project_root / folder
            if path.exists():
                shutil.rmtree(path, ignore_errors=True)
                print(f"[OK] Removed {folder}/")
    
    def run(self, target='all'):
        """Run build process."""
        if target == 'clean':
            self.clean()
            return True
        
        success = True
        
        if target in ['all', 'gui']:
            if not self.build_gui():
                print("[ERROR] GUI build failed")
                success = False
        
        if target in ['all', 'cli']:
            if not self.build_cli():
                print("[ERROR] CLI build failed")
                success = False
        
        if success:
            print(f"\n{'='*60}")
            print("[SUCCESS] Build completed!")
            print(f"{'='*60}")
            print(f"\nExecutables ready in: {self.project_root / 'dist'}/")
        
        return success

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'all'
    
    if target not in ['gui', 'cli', 'all', 'clean']:
        print(f"Usage: python build.py [gui|cli|all|clean]")
        print(f"Got: {target}")
        sys.exit(1)
    
    launcher = BuildLauncher()
    success = launcher.run(target)
    sys.exit(0 if success else 1)
