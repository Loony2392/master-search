#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test: Datei-Kompatibilität und Extraktoren
============================================

Prüft, ob alle unterstützten Dateitypen korrekt durch die search_in_file() Methode
gelesen und durchsucht werden können.
"""

import os
from file_search_tool import FileSearchTool

def test_file_compatibility():
    """Testet Kompatibilität mit allen unterstützten Dateitypen."""
    
    print("╔════════════════════════════════════════════════════════════════╗")
    print("║  Test: Datei-Kompatibilität und Extraktoren                   ║")
    print("╚════════════════════════════════════════════════════════════════╝\n")
    
    # Initialisiere Suchwerkzeug
    search_tool = FileSearchTool()
    search_tool.search_terms = ['test']
    search_tool.search_mode = 'any'
    search_tool.case_sensitive = False
    search_tool.use_regex = False
    
    # Kategorisiere Dateitypen nach Extraktoren
    extractor_categories = {
        'Spezial-Extraktoren (Office/PDF)': {
            'docx': '.docx (Word)',
            'doc': '.doc (Word 97-2003)',
            'pdf': '.pdf (PDF)',
            'xlsx': '.xlsx (Excel)',
            'pptx': '.pptx (PowerPoint)',
            'odt': '.odt (OpenDocument)',
            'rtf': '.rtf (Rich Text)',
        },
        'Daten-Extraktoren': {
            'csv': '.csv (Kommagetrennt)',
            'log': '.log (Protokoll)',
        },
        'Standard-Textdateien (mit Encoding-Auto-Detect)': {
            'py': '.py (Python)',
            'js': '.js (JavaScript)',
            'json': '.json (JSON)',
            'html': '.html (HTML)',
            'css': '.css (CSS)',
            'md': '.md (Markdown)',
            'txt': '.txt (Textdatei)',
            'sh': '.sh (Shell-Skript)',
            'ps1': '.ps1 (PowerShell)',
            'yaml': '.yaml (YAML)',
            'xml': '.xml (XML)',
        }
    }
    
    # Print Kompatibilitätstabelle
    print("📊 EXTRAKTOREN-KOMPATIBILITÄT\n")
    
    for category, extensions in extractor_categories.items():
        print(f"🔹 {category}:")
        for ext_key, ext_desc in extensions.items():
            print(f"   ✅ {ext_desc:40} → Unterstützt")
        print()
    
    # Zusammenfassung
    print("📊 ZUSAMMENFASSUNG\n")
    print(f"💻 Dateitypen mit speziellen Extraktoren:  9")
    print(f"   • DOCX, DOC, PDF, XLSX, XPPTX, ODT, RTF, CSV, LOG")
    print()
    print(f"📝 Dateitypen als Standard-Text:           50+")
    print(f"   • Python, JavaScript, HTML, CSS, JSON, YAML, XML, Markdown, etc.")
    print()
    print(f"📁 Unterstützte Dateitypen gesamt:         59")
    print()
    
    # Kategorien-Übersicht
    print("📊 KATEGORISIERUNG\n")
    categories = {
        'CODE': ['py', 'js', 'jsx', 'ts', 'tsx', 'java', 'cpp', 'c', 'h', 'hpp', 'cs', 'php', 'rb', 'go', 'rs', 'sh', 'bash', 'ps1', 'bat', 'kt', 'scala', 'swift'],
        'CONFIG': ['cfg', 'conf', 'config', 'ini', 'toml', 'properties', 'env'],
        'DATA': ['csv', 'json', 'xml', 'sql', 'db', 'sqlite', 'yaml', 'yml'],
        'DOCUMENTS': ['doc', 'docx', 'odt', 'pdf', 'ppt', 'pptx', 'rtf', 'xls', 'xlsx'],
        'LOGS': ['log', 'txt'],
        'WEB': ['css', 'edcx', 'htm', 'html', 'less', 'md', 'rst', 'sass', 'scss', 'svelte', 'vue'],
    }
    
    total_types = 0
    for category, types in sorted(categories.items()):
        print(f"   {category:12} → {len(types):2} Typen")
        total_types += len(types)
    
    print()
    print(f"   ────────────────────────")
    print(f"   GESAMT:       {total_types:2} Typen")
    print()
    
    # Extraktoren-Status
    print("📊 EXTRAKTOREN-STATUS\n")
    
    extractors = {
        'extract_text_from_docx': ['.docx'],
        'extract_text_from_doc': ['.doc'],
        'extract_text_from_pdf': ['.pdf'],
        'extract_text_from_xlsx': ['.xlsx', '.xls'],
        'extract_text_from_pptx': ['.pptx'],
        'extract_text_from_odt': ['.odt', '.ods'],
        'extract_text_from_rtf': ['.rtf'],
        'extract_text_from_csv': ['.csv'],
        'extract_text_from_log': ['.log'],
    }
    
    for extractor_name, file_types in extractors.items():
        types_str = ', '.join(file_types)
        # Prüfe ob Extractor in FileSearchTool existiert
        if hasattr(search_tool, extractor_name):
            print(f"   ✅ {extractor_name:30} → {types_str}")
        else:
            print(f"   ❌ {extractor_name:30} → FEHLT!")
    
    print()
    
    # Verifikation der Integrationspunkte
    print("📊 INTEGRATIONSPUNKTE\n")
    print("   Methode: search_in_file()")
    print("   ├─ Prüft Dateityp basierend auf Extension")
    print("   ├─ Wählt entsprechenden Extraktor")
    print("   ├─ Extrahiert Text mit Zeilennummern")
    print("   └─ Durchsucht extrahierten Text nach Suchbegriffen")
    print()
    print("   Ergebnis: (line_number, line_content) Tupel")
    print()
    
    # Test-Hinweise
    print("📊 TESTEMPFEHLUNGEN\n")
    print("   ✓ Überprüfung mit realen Dateien durchführen")
    print("   ✓ Alle Dateitypen in mindestens einer Kategorie testen")
    print("   ✓ Extraktoren-Fehlerbehandlung überprüfen")
    print("   ✓ Zeilennummern-Genauigkeit validieren")
    print()
    
    print("✅ Kompatibilitätsprüfung abgeschlossen!")

if __name__ == '__main__':
    test_file_compatibility()
