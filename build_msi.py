#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - MSI Installer Builder
======================================
Creates native Windows MSI installers using cx_Freeze

Author: Loony2392
Company: LOONY-TECH
Email: info@loony-tech.de
Version: 2025.11.13
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path
import time

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

class MSIBuilder:
    """MSI Builder for Windows installer creation."""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.scripts_dir = self.project_root / 'scripts'
        # Output to releases/windows/ instead of dist/
        self.dist_folder = self.project_root / 'releases' / 'windows'
        self.build_folder = self.project_root / 'build'
        self.app_name = "Master Search"
        
        # Import version info
        try:
            sys.path.insert(0, str(self.project_root))
            from version import VERSION, AUTHOR, EMAIL, COMPANY
            self.version = VERSION
            self.author = AUTHOR
            self.email = EMAIL
            self.company = COMPANY
        except ImportError:
            self.version = "2025.11.13"
            self.author = "Loony2392"
            self.email = "info@loony-tech.de"
            self.company = "LOONY-TECH"
        
        # Fixed upgrade code for consistent updates
        self.upgrade_code = "{3F692526-948B-4B39-BF5F-1C3FD99FC7F4}"
        
        # MSI filename
        self.msi_filename = f"Master_Search-{self.version}-win64.msi"
        
        print(f"🚀 Master Search MSI Builder v{self.version}")
        print("=" * 60)
    
    def check_dependencies(self):
        """Check if required tools are available."""
        print("🔍 Checking dependencies...")
        
        try:
            import PyInstaller
            print("✅ PyInstaller found")
        except ImportError:
            print("❌ PyInstaller not installed")
            print("   Installing PyInstaller...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'PyInstaller>=6.0'], check=True)
        
        try:
            import cx_Freeze
            print(f"✅ cx_Freeze {cx_Freeze.__version__} found")
        except ImportError:
            print("❌ cx_Freeze not installed")
            print("   Installing cx_Freeze...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', 'cx_Freeze>=7.0'], check=True)
        
        print("✅ All dependencies satisfied")
        return True
    
    def clean_previous_builds(self):
        """Clean previous build artifacts."""
        print("\n🧹 Cleaning previous builds...")
        
        for folder in [self.dist_folder, self.build_folder]:
            if folder.exists():
                print(f"   Removing {folder.name}")
                shutil.rmtree(folder, ignore_errors=True)
        
        self.dist_folder.mkdir(parents=True, exist_ok=True)
        
        print("✅ Build directories cleaned")
    
    def build_executables(self):
        """Build GUI and CLI executables using PyInstaller."""
        print("\n🏗️  Building executables with PyInstaller...")
        
        try:
            # Build GUI
            print("   Building GUI executable...")
            result = subprocess.run(
                [sys.executable, '-m', 'PyInstaller', str(self.scripts_dir / 'gui.spec')],
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                print(f"❌ GUI build failed: {result.stderr}")
                return False
            
            print("   ✅ GUI executable created")
            
            # Build CLI
            print("   Building CLI executable...")
            result = subprocess.run(
                [sys.executable, '-m', 'PyInstaller', str(self.scripts_dir / 'cli.spec')],
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                print(f"❌ CLI build failed: {result.stderr}")
                return False
            
            print("   ✅ CLI executable created")
            return True
            
        except Exception as e:
            print(f"❌ Error building executables: {e}")
            return False
    
    def create_msi_setup(self):
        """Create cx_Freeze setup.py for MSI."""
        print("\n📝 Creating cx_Freeze setup for MSI...")
        
        setup_content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - cx_Freeze MSI Setup
Automated setup for Windows MSI installer creation
"""

from cx_Freeze import setup, Executable
from pathlib import Path

# Paths
project_root = Path(__file__).parent

# App executables
executables = [
    Executable(
        "gui_main.py",
        target_name="Master_Search.exe",
        icon=str(project_root / "media" / "icon.ico") if (project_root / "media" / "icon.ico").exists() else None
    ),
    Executable(
        "cli_main.py",
        target_name="MasterSearch_CLI.exe"
    )
]

# Build options
options = {{
    "bdist_msi": {{
        "add_to_path": True,
        "upgrade_code": "{self.upgrade_code}",
        "initial_target_dir": r"[ProgramFilesFolder]\\Master Search",
    }}
}}

# Setup configuration
setup(
    name="{self.app_name}",
    version="{self.version}",
    author="{self.author}",
    author_email="{self.email}",
    description="Professional file search tool with German localization",
    long_description="Master Search - Advanced full-text file system search with HTML reports",
    url="https://github.com/Loony2392/master-search",
    executables=executables,
    options=options
)
'''
        
        setup_file = self.scripts_dir / 'setup_msi.py'
        setup_file.write_text(setup_content, encoding='utf-8')
        
        print(f"✅ Created {setup_file.name}")
        return setup_file
    
    def build_msi(self, setup_file):
        """Build MSI installer using cx_Freeze."""
        print("\n🔨 Building MSI installer with cx_Freeze...")
        
        try:
            cmd = [sys.executable, str(setup_file), 'bdist_msi']
            
            print(f"   Running: {' '.join(cmd)}")
            print(f"   Working directory: {self.project_root}")
            
            result = subprocess.run(
                cmd,
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode != 0:
                print(f"❌ MSI build failed with exit code {result.returncode}")
                print("STDERR:", result.stderr[-500:] if len(result.stderr) > 500 else result.stderr)
                return False
            
            print("✅ MSI builder completed")
            
            # Find and move the generated MSI
            return self.move_msi_to_dist()
            
        except Exception as e:
            print(f"❌ Error building MSI: {e}")
            return False
    
    def move_msi_to_dist(self):
        """Find generated MSI and move it to dist folder."""
        print("   Locating generated MSI file...")
        
        try:
            # Search for MSI in build folder
            msi_files = list(self.build_folder.glob('**/*.msi'))
            
            if msi_files:
                src = msi_files[0]
                dst = self.dist_folder / self.msi_filename
                shutil.move(str(src), str(dst))
                print(f"   ✅ MSI moved to {self.msi_filename}")
                return True
            
            # Check if already in dist with different name
            msi_files = list(self.dist_folder.glob('*.msi'))
            if msi_files:
                src = msi_files[0]
                dst = self.dist_folder / self.msi_filename
                if src != dst:
                    src.rename(dst)
                print(f"   ✅ MSI found and renamed to {self.msi_filename}")
                return True
            
            print("❌ No MSI file found in build or dist")
            return False
            
        except Exception as e:
            print(f"❌ Error moving MSI: {e}")
            return False
    
    def create_checksum(self):
        """Create SHA256 checksum for the MSI."""
        print("\n🔐 Creating SHA256 checksum...")
        
        try:
            import hashlib
            
            msi_path = self.dist_folder / self.msi_filename
            
            if not msi_path.exists():
                print(f"❌ MSI file not found: {msi_path}")
                return False
            
            # Calculate SHA256
            sha256_hash = hashlib.sha256()
            with open(msi_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            
            checksum = sha256_hash.hexdigest()
            
            # Save checksum to file
            checksum_file = self.dist_folder / f"{self.msi_filename}.sha256"
            checksum_file.write_text(f"{checksum}  {self.msi_filename}\n", encoding='utf-8')
            
            print(f"✅ Checksum: {checksum}")
            print(f"   Saved to: {checksum_file.name}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error creating checksum: {e}")
            return False
    
    def show_results(self):
        """Display build results."""
        print("\n" + "=" * 60)
        print("🎉 MSI BUILD COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
        msi_path = self.dist_folder / self.msi_filename
        
        if msi_path.exists():
            file_size = msi_path.stat().st_size / (1024 * 1024)  # MB
            
            print("\n📦 MSI FILE DETAILS:")
            print(f"   File: {self.msi_filename}")
            print(f"   Path: {msi_path.absolute()}")
            print(f"   Size: {file_size:.1f} MB")
            print(f"   Version: {self.version}")
            print(f"   Upgrade Code: {self.upgrade_code}")
            
            print("\n📋 NEXT STEPS:")
            print("1. Test the MSI installation:")
            print(f"   msiexec /i \"{self.msi_filename}\"")
            print("\n2. Test silent installation:")
            print(f"   msiexec /i \"{self.msi_filename}\" /quiet")
            print("\n3. Test uninstallation:")
            print("   Add/Remove Programs → Master Search → Uninstall")
            print("\n4. Optional: Code sign for trusted distribution:")
            print("   signtool sign /f certificate.pfx /p password \\")
            print(f"     \"{self.msi_filename}\"")
            
        else:
            print("❌ MSI file was not created successfully")
    
    def build(self):
        """Main build process."""
        try:
            start_time = time.time()
            
            # Check dependencies
            if not self.check_dependencies():
                return False
            
            # Clean previous builds
            self.clean_previous_builds()
            
            # Build executables
            if not self.build_executables():
                return False
            
            # Create MSI setup script
            setup_file = self.create_msi_setup()
            
            # Build MSI
            if not self.build_msi(setup_file):
                return False
            
            # Create checksum
            self.create_checksum()
            
            # Show results
            elapsed = time.time() - start_time
            print(f"\n⏱️  Build completed in {elapsed:.1f} seconds")
            
            self.show_results()
            
            # Clean up setup script
            if setup_file.exists():
                setup_file.unlink()
            
            return True
            
        except KeyboardInterrupt:
            print("\n❌ Build interrupted by user")
            return False
        except Exception as e:
            print(f"\n❌ Build failed: {e}")
            import traceback
            traceback.print_exc()
            return False


def main():
    """Main entry point."""
    print("🪟 Master Search MSI Builder for Windows")
    
    if sys.platform != 'win32':
        print("❌ This script only works on Windows!")
        print("   For macOS: Use scripts/build_dmg.py")
        print("   For Linux: Use scripts/build_deb.py (coming soon)")
        sys.exit(1)
    
    try:
        builder = MSIBuilder()
        success = builder.build()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
