#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Script für Zeilennummern-Feature (erweitert)
Testet die Zeilennummern-Extraktion für ALLE Dateitypen
"""

import os
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from file_search_tool import FileSearchTool

def create_test_files():
    """Erstelle Test-Dateien für verschiedene Formate."""
    test_dir = Path(__file__).parent / "test_files"
    test_dir.mkdir(exist_ok=True)
    
    # Textdatei
    (test_dir / "test.txt").write_text("""Zeile 1: Dies ist die erste Zeile
Zeile 2: Diese Zeile enthält "test"
Zeile 3: Noch eine Zeile ohne Treffer
Zeile 4: Hier ist wieder "test" vorhanden
Zeile 5: Abschluss""")
    
    # CSV-Datei
    (test_dir / "test.csv").write_text("""Name,Vorname,Stadt
Mueller,Hans,Berlin
Schmidt,Anna,test-City
Weber,Peter,München
Becker,Lisa,test-Dorf""")
    
    # Python-Code
    (test_dir / "test.py").write_text("""def test_function():
    print("test message")
    test_var = 42
    return test_var

if __name__ == "__main__":
    result = test_function()
    print(result)""")
    
    # JSON-Datei
    (test_dir / "test.json").write_text("""{
  "test": "value1",
  "name": "test-app",
  "version": "1.0",
  "description": "A test application"
}""")
    
    # Log-Datei
    (test_dir / "test.log").write_text("""2025-11-12 10:00:00 INFO: Application started with test parameters
2025-11-12 10:00:01 DEBUG: Loading test configuration
2025-11-12 10:00:02 INFO: Ready for testing
2025-11-12 10:00:03 ERROR: test error occurred
2025-11-12 10:00:04 INFO: Application terminated""")
    
    # HTML-Datei
    (test_dir / "test.html").write_text("""<!DOCTYPE html>
<html>
<head>
    <title>Test Page</title>
</head>
<body>
    <h1>This is a test page</h1>
    <p>Some test content here</p>
    <p>More testing information</p>
</body>
</html>""")
    
    # XML-Datei
    (test_dir / "test.xml").write_text("""<?xml version="1.0" encoding="UTF-8"?>
<root>
    <item>
        <name>test-item-1</name>
        <value>100</value>
    </item>
    <item>
        <name>test-item-2</name>
        <value>200</value>
    </item>
</root>""")
    
    # SQL-Datei
    (test_dir / "test.sql").write_text("""CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE
);

INSERT INTO users VALUES (1, 'test_user', 'test@example.com');
INSERT INTO users VALUES (2, 'test_admin', 'admin@test.com');
SELECT * FROM users WHERE name LIKE '%test%';""")
    
    # Markdown-Datei
    (test_dir / "test.md").write_text("""# Test Documentation

This is a test markdown file.

## Test Section

Some test content here.

- test item 1
- test item 2
- Regular item

## Another Section

More test information.""")
    
    # YAML-Datei
    (test_dir / "test.yaml").write_text("""version: 1.0
name: test-project
description: This is a test project
dependencies:
  - test-lib-1
  - test-lib-2
settings:
  test_mode: true
  test_timeout: 30""")
    
    # Konfigurationsdatei
    (test_dir / "test.conf").write_text("""[general]
name=test-config
enabled=true

[database]
host=localhost
port=5432
test_db=test_database

[logging]
level=test
pattern=%d{test-format}""")
    
    # Batch-Datei
    (test_dir / "test.bat").write_text("""@echo off
REM This is a test batch file
echo Running test script
set TEST_VAR=test_value
if "%TEST_VAR%"=="test_value" (
    echo Test passed
) else (
    echo Test failed
)
pause""")
    
    # Shell-Script
    (test_dir / "test.sh").write_text("""#!/bin/bash
# Test shell script
echo "Running test script"
TEST_VAR="test_value"
if [ "$TEST_VAR" = "test_value" ]; then
    echo "Test passed"
else
    echo "Test failed"
fi""")
    
    return test_dir

def test_all_formats():
    """Teste Zeilennummern-Extraktion für alle Dateitypen."""
    test_dir = create_test_files()
    
    tool = FileSearchTool(verbose=False)
    tool.search_terms = ["test"]
    tool.case_sensitive = False
    tool.use_regex = False
    
    print("="*60)
    print("🧪 ZEILENNUMMERN-FEATURE - UMFASSENDER TEST")
    print("="*60)
    print()
    
    test_files = sorted(test_dir.glob("test.*"))
    results = {}
    
    for test_file in test_files:
        file_ext = test_file.suffix
        print(f"📄 Test: {test_file.name}")
        
        try:
            matches = tool.search_in_file(str(test_file))
            if matches:
                results[file_ext] = len(matches)
                print(f"   ✅ Gefundene Treffer: {len(matches)}")
                for i, match in enumerate(matches[:3], 1):  # Zeige nur erste 3
                    print(f"      {i}. Zeile {match['line_number']}: {match['line_content'][:50]}...")
                if len(matches) > 3:
                    print(f"      ... und {len(matches)-3} weitere Treffer")
            else:
                results[file_ext] = 0
                print(f"   ⚠️  Keine Treffer gefunden")
        except Exception as e:
            results[file_ext] = -1
            print(f"   ❌ Fehler: {str(e)[:60]}")
        
        print()
    
    # Zusammenfassung
    print("="*60)
    print("📊 ZUSAMMENFASSUNG")
    print("="*60)
    
    success_count = sum(1 for v in results.values() if v > 0)
    empty_count = sum(1 for v in results.values() if v == 0)
    error_count = sum(1 for v in results.values() if v == -1)
    
    print(f"\n✅ Erfolgreich getestet: {success_count} Dateitypen")
    print(f"⚠️  Keine Treffer: {empty_count} Dateitypen")
    print(f"❌ Fehler: {error_count} Dateitypen")
    
    print(f"\n📋 Detaillierte Ergebnisse:")
    for ext, count in sorted(results.items()):
        status = "✅" if count > 0 else ("⚠️" if count == 0 else "❌")
        matches_str = f"{count} Treffer" if count > 0 else ("Keine Treffer" if count == 0 else "Fehler")
        print(f"  {status} {ext:10s} → {matches_str}")
    
    print()
    print(f"📁 Test-Dateien: {test_dir}")
    print()

if __name__ == "__main__":
    test_all_formats()
