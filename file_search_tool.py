"""
Top-level shim for tests: re-export from src package so tests can import
`file_search_tool` without changing their imports.
"""
from src.file_search_tool import *

__all__ = [name for name in dir() if not name.startswith('_')]
