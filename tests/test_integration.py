#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funktionale Tests für GUI und i18n System

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
"""

import unittest
import os
import sys
from pathlib import Path
import json
import tempfile

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from i18n import I18n, set_language, get_language
from version import VERSION, AUTHOR, EMAIL


class TestI18nSystem(unittest.TestCase):
    """Tests für i18n Übersetzungssystem"""
    
    def setUp(self):
        """Setup für i18n Tests"""
        self.i18n = I18n()
    
    def test_i18n_initialization(self):
        """Test: i18n kann initialisiert werden"""
        self.assertIsNotNone(self.i18n)
    
    def test_language_files_exist(self):
        """Test: Sprach-Dateien existieren"""
        # Prüfe ob Übersetzungsdateien vorhanden sind
        locales_dir = Path(__file__).parent.parent / "locales"
        self.assertTrue(locales_dir.exists(), "locales Verzeichnis sollte existieren")
        
        en_file = locales_dir / "en.json"
        de_file = locales_dir / "de.json"
        
        self.assertTrue(en_file.exists(), "en.json sollte existieren")
        self.assertTrue(de_file.exists(), "de.json sollte existieren")
    
    def test_english_translations_valid(self):
        """Test: Englische Übersetzungen sind gültiges JSON"""
        locales_dir = Path(__file__).parent.parent / "locales"
        en_file = locales_dir / "en.json"
        
        try:
            with open(en_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.assertIsInstance(data, dict)
            self.assertGreater(len(data), 0)
        except json.JSONDecodeError:
            self.fail("en.json ist nicht gültiges JSON")
    
    def test_german_translations_valid(self):
        """Test: Deutsche Übersetzungen sind gültiges JSON"""
        locales_dir = Path(__file__).parent.parent / "locales"
        de_file = locales_dir / "de.json"
        
        try:
            with open(de_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.assertIsInstance(data, dict)
            self.assertGreater(len(data), 0)
        except json.JSONDecodeError:
            self.fail("de.json ist nicht gültiges JSON")
    
    def test_translation_keys_match(self):
        """Test: Englische und deutsche Keys stimmen überein"""
        locales_dir = Path(__file__).parent.parent / "locales"
        
        with open(locales_dir / "en.json", 'r', encoding='utf-8') as f:
            en_data = json.load(f)
        with open(locales_dir / "de.json", 'r', encoding='utf-8') as f:
            de_data = json.load(f)
        
        en_keys = set(en_data.keys())
        de_keys = set(de_data.keys())
        
        # Alle Keys sollten in beiden Dateien vorhanden sein
        missing_in_de = en_keys - de_keys
        missing_in_en = de_keys - en_keys
        
        self.assertEqual(len(missing_in_de), 0, 
                        f"Fehlende Keys in de.json: {missing_in_de}")
        self.assertEqual(len(missing_in_en), 0,
                        f"Fehlende Keys in en.json: {missing_in_en}")
    
    def test_no_empty_translations(self):
        """Test: Keine leeren Übersetzungen"""
        locales_dir = Path(__file__).parent.parent / "locales"
        
        for lang_file in [locales_dir / "en.json", locales_dir / "de.json"]:
            with open(lang_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for key, value in data.items():
                self.assertNotEqual(value, "", f"Leere Übersetzung für Key '{key}' in {lang_file.name}")
                self.assertIsNotNone(value, f"None-Übersetzung für Key '{key}' in {lang_file.name}")


class TestReportGenerator(unittest.TestCase):
    """Tests für Report Generator"""
    
    def test_report_generator_import(self):
        """Test: ReportGenerator kann importiert werden"""
        try:
            from report_generator import HTMLReportGenerator
            self.assertIsNotNone(HTMLReportGenerator)
        except ImportError:
            self.fail("ReportGenerator konnte nicht importiert werden")
    
    def test_report_generator_initialization(self):
        """Test: ReportGenerator kann initialisiert werden"""
        from report_generator import HTMLReportGenerator
        gen = HTMLReportGenerator(language="en")
        self.assertIsNotNone(gen)
    
    def test_report_with_empty_results(self):
        """Test: Report mit leeren Ergebnissen"""
        from report_generator import HTMLReportGenerator
        gen = HTMLReportGenerator(language="en")
        report = gen.generate({
            'search_term': 'test',
            'results': [],
            'statistics': {}
        })
        self.assertIsNotNone(report)
        self.assertIn("test", report)


class TestLanguageConfiguration(unittest.TestCase):
    """Tests für Sprach-Konfiguration"""
    
    def test_language_config_import(self):
        """Test: language_config kann importiert werden"""
        try:
            from language_config import LanguageConfig
            self.assertIsNotNone(LanguageConfig)
        except ImportError:
            self.fail("LanguageConfig konnte nicht importiert werden")
    
    def test_language_detection(self):
        """Test: Betriebssystem-Sprache kann erkannt werden"""
        try:
            import locale
            lang = locale.getdefaultlocale()[0]
            self.assertIsNotNone(lang)
        except:
            pass  # Optional


class TestVersionManagement(unittest.TestCase):
    """Tests für Versionsverwaltung"""
    
    def test_version_format(self):
        """Test: Version hat korrektes Format"""
        import re
        pattern = r'^\d+\.\d+\.\d+$'
        self.assertRegex(VERSION, pattern, 
                        f"Version '{VERSION}' hat nicht das richtige Format")
    
    def test_author_information(self):
        """Test: Author-Informationen sind vorhanden"""
        self.assertEqual(AUTHOR, "Loony2392")
        self.assertEqual(EMAIL, "info@loony-tech.de")
    
    def test_version_file_exists(self):
        """Test: version.py Datei existiert"""
        version_file = Path(__file__).parent.parent / "version.py"
        self.assertTrue(version_file.exists())


class TestIntegration(unittest.TestCase):
    """Integrations-Tests"""
    
    def test_all_main_modules_import(self):
        """Test: Alle Hauptmodule können importiert werden"""
        modules = [
            'file_search_tool',
            'gui_search_tool',
            'report_generator',
            'i18n',
            'language_config',
            'version'
        ]
        
        for module in modules:
            try:
                __import__(module)
            except ImportError as e:
                self.fail(f"Modul '{module}' konnte nicht importiert werden: {e}")
    
    def test_cli_entry_point(self):
        """Test: CLI Entry Point existiert"""
        cli_file = Path(__file__).parent.parent / "cli_main.py"
        self.assertTrue(cli_file.exists())
    
    def test_gui_entry_point(self):
        """Test: GUI Entry Point existiert"""
        gui_file = Path(__file__).parent.parent / "gui_main.py"
        self.assertTrue(gui_file.exists())
    
    def test_build_script_exists(self):
        """Test: Build-Script existiert"""
        build_file = Path(__file__).parent.parent / "build_msi.py"
        self.assertTrue(build_file.exists())
    
    def test_requirements_exist(self):
        """Test: Requirements-Datei existiert"""
        req_file = Path(__file__).parent.parent / "requirements.txt"
        self.assertTrue(req_file.exists())


class TestSyntaxValidation(unittest.TestCase):
    """Tests für Python Syntax"""
    
    def test_all_py_files_syntax(self):
        """Test: Alle Python-Dateien haben gültige Syntax"""
        import py_compile
        import tempfile
        
        base_dir = Path(__file__).parent.parent
        py_files = list(base_dir.glob("*.py"))
        
        for py_file in py_files:
            try:
                py_compile.compile(str(py_file), doraise=True)
            except py_compile.PyCompileError as e:
                self.fail(f"Syntax-Fehler in {py_file.name}: {e}")


class TestConfigurationFiles(unittest.TestCase):
    """Tests für Konfigurationsdateien"""
    
    def test_setup_msi_exists(self):
        """Test: setup_msi.py existiert"""
        setup_file = Path(__file__).parent.parent / "setup_msi.py"
        self.assertTrue(setup_file.exists())
    
    def test_performance_config_exists(self):
        """Test: performance_config.py existiert"""
        perf_file = Path(__file__).parent.parent / "performance_config.py"
        self.assertTrue(perf_file.exists())
    
    def test_workflow_files_exist(self):
        """Test: GitHub Workflow-Dateien existieren"""
        workflows_dir = Path(__file__).parent.parent / ".github" / "workflows"
        self.assertTrue(workflows_dir.exists())
        
        test_workflow = workflows_dir / "test.yml"
        release_workflow = workflows_dir / "release.yml"
        
        self.assertTrue(test_workflow.exists(), "test.yml sollte existieren")
        self.assertTrue(release_workflow.exists(), "release.yml sollte existieren")
    
    def test_documentation_files_exist(self):
        """Test: Dokumentation existiert"""
        docs = [
            Path(__file__).parent.parent / "README.md",
            Path(__file__).parent.parent / "VERSION_MANAGEMENT.md",
            Path(__file__).parent.parent / "SECURITY_AUDIT.md",
            Path(__file__).parent.parent / ".github" / "WORKFLOWS.md"
        ]
        
        for doc in docs:
            self.assertTrue(doc.exists(), f"{doc.name} sollte existieren")


if __name__ == '__main__':
    unittest.main(verbosity=2)
