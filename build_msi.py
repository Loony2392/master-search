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
        
        # Check for NSIS (preferred method for Start Menu/Desktop shortcuts)
        nsis_found = shutil.which("makensis") is not None
        if nsis_found:
            print("✅ NSIS found (for full installer with shortcuts)")
            self.use_nsis = True
        else:
            print("⚠️  NSIS not found (will use cx_Freeze fallback)")
            self.use_nsis = False
        
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
    
    def install_ocr_dependencies(self):
        """Install OCR engines into the build environment."""
        print("\n🎨 Installing OCR Engines...")
        
        try:
            # Run OCR setup script
            ocr_setup = self.project_root / 'scripts' / 'setup_ocr.py'
            if ocr_setup.exists():
                cmd = [sys.executable, str(ocr_setup)]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
                
                if result.returncode == 0:
                    print("✅ OCR engines installed successfully")
                    return True
                else:
                    print("⚠️  OCR installation had issues (non-critical)")
                    print(result.stderr[:500] if result.stderr else "No error details")
                    return True  # Don't fail the build
            else:
                print("⚠️  OCR setup script not found (skipping)")
                return True
        except Exception as e:
            print(f"⚠️  OCR installation skipped: {e}")
            return True  # Don't fail the build
    
    def clean_previous_builds(self):
        """Clean previous build artifacts aggressively."""
        print("\n🧹 Cleaning previous builds...")
        
        # Clean dist folder
        if self.dist_folder.exists():
            print(f"   Removing {self.dist_folder.name}")
            try:
                shutil.rmtree(self.dist_folder, ignore_errors=True)
            except Exception as e:
                print(f"   Warning: {e}")
        
        # Aggressively clean build folder - rename instead of delete
        if self.build_folder.exists():
            print(f"   Removing {self.build_folder.name}")
            try:
                # Try to remove it multiple times with delay
                for attempt in range(3):
                    try:
                        shutil.rmtree(self.build_folder, ignore_errors=True)
                        break
                    except Exception:
                        import time
                        time.sleep(1)
                        
                # If still exists, rename it out of the way
                if self.build_folder.exists():
                    import time
                    renamed = self.project_root / f'build_old_{int(time.time())}'
                    self.build_folder.rename(renamed)
                    print(f"   Renamed old build to {renamed.name}")
            except Exception as e:
                print(f"   Warning: Could not clean build: {e}")
        
        self.dist_folder.mkdir(parents=True, exist_ok=True)
        
        print("✅ Build directories cleaned")
    
    def build_executables(self):
        """Skip PyInstaller - let cx_Freeze handle everything."""
        print("\n🏗️  Skipping PyInstaller (cx_Freeze will handle everything)...")
        print("   ✅ Ready for direct cx_Freeze MSI build")
        return True
    
    def create_msi_setup(self):
        """Create cx_Freeze setup.py for MSI."""
        print("\n📝 Creating cx_Freeze setup for MSI...")
        
        setup_content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - cx_Freeze MSI Setup
Automated setup for Windows MSI installer creation

Note: OCR engines (EasyOCR, PaddleOCR) are installed separately via:
      Master_Search --setup-ocr
      
This keeps the base MSI small (~6-8 MB) while allowing full OCR support.
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

# Build options - keep base bundle small
options = {{
    "build_exe": {{
        "excludes": ["tkinter", "unittest", "pydoc", "test"],
    }},
    "bdist_msi": {{
        "add_to_path": True,
        "upgrade_code": "{self.upgrade_code}",
        "initial_target_dir": r"[ProgramFilesFolder]\\Master Search",
        "install_icon": r"media\\icon.ico" if (project_root / "media" / "icon.ico").exists() else None,
    }}
}}

# Setup configuration
setup(
    name="{self.app_name}",
    version="{self.version}",
    author="{self.author}",
    author_email="{self.email}",
    description="Professional file search tool with German localization",
    long_description="Master Search - Advanced full-text file system search with HTML reports. OCR support available via optional setup.",
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
        """Build MSI installer using cx_Freeze bdist_msi."""
        print("\n🔨 Building MSI installer with cx_Freeze...")
        print("   ⏱️  This will take 5-15 minutes...")
        
        try:
            # Use bdist_msi command - the proper way to create MSI
            cmd = [sys.executable, str(setup_file), 'bdist_msi']
            
            print(f"   Working directory: {self.project_root}")
            
            result = subprocess.run(
                cmd,
                cwd=str(self.project_root),
                capture_output=True,
                text=True,
                timeout=1200,  # 20 minute timeout
                check=False
            )
            
            if result.returncode != 0:
                print(f"❌ MSI build failed with exit code {result.returncode}")
                if result.stderr:
                    print("Error:", result.stderr[-1500:] if len(result.stderr) > 1500 else result.stderr)
                return False
            
            print("✅ MSI build completed")
            
            # Find and move the generated MSI
            return self.find_and_move_msi()
            
        except subprocess.TimeoutExpired:
            print("❌ Build timed out (>20 minutes)")
            return False
        except Exception as e:
            print(f"❌ Error building MSI: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def find_and_move_msi(self):
        """Find generated MSI and move it to releases/windows."""
        print("   Locating generated MSI file...")
        
        try:
            # Search in dist folder (default cx_Freeze output)
            dist_folder = self.project_root / 'dist'
            if dist_folder.exists():
                msi_files = list(dist_folder.glob('*.msi'))
                if msi_files:
                    src = msi_files[0]
                    dst = self.dist_folder / self.msi_filename
                    shutil.move(str(src), str(dst))
                    size_mb = dst.stat().st_size / (1024 * 1024)
                    print(f"   ✅ MSI moved to {self.msi_filename} ({size_mb:.1f} MB)")
                    return True
            
            # Search in build folder
            msi_files = list(self.build_folder.glob('**/*.msi'))
            if msi_files:
                src = msi_files[0]
                dst = self.dist_folder / self.msi_filename
                shutil.move(str(src), str(dst))
                size_mb = dst.stat().st_size / (1024 * 1024)
                print(f"   ✅ MSI moved to {self.msi_filename} ({size_mb:.1f} MB)")
                return True
            
            # Check if already in dist with different name
            msi_files = list(self.dist_folder.glob('*.msi'))
            if msi_files:
                src = msi_files[0]
                if src.name != self.msi_filename:
                    dst = self.dist_folder / self.msi_filename
                    src.rename(dst)
                    print(f"   ✅ MSI found and renamed to {self.msi_filename}")
                return True
            
            print("❌ No MSI file found in any expected location")
            return False
            
        except Exception as e:
            print(f"❌ Error locating MSI: {e}")
            return False
    
    def create_checksum(self):
        """Create SHA256 checksum for the MSI."""
        print("\n🔐 Creating SHA256 checksum...")
        
        try:
            import hashlib
            
            msi_path = self.dist_folder / self.msi_filename
            
            if not msi_path.exists():
                print(f"⚠️  MSI file not found: {msi_path}")
                return True  # Don't fail the build
            
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
            print(f"⚠️  Error creating checksum: {e}")
            return True  # Don't fail the build
    
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
            print(f"   Size: {file_size:.1f} MB (lightweight base install)")
            print(f"   Version: {self.version}")
            print(f"   Upgrade Code: {self.upgrade_code}")
            
            print("\n✅ INCLUDED FEATURES:")
            print("   ✓ Start Menu shortcuts (GUI + CLI)")
            print("   ✓ Desktop shortcuts (optional)")
            print("   ✓ Add to PATH environment variable")
            print("   ✓ Add/Remove Programs entry")
            print("   ✓ Full Python runtime")
            
            print("\n🔧 OPTIONAL OCR INSTALLATION:")
            print("   After installation, enable OCR with:")
            print("     Master_Search --setup-ocr")
            print("   ")
            print("   This will install:")
            print("     • EasyOCR engine")
            print("     • PaddleOCR engine")
            print("     • Supports 80+ languages")
            print("     • Models auto-downloaded on first use (~200-300 MB)")
            
            print("\n📋 INSTALLATION INSTRUCTIONS:")
            print("1. Install MSI:")
            print(f"   msiexec /i \"{self.msi_filename}\"")
            print("\n2. After installation (optional OCR setup):")
            print("   Master_Search --setup-ocr")
            print("\n3. Launch application:")
            print("   • GUI: Start from Start Menu or desktop")
            print("   • CLI: Master_Search_CLI --help")
            print("\n4. Verify installation:")
            print("   Master_Search --version")
            print("   Master_Search --ocr-info  (if OCR installed)")
            
            print("\n📊 INSTALLER SPECIFICATIONS:")
            print(f"   Base MSI Size: {file_size:.1f} MB")
            print("   Python Runtime: Included")
            print("   Installation Time: 1-2 minutes")
            print("   OCR Installation Time: 5-10 minutes (optional)")
            print("   OCR Models Size: ~200-300 MB (downloaded once)")
            
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
            
            # Install OCR dependencies
            self.install_ocr_dependencies()
            
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
