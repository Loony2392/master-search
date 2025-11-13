#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Cross-Platform Utilities
=========================================
Platform-specific functionality for Windows, macOS and Linux compatibility

Author: Loony2392
Email: info@loony-tech.de
Version: 2025.11.9
"""

import sys
import os
import subprocess
import tempfile
from pathlib import Path
import webbrowser


class PlatformUtils:
    """Cross-platform utility functions for file operations and system interaction."""
    
    @staticmethod
    def get_platform():
        """Get the current platform name."""
        if sys.platform == 'win32':
            return 'windows'
        elif sys.platform == 'darwin':
            return 'macos'
        else:
            return 'linux'
    
    @staticmethod
    def get_temp_dir():
        """Get platform-appropriate temporary directory."""
        platform = PlatformUtils.get_platform()
        
        if platform == 'windows':
            # Prefer C:\TEMP for Windows, fallback to system temp
            temp_paths = [
                Path(r"C:\TEMP"),
                Path(tempfile.gettempdir())
            ]
            
            for temp_path in temp_paths:
                try:
                    temp_path.mkdir(parents=True, exist_ok=True)
                    return temp_path
                except (PermissionError, OSError):
                    continue
            return Path(tempfile.gettempdir())
            
        elif platform == 'macos':
            # macOS: Use ~/Downloads or system temp
            user_downloads = Path.home() / 'Downloads'
            if user_downloads.exists() and user_downloads.is_dir():
                return user_downloads / 'Master Search'
            return Path(tempfile.gettempdir()) / 'Master Search'
            
        else:  # Linux
            # Linux: Use ~/Documents or system temp
            user_docs = Path.home() / 'Documents'
            if user_docs.exists() and user_docs.is_dir():
                return user_docs / 'Master Search'
            return Path(tempfile.gettempdir()) / 'Master Search'
    
    @staticmethod
    def open_file(file_path):
        """Open file or folder in system's default application."""
        platform = PlatformUtils.get_platform()
        file_path = str(Path(file_path).absolute())
        
        try:
            if platform == 'windows':
                # Windows: Use os.startfile
                os.startfile(file_path)
                return True
                
            elif platform == 'macos':
                # macOS: Use 'open' command
                subprocess.run(['open', file_path], check=True)
                return True
                
            else:  # Linux
                # Linux: Use 'xdg-open' command
                subprocess.run(['xdg-open', file_path], check=True)
                return True
                
        except (OSError, subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"⚠️  Could not open file: {e}")
            return False
    
    @staticmethod
    def open_folder(folder_path):
        """Open folder in system's file manager."""
        platform = PlatformUtils.get_platform()
        folder_path = Path(folder_path).absolute()
        
        try:
            if platform == 'windows':
                # Windows: Open folder in Explorer
                os.startfile(str(folder_path))
                return True
                
            elif platform == 'macos':
                # macOS: Open folder in Finder
                subprocess.run(['open', str(folder_path)], check=True)
                return True
                
            else:  # Linux
                # Linux: Open folder in file manager
                subprocess.run(['xdg-open', str(folder_path)], check=True)
                return True
                
        except (OSError, subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"⚠️  Could not open folder: {e}")
            return False
    
    @staticmethod
    def reveal_in_folder(file_path):
        """Reveal/select file in system's file manager."""
        platform = PlatformUtils.get_platform()
        file_path = Path(file_path).absolute()
        
        try:
            if platform == 'windows':
                # Windows: Use Explorer /select to highlight file
                subprocess.run(['explorer.exe', '/select,', str(file_path)], check=True)
                return True
                
            elif platform == 'macos':
                # macOS: Use Finder to reveal file
                subprocess.run(['open', '-R', str(file_path)], check=True)
                return True
                
            else:  # Linux
                # Linux: Open parent folder (no direct reveal equivalent)
                parent_folder = file_path.parent
                subprocess.run(['xdg-open', str(parent_folder)], check=True)
                return True
                
        except (OSError, subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"⚠️  Could not reveal file: {e}")
            return False
    
    @staticmethod
    def open_url_in_browser(url):
        """Open URL in default web browser."""
        try:
            webbrowser.open(url)
            return True
        except Exception as e:
            print(f"⚠️  Could not open browser: {e}")
            return False
    
    @staticmethod
    def get_app_data_dir(app_name="Master Search"):
        """Get platform-appropriate application data directory."""
        platform = PlatformUtils.get_platform()
        
        if platform == 'windows':
            # Windows: %APPDATA%/Master Search
            appdata = os.environ.get('APPDATA', '')
            if appdata:
                return Path(appdata) / app_name
            return Path.home() / 'AppData' / 'Roaming' / app_name
            
        elif platform == 'macos':
            # macOS: ~/Library/Application Support/Master Search
            return Path.home() / 'Library' / 'Application Support' / app_name
            
        else:  # Linux
            # Linux: ~/.config/Master Search
            return Path.home() / '.config' / app_name
    
    @staticmethod
    def get_executable_name(base_name="master_search"):
        """Get platform-appropriate executable name."""
        platform = PlatformUtils.get_platform()
        
        if platform == 'windows':
            return f"{base_name}.exe"
        elif platform == 'macos':
            return f"{base_name}.app"
        else:  # Linux
            return base_name
    
    @staticmethod
    def get_installer_extension():
        """Get platform-appropriate installer file extension."""
        platform = PlatformUtils.get_platform()
        
        if platform == 'windows':
            return '.msi'
        elif platform == 'macos':
            return '.dmg'
        else:  # Linux
            return '.deb'  # or .rpm depending on distribution
    
    @staticmethod
    def is_gui_available():
        """Check if GUI functionality is available on current platform."""
        try:
            import tkinter
            # Try to create a root window (but don't show it)
            root = tkinter.Tk()
            root.withdraw()
            root.destroy()
            return True
        except (ImportError, tkinter.TclError):
            return False
    
    @staticmethod
    def get_platform_info():
        """Get detailed platform information for diagnostics."""
        platform = PlatformUtils.get_platform()
        
        info = {
            'platform': platform,
            'system': sys.platform,
            'python_version': sys.version,
            'temp_dir': str(PlatformUtils.get_temp_dir()),
            'app_data_dir': str(PlatformUtils.get_app_data_dir()),
            'gui_available': PlatformUtils.is_gui_available()
        }
        
        if platform == 'macos':
            try:
                import platform as platform_module
                info['macos_version'] = platform_module.mac_ver()[0]
            except:
                pass
                
        return info


# Create convenience instance
platform_utils = PlatformUtils()

# Export commonly used functions
get_platform = PlatformUtils.get_platform
get_temp_dir = PlatformUtils.get_temp_dir
open_file = PlatformUtils.open_file
open_folder = PlatformUtils.open_folder
reveal_in_folder = PlatformUtils.reveal_in_folder
get_platform_info = PlatformUtils.get_platform_info


if __name__ == "__main__":
    # Demo/Test functionality
    print("🔧 Master Search - Platform Utilities Test")
    print("=" * 50)
    
    info = get_platform_info()
    print(f"Platform: {info['platform']}")
    print(f"System: {info['system']}")
    print(f"Python: {info['python_version'][:20]}...")
    print(f"Temp Dir: {info['temp_dir']}")
    print(f"App Data: {info['app_data_dir']}")
    print(f"GUI Available: {info['gui_available']}")
    
    if info['platform'] == 'macos' and 'macos_version' in info:
        print(f"macOS Version: {info['macos_version']}")
    
    print("\n✅ Platform utilities loaded successfully!")