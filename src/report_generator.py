#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - HTML Report Generator
======================================
Standalone module for generating professional HTML reports from search results.

Author: Loony2392
Email: info@loony-tech.de
Version: 2025.11.9 (Limited Results Display Feature)
Created: November 2025

New in v2025.11.9:
- Limited results display: Show only first 3 matches per file
- "Show more matches" button for files with >3 matches
- Toggle functionality to expand/collapse additional matches
- Improved report readability and user experience

Bug Fixes (v2025.11.8):
- Implemented context-limited display in reports (5 words before/after search term)
- Fixed UI layout overlap in GUI
- Verified category filter functionality

Features:
    - Professional HTML report generation
    - Support for file and folder results
    - Click-to-open functionality
    - Multi-term highlighting with regex support
    - Responsive design with inline CSS
    - Custom logo with SVG graphics
    - Context-aware text extraction for long lines
    - Limited results display for better overview
"""

import os
import re
import html
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional

# Add config directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'config'))

# Import version and internationalization
try:
    from version import VERSION, AUTHOR, EMAIL, COMPANY
    from platform_utils import PlatformUtils, get_temp_dir, open_file
except ImportError:
    # Fallback if imports fail
    VERSION = "2025.11.9"
    AUTHOR = "Loony2392"
    EMAIL = "info@loony-tech.de"
    COMPANY = "LOONY-TECH"
    
    # Mock platform utilities for fallback
    class MockPlatformUtils:
        @staticmethod
        def open_file(file_path):
            import webbrowser
            webbrowser.open(f'file://{os.path.abspath(file_path)}')
            return True
    
    open_file = MockPlatformUtils.open_file

# Try to import i18n, with fallback implementation
try:
    from i18n import tr, _CURRENT_LANG
    _I18N_AVAILABLE = True
except ImportError:
    _I18N_AVAILABLE = False
    _I18N_CACHE = {}
    _CURRENT_LANG = 'en'
    
    def _find_locales_dir():
        """Find locales directory - handle both normal Python and cx_Freeze."""
        try:
            # Try normal file system first
            path = Path(__file__).parent.parent / "config" / "locales"
            if path.exists():
                return path
            
            # Fallback for cx_Freeze
            if hasattr(sys, 'frozen'):
                path = Path(sys.executable).parent / "locales"
                if path.exists():
                    return path
            
            # Last resort
            return Path.cwd() / "locales"
        except Exception:
            return Path.cwd() / "locales"
    
    def _load_json_locale(lang):
        """Load locale from JSON file."""
        if lang in _I18N_CACHE:
            return _I18N_CACHE[lang]
        
        locales_dir = _find_locales_dir()
        lang_file = locales_dir / f"{lang}.json"
        
        if not lang_file.exists():
            lang_file = locales_dir / "en.json"
        
        try:
            with open(lang_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                _I18N_CACHE[lang] = data
                return data
        except Exception:
            return {}
    
    def tr(key, **kwargs):
        """Translation function - fallback implementation."""
        data = _load_json_locale(_CURRENT_LANG)
        val = data.get(key)
        
        if val is None and _CURRENT_LANG != 'en':
            data_en = _load_json_locale('en')
            val = data_en.get(key)
        
        if val is None:
            val = key
        
        try:
            return val.format(**kwargs) if kwargs else val
        except:
            return val


class HTMLReportGenerator:
    """Generates professional HTML reports from search results."""
    
    def __init__(self, search_terms: List[str], search_path: str, 
                 case_sensitive: bool = False, use_regex: bool = False,
                 output_dir: Optional[str] = None):
        """
        Initialize the report generator.
        
        Args:
            search_terms: List of search terms used
            search_path: Path that was searched
            case_sensitive: Whether search was case-sensitive
            use_regex: Whether regex was used in search
            output_dir: Directory to save reports (default: current dir)
        """
        self.search_terms = search_terms
        self.search_path = search_path
        self.case_sensitive = case_sensitive
        self.use_regex = use_regex
        self.output_dir = output_dir or Path.cwd()
        
        # Ensure output directory exists
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
    
    def generate(self, results: List[Dict[str, Any]], 
                 auto_open: bool = False) -> Optional[str]:
        """
        Generate HTML report from search results.
        
        Args:
            results: List of search result dictionaries
            auto_open: Whether to automatically open the report in browser
            
        Returns:
            Path to generated HTML file or None if error
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            html_file = Path(self.output_dir) / f"search_results_{timestamp}.html"
            
            # Generate HTML content
            html_content = self._generate_html(results)
            
            # Write to file
            html_file.write_text(html_content, encoding='utf-8')
            
            # Auto-open if requested with Windows default app for filetype
            if auto_open:
                try:
                    if not open_file(str(html_file)):
                        # Fallback to webbrowser if platform utils fail
                        import webbrowser
                        webbrowser.open(f'file://{html_file}')
                except Exception:
                    pass  # Silently fail if opening fails
            
            return str(html_file)
            
        except Exception as e:
            print(f"❌ Error generating report: {e}")
            return None
    
    def _generate_html(self, results: List[Dict[str, Any]]) -> str:
        """Generate complete HTML document."""
        search_terms_display = ", ".join(self.search_terms)
        
        # Count results by type
        file_count = len([r for r in results if r['type'] == 'file'])
        folder_count = len([r for r in results if r['type'] == 'folder'])
        total_count = len(results)
        
        # Build HTML
        html_parts = [
            self._get_html_header(search_terms_display),
            self._get_html_style(),
            '</head>',
            '<body>',
            '    <div class="container">',
            self._get_html_header_section(),
            self._get_html_search_info(search_terms_display),
            self._get_html_stats(total_count, file_count, folder_count),
        ]
        
        # Add category overview if results exist
        if results:
            html_parts.append(self._get_category_stats(results))
            html_parts.append(self._get_html_results(results))
        else:
            html_parts.append(self._get_html_no_results())
        
        # Close HTML
        html_parts.extend([
            '    </div>',
            self._get_html_scripts(),
            '</body>',
            '</html>',
        ])
        
        return '\n'.join(html_parts)
    
    def _get_html_header(self, search_terms: str) -> str:
        """Get HTML head section with title."""
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Master Search - {tr('report_title')}: "{html.escape(search_terms)}"</title>'''
    
    def _get_html_style(self) -> str:
        """Get CSS styling."""
        return '''    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }
        
        .header {
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 30px;
            border-bottom: 4px solid #007acc;
        }
        
        .header h1 {
            color: #333;
            margin: 20px 0;
            font-size: 2.8em;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
        }
        
        .logo {
            width: 56px;
            height: 56px;
            flex-shrink: 0;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
        }
        
        .logo-container {
            width: 56px;
            height: 56px;
            flex-shrink: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .logo-container svg {
            width: 56px;
            height: 56px;
            filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
        }
        
        .header p {
            color: #666;
            font-size: 1.1em;
            margin-top: 10px;
        }
        
        .search-info {
            background: linear-gradient(135deg, #e7f3ff 0%, #f0f8ff 100%);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
            border-left: 5px solid #007acc;
            box-shadow: 0 2px 8px rgba(0,122,204,0.1);
        }
        
        .search-info strong {
            color: #007acc;
            display: inline-block;
            min-width: 120px;
        }
        
        .search-info div {
            margin: 8px 0;
            word-break: break-all;
        }
        
        .stats {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        
        .stat-item {
            text-align: center;
            padding: 25px;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            border-radius: 8px;
            border-top: 4px solid #007acc;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .stat-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,122,204,0.2);
        }
        
        .stat-number {
            font-size: 2.5em;
            font-weight: bold;
            color: #007acc;
            display: block;
        }
        
        .stat-label {
            color: #666;
            margin-top: 8px;
            font-size: 0.95em;
        }
        
        .categories {
            background: linear-gradient(135deg, #fff9e6 0%, #ffe6cc 100%);
            padding: 25px;
            border-radius: 8px;
            margin-bottom: 40px;
            border-left: 5px solid #ff9800;
            box-shadow: 0 2px 8px rgba(255,152,0,0.1);
        }
        
        .categories h3 {
            color: #ff9800;
            margin-bottom: 20px;
            font-size: 1.2em;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .category-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
            gap: 12px;
        }
        
        .category-item {
            background: white;
            padding: 15px;
            border-radius: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 2px solid #ff9800;
            transition: all 0.3s;
        }
        
        .category-item:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(255,152,0,0.2);
            background: #fff8f0;
        }
        
        .category-name {
            font-weight: 600;
            color: #333;
            font-size: 0.9em;
        }
        
        .category-count {
            background: #ff9800;
            color: white;
            padding: 4px 10px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9em;
            min-width: 30px;
            text-align: center;
        }
        
        .results {
            margin-top: 30px;
        }
        
        .result-item {
            background-color: #fff;
            margin-bottom: 25px;
            padding: 25px;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
            transition: box-shadow 0.3s, border-color 0.3s;
        }
        
        .result-item:hover {
            box-shadow: 0 4px 16px rgba(0,0,0,0.12);
            border-color: #007acc;
        }
        
        .result-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            gap: 20px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }
        
        .result-info {
            flex: 1;
            min-width: 300px;
        }
        
        .file-name {
            font-size: 1.3em;
            font-weight: bold;
            color: #333;
            word-break: break-word;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .file-type {
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.75em;
            font-weight: bold;
            text-transform: uppercase;
            white-space: nowrap;
        }
        
        .file-type.file {
            background-color: #28a745;
            color: white;
        }
        
        .file-type.folder {
            background-color: #ffc107;
            color: #333;
        }
        
        .file-path {
            color: #666;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            word-break: break-all;
            margin-top: 8px;
            padding: 10px;
            background-color: #f8f9fa;
            border-radius: 4px;
        }
        
        .copy-button {
            background: linear-gradient(135deg, #007acc 0%, #005a9e 100%);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.95em;
            font-weight: 600;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s;
            white-space: nowrap;
        }
        
        .button-group {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        
        .copy-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.2);
            background: linear-gradient(135deg, #005a9e 0%, #003d6b 100%);
        }
        
        .copy-button:active {
            transform: translateY(0);
        }
            color: white;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,122,204,0.3);
        }
        
        .matches-section {
            margin-top: 20px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
        }
        
        .matches-title {
            font-weight: bold;
            color: #007acc;
            margin-bottom: 12px;
        }
        
        .match-item {
            background-color: #f8f9fa;
            padding: 12px;
            margin-bottom: 10px;
            border-radius: 4px;
            border-left: 4px solid #28a745;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            word-break: break-word;
        }
        
        .match-item.filename-match {
            border-left-color: #ffc107;
            background-color: #fffbf0;
        }
        
        .line-number {
            color: #007acc;
            font-weight: bold;
            margin-right: 10px;
        }
        
        .highlight {
            background-color: #ffeb3b;
            padding: 2px 4px;
            border-radius: 2px;
            font-weight: 600;
        }
        
        .show-more-container {
            margin-top: 15px;
            text-align: center;
            border-top: 1px dashed #ddd;
            padding-top: 15px;
        }
        
        .show-more-button {
            background: linear-gradient(135deg, #6c757d 0%, #495057 100%);
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 0.9em;
            font-weight: 500;
            transition: all 0.3s;
            display: inline-flex;
            align-items: center;
            gap: 8px;
        }
        
        .show-more-button:hover {
            background: linear-gradient(135deg, #495057 0%, #343a40 100%);
            transform: translateY(-1px);
            box-shadow: 0 3px 8px rgba(0,0,0,0.2);
        }
        
        .show-more-button:active {
            transform: translateY(0);
        }
        
        .no-results {
            text-align: center;
            padding: 80px 20px;
            color: #999;
        }
        
        .no-results h2 {
            font-size: 2em;
            margin-bottom: 15px;
            color: #666;
        }
        
        .no-results p {
            font-size: 1.1em;
        }
        
        .footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #e0e0e0;
            color: #999;
            font-size: 0.9em;
        }
        
        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }
            
            .header h1 {
                font-size: 1.8em;
                gap: 10px;
            }
            
            .result-header {
                flex-direction: column;
            }
            
            .button-group {
                width: 100%;
                justify-content: flex-start;
            }
            
            .copy-button {
                flex: 1;
                justify-content: center;
                min-width: 120px;
            }
        }
        
        /* Smooth Fade-In Animations */
        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        
        /* Apply animations to elements - All from top-to-bottom */
        /* Elements start invisible (opacity: 0) and fade in with animations */
        .container {
            animation: fadeInDown 0.8s ease-out both;
        }
        
        .header {
            animation: fadeInDown 0.8s ease-out 0.1s both;
        }
        
        .header h1 {
            animation: fadeInDown 1s ease-out 0.3s both;
        }
        
        .logo {
            animation: fadeIn 1s ease-out 0.4s both;
        }
        
        .logo-container {
            animation: fadeIn 1s ease-out 0.4s both;
        }
        
        .header p {
            animation: fadeInDown 1s ease-out 0.5s both;
        }
        
        .search-info {
            animation: fadeInDown 1s ease-out 0.6s both;
        }
        
        .stats {
            animation: fadeInDown 1s ease-out 0.7s both;
        }
        
        .stat-item {
            animation: fadeInDown 0.8s ease-out both;
        }
        
        .stat-item:nth-child(1) {
            animation-delay: 0.8s;
        }
        
        .stat-item:nth-child(2) {
            animation-delay: 0.9s;
        }
        
        .stat-item:nth-child(3) {
            animation-delay: 1s;
        }
        
        .categories {
            animation: fadeInDown 1s ease-out 1.1s both;
        }
        
        .category-item {
            animation: fadeInDown 0.6s ease-out both;
        }
        
        .category-list > .category-item:nth-child(1) {
            animation-delay: 1.2s;
        }
        
        .category-list > .category-item:nth-child(2) {
            animation-delay: 1.3s;
        }
        
        .category-list > .category-item:nth-child(3) {
            animation-delay: 1.4s;
        }
        
        .category-list > .category-item:nth-child(n+4) {
            animation-delay: 1.5s;
        }
        
        .result-item {
            animation: fadeInDown 0.8s ease-out both;
        }
        
        .result-item:nth-child(1) {
            animation-delay: 1.6s;
        }
        
        .result-item:nth-child(2) {
            animation-delay: 1.7s;
        }
        
        .result-item:nth-child(3) {
            animation-delay: 1.8s;
        }
        
        .result-item:nth-child(4) {
            animation-delay: 1.9s;
        }
        
        .result-item:nth-child(5) {
            animation-delay: 2s;
        }
        
        .result-item:nth-child(n+6) {
            animation-delay: 2.1s;
        }
    </style>'''
    
    def _get_html_header_section(self) -> str:
        """Get header section with logo and title."""
        svg_logo = self._get_svg_logo()
        return f'''        <div class="header">
            {svg_logo}
            <h1>
                Master Search
            </h1>
            <p>{tr('professional_search')}</p>
        </div>'''
    
    def _get_svg_logo(self) -> str:
        """Get SVG logo from icon.svg file."""
        try:
            # Try to load icon.svg from media folder
            icon_path = os.path.join(os.path.dirname(__file__), 'media', 'icon.svg')
            if os.path.exists(icon_path):
                with open(icon_path, 'r', encoding='utf-8') as f:
                    svg_content = f.read()
                    # Wrap SVG with logo class for styling
                    return f'<div class="logo-container">{svg_content}</div>'
        except Exception as e:
            print(f"Warning: Could not load icon.svg: {e}")
        
        # Fallback to embedded simple logo if icon.svg not found
        return '''<svg class="logo" width="56" height="56" viewBox="0 0 56 56" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="28" cy="28" r="28" fill="#007ACC"/>
                <g transform="translate(8, 8)">
                    <circle cx="10" cy="10" r="8" stroke="white" stroke-width="2" fill="none"/>
                    <line x1="17" y1="17" x2="23" y2="23" stroke="white" stroke-width="2" stroke-linecap="round"/>
                </g>
            </svg>'''
    
    def _get_html_search_info(self, search_terms: str) -> str:
        """Get search information section."""
        return f'''        <div class="search-info">
            <div><strong>🔍 {tr('search_terms')}:</strong> {html.escape(search_terms)}</div>
            <div><strong>📂 {tr('search_path')}:</strong> {html.escape(self.search_path)}</div>
            <div><strong>⏰ {tr('report_generated')}:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</div>
            <div><strong>⚙️  {tr('options')}:</strong> 
                {tr('case_sensitive')}: {'Yes' if self.case_sensitive else 'No'}, 
                {tr('regex_mode')}: {'Yes' if self.use_regex else 'No'}
            </div>
        </div>'''
    
    def _get_html_stats(self, total: int, files: int, folders: int) -> str:
        """Get statistics section."""
        return f'''        <div class="stats">
            <div class="stat-item">
                <span class="stat-number">{total}</span>
                <div class="stat-label">{tr('total_results')}</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">{files}</span>
                <div class="stat-label">{tr('files_found')}</div>
            </div>
            <div class="stat-item">
                <span class="stat-number">{folders}</span>
                <div class="stat-label">{tr('folders_found')}</div>
            </div>
        </div>'''
    
    def _get_category_stats(self, results: List[Dict[str, Any]]) -> str:
        """Get category statistics by file type."""
        if not results:
            return ''
        
        # Count results by file type
        category_counts = {}
        for result in results:
            file_type = result.get('type', 'unknown')
            category_counts[file_type] = category_counts.get(file_type, 0) + 1
        
        # Sort by count (descending), then alphabetically
        sorted_categories = sorted(category_counts.items(), 
                                  key=lambda x: (-x[1], x[0]))
        
        # Build category items HTML
        category_items = []
        for file_type, count in sorted_categories:
            category_items.append(f'''            <div class="category-item">
                <span class="category-name">{html.escape(file_type.upper())}</span>
                <span class="category-count">{count}</span>
            </div>''')
        
        return f'''        <div class="categories">
            <h3>{tr('file_types')}</h3>
            <div class="category-list">
{''.join(category_items)}
            </div>
        </div>'''
    
    def _get_html_results(self, results: List[Dict[str, Any]]) -> str:
        """Get results section."""
        html_parts = ['        <div class="results">']
        
        for result in results:
            html_parts.append(self._get_result_item_html(result))
        
        html_parts.append('        </div>')
        return '\n'.join(html_parts)
    
    def _extract_context_words(self, line_content: str, search_terms: List[str], context_words: int = 5) -> str:
        """Extract context around search terms: show only N words before and after."""
        try:
            words = line_content.split()
            
            # If line is short enough, return as is
            if len(words) <= context_words * 2 + 3:
                return line_content
            
            # Find positions of any search term
            positions = []
            for i, word in enumerate(words):
                for term in search_terms:
                    if term.lower() in word.lower():
                        positions.append(i)
                        break
            
            if not positions:
                # No terms found, return truncated version
                return ' '.join(words[:context_words * 2 + 1]) + '...'
            
            # Find the range to display (with context)
            min_pos = min(positions)
            max_pos = max(positions)
            
            start = max(0, min_pos - context_words)
            end = min(len(words), max_pos + context_words + 1)
            
            # Build result
            result_words = []
            if start > 0:
                result_words.append('...')
            
            result_words.extend(words[start:end])
            
            if end < len(words):
                result_words.append('...')
            
            return ' '.join(result_words)
        
        except Exception:
            return line_content
    
    def _get_result_item_html(self, result: Dict[str, Any]) -> str:
        """Get HTML for a single result item."""
        result_type = result['type']
        name = html.escape(result['name'])
        path = html.escape(result['path'])
        
        # Ensure proper path format for Windows
        raw_path = result['path']  # Keep unescaped for JavaScript
        # Normalize path: backslashes, handle spaces properly
        js_path = raw_path.replace('\\', '\\\\').replace("'", "\\'")
        
        # Build match items
        all_matches = result.get('matches', [])
        total_matches = len(all_matches)
        
        # Show only first 3 matches initially
        visible_matches = all_matches[:3]
        hidden_matches = all_matches[3:]
        
        # Generate unique ID for this result
        import random
        unique_id = f"result_{random.randint(100000, 999999)}"
        
        match_items = []
        # Add visible matches
        for match in visible_matches:
            line_content = match.get('line_content', '')
            
            # For long lines, extract only context around search terms (5 words before/after)
            if len(line_content.split()) > 20:  # Only if line is longer than 20 words
                context_content = self._extract_context_words(line_content, self.search_terms)
            else:
                context_content = line_content
            
            content = html.escape(context_content)
            
            # Highlight search terms
            if match.get('found_terms'):
                for term in match['found_terms']:
                    content = self._highlight_term(content, term)
            
            line_num = match.get('line_number', 0)
            
            if line_num > 0:
                match_items.append(f'''            <div class="match-item">
                <span class="line-number">{tr('line')} {line_num}:</span>{content}
            </div>''')
            else:
                is_filename = content.startswith('📄') or content.startswith('📁')
                css_class = 'filename-match' if is_filename else ''
                match_items.append(f'''            <div class="match-item {css_class}">
                {content}
            </div>''')
        
        # Add hidden matches (initially hidden)
        hidden_match_items = []
        for match in hidden_matches:
            line_content = match.get('line_content', '')
            
            # For long lines, extract only context around search terms (5 words before/after)
            if len(line_content.split()) > 20:  # Only if line is longer than 20 words
                context_content = self._extract_context_words(line_content, self.search_terms)
            else:
                context_content = line_content
            
            content = html.escape(context_content)
            
            # Highlight search terms
            if match.get('found_terms'):
                for term in match['found_terms']:
                    content = self._highlight_term(content, term)
            
            line_num = match.get('line_number', 0)
            
            if line_num > 0:
                hidden_match_items.append(f'''            <div class="match-item">
                <span class="line-number">{tr('line')} {line_num}:</span>{content}
            </div>''')
            else:
                is_filename = content.startswith('📄') or content.startswith('📁')
                css_class = 'filename-match' if is_filename else ''
                hidden_match_items.append(f'''            <div class="match-item {css_class}">
                {content}
            </div>''')
        
        # Build matches section HTML
        matches_html = ''.join(match_items)
        
        # Add hidden matches section if there are more than 3
        if len(hidden_matches) > 0:
            matches_html += f'''
            <div id="hidden_matches_{unique_id}" style="display: none;">
                {''.join(hidden_match_items)}
            </div>
            <div class="show-more-container">
                <button id="show_more_btn_{unique_id}" onclick="toggleMoreMatches('{unique_id}')" class="show-more-button">
                    📄 Weitere {len(hidden_matches)} Treffer in der Datei anzeigen
                </button>
            </div>'''
        
        return f'''        <div class="result-item">
            <div class="result-header">
                <div class="result-info">
                    <div class="file-name">
                        {name}
                        <span class="file-type {result_type}">{result_type}</span>
                    </div>
                    <div class="file-path">{path}</div>
                </div>
                <div class="button-group">
                    <button onclick="copyPathToClipboard('{js_path}');" class="copy-button" title="Pfad in Zwischenablage kopieren">
                        📋 {tr('copy_path')}
                    </button>
                </div>
            </div>
            <div class="matches-section">
                <div class="matches-title">{tr('matches')} ({total_matches})</div>
                {matches_html}
            </div>
        </div>'''
    
    def _highlight_term(self, content: str, term: str) -> str:
        """Highlight search term in content."""
        try:
            if self.use_regex:
                flags = 0 if self.case_sensitive else re.IGNORECASE
                pattern = re.compile(term, flags)
                content = pattern.sub(
                    lambda m: f'<span class="highlight">{html.escape(m.group())}</span>',
                    content
                )
            else:
                flags = 0 if self.case_sensitive else re.IGNORECASE
                pattern = re.compile(re.escape(term), flags)
                content = pattern.sub(
                    lambda m: f'<span class="highlight">{html.escape(m.group())}</span>',
                    content
                )
        except Exception:
            pass  # Silently fail on regex errors
        
        return content
    
    def _get_html_no_results(self) -> str:
        """Get no results message."""
        return f'''        <div class="no-results">
            <h2>🚫 {tr('no_results')}</h2>
            <p>{tr('no_results_msg')}</p>
        </div>'''
    
    def _get_html_scripts(self) -> str:
        """Get JavaScript code for file operations - Simple clipboard copy solution."""
        return '''    <script>
        /**
         * Toggle display of additional matches in a file
         */
        function toggleMoreMatches(uniqueId) {
            var hiddenMatches = document.getElementById('hidden_matches_' + uniqueId);
            var showMoreBtn = document.getElementById('show_more_btn_' + uniqueId);
            
            if (hiddenMatches && showMoreBtn) {
                if (hiddenMatches.style.display === 'none') {
                    // Show hidden matches
                    hiddenMatches.style.display = 'block';
                    var hiddenCount = hiddenMatches.querySelectorAll('.match-item').length;
                    showMoreBtn.innerHTML = '📄 Weitere Treffer ausblenden';
                    showMoreBtn.title = 'Zusätzliche ' + hiddenCount + ' Treffer ausblenden';
                } else {
                    // Hide matches again
                    hiddenMatches.style.display = 'none';
                    var hiddenCount = hiddenMatches.querySelectorAll('.match-item').length;
                    showMoreBtn.innerHTML = '📄 Weitere ' + hiddenCount + ' Treffer in der Datei anzeigen';
                    showMoreBtn.title = 'Weitere ' + hiddenCount + ' Treffer anzeigen';
                }
            }
        }
        
        /**
         * Copy file/folder path to clipboard
         */
        function copyPathToClipboard(path) {
            console.log('[COPY] Copying to clipboard: ' + path);
            
            copyToClipboard(path);
            
            // Show temporary notification
            showNotification('✓ In Zwischenablage kopiert!');
        }
        
        /**
         * Copy path to clipboard using modern or legacy API
         */
        function copyToClipboard(text) {
            try {
                // Modern Clipboard API
                if (navigator.clipboard && navigator.clipboard.writeText) {
                    navigator.clipboard.writeText(text)
                        .then(function() {
                            console.log('[CLIP] Erfolgreich kopiert');
                        })
                        .catch(function(err) {
                            console.log('[CLIP] Modern API fehlgeschlagen, versuche Legacy');
                            copyToClipboardLegacy(text);
                        });
                } else {
                    copyToClipboardLegacy(text);
                }
            } catch (e) {
                console.error('[CLIP] Error: ' + e);
                copyToClipboardLegacy(text);
            }
        }
        
        /**
         * Legacy clipboard copy using execCommand
         */
        function copyToClipboardLegacy(text) {
            try {
                var textarea = document.createElement('textarea');
                textarea.value = text;
                textarea.style.position = 'fixed';
                textarea.style.left = '-9999px';
                textarea.style.opacity = '0';
                document.body.appendChild(textarea);
                textarea.focus();
                textarea.select();
                
                if (document.execCommand('copy')) {
                    console.log('[CLIP] Legacy copy erfolgreich');
                } else {
                    console.log('[CLIP] Legacy copy fehlgeschlagen');
                }
                
                document.body.removeChild(textarea);
            } catch (e) {
                console.error('[CLIP] Legacy error: ' + e);
            }
        }
        
        /**
         * Show temporary notification message
         */
        function showNotification(message) {
            // Remove existing notification if any
            var existing = document.getElementById('clipboard-notification');
            if (existing) {
                existing.remove();
            }
            
            // Create notification element
            var notification = document.createElement('div');
            notification.id = 'clipboard-notification';
            notification.style.position = 'fixed';
            notification.style.bottom = '20px';
            notification.style.right = '20px';
            notification.style.backgroundColor = '#28a745';
            notification.style.color = 'white';
            notification.style.padding = '12px 20px';
            notification.style.borderRadius = '6px';
            notification.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
            notification.style.fontSize = '14px';
            notification.style.fontWeight = '600';
            notification.style.zIndex = '10000';
            notification.style.animation = 'fadeInOut 2s ease-in-out';
            notification.textContent = message;
            
            document.body.appendChild(notification);
            
            // Auto-remove after 2 seconds
            setTimeout(function() {
                try {
                    notification.remove();
                } catch (e) {}
            }, 2000);
        }
        
        /**
         * Animation für Notification
         */
        var style = document.createElement('style');
        style.innerHTML = `
            @keyframes fadeInOut {
                0% { opacity: 0; transform: translateY(10px); }
                10% { opacity: 1; transform: translateY(0); }
                90% { opacity: 1; transform: translateY(0); }
                100% { opacity: 0; transform: translateY(10px); }
            }
        `;
        document.head.appendChild(style);
        
        /**
         * Debug logging
         */
        function log(msg) {
            console.log('[MASTER_SEARCH] ' + msg);
        }
        
        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            log('Report loaded - Clipboard copy ready');
        });
    </script>'''
