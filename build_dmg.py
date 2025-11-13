#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - DMG Build Script
=================================
Automated DMG Creation for Master Search on macOS

Author: Loony2392
Company: LOONY-TECH
Email: info@loony-tech.de
Version: 2025.11.9
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path
import time
import json
import plistlib

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.stderr.reconfigure(encoding='utf-8', errors='replace')

class DMGBuilder:
    """DMG Builder for macOS App Bundle creation and distribution."""
    
    def __init__(self):
        # project_root should be the repository root (where `src/` and `config/` live)
        # build_dmg.py sits in the repo root, so use parent (no extra ..)
        self.project_root = Path(__file__).parent
        self.scripts_dir = Path(__file__).parent
        # Output to releases/macos/ instead of dist/
        self.dist_folder = self.project_root / 'releases' / 'macos'
        self.build_folder = self.project_root / 'build'
        self.app_name = "Master Search"
        self.bundle_identifier = "tech.loony.mastersearch"
        
        # Import version info
        try:
            sys.path.insert(0, str(self.project_root))
            from version import VERSION, AUTHOR, EMAIL, COMPANY
            self.version = VERSION
            self.author = AUTHOR
            self.email = EMAIL
            self.company = COMPANY
        except ImportError:
            self.version = "2025.11.9"
            self.author = "Loony2392"
            self.email = "info@loony-tech.de"
            self.company = "LOONY-TECH"
        
        # Check platform
        if sys.platform != 'darwin':
            raise RuntimeError("❌ DMG building is only supported on macOS!")
        
        # Detect macOS architecture
        self.arch = self._detect_architecture()
        
        print(f"🚀 Master Search DMG Builder v{self.version}")
        print(f"📦 Architecture: {self.arch}")
        print("=" * 60)
    
    def _detect_architecture(self):
        """Detect the current macOS architecture."""
        try:
            result = subprocess.run(['uname', '-m'], capture_output=True, text=True, check=True)
            arch = result.stdout.strip()
            
            if arch == 'arm64':
                return "Apple Silicon (ARM64/M1/M2/M3+)"
            elif arch == 'x86_64':
                return "Intel (x86_64)"
            else:
                return f"Unknown ({arch})"
        except:
            return "Unknown"
    
    def check_dependencies(self):
        """Check if required tools are available."""
        print("🔍 Checking dependencies...")
        
        required_tools = {
            'python3': 'Python 3 interpreter',
            'py2app': 'py2app for App Bundle creation',
            'hdiutil': 'macOS Disk Utility for DMG creation',
            'codesign': 'Code signing tool (optional)',
        }
        
        missing = []
        
        # Check Python
        if shutil.which('python3') is None:
            missing.append('python3')
        
        # Check py2app
        try:
            import py2app
            print("✅ py2app found")
        except ImportError:
            missing.append('py2app')
            print("❌ py2app not installed")
        
        # Check hdiutil
        if shutil.which('hdiutil') is None:
            missing.append('hdiutil')
        else:
            print("✅ hdiutil found")
        
        # Check codesign (optional)
        if shutil.which('codesign') is None:
            print("⚠️  codesign not found (optional for signing)")
        else:
            print("✅ codesign found")
        
        if missing:
            print("\n❌ Missing dependencies:")
            for tool in missing:
                description = required_tools.get(tool, tool)
                print(f"   - {tool}: {description}")
                
                if tool == 'py2app':
                    print("     Install with: pip install py2app")
            
            return False
        
        print("✅ All dependencies satisfied")
        return True
    
    def clean_previous_builds(self):
        """Clean previous build artifacts."""
        print("\n🧹 Cleaning previous builds...")
        
        # Remove dist and build folders
        for folder in [self.dist_folder, self.build_folder]:
            if folder.exists():
                print(f"   Removing {folder}")
                shutil.rmtree(folder)
        
        # Create fresh directories
        self.dist_folder.mkdir(parents=True, exist_ok=True)
        self.build_folder.mkdir(parents=True, exist_ok=True)
        
        print("✅ Build directories cleaned")
    
    def create_setup_py(self):
        """Create setup.py for py2app."""
        print("\n📝 Creating setup.py for py2app...")
        
        setup_content = f'''#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - py2app Setup Script
Automated setup for macOS App Bundle creation
"""

from setuptools import setup
import py2app
import sys
import os
from pathlib import Path

# Add source directories to path
sys.path.insert(0, 'src')
sys.path.insert(0, 'config')

# App configuration
APP = ['gui_main.py']
DATA_FILES = [
    ('locales', ['locales/de.json', 'locales/en.json', 'locales/fr.json']),
    ('', ['README.md']),
]

OPTIONS = {{
    # Avoid argv_emulation to prevent py2app from loading legacy Carbon APIs
    # (which can fail on modern macOS/Cryptex setups). Use False so the
    # bundled app doesn't attempt to load Carbon.framework at runtime.
    'argv_emulation': False,
    'packages': ['tkinter', 'pathlib', 'json', 'datetime', 'threading', 
                'concurrent', 'queue', 'multiprocessing'],
    'includes': ['gui_search_tool', 'platform_utils', 'file_search_tool', 'report_generator',
                'settings_manager', 'update_notifier', 'i18n', 'version',
                'language_config', 'performance_config', 'loading_animations'],
    # Exclude heavy or build-time-only packages to avoid duplicate metadata files
    'excludes': ['PyQt4', 'PyQt5', 'matplotlib', 'numpy', 'scipy', 'wheel', 'setuptools', 'pkg_resources'],
    'resources': ['locales/', 'media/'],
    'plist': {{
        'CFBundleName': '{self.app_name}',
        'CFBundleDisplayName': '{self.app_name}',
        'CFBundleIdentifier': '{self.bundle_identifier}',
        'CFBundleShortVersionString': '{self.version}',
        'CFBundleVersion': '{self.version}',
        'CFBundleInfoDictionaryVersion': '6.0',
        'NSHumanReadableCopyright': '© 2025 {self.company}. All rights reserved.',
        'NSHighResolutionCapable': True,
        'LSMinimumSystemVersion': '10.12.0',
        'NSPrincipalClass': 'NSApplication',
        'NSMainNibFile': 'MainMenu',
        'NSRequiresAquaSystemAppearance': False,
        'LSApplicationCategoryType': 'public.app-category.utilities',
        'CFBundleDocumentTypes': [
            {{
                'CFBundleTypeExtensions': ['txt', 'log', 'md', 'py', 'json', 'xml', 'html'],
                'CFBundleTypeRole': 'Viewer',
                'LSHandlerRank': 'Alternate',
                'LSTypeIsPackage': False,
            }}
        ],
    }},
    'iconfile': None,  # Add icon file if available
}}

# Copy source files to build directory
import shutil
if os.path.exists('build/src'):
    shutil.rmtree('build/src')
shutil.copytree('src', 'build/src')

if os.path.exists('build/config'):
    shutil.rmtree('build/config')
shutil.copytree('config', 'build/config')

setup(
    name='{self.app_name}',
    version='{self.version}',
    author='{self.author}',
    author_email='{self.email}',
    description='Professional File Search Tool',
    app=APP,
    data_files=DATA_FILES,
    options={{'py2app': OPTIONS}},
    setup_requires=['py2app'],
)
'''
        
        setup_file = self.project_root / 'setup_dmg.py'
        setup_file.write_text(setup_content, encoding='utf-8')
        
        print(f"✅ Created {setup_file}")
        return setup_file
    
    def build_app_bundle(self):
        """Build the macOS App Bundle."""
        print("\n🏗️  Building macOS App Bundle...")
        
        try:
            # Run py2app from project root with cwd parameter
            cmd = [sys.executable, str(self.project_root / 'setup_dmg.py'), 'py2app']
            
            print(f"Running: {' '.join(cmd)}")
            print(f"Working directory: {self.project_root}")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=False,
                cwd=str(self.project_root)
            )
            
            if result.returncode != 0:
                print(f"❌ py2app failed with exit code {result.returncode}")
                print("STDOUT:", result.stdout)
                print("STDERR:", result.stderr)
                return False
            
            print("✅ App Bundle created successfully")
            
            # py2app always builds to dist/, so we need to move it to releases/macos/
            default_dist = self.project_root / 'dist'
            app_path_source = default_dist / f"{self.app_name}.app"
            app_path_target = self.dist_folder / f"{self.app_name}.app"
            
            if app_path_source.exists():
                # Ensure target directory exists
                self.dist_folder.mkdir(parents=True, exist_ok=True)
                
                # Remove target if it exists
                if app_path_target.exists():
                    shutil.rmtree(app_path_target)
                
                # Move app to releases/macos/
                shutil.move(str(app_path_source), str(app_path_target))
                print(f"✅ Moved App Bundle to: {app_path_target}")
                
                # Fix: Manually copy _tkinter module that py2app sometimes misses
                self._fix_tkinter_in_app(app_path_target)
                
                return app_path_target
            else:
                print(f"❌ App Bundle not found at expected location: {app_path_source}")
                return False
            
        except Exception as e:
            print(f"❌ Error building app bundle: {e}")
            return False
    
    def _fix_tkinter_in_app(self, app_path):
        """Fix missing _tkinter module by copying from system Python."""
        print("\n🔧 Checking and fixing tkinter module...")
        
        try:
            import tkinter
            import sysconfig
            
            # Find system tkinter library directory
            tkinter_path = Path(tkinter.__file__).parent
            
            # Destination in app bundle
            resources_lib = app_path / 'Contents' / 'Resources' / 'lib' / f'python{sys.version_info.major}.{sys.version_info.minor}'
            resources_lib.mkdir(parents=True, exist_ok=True)
            
            # Copy entire tkinter package
            dest_tkinter = resources_lib / 'tkinter'
            if dest_tkinter.exists():
                print(f"   ✅ tkinter already in app bundle")
            else:
                print(f"   📦 Copying tkinter package from {tkinter_path}...")
                shutil.copytree(tkinter_path, dest_tkinter, dirs_exist_ok=True)
                print(f"   ✅ tkinter package copied")
            
            # Also try to find and copy _tkinter.so directly
            for search_dir in [Path(sys.executable).parent.parent / 'lib', Path(sysconfig.get_config_var('LIBDIR'))]:
                if search_dir and search_dir.exists():
                    for tkinter_so in search_dir.glob('**/[_]tkinter*.so'):
                        dest = resources_lib / tkinter_so.name
                        if not dest.exists():
                            print(f"   📦 Copying {tkinter_so.name}...")
                            shutil.copy2(tkinter_so, dest)
                        break
            
            print(f"   ✅ tkinter fix completed")
            
        except Exception as e:
            print(f"   ⚠️  Warning: Could not fully fix tkinter: {e}")
            print(f"   (App may still work, but GUI features may be limited)")
    
    def create_dmg_structure(self, app_path):
        """Create DMG directory structure."""
        print("\n📁 Creating DMG structure...")
        
        dmg_temp = self.build_folder / 'dmg_temp'
        if dmg_temp.exists():
            shutil.rmtree(dmg_temp)
        
        dmg_temp.mkdir(parents=True)
        
        # Copy App Bundle to DMG temp directory
        app_in_dmg = dmg_temp / f"{self.app_name}.app"
        print(f"   Copying {app_path} to {app_in_dmg}")
        shutil.copytree(app_path, app_in_dmg)
        
        # Create Applications symlink
        applications_link = dmg_temp / "Applications"
        try:
            applications_link.symlink_to("/Applications")
            print("   Created Applications symlink")
        except OSError:
            print("   ⚠️  Could not create Applications symlink")
        
        # Copy background image (icon.svg or PNG version)
        self.copy_dmg_background(dmg_temp)
        
        # Add README or other files
        readme_content = f"""# {self.app_name} v{self.version}

Thank you for downloading {self.app_name}!

## Installation
1. Drag "{self.app_name}.app" to the "Applications" folder
2. Launch from Applications or Spotlight search

## About
{self.app_name} is a professional file search tool for macOS.

Author: {self.author}
Email: {self.email}
Company: {self.company}
Version: {self.version}

© 2025 {self.company}. All rights reserved.
"""
        
        readme_file = dmg_temp / "README.txt"
        readme_file.write_text(readme_content, encoding='utf-8')
        print("   Created README.txt")
        
        return dmg_temp
    
    def copy_dmg_background(self, dmg_temp):
        """Copy background image to DMG. Try to use PNG version of icon."""
        # Create hidden folder for background image (macOS convention)
        bg_folder = dmg_temp / '.background'
        bg_folder.mkdir(exist_ok=True)
        
        # Try to use the largest icon PNG as background
        icon_256_path = self.project_root / 'media' / 'master_search_icon_256x256.png'
        bg_image_path = bg_folder / 'background.png'
        
        if icon_256_path.exists():
            try:
                shutil.copy2(icon_256_path, bg_image_path)
                print("   ✅ Copied background image (256x256 PNG)")
            except Exception as e:
                print(f"   ⚠️  Could not copy background image: {e}")
        else:
            print(f"   ℹ️  Background image not found at {icon_256_path}")

    
    def create_dmg(self, dmg_temp):
        """Create the final DMG file."""
        print("\n💿 Creating DMG file...")
        
        dmg_name = f"{self.app_name.replace(' ', '_')}_v{self.version}.dmg"
        dmg_path = self.dist_folder / dmg_name
        
        # Remove existing DMG
        if dmg_path.exists():
            dmg_path.unlink()
        
        # Create temporary DMG
        temp_dmg = self.build_folder / 'temp.dmg'
        if temp_dmg.exists():
            temp_dmg.unlink()
        
        # Calculate size needed
        size_cmd = ['du', '-sh', str(dmg_temp)]
        size_result = subprocess.run(size_cmd, capture_output=True, text=True)
        print(f"   DMG content size: {size_result.stdout.split()[0] if size_result.returncode == 0 else 'unknown'}")
        
        # Create DMG with hdiutil
        create_cmd = [
            'hdiutil', 'create',
            '-srcfolder', str(dmg_temp),
            '-volname', self.app_name,
            '-fs', 'HFS+',
            '-fsargs', '-c c=64,a=16,e=16',
            '-format', 'UDRW',
            str(temp_dmg)
        ]
        
        print(f"Running: {' '.join(create_cmd)}")
        result = subprocess.run(create_cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ DMG creation failed: {result.stderr}")
            return False
        
        # Mount DMG for customization
        print("   Mounting DMG for customization...")
        mount_cmd = ['hdiutil', 'attach', str(temp_dmg), '-readwrite', '-noverify', '-plist']
        mount_result = subprocess.run(mount_cmd, capture_output=True, text=True)
        
        if mount_result.returncode != 0:
            print(f"❌ Could not mount DMG: {mount_result.stderr}")
            return False
        
        # Extract mount point from plist output
        import plistlib
        mount_point = None
        try:
            plist_data = plistlib.loads(mount_result.stdout.encode())
            for item in plist_data.get('system-entities', []):
                if 'mount-point' in item:
                    mount_point = item['mount-point']
                    break
        except Exception as e:
            print(f"   ⚠️  Could not parse plist: {e}")
            # Fallback: try to find mount point manually
            for line in mount_result.stdout.splitlines():
                if '/Volumes/' in line:
                    mount_point = line.strip()
                    break
        
        if mount_point:
            print(f"   DMG mounted at: {mount_point}")
            
            # Customize DMG appearance (optional)
            try:
                self.customize_dmg_appearance(mount_point)
            except Exception as e:
                print(f"   ⚠️  DMG customization failed: {e}")
            
            # Unmount
            print("   Unmounting DMG...")
            detach_result = subprocess.run(['hdiutil', 'detach', mount_point], capture_output=True, text=True)
            if detach_result.returncode != 0:
                print(f"   ⚠️  Detach issue: {detach_result.stderr.strip()}")
                # Try force detach
                subprocess.run(['hdiutil', 'detach', mount_point, '-force'], capture_output=True)
            time.sleep(1)  # Give system time to fully detach
        
        # Convert to compressed DMG
        print("   Converting to compressed DMG...")
        convert_cmd = [
            'hdiutil', 'convert', str(temp_dmg),
            '-format', 'UDZO',
            '-imagekey', 'zlib-level=9',
            '-o', str(dmg_path)
        ]
        
        # Try conversion with a small retry loop to handle transient resource errors
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            convert_result = subprocess.run(convert_cmd, capture_output=True, text=True)
            if convert_result.returncode == 0:
                break
            print(f"   ⚠️  DMG conversion attempt {attempt} failed: {convert_result.stderr.strip()}")
            if attempt < max_attempts:
                print("   Retrying in 2s...")
                time.sleep(2)
        else:
            print(f"❌ DMG compression failed after {max_attempts} attempts: {convert_result.stderr}")
            return False
        
        # Clean up temporary DMG
        if temp_dmg.exists():
            temp_dmg.unlink()
        
        print(f"✅ DMG created: {dmg_path}")
        return dmg_path
    
    def customize_dmg_appearance(self, mount_point):
        """Customize DMG appearance with AppleScript."""
        print("   Customizing DMG appearance...")
        
        # AppleScript for DMG customization with background image
        applescript = f'''
        tell application "Finder"
            tell disk "{self.app_name}"
                open
                set current view of container window to icon view
                set toolbar visible of container window to false
                set statusbar visible of container window to false
                set the bounds of container window to {{100, 100, 700, 500}}
                set viewOptions to the icon view options of container window
                set arrangement of viewOptions to not arranged
                set icon size of viewOptions to 128
                
                -- Set background image if it exists
                try
                    set background picture of viewOptions to file ".background:background.png"
                end try
                
                delay 1
                set position of item "{self.app_name}.app" of container window to {{150, 300}}
                set position of item "Applications" of container window to {{450, 300}}
                close
            end tell
        end tell
        '''
        
        # Execute AppleScript
        try:
            subprocess.run(['osascript', '-e', applescript], check=True, capture_output=True)
            print("   ✅ DMG appearance customized with background")
        except subprocess.CalledProcessError as e:
            print(f"   ⚠️  AppleScript failed: {e}")
    
    def show_results(self, dmg_path):
        """Display build results."""
        print("\n" + "=" * 60)
        print("🎉 DMG BUILD COMPLETED SUCCESSFULLY!")
        print("=" * 60)
        
        if dmg_path and dmg_path.exists():
            file_size = dmg_path.stat().st_size / (1024 * 1024)  # MB
            
            print("📦 DMG FILE DETAILS:")
            print(f"   File: {dmg_path.name}")
            print(f"   Path: {dmg_path.absolute()}")
            print(f"   Size: {file_size:.1f} MB")
            
            print("\n📋 NEXT STEPS:")
            print("1. Test the DMG by mounting it:")
            print(f"   open {dmg_path}")
            print("\n2. Install the app:")
            print("   - Mount the DMG")
            print(f"   - Drag '{self.app_name}.app' to Applications")
            print("\n3. Optional: Code sign for distribution:")
            print("   codesign -s 'Developer ID' --deep --force \\")
            print(f"     '{self.dist_folder}/{self.app_name}.app'")
            print("\n4. Optional: Notarize for macOS Gatekeeper:")
            print("   xcrun altool --notarize-app ...")
            
        else:
            print("❌ DMG file was not created successfully")
    
    def build(self):
        """Main build process."""
        try:
            start_time = time.time()
            
            # Check dependencies
            if not self.check_dependencies():
                return False
            
            # Clean previous builds
            self.clean_previous_builds()
            
            # Create setup.py
            setup_file = self.create_setup_py()
            
            # Build App Bundle
            app_path = self.build_app_bundle()
            if not app_path:
                return False
            
            # Create DMG structure
            dmg_temp = self.create_dmg_structure(app_path)
            
            # Create DMG
            dmg_path = self.create_dmg(dmg_temp)
            
            # Show results
            elapsed = time.time() - start_time
            print(f"\n⏱️  Build completed in {elapsed:.1f} seconds")
            
            self.show_results(dmg_path)
            
            # Clean up
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
    print("🍎 Master Search DMG Builder for macOS")
    
    if sys.platform != 'darwin':
        print("❌ This script only works on macOS!")
        print("   For Windows: Use scripts/build_msi.py")
        print("   For Linux: Use scripts/build_deb.py (coming soon)")
        sys.exit(1)
    
    try:
        builder = DMGBuilder()
        success = builder.build()
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()