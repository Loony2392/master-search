# tests/conftest.py
# Ensure the repository `src/` and top-level packages are importable during pytest
import sys
from pathlib import Path

repo_root = Path(__file__).resolve().parent.parent
src_path = repo_root / 'src'
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

# Also add repo root so imports that expect top-level modules work
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))
