#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Path Repair Script for Master Search
====================================
Repairs import paths after reorganization into folder structure.
"""

import os
import re
from pathlib import Path

def repair_imports():
    """Repair all import statements in the reorganized project structure."""
    
    base_dir = Path(__file__).parent
    
    print("🔧 Repariere Import-Pfade nach Ordner-Reorganisation...")
    
    # 1. Repair i18n.py
    i18n_file = base_dir / "src" / "i18n.py"
    if i18n_file.exists():
        content = i18n_file.read_text(encoding='utf-8')
        
        # Add path configuration for locales
        if '_find_locales_dir()' in content:
            print("✅ i18n.py bereits konfiguriert")
        else:
            # Insert path configuration after imports
            lines = content.split('\n')
            insert_idx = None
            for i, line in enumerate(lines):
                if line.startswith('# Current active language'):
                    insert_idx = i
                    break
            
            if insert_idx:
                path_setup = '''
# Find locales directory relative to config folder
def _find_locales_dir():
    """Find locales directory."""
    try:
        # From config/locales
        path = Path(__file__).parent / "locales"
        if path.exists():
            return path
        # Fallback
        return Path.cwd() / "config" / "locales"
    except Exception:
        return Path.cwd() / "config" / "locales"
'''
                lines.insert(insert_idx, path_setup)
                
                # Update _load_translations function to use the new function
                new_content = '\n'.join(lines)
                new_content = new_content.replace(
                    'locales_dir = os.path.join(os.path.dirname(__file__), "locales")',
                    'locales_dir = _find_locales_dir()'
                )
                
                i18n_file.write_text(new_content, encoding='utf-8')
                print("✅ i18n.py Import-Pfade repariert")
    
    # 2. Repair settings_manager.py  
    settings_file = base_dir / "src" / "settings_manager.py"
    if settings_file.exists():
        print("✅ settings_manager.py bereits im src/ Ordner")
    
    # 3. Update _find_locales_dir in report_generator.py
    report_file = base_dir / "src" / "report_generator.py" 
    if report_file.exists():
        content = report_file.read_text(encoding='utf-8')
        
        # Update locales path in report generator
        new_content = content.replace(
            'path = Path(__file__).parent / "locales"',
            'path = Path(__file__).parent.parent / "config" / "locales"'
        )
        
        if new_content != content:
            report_file.write_text(new_content, encoding='utf-8')
            print("✅ report_generator.py Locales-Pfad repariert")
        else:
            print("✅ report_generator.py bereits korrekt")
    
    # 4. Update build directory paths to reference new structure
    build_dir = base_dir / "build" / "exe.win-amd64-3.11"
    if build_dir.exists():
        print("📂 Build-Verzeichnis gefunden - Import-Pfade werden angepasst...")
        
        # Update imports in build files to reference new src structure
        for py_file in build_dir.glob("*.py"):
            if py_file.name in ['gui_search_tool.py', 'file_search_tool.py', 'report_generator.py']:
                content = py_file.read_text(encoding='utf-8')
                
                # Add fallback sys.path setup for build environment  
                if 'sys.path.insert' not in content:
                    lines = content.split('\n')
                    import_idx = None
                    for i, line in enumerate(lines):
                        if line.startswith('import') or line.startswith('from'):
                            import_idx = i
                            break
                    
                    if import_idx is not None:
                        path_setup = '''
# Setup paths for build environment
try:
    # Add source paths for imports
    import os, sys
    base_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, base_path)
    sys.path.insert(0, os.path.join(base_path, 'src'))
    sys.path.insert(0, os.path.join(base_path, 'config'))
except:
    pass
'''
                        lines.insert(import_idx, path_setup)
                        new_content = '\n'.join(lines)
                        py_file.write_text(new_content, encoding='utf-8')
                        print(f"✅ {py_file.name} Build-Pfade repariert")
    
    print("\n🎯 Import-Pfad-Reparatur abgeschlossen!")
    print("\n📋 Getestete Konfiguration:")
    print(f"  ├── src/           - Haupt-Sourcecode")
    print(f"  ├── config/        - Konfiguration & Locales")  
    print(f"  ├── scripts/       - Build & Test Scripts")
    print(f"  ├── docs/          - Dokumentation")
    print(f"  ├── temp/          - Temporäre Dateien") 
    print(f"  ├── tests/         - Unit Tests")
    print(f"  └── build/         - Build-Ausgaben")
    print(f"\n✅ Alle Import-Pfade sollten nun funktionieren!")

if __name__ == "__main__":
    repair_imports()