#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Script: Limited Results Display Feature
=============================================

Testet die neue Funktionalität zur begrenzten Anzeige von Treffern (nur erste 3 Treffer sichtbar).
"""

import sys
import os
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from report_generator import HTMLReportGenerator

def test_limited_results_display():
    """Test report generation with many matches to test the show/hide functionality."""
    
    print("╔══════════════════════════════════════════════════════════════════════╗")
    print("║         Test: Begrenzte Treffer-Anzeige (nur erste 3 Treffer)       ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\n")
    
    # Create test data with many matches per file
    test_results = [
        {
            'type': 'file',
            'name': 'large_file_with_many_matches.py',
            'path': r'C:\Users\b.kolb\OneDrive - TSL-Escha GmbH\Code\Master Search\large_file_with_many_matches.py',
            'matches': [
                {
                    'line_number': 15,
                    'line_content': 'def search_function(term):',
                    'found_terms': ['search']
                },
                {
                    'line_number': 23,
                    'line_content': '    if search_term in line:',
                    'found_terms': ['search']
                },
                {
                    'line_number': 45,
                    'line_content': '    return search_results',
                    'found_terms': ['search']
                },
                {
                    'line_number': 67,
                    'line_content': '# This is the 4th search match - should be hidden initially',
                    'found_terms': ['search']
                },
                {
                    'line_number': 78,
                    'line_content': 'class SearchEngine:',
                    'found_terms': ['search']
                },
                {
                    'line_number': 89,
                    'line_content': '    def advanced_search(self, pattern):',
                    'found_terms': ['search']
                },
                {
                    'line_number': 102,
                    'line_content': '        # Perform binary search',
                    'found_terms': ['search']
                },
                {
                    'line_number': 115,
                    'line_content': '        return self.search_index[key]',
                    'found_terms': ['search']
                }
            ]
        },
        {
            'type': 'file',
            'name': 'another_file_with_few_matches.py',
            'path': r'C:\Users\b.kolb\OneDrive - TSL-Escha GmbH\Code\Master Search\another_file_with_few_matches.py',
            'matches': [
                {
                    'line_number': 10,
                    'line_content': 'import search_utils',
                    'found_terms': ['search']
                },
                {
                    'line_number': 20,
                    'line_content': 'result = search_utils.find(pattern)',
                    'found_terms': ['search']
                }
            ]
        },
        {
            'type': 'file',
            'name': 'config_with_exact_3_matches.py',
            'path': r'C:\Users\b.kolb\OneDrive - TSL-Escha GmbH\Code\Master Search\config_with_exact_3_matches.py',
            'matches': [
                {
                    'line_number': 5,
                    'line_content': 'SEARCH_ENABLED = True',
                    'found_terms': ['search']
                },
                {
                    'line_number': 12,
                    'line_content': 'SEARCH_TIMEOUT = 30',
                    'found_terms': ['search']
                },
                {
                    'line_number': 18,
                    'line_content': 'DEFAULT_SEARCH_PATH = "/home/user"',
                    'found_terms': ['search']
                }
            ]
        }
    ]
    
    # Generate report
    generator = HTMLReportGenerator(
        search_terms=['search', 'pattern'],
        search_path=r'C:\Users\b.kolb\OneDrive - TSL-Escha GmbH\Code\Master Search',
        case_sensitive=False,
        use_regex=False,
        output_dir=Path.home() / 'Desktop'
    )
    
    print("📊 Report-Generierung startet...\n")
    report_path = generator.generate(test_results, auto_open=False)
    
    if report_path:
        print(f"✅ Report erfolgreich erstellt!")
        print(f"📄 Pfad: {report_path}\n")
        
        print("╔══════════════════════════════════════════════════════════════════════╗")
        print("║                          TESTHERGEBNISSE                             ║")
        print("╚══════════════════════════════════════════════════════════════════════╝\n")
        
        print("✅ NEUE FEATURE: BEGRENZTE TREFFER-ANZEIGE\n")
        
        print("📋 ERWARTETE ERGEBNISSE PRO DATEI:\n")
        
        print("1. 'large_file_with_many_matches.py' (8 Treffer total):")
        print("   ✓ Nur erste 3 Treffer sofort sichtbar")
        print("   ✓ Button: '📄 Weitere 5 Treffer in der Datei anzeigen'")
        print("   ✓ Klick zeigt alle versteckten Treffer an")
        print("   ✓ Button ändert sich zu: '📄 Weitere Treffer ausblenden'\n")
        
        print("2. 'another_file_with_few_matches.py' (2 Treffer total):")
        print("   ✓ Alle 2 Treffer sichtbar (weniger als 3)")
        print("   ✓ KEIN 'Weitere Treffer anzeigen' Button\n")
        
        print("3. 'config_with_exact_3_matches.py' (3 Treffer total):")
        print("   ✓ Alle 3 Treffer sichtbar (exakt 3)")
        print("   ✓ KEIN 'Weitere Treffer anzeigen' Button\n")
        
        print("═══════════════════════════════════════════════════════════════════════\n")
        
        print("📋 EMPFOHLENE TESTS:\n")
        
        print("1. Öffnen Sie den Report im Browser:")
        print(f"   {report_path}\n")
        
        print("2. Überprüfen Sie die erste Datei:")
        print("   → Nur 3 Treffer sichtbar (Zeilen 15, 23, 45)")
        print("   → Button am Ende: 'Weitere 5 Treffer in der Datei anzeigen'\n")
        
        print("3. Klicken Sie auf den Button:")
        print("   → Alle 8 Treffer werden angezeigt")
        print("   → Button ändert Text zu: 'Weitere Treffer ausblenden'\n")
        
        print("4. Klicken Sie erneut auf den Button:")
        print("   → Nur erste 3 Treffer wieder sichtbar")
        print("   → Button zurück zum ursprünglichen Text\n")
        
        print("5. Überprüfen Sie die anderen Dateien:")
        print("   → 2. Datei: Kein Button (nur 2 Treffer)")
        print("   → 3. Datei: Kein Button (exakt 3 Treffer)\n")
        
        print("═══════════════════════════════════════════════════════════════════════")
        
        print("\n✅ Test-Report erstellt! Öffnen Sie den Report, um die neue Funktion zu testen.")
    
    else:
        print("❌ Fehler beim Erstellen des Reports")

if __name__ == '__main__':
    test_limited_results_display()