#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prüfung: Konsistenz der unterstützten Dateitypen
================================================

Überprüft, ob alle Dateitypen konsistent in allen Skripten erfasst sind.
"""

import re
from pathlib import Path

# ============================================================
# 1. SUPPORTED_TEXT_EXTENSIONS aus file_search_tool.py
# ============================================================
file_search_supported = {
    # Web & Markup
    'html', 'htm', 'xml', 'json',
    # Scripting & Programming
    'py', 'js', 'jsx', 'ts', 'tsx', 'java', 'cpp', 'c', 'h', 'hpp', 'cs', 
    'php', 'rb', 'go', 'rs', 'sh', 'bash', 'ps1', 'bat', 'kt', 'scala', 'swift',
    # Styling
    'css', 'scss', 'sass', 'less',
    # Data & Configuration
    'csv', 'yml', 'yaml', 'toml', 'ini', 'cfg', 'conf', 'config', 'env', 'sql',
    # Documentation
    'txt', 'md', 'rst',
    # Office Documents
    'doc', 'docx', 'pdf', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'rtf',
    # Databases
    'db', 'sqlite',
    # Other
    'log', 'edcx', 'vue', 'svelte', 'properties'
}

# ============================================================
# 2. CATEGORY_MAPPING aus gui_search_tool.py
# ============================================================
gui_category_mapping = {
    # Code
    'py': 'code', 'java': 'code', 'js': 'code', 'jsx': 'code', 'ts': 'code', 'tsx': 'code',
    'cpp': 'code', 'c': 'code', 'h': 'code', 'hpp': 'code', 'cs': 'code', 'swift': 'code',
    'go': 'code', 'rs': 'code', 'rb': 'code', 'php': 'code', 'scala': 'code',
    'kt': 'code', 'sh': 'code', 'bash': 'code', 'ps1': 'code', 'bat': 'code',
    
    # Documents
    'pdf': 'documents', 'docx': 'documents', 'doc': 'documents', 'xlsx': 'documents',
    'xls': 'documents', 'pptx': 'documents', 'ppt': 'documents', 'odt': 'documents',
    'rtf': 'documents',
    
    # Data
    'csv': 'data', 'json': 'data', 'xml': 'data', 'sql': 'data', 'db': 'data',
    'sqlite': 'data', 'yaml': 'data', 'yml': 'data',
    
    # Logs
    'log': 'logs', 'txt': 'logs',
    
    # Config
    'cfg': 'config', 'conf': 'config', 'config': 'config', 'ini': 'config', 'toml': 'config',
    'properties': 'config', 'env': 'config',
    
    # Web (includes documentation markup)
    'html': 'web', 'htm': 'web', 'css': 'web', 'scss': 'web', 'sass': 'web', 'less': 'web',
    'vue': 'web', 'svelte': 'web', 'md': 'web', 'rst': 'web', 'edcx': 'web',
}

# ============================================================
# 3. EXTRACTORS - Überprüfe welche Dateitypen Extraktoren haben
# ============================================================
extractors = {
    'docx': 'extract_text_from_docx()',
    'doc': 'extract_text_from_doc()',
    'pdf': 'extract_text_from_pdf()',
    'xlsx': 'extract_text_from_xlsx()',
    'pptx': 'extract_text_from_pptx()',
    'odt': 'extract_text_from_odt()',
    'rtf': 'extract_text_from_rtf()',
    'csv': 'extract_text_from_csv()',
    'log': 'extract_text_from_log()',
}

# ============================================================
# ANALYSE
# ============================================================

def analyze():
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║  Prüfung: Konsistenz der unterstützten Dateitypen            ║")
    print("╚════════════════════════════════════════════════════════════════╝\n")
    
    # 1. Erweiterungen in file_search_tool.py aber nicht in CATEGORY_MAPPING
    print("📊 ANALYSE 1: Dateitypen in file_search_tool.py aber NICHT in CATEGORY_MAPPING")
    print("─" * 70)
    missing_in_gui = file_search_supported - set(gui_category_mapping.keys())
    
    if missing_in_gui:
        print(f"❌ FEHLER: {len(missing_in_gui)} Dateityp(en) fehlen in CATEGORY_MAPPING:")
        for ext in sorted(missing_in_gui):
            print(f"   • .{ext}")
        print()
    else:
        print("✅ OK: Alle Dateitypen aus file_search_tool.py sind in CATEGORY_MAPPING\n")
    
    # 2. Erweiterungen in CATEGORY_MAPPING aber nicht in file_search_tool.py
    print("📊 ANALYSE 2: Dateitypen in CATEGORY_MAPPING aber NICHT in file_search_tool.py")
    print("─" * 70)
    extra_in_gui = set(gui_category_mapping.keys()) - file_search_supported
    
    if extra_in_gui:
        print(f"⚠️  WARNUNG: {len(extra_in_gui)} Dateityp(en) sind in CATEGORY_MAPPING aber nicht in file_search_tool.py:")
        for ext in sorted(extra_in_gui):
            cat = gui_category_mapping[ext]
            print(f"   • .{ext} ({cat})")
        print()
    else:
        print("✅ OK: Keine zusätzlichen Dateitypen in CATEGORY_MAPPING\n")
    
    # 3. Extraktoren-Abdeckung
    print("📊 ANALYSE 3: Extraktoren-Abdeckung")
    print("─" * 70)
    supported_with_special = {'pdf', 'docx', 'doc', 'xlsx', 'pptx', 'odt', 'rtf', 'csv'}
    
    missing_extractors = supported_with_special - set(extractors.keys())
    if missing_extractors:
        print(f"❌ FEHLER: {len(missing_extractors)} Dateityp(en) sollten Extraktoren haben:")
        for ext in sorted(missing_extractors):
            print(f"   • .{ext}")
    else:
        print(f"✅ OK: Alle Office/Spezial-Dateitypen haben Extraktoren")
        print(f"   Extraktoren verfügbar für: {', '.join(sorted(extractors.keys()))}")
    print()
    
    # 4. Zusammenfassung
    print("📊 ZUSAMMENFASSUNG")
    print("─" * 70)
    print(f"📁 Dateitypen in file_search_tool.py:  {len(file_search_supported)}")
    print(f"📁 Dateitypen in CATEGORY_MAPPING:     {len(gui_category_mapping)}")
    print(f"📁 Extraktoren (spezial):              {len(extractors)}")
    print()
    
    # 5. Kategorie-Übersicht
    print("📊 KATEGORIE-ÜBERSICHT")
    print("─" * 70)
    categories = {}
    for ext, cat in gui_category_mapping.items():
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(ext)
    
    for cat in sorted(categories.keys()):
        exts = sorted(categories[cat])
        icons = {
            'code': '💻',
            'documents': '📄',
            'data': '📊',
            'logs': '📝',
            'config': '⚙️',
            'web': '🌐'
        }
        icon = icons.get(cat, '📁')
        print(f"\n{icon} {cat.upper()} ({len(exts)} Typen):")
        print(f"   {', '.join([f'.{e}' for e in exts])}")
    print()
    
    # 6. Empfehlungen
    print("📊 EMPFEHLUNGEN")
    print("─" * 70)
    if missing_in_gui:
        print("⚠️  Empfehlung 1: Fehlende Dateitypen zu CATEGORY_MAPPING hinzufügen:")
        for ext in sorted(missing_in_gui):
            print(f"   '{ext}': 'category',  # .{ext}")
    
    if extra_in_gui:
        print("⚠️  Empfehlung 2: Überprüfen ob extra Dateitypen in file_search_tool.py aufgenommen werden sollten")
    
    print("\n✅ Prüfung abgeschlossen!")

if __name__ == '__main__':
    analyze()
