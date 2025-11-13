#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - Professional File Search Tool
==============================================
A comprehensive file and content search utility with HTML reporting capabilities.

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025

Description:
    Master Search is a powerful Python-based file search tool that allows users to:
    - Search for keywords in file names and folder names
    - Perform content search within text files
    - Generate professional HTML reports with direct file access links
    - Support multiple file formats and encodings
    - Provide real-time progress tracking with colorful console output

Features:
    - Professional colored console interface with emojis
    - Progress bars and real-time statistics
    - Intelligent text file detection
    - HTML report generation with click-to-open functionality
    - Cross-platform compatibility
    - Error handling and graceful fallbacks
"""

import os
import sys
import re
import html
from pathlib import Path
from datetime import datetime
import mimetypes
import time
import subprocess
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import threading
from queue import Queue

# Add parent directory to path for version import
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from version import VERSION, AUTHOR, EMAIL, COMPANY
from .report_generator import HTMLReportGenerator
from .platform_utils import PlatformUtils, get_temp_dir, open_file

# Cross-platform default report directory
DEFAULT_REPORT_DIR = get_temp_dir()

# Versuche psutil für System-Informationen zu importieren
try:
    import psutil
    PSUTIL_AVAILABLE = True 
except ImportError:
    PSUTIL_AVAILABLE = False

# Versuche colorama zu importieren, installiere es falls nötig
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    COLORAMA_AVAILABLE = True
except ImportError:
    print("🔧 colorama ist nicht installiert. Installiere es jetzt...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama>=0.4.6"])
        print("✅ colorama erfolgreich installiert!")
        from colorama import init, Fore, Back, Style
        init(autoreset=True)
        COLORAMA_AVAILABLE = True
    except Exception as e:
        print(f"⚠️  colorama konnte nicht installiert werden: {e}")
        print("🎨 Verwende Fallback ohne Farben...")
        COLORAMA_AVAILABLE = False
        # Fallback-Definitionen
        class MockColorama:
            def __getattr__(self, name):
                return ''
        
        Fore = MockColorama()
        Back = MockColorama()
        Style = MockColorama()
        
        def init(*args, **kwargs):
            pass

class FileSearchTool:
    def __init__(self, verbose=False):
        self.search_terms = []  # Geändert von search_term zu search_terms (Liste)
        self.search_mode = "any"  # "any" (OR) oder "all" (AND)
        self.case_sensitive = False
        self.use_regex = False
        self.search_path = ""
        self.results = []
        self.verbose = verbose  # Flag for verbose console output
        self.supported_text_extensions = {
            # Web & Markup
            '.html', '.htm', '.xml', '.json',
            # Scripting & Programming
            '.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.cpp', '.c', '.h', '.hpp', '.cs', 
            '.php', '.rb', '.go', '.rs', '.sh', '.bash', '.ps1', '.bat', '.kt', '.scala', '.swift',
            # Styling
            '.css', '.scss', '.sass', '.less',
            # Data & Configuration
            '.csv', '.yml', '.yaml', '.toml', '.ini', '.cfg', '.conf', '.config', '.env', '.sql',
            # Documentation
            '.txt', '.md', '.rst',
            # Office Documents
            '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.rtf',
            # Databases
            '.db', '.sqlite',
            # Other
            '.log', '.edcx', '.vue', '.svelte', '.properties'
        }
        # Farben für verschiedene Betriebssysteme
        self.colors = self._init_colors()
        
        # Performance-Einstellungen
        self.max_workers = self._get_optimal_worker_count()
        self.chunk_size = 100  # Anzahl Dateien pro Worker-Batch
        self.max_file_size = 50 * 1024 * 1024  # 50MB
        self.use_multiprocessing = True  # Für CPU-intensive Aufgaben
        self.use_threading = True  # Für I/O-intensive Aufgaben
        
        # Thread-sichere Komponenten
        self.results_lock = threading.Lock()
        self.progress_lock = threading.Lock()
        self.current_progress = {'files': 0, 'processed': 0, 'matches': 0}
        
        # Stop-Flag für schnelle Unterbrechung
        self.stop_requested = False
        
        # Real-time status callback
        self.status_callback = None  # Callback-Funktion für GUI-Updates
    
    def _get_optimal_worker_count(self):
        """Ermittelt die optimale Anzahl von Worker-Threads/Prozessen."""
        try:
            # Anzahl CPU-Kerne
            cpu_count = mp.cpu_count()
            
            # Wenn psutil verfügbar ist, berücksichtige auch verfügbaren RAM
            if PSUTIL_AVAILABLE:
                # Verfügbarer RAM in GB
                available_ram = psutil.virtual_memory().available / (1024**3)
                # Begrenze Worker basierend auf verfügbarem RAM (ca. 500MB pro Worker)
                max_workers_by_ram = max(1, int(available_ram / 0.5))
                optimal_workers = min(cpu_count * 2, max_workers_by_ram, 16)  # Max 16 Worker
            else:
                # Konservative Einstellung ohne RAM-Information
                optimal_workers = min(cpu_count * 2, 8)
            
            return max(1, optimal_workers)
        except:
            return 4  # Fallback
    
    def _init_colors(self):
        """Initialisiert Farben basierend auf dem Betriebssystem."""
        if COLORAMA_AVAILABLE:
            return {
                'header': Fore.CYAN + Style.BRIGHT,
                'success': Fore.GREEN + Style.BRIGHT,
                'error': Fore.RED + Style.BRIGHT,
                'warning': Fore.YELLOW + Style.BRIGHT,
                'info': Fore.BLUE + Style.BRIGHT,
                'highlight': Fore.MAGENTA + Style.BRIGHT,
                'path': Fore.WHITE + Style.DIM,
                'number': Fore.CYAN + Style.BRIGHT,
                'reset': Style.RESET_ALL
            }
        else:
            # Fallback ohne Farben aber mit Emojis
            return {key: '' for key in ['header', 'success', 'error', 'warning', 
                                      'info', 'highlight', 'path', 'number', 'reset']}
    
    def print_colored(self, text, color_key='info', emoji=''):
        """Druckt Text mit Farben und Emojis (nur wenn verbose=True)."""
        if not self.verbose:
            return
        color = self.colors.get(color_key, '')
        reset = self.colors.get('reset', '')
        print(f"{color}{emoji} {text}{reset}")
    
    def print_separator(self, char='═', length=80, color_key='header'):
        """Druckt eine farbige Trennlinie."""
        color = self.colors.get(color_key, '')
        reset = self.colors.get('reset', '')
        print(f"{color}{char * length}{reset}")
    
    def print_progress_bar(self, current, total, length=50, emoji='🔍'):
        """Zeigt eine Fortschrittsbalken an."""
        if total == 0:
            return
        
        percent = (current / total) * 100
        filled = int((current / total) * length)
        bar = '█' * filled + '░' * (length - filled)
        
        color = self.colors.get('info', '')
        reset = self.colors.get('reset', '')
        
        print(f"\r{color}{emoji} Fortschritt: [{bar}] {percent:.1f}% ({current}/{total}){reset}", end='', flush=True)
    
    def send_status_update(self, status_data):
        """Sendet Real-Time Status-Updates an GUI-Callback (thread-safe)."""
        if self.status_callback and callable(self.status_callback):
            try:
                self.status_callback(status_data)
            except Exception as e:
                if self.verbose:
                    print(f"Fehler beim Status-Callback: {e}")
    
    def get_user_input(self):
        """Fragt den Benutzer nach Suchbegriffen und Pfad."""
        # Header mit Stil
        self.print_separator('═', 80, 'header')
        self.print_colored('MASTER SEARCH - PREMIUM EDITION', 'header', '🔍')
        self.print_separator('═', 80, 'header')
        self.print_colored('Professionelle Multi-Term Dateisuche mit erweiterten Funktionen', 'info', '⭐')
        self.print_colored(f'Author: {AUTHOR} | Email: {EMAIL} | Version {VERSION}', 'path', '👨‍💻')
        print()
        
        # Suchbegriffe eingeben
        self.print_colored('MULTI-SEARCH KONFIGURATION', 'header', '🎯')
        print()
        
        while True:
            self.print_colored('SUCHBEGRIFFE EINGEBEN', 'warning', '📝')
            self.print_colored('Eingabe-Optionen:', 'info', 'ℹ️')
            self.print_colored('• Einzelner Begriff: "config"', 'path', '  ')
            self.print_colored('• Mehrere Begriffe: "config, settings, database"', 'path', '  ')
            self.print_colored('• Mit Anführungszeichen: "error message", warning', 'path', '  ')
            print()
            
            search_input = input(f"{self.colors.get('highlight', '')}🔎 Suchbegriffe eingeben: {self.colors.get('reset', '')}").strip()
            
            if search_input:
                # Parse Suchbegriffe
                self.search_terms = self.parse_search_terms(search_input)
                if self.search_terms:
                    self.print_colored(f'Suchbegriffe erkannt: {len(self.search_terms)} Begriffe', 'success', '✅')
                    for i, term in enumerate(self.search_terms, 1):
                        self.print_colored(f'  {i}. "{term}"', 'path', '🔸')
                    break
                else:
                    self.print_colored('Fehler: Keine gültigen Suchbegriffe gefunden!', 'error', '❌')
            else:
                self.print_colored('Fehler: Bitte geben Sie mindestens einen Suchbegriff ein!', 'error', '❌')
        
        print()
        
        # Suchmodus konfigurieren (falls mehrere Begriffe)
        if len(self.search_terms) > 1:
            self.print_colored('SUCHMODUS WÄHLEN', 'warning', '⚙️')
            self.print_colored('1. ANY (OR) - Findet Dateien mit EINEM der Begriffe', 'info', '🔍')
            self.print_colored('2. ALL (AND) - Findet Dateien mit ALLEN Begriffen', 'info', '🎯')
            
            while True:
                mode_input = input(f"{self.colors.get('highlight', '')}Modus wählen (1 für ANY, 2 für ALL) [1]: {self.colors.get('reset', '')}").strip()
                
                if mode_input == "" or mode_input == "1":
                    self.search_mode = "any"
                    self.print_colored('Modus gesetzt: ANY (OR) - Findet Dateien mit einem beliebigen Begriff', 'success', '✅')
                    break
                elif mode_input == "2":
                    self.search_mode = "all"
                    self.print_colored('Modus gesetzt: ALL (AND) - Findet Dateien mit allen Begriffen', 'success', '✅')
                    break
                else:
                    self.print_colored('Ungültige Eingabe! Bitte 1 oder 2 wählen.', 'error', '❌')
        else:
            self.search_mode = "any"  # Bei einem Begriff ist der Modus irrelevant
        
        print()
        
        # Erweiterte Optionen
        self.print_colored('ERWEITERTE OPTIONEN', 'warning', '⚙️')
        
        # Case Sensitivity
        case_input = input(f"{self.colors.get('highlight', '')}Groß-/Kleinschreibung beachten? (j/N) [N]: {self.colors.get('reset', '')}").strip().lower()
        self.case_sensitive = case_input in ['j', 'ja', 'y', 'yes']
        status = "aktiviert" if self.case_sensitive else "deaktiviert"
        self.print_colored(f'Groß-/Kleinschreibung: {status}', 'success', '✅')
        
        # Regex Option
        regex_input = input(f"{self.colors.get('highlight', '')}Regex-Suche verwenden? (j/N) [N]: {self.colors.get('reset', '')}").strip().lower()
        self.use_regex = regex_input in ['j', 'ja', 'y', 'yes']
        status = "aktiviert" if self.use_regex else "deaktiviert"
        self.print_colored(f'Regex-Suche: {status}', 'success', '✅')
        
        print()
        
        # Pfad eingeben
        while True:
            self.print_colored('PFAD-EINGABE', 'warning', '📁')
            self.search_path = input(f"{self.colors.get('highlight', '')}📂 Geben Sie den Suchpfad ein: {self.colors.get('reset', '')}").strip()
            if os.path.exists(self.search_path):
                self.print_colored(f'Suchpfad gefunden: "{self.search_path}"', 'success', '✅')
                break
            self.print_colored('Fehler: Der angegebene Pfad existiert nicht!', 'error', '❌')
            self.print_colored('Bitte geben Sie einen gültigen Pfad ein.', 'warning', '⚠️')
        
        print()
        self.print_separator('─', 80, 'info')
        self.print_colored('SUCHE WIRD GESTARTET', 'header', '🚀')
        
        # Formatiere Suchbegriffe für Anzeige
        terms_display = ", ".join([f'"{term}"' for term in self.search_terms])
        self.print_colored(f'Suchbegriffe: {terms_display}', 'highlight', '🎯')
        self.print_colored(f'Suchmodus: {self.search_mode.upper()}', 'highlight', '⚙️')
        self.print_colored(f'Suchbereich: "{self.search_path}"', 'path', '🗂️')
        if self.case_sensitive:
            self.print_colored('Groß-/Kleinschreibung wird beachtet', 'warning', '🔤')
        if self.use_regex:
            self.print_colored('Regex-Modus aktiviert', 'warning', '📝')
        self.print_separator('─', 80, 'info')
        time.sleep(1)  # Kurze Pause für bessere Benutzererfahrung
    
    def parse_search_terms(self, input_string):
        """Parst die Eingabe und extrahiert Suchbegriffe."""
        terms = []
        
        # Regex für quoted strings und normale Begriffe
        import re
        pattern = r'"([^"]+)"|([^,]+)'
        matches = re.findall(pattern, input_string)
        
        for quoted, unquoted in matches:
            term = quoted if quoted else unquoted
            term = term.strip()
            if term:
                terms.append(term)
        
        return terms
    
    def is_text_file(self, file_path):
        """Prüft, ob eine Datei als Textdatei behandelt werden kann."""
        # Prüfe Dateierweiterung
        extension = Path(file_path).suffix.lower()
        if extension in self.supported_text_extensions:
            return True
        
        # Prüfe MIME-Type
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type and mime_type.startswith('text/'):
            return True
        
        # Prüfe, ob Datei ohne Erweiterung Text enthält (erste 1024 Bytes)
        if not extension:
            try:
                with open(file_path, 'rb') as f:
                    chunk = f.read(1024)
                    if chunk:
                        # Prüfe auf NULL-Bytes (typisch für Binärdateien)
                        if b'\x00' in chunk:
                            return False
                        # Versuche als UTF-8 zu dekodieren
                        try:
                            chunk.decode('utf-8')
                            return True
                        except UnicodeDecodeError:
                            try:
                                chunk.decode('latin-1')
                                return True
                            except UnicodeDecodeError:
                                return False
            except:
                return False
        
        return False
    
    def match_text(self, text, search_terms, mode="any", case_sensitive=False, use_regex=False):
        """Prüft ob Text den Suchkriterien entspricht."""
        if not search_terms:
            return False
        
        # Text für Vergleich vorbereiten
        compare_text = text if case_sensitive else text.lower()
        
        matches = []
        
        for term in search_terms:
            compare_term = term if case_sensitive else term.lower()
            
            if use_regex:
                try:
                    import re
                    flags = 0 if case_sensitive else re.IGNORECASE
                    pattern = re.compile(compare_term, flags)
                    match = pattern.search(text)
                    matches.append(match is not None)
                except re.error:
                    # Fallback bei ungültiger Regex
                    matches.append(compare_term in compare_text)
            else:
                matches.append(compare_term in compare_text)
        
        # Rückgabe basierend auf Modus
        if mode == "all":
            return all(matches)  # Alle Begriffe müssen gefunden werden
        else:  # mode == "any"
            return any(matches)  # Mindestens ein Begriff muss gefunden werden
    
    def get_matching_terms(self, text, search_terms, case_sensitive=False, use_regex=False):
        """Gibt alle gefundenen Suchbegriffe in einem Text zurück."""
        found_terms = []
        compare_text = text if case_sensitive else text.lower()
        
        for term in search_terms:
            compare_term = term if case_sensitive else term.lower()
            
            if use_regex:
                try:
                    import re
                    flags = 0 if case_sensitive else re.IGNORECASE
                    pattern = re.compile(compare_term, flags)
                    if pattern.search(text):
                        found_terms.append(term)
                except re.error:
                    if compare_term in compare_text:
                        found_terms.append(term)
            else:
                if compare_term in compare_text:
                    found_terms.append(term)
        
        return found_terms

    def extract_text_from_docx(self, file_path):
        """Extrahiert Text aus DOCX Dateien mit Zeilennummern."""
        lines = []
        try:
            from zipfile import ZipFile
            from xml.etree import ElementTree as ET
            
            with ZipFile(file_path, 'r') as zip_ref:
                xml_content = zip_ref.read('word/document.xml')
                root = ET.fromstring(xml_content)
                
                # Namespace für Word
                ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
                
                # Sammle Absätze (Paragraphen = Zeilen)
                for para_idx, paragraph in enumerate(root.findall('.//w:p', ns), 1):
                    text_parts = []
                    for text_elem in paragraph.findall('.//w:t', ns):
                        if text_elem.text:
                            text_parts.append(text_elem.text)
                    
                    if text_parts:
                        line_text = ''.join(text_parts).strip()
                        if line_text:
                            lines.append((para_idx, line_text))
        except Exception as e:
            pass  # DOCX-Extraktion fehlgeschlagen, wird als Binärdatei behandelt
        
        return lines
    
    def extract_text_from_pdf(self, file_path):
        """Extrahiert Text aus PDF Dateien mit Zeilennummern."""
        lines = []
        try:
            import PyPDF2
            
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                line_counter = 0
                
                for page_num, page in enumerate(reader.pages, 1):
                    text = page.extract_text()
                    for line in text.split('\n'):
                        line = line.strip()
                        if line:
                            line_counter += 1
                            lines.append((line_counter, line))
        except ImportError:
            pass  # PyPDF2 nicht installiert
        except Exception as e:
            pass  # PDF-Extraktion fehlgeschlagen
        
        return lines
    
    def extract_text_from_xlsx(self, file_path):
        """Extrahiert Text aus XLSX Dateien mit Zeilennummern."""
        lines = []
        try:
            from zipfile import ZipFile
            from xml.etree import ElementTree as ET
            
            with ZipFile(file_path, 'r') as zip_ref:
                xml_content = zip_ref.read('xl/worksheets/sheet1.xml')
                root = ET.fromstring(xml_content)
                
                # Namespace für Excel
                ns = {'': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
                
                # Sammle Zeilen
                for row_idx, row in enumerate(root.findall('.//{}row', ns), 1):
                    cells = []
                    for cell in row.findall('.//{}v', ns):
                        if cell.text:
                            cells.append(cell.text)
                    
                    if cells:
                        line_text = ' | '.join(cells).strip()
                        if line_text:
                            lines.append((row_idx, line_text))
        except Exception as e:
            pass  # XLSX-Extraktion fehlgeschlagen
        
        return lines
    
    def extract_text_from_csv(self, file_path):
        """Extrahiert Text aus CSV Dateien mit Zeilennummern."""
        lines = []
        try:
            import csv
            
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as csvfile:
                        reader = csv.reader(csvfile)
                        for row_num, row in enumerate(reader, 1):
                            line_text = ' | '.join([cell.strip() for cell in row if cell.strip()])
                            if line_text:
                                lines.append((row_num, line_text))
                    return lines
                except (UnicodeDecodeError, UnicodeError):
                    continue
        except Exception as e:
            pass  # CSV-Extraktion fehlgeschlagen
        
        return lines
    
    def extract_text_from_pptx(self, file_path):
        """Extrahiert Text aus PPTX (PowerPoint) Dateien mit Zeilennummern."""
        lines = []
        try:
            from zipfile import ZipFile
            from xml.etree import ElementTree as ET
            
            with ZipFile(file_path, 'r') as zip_ref:
                # Durchsuche alle Slides
                slide_files = [f for f in zip_ref.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
                line_counter = 0
                
                for slide_file in sorted(slide_files):
                    xml_content = zip_ref.read(slide_file)
                    root = ET.fromstring(xml_content)
                    
                    # Namespace für PowerPoint
                    ns = {
                        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
                        'p': 'http://schemas.openxmlformats.org/presentationml/2006/main'
                    }
                    
                    # Sammle Text-Elemente
                    for t_elem in root.findall('.//a:t', ns):
                        if t_elem.text and t_elem.text.strip():
                            line_counter += 1
                            lines.append((line_counter, t_elem.text.strip()))
        except Exception as e:
            pass  # PPTX-Extraktion fehlgeschlagen
        
        return lines
    
    def extract_text_from_odt(self, file_path):
        """Extrahiert Text aus ODT (OpenDocument) Dateien mit Zeilennummern."""
        lines = []
        try:
            from zipfile import ZipFile
            from xml.etree import ElementTree as ET
            
            with ZipFile(file_path, 'r') as zip_ref:
                xml_content = zip_ref.read('content.xml')
                root = ET.fromstring(xml_content)
                
                # Namespace für ODF
                ns = {
                    'text': 'urn:oasis:names:tc:opendocument:xmlns:text:1.0',
                    'office': 'urn:oasis:names:tc:opendocument:xmlns:office:1.0'
                }
                
                # Sammle Absätze
                line_counter = 0
                for paragraph in root.findall('.//text:p', ns):
                    text_parts = []
                    for text_elem in paragraph.findall('.//text:span', ns):
                        if text_elem.text:
                            text_parts.append(text_elem.text)
                    
                    if text_parts:
                        line_counter += 1
                        line_text = ''.join(text_parts).strip()
                        if line_text:
                            lines.append((line_counter, line_text))
        except Exception as e:
            pass  # ODT-Extraktion fehlgeschlagen
        
        return lines
    
    def extract_text_from_rtf(self, file_path):
        """Extrahiert Text aus RTF (Rich Text Format) Dateien mit Zeilennummern."""
        lines = []
        try:
            import re
            
            with open(file_path, 'r', encoding='latin-1', errors='ignore') as f:
                content = f.read()
            
            # Einfaches RTF-Parsing: entferne RTF-Befehle
            # Entferne RTF-Header und Steuerzeichen
            content = re.sub(r'\\[a-z]+\d*\s?', ' ', content)
            content = re.sub(r'[{}]', '', content)
            content = re.sub(r'\\\?', '', content)
            
            # Teile in Zeilen
            line_counter = 0
            for line in content.split('\n'):
                line = line.strip()
                if line and len(line) > 2:  # Ignoriere sehr kurze Zeilen
                    line_counter += 1
                    lines.append((line_counter, line))
        except Exception as e:
            pass  # RTF-Extraktion fehlgeschlagen
        
        return lines
    
    def extract_text_from_doc(self, file_path):
        """Extrahiert Text aus DOC (alte Word) Dateien mit Zeilennummern."""
        lines = []
        try:
            # Versuche python-docx für moderne .doc-Dateien
            from docx import Document
            
            doc = Document(file_path)
            line_counter = 0
            
            for paragraph in doc.paragraphs:
                if paragraph.text.strip():
                    line_counter += 1
                    lines.append((line_counter, paragraph.text.strip()))
        except ImportError:
            # Fallback: Versuche text-Extraktion mit Regex
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                    # Einfacher Text-Extraktion aus Binärdatei
                    text = ''.join(chr(b) if 32 <= b < 127 else ' ' for b in content)
                    line_counter = 0
                    for line in text.split('\n'):
                        line = line.strip()
                        if line and len(line) > 5:  # Mindest-Länge
                            line_counter += 1
                            lines.append((line_counter, line))
            except Exception:
                pass
        except Exception as e:
            pass  # DOC-Extraktion fehlgeschlagen
        
        return lines
    
    def extract_text_from_log(self, file_path):
        """Extrahiert Text aus LOG Dateien mit Zeilennummern (Alias für Textdatei)."""
        lines = []
        try:
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        for line_num, line in enumerate(f, 1):
                            line_content = line.rstrip('\n')  # Behalte Einrückung
                            if line_content.strip():
                                lines.append((line_num, line_content.strip()))
                    return lines
                except (UnicodeDecodeError, UnicodeError):
                    continue
        except Exception as e:
            pass
        
        return lines

    def search_in_file(self, file_path):
        """Durchsucht eine Datei nach den Suchbegriffen mit Zeilennummern."""
        matches = []
        file_ext = os.path.splitext(file_path)[1].lower()
        
        # Wähle Extraktor basierend auf Dateityp
        lines_to_search = []
        
        if file_ext == '.docx':
            lines_to_search = self.extract_text_from_docx(file_path)
        elif file_ext == '.doc':
            lines_to_search = self.extract_text_from_doc(file_path)
        elif file_ext == '.pdf':
            lines_to_search = self.extract_text_from_pdf(file_path)
        elif file_ext in ['.xlsx', '.xls']:
            lines_to_search = self.extract_text_from_xlsx(file_path)
        elif file_ext == '.pptx':
            lines_to_search = self.extract_text_from_pptx(file_path)
        elif file_ext in ['.odt', '.ods']:
            lines_to_search = self.extract_text_from_odt(file_path)
        elif file_ext == '.rtf':
            lines_to_search = self.extract_text_from_rtf(file_path)
        elif file_ext == '.csv':
            lines_to_search = self.extract_text_from_csv(file_path)
        elif file_ext == '.log':
            lines_to_search = self.extract_text_from_log(file_path)
        else:
            # Standard-Textdatei Behandlung
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        for line_num, line in enumerate(f, 1):
                            line_content = line.strip()
                            if line_content:
                                lines_to_search.append((line_num, line_content))
                    break  # Erfolgreich gelesen
                except (UnicodeDecodeError, UnicodeError):
                    continue
                except Exception as e:
                    break
        
        # Durchsuche alle extrahierten Zeilen
        for line_num, line_content in lines_to_search:
            if self.match_text(line_content, self.search_terms, 
                             self.search_mode, self.case_sensitive, self.use_regex):
                
                # Finde alle passenden Begriffe für Hervorhebung
                found_terms = self.get_matching_terms(line_content, self.search_terms,
                                                     self.case_sensitive, self.use_regex)
                
                matches.append({
                    'line_number': line_num,
                    'line_content': line_content,
                    'found_terms': found_terms
                })
        
        return matches
    
    def process_file_batch(self, file_batch):
        """Verarbeitet einen Batch von Dateien - für Multiprocessing optimiert."""
        batch_results = []
        
        for file_info in file_batch:
            file_path, file_name = file_info
            
            try:
                # Überspringe sehr große Dateien
                file_size = os.path.getsize(file_path)
                if file_size > self.max_file_size:
                    continue
                
                matches = []
                
                # Prüfe Dateiname mit Multi-Term-Unterstützung
                if self.match_text(file_name, self.search_terms, self.search_mode, 
                                 self.case_sensitive, self.use_regex):
                    found_terms = self.get_matching_terms(file_name, self.search_terms,
                                                        self.case_sensitive, self.use_regex)
                    terms_text = ", ".join(found_terms)
                    matches.append({
                        'line_number': 0, 
                        'line_content': f'📄 Dateiname enthält: {terms_text}',
                        'found_terms': found_terms
                    })
                
                # Prüfe Dateiinhalt (nur bei Textdateien)
                if self.is_text_file(file_path):
                    content_matches = self.search_in_file(file_path)
                    matches.extend(content_matches)
                
                # Wenn Treffer gefunden, zu Batch-Ergebnissen hinzufügen
                if matches:
                    batch_results.append({
                        'type': 'file',
                        'path': file_path,
                        'name': file_name,
                        'matches': matches
                    })
                    
            except Exception as e:
                continue  # Ignoriere fehlerhafte Dateien
        
        return batch_results
    
    def update_progress(self, processed_files, total_files, matches_found):
        """Thread-sichere Fortschritts-Updates."""
        with self.progress_lock:
            self.current_progress['files'] = total_files
            self.current_progress['processed'] = processed_files
            self.current_progress['matches'] = matches_found
            
            if processed_files % 50 == 0 or processed_files == total_files:
                self.print_progress_bar(processed_files, total_files, emoji='⚡')
                
                # Real-time Status-Update an GUI senden
                self.send_status_update({
                    'type': 'progress',
                    'processed': processed_files,
                    'total': total_files,
                    'matches': matches_found,
                    'percent': round((processed_files / total_files * 100) if total_files > 0 else 0, 1)
                })
                
                if processed_files % 200 == 0:
                    print(f"\n{self.colors.get('info', '')}📈 Aktueller Stand:{self.colors.get('reset', '')}")
                    self.print_colored(f'Verarbeitet: {processed_files}/{total_files} Dateien', 'number', '📊')
                    self.print_colored(f'Treffer gefunden: {matches_found}', 'success', '🎯')
                    print()
    
    def search_files_and_folders(self):
        """Durchsucht alle Dateien und Ordner nach dem Suchwort - Optimierte Version."""
        start_time = time.time()
        
        self.print_colored('HOCHPERFORMANCE-DURCHSUCHUNG GESTARTET', 'header', '🚀')
        self.print_colored(f'Verwende {self.max_workers} Worker-Threads/Prozesse', 'info', '⚡')
        if PSUTIL_AVAILABLE:
            ram_gb = psutil.virtual_memory().total / (1024**3)
            self.print_colored(f'System: {mp.cpu_count()} CPU-Kerne, {ram_gb:.1f}GB RAM', 'info', '�')
        self.print_colored('Sammle Dateien...', 'info', '📊')
        print()
        
        # Schritt 1: Sammle alle Dateien und Ordner (schnell, single-threaded)
        all_files = []
        all_folders = []
        
        for root, dirs, files in os.walk(self.search_path):
            # Sammle Ordner mit Multi-Term-Unterstützung
            for dir_name in dirs:
                if self.match_text(dir_name, self.search_terms, self.search_mode, 
                                 self.case_sensitive, self.use_regex):
                    dir_path = os.path.join(root, dir_name)
                    found_terms = self.get_matching_terms(dir_name, self.search_terms,
                                                        self.case_sensitive, self.use_regex)
                    terms_text = ", ".join(found_terms)
                    all_folders.append({
                        'type': 'folder',
                        'path': dir_path,
                        'name': dir_name,
                        'matches': [{
                            'line_number': 0, 
                            'line_content': f'📁 Ordnername enthält: {terms_text}',
                            'found_terms': found_terms
                        }]
                    })
            
            # Sammle Dateien mit Pfad-Info
            for file_name in files:
                file_path = os.path.join(root, file_name)
                all_files.append((file_path, file_name))
        
        total_files = len(all_files)
        folders_found = len(all_folders)
        
        self.print_colored(f'Gefunden: {total_files:,} Dateien, {len(all_folders)} passende Ordner', 'success', '📁')
        
        # Füge Ordner-Treffer zu Ergebnissen hinzu
        with self.results_lock:
            self.results.extend(all_folders)
        
        if total_files == 0:
            self.print_colored('Keine Dateien zu verarbeiten', 'warning', '⚠️')
            return
        
        # Schritt 2: Verarbeite Dateien parallel
        self.print_colored('Starte parallele Dateiverarbeitung...', 'header', '🔥')
        
        # Teile Dateien in Batches auf
        file_batches = [
            all_files[i:i + self.chunk_size] 
            for i in range(0, len(all_files), self.chunk_size)
        ]
        
        processed_files = 0
        file_results = []
        
        # Verwende ProcessPoolExecutor für CPU-intensive Aufgaben
        if self.use_multiprocessing and len(file_batches) > 1:
            self.print_colored(f'Multiprocessing: {len(file_batches)} Batches mit je ~{self.chunk_size} Dateien', 'info', '🔄')
            
            try:
                with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
                    # Erstelle Worker-Prozesse
                    future_to_batch = {
                        executor.submit(self.process_file_batch_static, batch, self.search_terms, 
                                      self.search_mode, self.case_sensitive, self.use_regex,
                                      self.supported_text_extensions, self.max_file_size): batch
                        for batch in file_batches
                    }
                    
                    # Sammle Ergebnisse
                    for future in as_completed(future_to_batch):
                        try:
                            batch_results = future.result()
                            file_results.extend(batch_results)
                            processed_files += len(future_to_batch[future])
                            
                            self.update_progress(processed_files, total_files, len(file_results))
                            
                        except Exception as e:
                            self.print_colored(f'Batch-Fehler: {str(e)}', 'error', '❌')
                            
            except Exception as e:
                self.print_colored(f'Multiprocessing fehlgeschlagen: {str(e)}', 'error', '❌')
                self.print_colored('Fallback zu Threading...', 'warning', '🔄')
                self.use_multiprocessing = False
        
        # Fallback zu Threading falls Multiprocessing fehlschlägt
        if not self.use_multiprocessing or len(file_batches) == 1:
            self.print_colored(f'Threading: {min(self.max_workers, len(file_batches))} Threads', 'info', '🧵')
            
            with ThreadPoolExecutor(max_workers=min(self.max_workers, len(file_batches))) as executor:
                future_to_batch = {
                    executor.submit(self.process_file_batch, batch): batch
                    for batch in file_batches
                }
                
                for future in as_completed(future_to_batch):
                    try:
                        batch_results = future.result()
                        file_results.extend(batch_results)
                        processed_files += len(future_to_batch[future])
                        
                        self.update_progress(processed_files, total_files, len(file_results))
                        
                    except Exception as e:
                        self.print_colored(f'Thread-Fehler: {str(e)}', 'error', '❌')
        
        # Füge Datei-Ergebnisse zu Hauptergebnissen hinzu
        with self.results_lock:
            self.results.extend(file_results)
        
        # Abschluss-Statistiken
        elapsed_time = time.time() - start_time
        files_found = len(file_results)
        
        print(f"\n{self.colors.get('reset', '')}")
        self.print_separator('═', 80, 'success')
        self.print_colored('HOCHPERFORMANCE-SUCHE ABGESCHLOSSEN', 'success', '�')
        self.print_separator('═', 80, 'success')
        
        # Detaillierte Performance-Statistiken
        print()
        self.print_colored('PERFORMANCE-ANALYSE:', 'header', '📊')
        self.print_colored(f'Gesamt durchsucht: {total_files:,} Dateien', 'number', '📁')
        self.print_colored(f'Ordner-Treffer: {folders_found}', 'success', '📁')
        self.print_colored(f'Datei-Treffer: {files_found}', 'success', '📄')
        self.print_colored(f'Gesamt-Treffer: {len(self.results)}', 'highlight', '🎯')
        self.print_colored(f'Verarbeitungszeit: {elapsed_time:.2f} Sekunden', 'info', '⏱️')
        
        if elapsed_time > 0:
            files_per_sec = total_files / elapsed_time
            self.print_colored(f'Geschwindigkeit: {files_per_sec:.0f} Dateien/Sekunde', 'info', '⚡')
            
        self.print_colored(f'Worker verwendet: {self.max_workers} ({mp.cpu_count()} CPU-Kerne)', 'info', '🔧')
        
        if PSUTIL_AVAILABLE:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_percent = psutil.virtual_memory().percent
            self.print_colored(f'System-Auslastung: CPU {cpu_percent:.1f}%, RAM {memory_percent:.1f}%', 'info', '💻')
        
        # Sende finale Status-Update an GUI
        self.send_status_update({
            'type': 'complete',
            'total': total_files,
            'matches': len(self.results),
            'elapsed_time': elapsed_time,
            'speed': (total_files / elapsed_time) if elapsed_time > 0 else 0
        })
        
        print()
    
    @staticmethod
    def process_file_batch_static(file_batch, search_terms, search_mode, case_sensitive, use_regex, supported_extensions, max_file_size):
        """Statische Methode für Multiprocessing - Multi-Term-Version."""
        batch_results = []
        
        def match_text_static(text, search_terms, mode, case_sensitive, use_regex):
            """Statische Version der match_text Methode."""
            if not search_terms:
                return False
            
            compare_text = text if case_sensitive else text.lower()
            matches = []
            
            for term in search_terms:
                compare_term = term if case_sensitive else term.lower()
                
                if use_regex:
                    try:
                        import re
                        flags = 0 if case_sensitive else re.IGNORECASE
                        pattern = re.compile(compare_term, flags)
                        match = pattern.search(text)
                        matches.append(match is not None)
                    except re.error:
                        matches.append(compare_term in compare_text)
                else:
                    matches.append(compare_term in compare_text)
            
            if mode == "all":
                return all(matches)
            else:  # mode == "any"
                return any(matches)
        
        def get_matching_terms_static(text, search_terms, case_sensitive, use_regex):
            """Statische Version der get_matching_terms Methode."""
            found_terms = []
            compare_text = text if case_sensitive else text.lower()
            
            for term in search_terms:
                compare_term = term if case_sensitive else term.lower()
                
                if use_regex:
                    try:
                        import re
                        flags = 0 if case_sensitive else re.IGNORECASE
                        pattern = re.compile(compare_term, flags)
                        if pattern.search(text):
                            found_terms.append(term)
                    except re.error:
                        if compare_term in compare_text:
                            found_terms.append(term)
                else:
                    if compare_term in compare_text:
                        found_terms.append(term)
            
            return found_terms
        
        def is_text_file_static(file_path):
            """Statische Version der is_text_file Methode."""
            extension = Path(file_path).suffix.lower()
            if extension in supported_extensions:
                return True
            
            import mimetypes
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type and mime_type.startswith('text/'):
                return True
            
            if not extension:
                try:
                    with open(file_path, 'rb') as f:
                        chunk = f.read(1024)
                        if chunk and b'\x00' not in chunk:
                            try:
                                chunk.decode('utf-8')
                                return True
                            except UnicodeDecodeError:
                                try:
                                    chunk.decode('latin-1')
                                    return True
                                except UnicodeDecodeError:
                                    return False
                except:
                    return False
            return False
        
        def search_in_file_static(file_path, search_terms, search_mode, case_sensitive, use_regex):
            """Statische Multi-Term-Version der search_in_file Methode."""
            matches = []
            encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
            
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as f:
                        for line_num, line in enumerate(f, 1):
                            line_content = line.strip()
                            
                            if match_text_static(line_content, search_terms, search_mode, case_sensitive, use_regex):
                                found_terms = get_matching_terms_static(line_content, search_terms, case_sensitive, use_regex)
                                matches.append({
                                    'line_number': line_num,
                                    'line_content': line_content,
                                    'found_terms': found_terms
                                })
                    break
                except (UnicodeDecodeError, UnicodeError):
                    continue
                except Exception:
                    break
            
            return matches
        
        for file_info in file_batch:
            file_path, file_name = file_info
            
            try:
                # Überspringe sehr große Dateien
                file_size = os.path.getsize(file_path)
                if file_size > max_file_size:
                    continue
                
                matches = []
                
                # Prüfe Dateiname mit Multi-Term-Unterstützung
                if match_text_static(file_name, search_terms, search_mode, case_sensitive, use_regex):
                    found_terms = get_matching_terms_static(file_name, search_terms, case_sensitive, use_regex)
                    terms_text = ", ".join(found_terms)
                    matches.append({
                        'line_number': 0, 
                        'line_content': f'📄 Dateiname enthält: {terms_text}',
                        'found_terms': found_terms
                    })
                
                # Prüfe Dateiinhalt (nur bei Textdateien)
                if is_text_file_static(file_path):
                    content_matches = search_in_file_static(file_path, search_terms, search_mode, case_sensitive, use_regex)
                    matches.extend(content_matches)
                
                # Wenn Treffer gefunden, zu Batch-Ergebnissen hinzufügen
                if matches:
                    batch_results.append({
                        'type': 'file',
                        'path': file_path,
                        'name': file_name,
                        'matches': matches
                    })
                    
            except Exception:
                continue  # Ignoriere fehlerhafte Dateien
        
        return batch_results
    
    def generate_html_report(self):
        """Erstellt eine HTML-Datei mit den Suchergebnissen."""
        try:
            self.print_colored('HTML-BERICHT WIRD ERSTELLT', 'header', '📄')
            self.print_colored('Generiere HTML-Struktur...', 'info', '🏗️')
            time.sleep(0.5)
            
            # Use the standalone report generator
            generator = HTMLReportGenerator(
                search_terms=self.search_terms,
                search_path=self.search_path,
                case_sensitive=self.case_sensitive,
                use_regex=self.use_regex,
                output_dir=str(DEFAULT_REPORT_DIR)
            )
            
            html_file = generator.generate(self.results, auto_open=False)
            
            if html_file:
                file_size = os.path.getsize(html_file) / 1024  # KB
                
                self.print_separator('─', 80, 'success')
                self.print_colored('HTML-BERICHT ERFOLGREICH ERSTELLT', 'success', '✅')
                self.print_separator('─', 80, 'success')
                self.print_colored(f'Datei: {os.path.basename(html_file)}', 'highlight', '📄')
                self.print_colored(f'Pfad: {os.path.abspath(html_file)}', 'path', '📁')
                self.print_colored(f'Größe: {file_size:.1f} KB', 'number', '💾')
                self.print_colored(f'Inhalt: {len(self.results)} Suchergebnisse', 'number', '📊')
                
                return html_file
            else:
                self.print_colored('Fehler beim Erstellen der HTML-Datei', 'error', '❌')
                return None
                
        except Exception as e:
            self.print_colored(f'Fehler beim Generieren des Reports: {e}', 'error', '❌')
            return None

    def run(self):
        """Führt das komplette Suchprogramm aus."""
        try:
            # Willkommensbildschirm
            print()
            self.print_separator('█', 80, 'header')
            self.print_colored('WILLKOMMEN ZU MASTER SEARCH', 'header', '🚀')
            self.print_colored('Professionelle Dateisuche mit erweiterten Funktionen', 'info', '⭐')
            self.print_colored(f'Author: {AUTHOR} | Email: {EMAIL} | Version {VERSION}', 'path', '👨‍💻')
            self.print_separator('█', 80, 'header')
            print()
            
            # Benutzereingaben
            self.get_user_input()
            
            # Suche durchführen
            self.search_files_and_folders()
            
            # HTML-Bericht erstellen
            html_file = self.generate_html_report()
            
            if html_file:
                print()
                self.print_separator('═', 80, 'success')
                self.print_colored('MISSION ERFOLGREICH ABGESCHLOSSEN', 'success', '🎉')
                self.print_separator('═', 80, 'success')
                
                # Finale Statistiken
                folders = len([r for r in self.results if r['type'] == 'folder'])
                files = len([r for r in self.results if r['type'] == 'file'])
                
                self.print_colored('FINALE ERGEBNISSE:', 'header', '🏆')
                self.print_colored(f'Gesamte Treffer: {len(self.results)}', 'highlight', '🎯')
                self.print_colored(f'Ordner gefunden: {folders}', 'success', '📁')
                self.print_colored(f'Dateien gefunden: {files}', 'success', '📄')
                self.print_colored(f'HTML-Bericht: {html_file}', 'info', '📋')
                
                # Versuche HTML-Datei zu öffnen
                try:
                    self.print_colored('Browser wird geöffnet...', 'info', '🌐')
                    if not open_file(html_file):
                        # Fallback: Try to open in browser
                        import webbrowser
                        webbrowser.open(f'file://{os.path.abspath(html_file)}')
                    time.sleep(1)
                    self.print_colored('HTML-Datei wurde im Standardbrowser geöffnet', 'success', '✅')
                except Exception as e:
                    self.print_colored('Browser konnte nicht automatisch geöffnet werden', 'warning', '⚠️')
                    self.print_colored(f'Öffnen Sie die Datei manuell: {os.path.abspath(html_file)}', 'info', 'ℹ️')
                
                print()
                self.print_colored('Vielen Dank für die Nutzung von Master Search!', 'header', '🙏')
                self.print_separator('─', 80, 'info')
            
        except KeyboardInterrupt:
            print(f"\n\n{self.colors.get('warning', '')}🛑 SUCHE WURDE VOM BENUTZER ABGEBROCHEN{self.colors.get('reset', '')}")
            self.print_colored('Das Programm wurde sicher beendet.', 'info', 'ℹ️')
        except Exception as e:
            print(f"\n{self.colors.get('error', '')}❌ UNERWARTETER FEHLER{self.colors.get('reset', '')}")
            self.print_colored(f'Fehlermeldung: {str(e)}', 'error', '🚨')
            self.print_colored('Bitte versuchen Sie es erneut oder kontaktieren Sie den Support.', 'warning', '⚠️')

def main():
    """Hauptfunktion des Programms."""
    try:
        search_tool = FileSearchTool()
        search_tool.run()
        
    except Exception as e:
        print(f"❌ Kritischer Fehler beim Starten des Programms: {e}")
        print("⚠️  Stellen Sie sicher, dass Python ordnungsgemäß installiert ist.")

if __name__ == "__main__":
    main()