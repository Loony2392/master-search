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

def main():
    """Launch the Master Search CLI."""
    try:
        # Add current directory and src to path for imports
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))
        sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config'))
        
        # Set language from config
        from language_config import get_active_language
        import i18n
        i18n.set_locale(get_active_language())
        
        # Import and run CLI
        from file_search_tool import FileSearchTool
        
        tool = FileSearchTool()
        tool.run()
        
    except KeyboardInterrupt:
        print("\n[*] Interrupted by user.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"[ERROR] Failed to start Master Search CLI: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
