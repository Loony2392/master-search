#!/usr/bin/env python3
"""
Update package.json version from version.py to keep them in sync.
This ensures version.py is the single source of truth for versioning.
"""

import json
import re
import sys
from pathlib import Path


def get_version_from_python():
    """Extract VERSION from version.py"""
    version_file = Path(__file__).parent.parent / "version.py"
    
    if not version_file.exists():
        print(f"❌ version.py not found at {version_file}")
        sys.exit(1)
    
    with open(version_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Match: VERSION = "2025.11.24"
    match = re.search(r'VERSION\s*=\s*["\']([^"\']+)["\']', content)
    if not match:
        print("❌ Could not parse VERSION from version.py")
        sys.exit(1)
    
    version = match.group(1)
    print(f"📖 Read version from version.py: {version}")
    return version


def update_package_json(version):
    """Update version in package.json"""
    package_file = Path(__file__).parent.parent / "package.json"
    
    if not package_file.exists():
        print(f"❌ package.json not found at {package_file}")
        sys.exit(1)
    
    with open(package_file, "r", encoding="utf-8") as f:
        package = json.load(f)
    
    old_version = package.get("version")
    package["version"] = version
    
    with open(package_file, "w", encoding="utf-8") as f:
        json.dump(package, f, indent=2, ensure_ascii=False)
        f.write("\n")  # Add newline at end of file
    
    print(f"✅ Updated package.json: {old_version} → {version}")


def main():
    """Main function"""
    version = get_version_from_python()
    update_package_json(version)
    print("✅ Version sync complete!")


if __name__ == "__main__":
    main()
