#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - macOS CLI Entry Point
=====================================
Platform-optimized command-line interface for macOS

Author: Loony2392  
Email: info@loony-tech.de
Version: 2025.11.9
"""

import sys
import os
from pathlib import Path

def setup_mac_environment():
    """Setup macOS-specific environment."""
    
    # Get the execution context
    if getattr(sys, 'frozen', False):
        # Running in py2app bundle
        bundle_dir = Path(sys.executable).parent
        resources_dir = bundle_dir / 'Resources'
        
        # Add Python paths
        site_packages = bundle_dir / 'lib' / 'python3.11' / 'site-packages'
        if site_packages.exists():
            sys.path.insert(0, str(site_packages))
        
        if resources_dir.exists():
            sys.path.insert(0, str(resources_dir))
            
        # Set locale environment
        locales_dir = resources_dir / 'locales'
        if locales_dir.exists():
            os.environ['MASTER_SEARCH_LOCALES'] = str(locales_dir)
    else:
        # Development mode
        project_root = Path(__file__).parent.parent
        src_dir = project_root / 'src'
        config_dir = project_root / 'config'
        
        sys.path.insert(0, str(src_dir))
        sys.path.insert(0, str(config_dir))
        sys.path.insert(0, str(project_root))
        
        # Set locale environment
        locales_dir = project_root / 'locales'
        if locales_dir.exists():
            os.environ['MASTER_SEARCH_LOCALES'] = str(locales_dir)


def main():
    """Main CLI entry point for macOS."""
    try:
        # Setup macOS environment
        setup_mac_environment()
        
        # Import and run CLI
        import cli_main
        
        # Run the CLI with original arguments
        sys.exit(cli_main.main())
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please check your installation and dependencies.")
        sys.exit(1)
        
    except Exception as e:
        print(f"❌ Error starting Master Search CLI: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()