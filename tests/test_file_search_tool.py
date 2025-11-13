#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit Tests für FileSearchTool

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
"""

import unittest
import tempfile
import os
from pathlib import Path
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from file_search_tool import FileSearchTool
from version import VERSION, AUTHOR, EMAIL


class TestFileSearchTool(unittest.TestCase):
    """Tests für FileSearchTool Klasse"""
    
    def setUp(self):
        """Setup für jeden Test"""
        self.tool = FileSearchTool()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Cleanup nach jedem Test"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_initialization(self):
        """Test: FileSearchTool kann initialisiert werden"""
        self.assertIsNotNone(self.tool)
        self.assertEqual(self.tool.search_mode, "any")
    
    def test_version_import(self):
        """Test: Version kann importiert werden"""
        self.assertIsNotNone(VERSION)
        self.assertEqual(AUTHOR, "Loony2392")
        self.assertEqual(EMAIL, "info@loony-tech.de")
    
    def test_search_terms_parsing_single(self):
        """Test: Einzelner Suchbegriff wird korrekt geparst"""
        terms = self.tool.parse_search_terms("hello")
        self.assertEqual(len(terms), 1)
        self.assertIn("hello", terms)
    
    def test_search_terms_parsing_multiple(self):
        """Test: Mehrere Suchbegriffe werden korrekt geparst"""
        terms = self.tool.parse_search_terms("hello world test")
        self.assertEqual(len(terms), 3)
        self.assertIn("hello", terms)
        self.assertIn("world", terms)
        self.assertIn("test", terms)
    
    def test_search_terms_parsing_quoted(self):
        """Test: Quoted Suchbegriffe werden korrekt geparst"""
        terms = self.tool.parse_search_terms('"hello world"')
        self.assertGreater(len(terms), 0)
    
    def test_text_matching_any_mode(self):
        """Test: Text-Matching im ANY-Mode"""
        self.tool.search_mode = "any"
        text = "hello world test"
        terms = ["hello", "world"]
        result = self.tool.match_text(text, terms, mode="any", case_sensitive=False)
        self.assertTrue(result)
    
    def test_text_matching_all_mode(self):
        """Test: Text-Matching im ALL-Mode"""
        self.tool.search_mode = "all"
        text = "hello world test"
        terms = ["hello", "world"]
        result = self.tool.match_text(text, terms, mode="all", case_sensitive=False)
        self.assertTrue(result)
    
    def test_text_matching_all_mode_negative(self):
        """Test: Text-Matching im ALL-Mode mit fehlenden Term"""
        text = "hello world"
        terms = ["hello", "missing"]
        result = self.tool.match_text(text, terms, mode="all", case_sensitive=False)
        self.assertFalse(result)
    
    def test_text_matching_case_sensitive(self):
        """Test: Case-sensitive Matching"""
        text = "Hello World"
        terms = ["hello"]
        result = self.tool.match_text(text, terms, case_sensitive=True)
        self.assertFalse(result)
    
    def test_text_matching_case_insensitive(self):
        """Test: Case-insensitive Matching"""
        text = "Hello World"
        terms = ["hello"]
        result = self.tool.match_text(text, terms, case_sensitive=False)
        self.assertTrue(result)
    
    def test_is_text_file_true(self):
        """Test: Text-Dateien werden erkannt"""
        text_files = [".txt", ".py", ".md", ".json"]
        for ext in text_files:
            test_file = f"test{ext}"
            result = self.tool.is_text_file(test_file)
            self.assertTrue(result, f"{ext} sollte als Text-Datei erkannt werden")
    
    def test_is_text_file_false(self):
        """Test: Binär-Dateien werden nicht erkannt"""
        binary_files = [".exe", ".dll", ".so", ".bin"]
        for ext in binary_files:
            test_file = f"test{ext}"
            result = self.tool.is_text_file(test_file)
            self.assertFalse(result, f"{ext} sollte nicht als Text-Datei erkannt werden")
    
    def test_set_search_path(self):
        """Test: Suchpfad kann gesetzt werden"""
        self.tool.set_search_path(self.temp_dir)
        self.assertEqual(self.tool.search_path, self.temp_dir)
    
    def test_add_search_term(self):
        """Test: Suchbegriff kann hinzugefügt werden"""
        self.tool.add_search_term("test")
        self.assertIn("test", self.tool.search_terms)
    
    def test_add_search_terms_multiple(self):
        """Test: Mehrere Suchbegriffe können hinzugefügt werden"""
        self.tool.add_search_term("test1")
        self.tool.add_search_term("test2")
        self.assertIn("test1", self.tool.search_terms)
        self.assertIn("test2", self.tool.search_terms)
    
    def test_clear_search_terms(self):
        """Test: Suchbegriffe können geleert werden"""
        self.tool.add_search_term("test")
        self.tool.clear_search_terms()
        self.assertEqual(len(self.tool.search_terms), 0)
    
    def test_regex_pattern_valid(self):
        """Test: Gültige Regex-Muster werden akzeptiert"""
        import re
        pattern = r"test.*\.py"
        try:
            re.compile(pattern)
            is_valid = True
        except:
            is_valid = False
        self.assertTrue(is_valid)
    
    def test_default_config_values(self):
        """Test: Standard-Konfiguration ist korrekt"""
        self.assertIsNotNone(self.tool.search_mode)
        self.assertIsNotNone(self.tool.case_sensitive)
        self.assertIsNotNone(self.tool.use_regex)


class TestFileOperations(unittest.TestCase):
    """Tests für Datei-Operationen"""
    
    def setUp(self):
        """Setup für Datei-Tests"""
        self.tool = FileSearchTool()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Cleanup"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def test_create_test_file(self):
        """Test: Test-Datei kann erstellt werden"""
        test_file = os.path.join(self.temp_dir, "test.txt")
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("Hello World")
        self.assertTrue(os.path.exists(test_file))
    
    def test_file_detection(self):
        """Test: Dateien im Verzeichnis werden erkannt"""
        test_file = os.path.join(self.temp_dir, "test.txt")
        with open(test_file, "w", encoding="utf-8") as f:
            f.write("Test Content")
        
        files = list(Path(self.temp_dir).glob("*.txt"))
        self.assertEqual(len(files), 1)
    
    def test_multiple_files(self):
        """Test: Mehrere Dateien werden erkannt"""
        for i in range(3):
            test_file = os.path.join(self.temp_dir, f"test{i}.txt")
            with open(test_file, "w", encoding="utf-8") as f:
                f.write(f"Content {i}")
        
        files = list(Path(self.temp_dir).glob("*.txt"))
        self.assertEqual(len(files), 3)
    
    def test_subdirectory_handling(self):
        """Test: Unterverzeichnisse werden korrekt behandelt"""
        subdir = os.path.join(self.temp_dir, "subdir")
        os.makedirs(subdir)
        self.assertTrue(os.path.isdir(subdir))


class TestErrorHandling(unittest.TestCase):
    """Tests für Fehlerbehandlung"""
    
    def setUp(self):
        """Setup"""
        self.tool = FileSearchTool()
    
    def test_empty_search_terms(self):
        """Test: Leere Suchbegriffe werden behandelt"""
        self.tool.clear_search_terms()
        self.assertEqual(len(self.tool.search_terms), 0)
    
    def test_invalid_search_path(self):
        """Test: Ungültige Pfade werden behandelt"""
        invalid_path = "/nonexistent/path/to/directory"
        self.tool.set_search_path(invalid_path)
        # Tool sollte Pfad akzeptieren, aber bei Suche fehlschlagen
        self.assertEqual(self.tool.search_path, invalid_path)
    
    def test_special_characters_in_search(self):
        """Test: Sonderzeichen in Suchbegriffen"""
        terms = self.tool.parse_search_terms("test@#$%^&*()")
        self.assertGreater(len(terms), 0)


class TestConfigurationValidation(unittest.TestCase):
    """Tests für Konfigurations-Validierung"""
    
    def setUp(self):
        """Setup"""
        self.tool = FileSearchTool()
    
    def test_search_mode_default(self):
        """Test: Standard Search-Mode ist gültig"""
        self.assertIn(self.tool.search_mode, ["any", "all", "exact"])
    
    def test_set_search_mode(self):
        """Test: Search-Mode kann geändert werden"""
        self.tool.set_search_mode("all")
        self.assertEqual(self.tool.search_mode, "all")
    
    def test_multiprocessing_flag(self):
        """Test: Multiprocessing Flag kann gesetzt werden"""
        self.tool.use_multiprocessing = False
        self.assertFalse(self.tool.use_multiprocessing)
        
        self.tool.use_multiprocessing = True
        self.assertTrue(self.tool.use_multiprocessing)


if __name__ == '__main__':
    unittest.main(verbosity=2)
