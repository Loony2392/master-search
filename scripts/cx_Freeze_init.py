"""
cx_Freeze Initialization Hook
==============================
This module runs before the main application to set up DLL search paths
in a way that won't cause cx_Freeze fatal errors.
"""

import sys
import os

# Suppress cx_Freeze's DLL directory change attempts
# by ensuring the directories are already accessible
if getattr(sys, 'frozen', False) and sys.platform == 'win32':
    app_dir = os.path.dirname(sys.executable)
    
    # Add to PATH first
    if app_dir not in os.environ.get('PATH', ''):
        os.environ['PATH'] = app_dir + os.pathsep + os.environ.get('PATH', '')
    
    # Add lib directory
    lib_dir = os.path.join(app_dir, 'lib')
    if lib_dir not in os.environ.get('PATH', ''):
        os.environ['PATH'] = lib_dir + os.pathsep + os.environ.get('PATH', '')
