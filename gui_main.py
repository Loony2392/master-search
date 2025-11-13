#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - GUI Entry Point
================================
Main entry point for the Master Search GUI application.

Developer: Loony2392
Company: LOONY-TECH
Email: info@loony-tech.de
"""

import sys
import os
import logging

# Setup logging to file for debugging (use temp directory for writable location)
try:
    # Try to use TEMP directory first
    log_dir = os.path.expandvars(r'%TEMP%\Master Search')
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "master_search_gui.log")
except Exception:
    # Fallback to application directory if available
    try:
        log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "master_search_gui.log")
    except Exception:
        # Last resort: just log to stderr
        log_file = None

# Configure logging
if log_file:
    try:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
    except Exception:
        # If file logging fails, just use stderr
        logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.DEBUG)

def main():
    """Launch the Master Search GUI."""
    try:
        logging.info("Starting Master Search GUI...")
        
        # Setup paths for imports - handle both frozen and dev mode
        if getattr(sys, 'frozen', False):
            # In cx_Freeze bundle, app_dir is the executable directory
            app_dir = os.path.dirname(sys.executable)
            logging.info("Running in frozen mode (cx_Freeze bundle)")
            logging.info(f"Executable directory: {app_dir}")
        else:
            # In development, use script directory
            app_dir = os.path.dirname(os.path.abspath(__file__))
            logging.info("Running in development mode")
            logging.info(f"Script directory: {app_dir}")
        
        # Add app directory to path for imports (root level imports)
        if app_dir not in sys.path:
            sys.path.insert(0, app_dir)
        
        logging.info(f"sys.path (first 5): {sys.path[:5]}")
        logging.info("=" * 60)
        
        # Import language config and i18n
        logging.info("Importing language configuration...")
        try:
            from config.language_config import get_active_language, show_language_dialog, get_saved_language
            logging.info("✓ Successfully imported from config.language_config")
        except ImportError as e:
            logging.error(f"✗ Failed to import language_config: {e}")
            logging.error(f"  app_dir={app_dir}")
            logging.error(f"  config dir exists: {os.path.exists(os.path.join(app_dir, 'config'))}")
            raise
        
        try:
            from src.i18n import set_locale
            logging.info("✓ Successfully imported src.i18n")
        except ImportError as e:
            logging.error(f"✗ Failed to import src.i18n: {e}")
            logging.error(f"  src dir exists: {os.path.exists(os.path.join(app_dir, 'src'))}")
            raise
        
        # Check if language is already configured
        saved_lang = get_saved_language()
        logging.info(f"Saved language: {saved_lang}")
        
        if not saved_lang:
            # First time - show language selection dialog
            logging.info("First run - showing language selection dialog...")
            selected_lang = show_language_dialog()
            logging.info(f"User selected language: {selected_lang}")
            set_locale(selected_lang)
        else:
            # Use saved language
            logging.info(f"Using saved language: {saved_lang}")
            set_locale(saved_lang)
        
        # Import and run GUI
        logging.info("Importing GUI module...")
        try:
            from src.gui_search_tool import MasterSearchGUI
            logging.info("✓ Successfully imported MasterSearchGUI")
        except ImportError as e:
            logging.error(f"✗ Failed to import MasterSearchGUI: {e}")
            raise
        
        logging.info("Creating GUI instance...")
        app = MasterSearchGUI()

        # Show update notification once per version (GUI dialog if possible)
        try:
            from src.update_notifier import check_and_show_update
            try:
                # Pass the main window so the dialog is modal to the app
                check_and_show_update(app.root)
            except Exception as e:
                logging.debug(f"GUI update dialog failed: {e}, trying console notification")
                # If GUI dialog fails for any reason, fall back to console notification
                check_and_show_update(None)
        except Exception as e:
            logging.debug(f"Update notifier not available or failed: {e}")
        
        logging.info("Running GUI...")
        app.run()
        
    except Exception as e:
        logging.error(f"Failed to start Master Search GUI: {e}", exc_info=True)
        print(f"[ERROR] Failed to start Master Search GUI: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
