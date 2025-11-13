
"""i18n shim for tests
Exports a small compatibility layer so tests that expect
`from i18n import I18n, set_language, get_language` work.
"""
from typing import Optional
import src.i18n as _i18n


class I18n:
	"""Lightweight wrapper around src.i18n functionality."""
	def __init__(self, default_language: Optional[str] = None):
		if default_language:
			_i18n.set_locale(default_language)

	def translate(self, key: str, **kwargs) -> str:
		return _i18n.tr(key, **kwargs)


def set_language(lang: str):
	"""Set active language (compat shim)."""
	return _i18n.set_locale(lang)


def get_language() -> str:
	"""Return current language code if available, else detect system language."""
	try:
		return getattr(_i18n, '_CURRENT_LANG') or _i18n._detect_system_lang()
	except Exception:
		return _i18n._detect_system_lang()


# Re-export common helpers
tr = _i18n.tr

__all__ = ['I18n', 'set_language', 'get_language', 'tr']
