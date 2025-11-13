#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Quick check for supported file extensions
"""

from file_search_tool import FileSearchTool

fst = FileSearchTool(verbose=False)
extensions = sorted(fst.supported_text_extensions)

print("=" * 70)
print("UNTERSTÜTZTE DATEITYPEN - Master Search")
print("=" * 70)
print(f"\n✅ Insgesamt {len(extensions)} Dateitypen unterstützt:\n")

# Kategorisiert ausgeben
categories = {
    "Web & Markup": ['.html', '.htm', '.xml', '.json'],
    "Scripting & Programming": ['.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.cpp', '.c', '.h', '.cs', '.php', '.rb', '.go', '.rs', '.sh', '.ps1', '.bat'],
    "Styling": ['.css', '.scss', '.sass', '.less'],
    "Data & Configuration": ['.csv', '.yml', '.yaml', '.toml', '.ini', '.cfg', '.conf', '.sql'],
    "Documentation": ['.txt', '.md', '.rst'],
    "Office Documents": ['.doc', '.docx', '.pdf', '.xlsx', '.pptx', '.odt', '.rtf'],
    "Other": ['.log', '.edcx', '.vue', '.svelte', '.properties']
}

for category, expected_exts in categories.items():
    actual_exts = [ext for ext in expected_exts if ext in extensions]
    print(f"\n📁 {category} ({len(actual_exts)}):")
    for ext in sorted(actual_exts):
        print(f"   • {ext}")

print("\n" + "=" * 70)
print(f"GESAMT: {len(extensions)} Dateitypen")
print("=" * 70)
