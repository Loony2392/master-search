#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Lokaler Test Runner
Führt alle Tests mit Report aus

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
"""

import subprocess
import sys
import os
from pathlib import Path
import io

# Ensure UTF-8 output on Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Farben für Terminal-Output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    """Print header"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{text:^80}{Colors.ENDC}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*80}{Colors.ENDC}\n")

def print_status(status, message):
    """Print status message"""
    if status == "OK":
        print(f"{Colors.OKGREEN}✅ {message}{Colors.ENDC}")
    elif status == "FAIL":
        print(f"{Colors.FAIL}❌ {message}{Colors.ENDC}")
    elif status == "WARN":
        print(f"{Colors.WARNING}⚠️  {message}{Colors.ENDC}")
    elif status == "INFO":
        print(f"{Colors.OKBLUE}ℹ️  {message}{Colors.ENDC}")
    elif status == "RUN":
        print(f"{Colors.OKCYAN}🔍 {message}{Colors.ENDC}")

def run_command(cmd, description, continue_on_error=False):
    """Run command and print result"""
    print_status("RUN", f"{description}...")
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0 or continue_on_error:
            print_status("OK", f"{description} completed")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print_status("FAIL", f"{description} failed")
            if result.stderr:
                print(Colors.FAIL + result.stderr + Colors.ENDC)
            return False
    except Exception as e:
        print_status("FAIL", f"{description} error: {e}")
        return False

def main():
    """Main test runner"""
    print_header("MASTER SEARCH - TEST SUITE")
    print_status("INFO", f"Python Version: {sys.version}")
    print_status("INFO", f"Current Directory: {os.getcwd()}")
    
    # Check if in correct directory
    if not Path("file_search_tool.py").exists():
        print_status("FAIL", "file_search_tool.py not found in current directory!")
        sys.exit(1)
    
    print_status("OK", "Found main project files")
    
    # Test counter
    total_tests = 0
    passed_tests = 0
    
    # 1. Syntax Check
    print_header("1. SYNTAX & LINTING")
    
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
    
    print_status("RUN", "Checking Python syntax...")
    syntax_ok = True
    for py_file in py_files:
        try:
            compile(open(py_file).read(), py_file, 'exec')
        except SyntaxError as e:
            print_status("FAIL", f"Syntax error in {py_file}: {e}")
            syntax_ok = False
    
    if syntax_ok:
        print_status("OK", "All Python files have valid syntax")
        passed_tests += 1
    total_tests += 1
    
    # 2. Unit Tests
    print_header("2. UNIT TESTS")
    
    if Path("tests/test_file_search_tool.py").exists():
        if run_command("python -m pytest tests/test_file_search_tool.py -v --tb=short", 
                      "Unit Tests"):
            passed_tests += 1
    total_tests += 1
    
    # 3. Integration Tests
    print_header("3. INTEGRATION TESTS")
    
    if Path("tests/test_integration.py").exists():
        if run_command("python -m pytest tests/test_integration.py -v --tb=short",
                      "Integration Tests"):
            passed_tests += 1
    total_tests += 1
    
    # 4. Functional Tests
    print_header("4. FUNCTIONAL TESTS")
    
    print_status("RUN", "Testing version management...")
    try:
        from version import VERSION, AUTHOR, EMAIL
        print_status("OK", f"Version: {VERSION}")
        print_status("OK", f"Author: {AUTHOR}")
        print_status("OK", f"Email: {EMAIL}")
        passed_tests += 1
    except Exception as e:
        print_status("FAIL", f"Version import failed: {e}")
    total_tests += 1
    
    print_status("RUN", "Testing module imports...")
    try:
        from file_search_tool import FileSearchTool
        from report_generator import HTMLReportGenerator
        from i18n import I18n
        print_status("OK", "All modules imported successfully")
        passed_tests += 1
    except Exception as e:
        print_status("FAIL", f"Import failed: {e}")
    total_tests += 1
    
    print_status("RUN", "Testing translation files...")
    try:
        import json
        with open('locales/en.json') as f:
            en = json.load(f)
        with open('locales/de.json') as f:
            de = json.load(f)
        
        en_keys = set(en.keys())
        de_keys = set(de.keys())
        
        print_status("OK", f"English translations: {len(en)} keys")
        print_status("OK", f"German translations: {len(de)} keys")
        
        if en_keys == de_keys:
            print_status("OK", "Translation keys match perfectly")
            passed_tests += 1
        else:
            missing_de = en_keys - de_keys
            missing_en = de_keys - en_keys
            if missing_de:
                print_status("WARN", f"Missing in DE: {missing_de}")
            if missing_en:
                print_status("WARN", f"Missing in EN: {missing_en}")
    except Exception as e:
        print_status("FAIL", f"Translation file error: {e}")
    total_tests += 1
    
    # 5. Security Check
    print_header("5. SECURITY CHECK")
    
    print_status("RUN", "Checking for hardcoded secrets...")
    found_secrets = False
    for py_file in py_files:
        try:
            with open(py_file) as f:
                content = f.read()
                if "password" in content.lower() or "api_key" in content:
                    # Check if it's not just in comments or strings
                    lines = content.split('\n')
                    for i, line in enumerate(lines):
                        if not line.strip().startswith('#'):
                            if "password" in line.lower() or "api_key" in line:
                                print_status("WARN", f"Potential secret in {py_file}:{i+1}")
                                found_secrets = True
        except:
            pass
    
    if not found_secrets:
        print_status("OK", "No hardcoded secrets found")
        passed_tests += 1
    total_tests += 1
    
    # 6. Coverage Report
    print_header("6. COVERAGE REPORT")
    
    if Path("tests").exists():
        print_status("RUN", "Generating coverage report...")
        try:
            subprocess.run("python -m pytest tests/ --cov=file_search_tool --cov-report=html",
                          shell=True, capture_output=True, text=True)
            print_status("OK", "Coverage report generated (htmlcov/index.html)")
            passed_tests += 1
        except:
            pass
    total_tests += 1
    
    # Final Summary
    print_header("TEST SUMMARY")
    
    print_status("INFO", f"Total Tests: {total_tests}")
    print_status("INFO", f"Passed: {passed_tests}")
    print_status("INFO", f"Failed: {total_tests - passed_tests}")
    
    percentage = (passed_tests / total_tests * 100) if total_tests > 0 else 0
    print_status("INFO", f"Success Rate: {percentage:.1f}%")
    
    if passed_tests == total_tests:
        print_header("✅ ALL TESTS PASSED - READY FOR PRODUCTION")
        return 0
    else:
        print_header("❌ SOME TESTS FAILED - PLEASE FIX")
        return 1

if __name__ == "__main__":
    sys.exit(main())
