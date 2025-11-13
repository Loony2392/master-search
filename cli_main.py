#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - CLI Entry Point
================================
Main entry point for the Master Search command-line interface.

Developer: Loony2392
Company: LOONY-TECH
Email: info@loony-tech.de
"""

import sys
import os
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    """Launch the Master Search CLI."""
    try:
        logging.info('Starting Master Search CLI...')
        
        # Setup paths for imports
        app_dir = os.path.dirname(os.path.abspath(__file__))
        sys.path.insert(0, app_dir)
        
        # Set language from config
        from config.language_config import get_active_language
        from src.i18n import set_locale
        set_locale(get_active_language())
        
        # Import and run CLI
        from src.file_search_tool import FileSearchTool
        
        tool = FileSearchTool()
        tool.run()
        
    except KeyboardInterrupt:
        print("\n[*] Interrupted by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        logging.error(f'Failed to start Master Search CLI: {e}', exc_info=True)
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
