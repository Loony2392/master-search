#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Simple Test Runner
Tests ohne Probleme mit Unicode/Encoding

Author: Loony2392
Version: 1.0.0
"""

import subprocess
import sys
import os
from pathlib import Path

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("\n" + "="*80)
    print("MASTER SEARCH - TEST SUITE".center(80))
    print("="*80 + "\n")
    
    # 1. Syntax Check
    print("1. SYNTAX & LINTING")
    print("-" * 80)
    
    py_files = [
        "file_search_tool.py",
        "gui_search_tool.py",
        "report_generator.py",
        "i18n.py",
        "language_config.py",
        "gui_main.py",
        "cli_main.py",
        "version.py",
        "setup_msi.py",
        "build_msi.py",
        "performance_config.py"
    ]
    
    print("Checking Python syntax...")
    syntax_ok = True
    for py_file in py_files:
        try:
            with open(py_file, encoding='utf-8') as f:
                compile(f.read(), py_file, 'exec')
        except SyntaxError as e:
            print(f"FAIL: Syntax error in {py_file}: {e}")
            syntax_ok = False
        except Exception as e:
            print(f"FAIL: Error in {py_file}: {e}")
            syntax_ok = False
    
    if syntax_ok:
        print("OK: All Python files have valid syntax\n")
    
    # 2. Unit Tests
    print("2. UNIT TESTS")
    print("-" * 80)
    
    if Path("tests/test_file_search_tool.py").exists():
        print("Running unit tests...")
        result = subprocess.run([sys.executable, "-m", "pytest", 
                                "tests/test_file_search_tool.py", "-v", "--tb=short"],
                              capture_output=False)
        print()
    
    # 3. Integration Tests
    print("3. INTEGRATION TESTS")
    print("-" * 80)
    
    if Path("tests/test_integration.py").exists():
        print("Running integration tests...")
        result = subprocess.run([sys.executable, "-m", "pytest",
                                "tests/test_integration.py", "-v", "--tb=short"],
                              capture_output=False)
        print()
    
    # 4. Functional Tests
    print("4. FUNCTIONAL TESTS")
    print("-" * 80)
    
    print("Testing version management...")
    try:
        from version import VERSION, AUTHOR, EMAIL
        print(f"OK: Version: {VERSION}")
        print(f"OK: Author: {AUTHOR}")
        print(f"OK: Email: {EMAIL}\n")
    except Exception as e:
        print(f"FAIL: Version import failed: {e}\n")
    
    print("Testing module imports...")
    try:
        from file_search_tool import FileSearchTool
        from report_generator import HTMLReportGenerator
        print("OK: All modules imported successfully\n")
    except Exception as e:
        print(f"FAIL: Import failed: {e}\n")
    
    print("Testing translation files...")
    try:
        import json
        with open('locales/en.json', encoding='utf-8') as f:
            en = json.load(f)
        with open('locales/de.json', encoding='utf-8') as f:
            de = json.load(f)
        
        print(f"OK: English translations: {len(en)} keys")
        print(f"OK: German translations: {len(de)} keys")
        
        en_keys = set(en.keys())
        de_keys = set(de.keys())
        
        if en_keys == de_keys:
            print("OK: Translation keys match perfectly\n")
        else:
            missing_de = en_keys - de_keys
            missing_en = de_keys - en_keys
            if missing_de:
                print(f"WARN: Missing in DE: {missing_de}")
            if missing_en:
                print(f"WARN: Missing in EN: {missing_en}\n")
    except Exception as e:
        print(f"FAIL: Translation file error: {e}\n")
    
    # 5. Configuration Files
    print("5. CONFIGURATION FILES")
    print("-" * 80)
    
    files_to_check = [
        ("tests/test_file_search_tool.py", "Unit Tests"),
        ("tests/test_integration.py", "Integration Tests"),
        ("pytest.ini", "Pytest Config"),
        (".coveragerc", "Coverage Config"),
        (".github/workflows/test.yml", "Test Workflow"),
        (".github/workflows/release.yml", "Release Workflow"),
        ("README.md", "README"),
        ("SECURITY_AUDIT.md", "Security Audit"),
        ("TESTING.md", "Testing Documentation"),
        ("VERSION_MANAGEMENT.md", "Version Management"),
    ]
    
    for file_path, description in files_to_check:
        if Path(file_path).exists():
            print(f"OK: {description} ({file_path})")
        else:
            print(f"FAIL: {description} not found ({file_path})")
    
    print("\n" + "="*80)
    print("TEST SUITE COMPLETED".center(80))
    print("="*80 + "\n")
    print("Run 'pytest tests/ -v' for detailed test output")
    print("Run 'pytest tests/ --cov=file_search_tool --cov-report=html' for coverage report\n")

if __name__ == "__main__":
    main()
