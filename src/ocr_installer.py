#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
OCR Engine Automatic Installation Manager
==========================================
Automatically installs the best OCR engine based on platform.
Supports Windows, macOS, and Linux.

Author: Loony2392
Email: info@loony-tech.de
Version: 1.0.0
Created: November 2025

Features:
    - Automatic platform detection
    - Smart engine selection (EasyOCR as primary)
    - Multi-step installation with progress tracking
    - Fallback options for different platforms
    - Error handling and troubleshooting guidance
"""

import os
import sys
import subprocess
import platform
import threading
from pathlib import Path
from typing import Callable, Optional, Tuple


class OCRInstaller:
    """Manages automatic OCR engine installation across platforms"""
    
    WINDOWS = "Windows"
    MACOS = "Darwin"
    LINUX = "Linux"
    
    # Installation strategies by platform
    INSTALL_STRATEGIES = {
        "easyocr": {
            "package": "easyocr",
            "priority": 1,
            "description": "EasyOCR (Primary - Pure Python, Cross-Platform)",
            "install_cmd": None,  # Uses pip by default
        },
        "paddleocr": {
            "package": "paddleocr",
            "priority": 2,
            "description": "PaddleOCR (Alternative - High Accuracy)",
            "install_cmd": None,  # Uses pip by default
        },
        "tesseract": {
            "package": "pytesseract",
            "priority": 3,
            "description": "Tesseract (Optional - System Binary Required)",
            "platform_specific": True,
        }
    }
    
    def __init__(self, callback: Optional[Callable[[str], None]] = None):
        """
        Initialize OCR Installer
        
        Args:
            callback: Optional callback function for progress updates
                     Signature: callback(message: str) -> None
        """
        self.callback = callback
        self.system = platform.system()
        self.is_windows = self.system == self.WINDOWS
        self.is_macos = self.system == self.MACOS
        self.is_linux = self.system == self.LINUX
    
    def _log(self, message: str) -> None:
        """Log message to callback or print"""
        if self.callback:
            self.callback(message)
        else:
            print(message)
    
    def install_easyocr(self) -> bool:
        """Install EasyOCR (recommended)"""
        self._log("📦 Installing EasyOCR...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--quiet", "easyocr"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            self._log("✅ EasyOCR installed successfully!")
            return True
        except Exception as e:
            self._log(f"❌ EasyOCR installation failed: {e}")
            return False
    
    def install_paddleocr(self) -> bool:
        """Install PaddleOCR (fallback)"""
        self._log("📦 Installing PaddleOCR...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--quiet", "paddleocr"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            self._log("✅ PaddleOCR installed successfully!")
            return True
        except Exception as e:
            self._log(f"❌ PaddleOCR installation failed: {e}")
            return False
    
    def install_tesseract_windows(self) -> bool:
        """Install Tesseract on Windows"""
        self._log("📦 Installing Tesseract OCR (Windows)...")
        self._log("⚠️  Tesseract requires manual system installation")
        self._log("📥 Visit: https://github.com/UB-Mannheim/tesseract/wiki")
        self._log("🔗 Download: https://github.com/UB-Mannheim/tesseract/releases")
        return False
    
    def install_tesseract_macos(self) -> bool:
        """Install Tesseract on macOS via Homebrew"""
        self._log("📦 Installing Tesseract OCR (macOS)...")
        try:
            # Check if Homebrew is installed
            result = subprocess.run(
                ["which", "brew"],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                self._log("⚠️  Homebrew not installed. Please install from https://brew.sh")
                return False
            
            # Install tesseract
            self._log("🍺 Using Homebrew to install tesseract...")
            subprocess.check_call(["brew", "install", "tesseract"])
            
            # Install Python bindings
            self._log("📦 Installing pytesseract...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--quiet", "pytesseract"]
            )
            
            self._log("✅ Tesseract installed successfully!")
            return True
        except Exception as e:
            self._log(f"❌ Tesseract installation failed: {e}")
            return False
    
    def install_tesseract_linux(self) -> bool:
        """Install Tesseract on Linux"""
        self._log("📦 Installing Tesseract OCR (Linux)...")
        
        # Detect package manager
        if os.path.exists("/etc/debian_version"):
            self._log("📦 Detected Debian/Ubuntu. Using apt...")
            try:
                subprocess.check_call(["sudo", "apt", "update"])
                subprocess.check_call(["sudo", "apt", "install", "-y", "tesseract-ocr"])
                
                self._log("📦 Installing pytesseract...")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "--quiet", "pytesseract"]
                )
                
                self._log("✅ Tesseract installed successfully!")
                return True
            except Exception as e:
                self._log(f"❌ Tesseract installation failed: {e}")
                return False
        
        elif os.path.exists("/etc/redhat-release"):
            self._log("📦 Detected RHEL/CentOS/Fedora. Using yum/dnf...")
            try:
                # Try dnf first (Fedora 22+)
                try:
                    subprocess.check_call(["sudo", "dnf", "install", "-y", "tesseract"])
                except FileNotFoundError:
                    subprocess.check_call(["sudo", "yum", "install", "-y", "tesseract"])
                
                self._log("📦 Installing pytesseract...")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "--quiet", "pytesseract"]
                )
                
                self._log("✅ Tesseract installed successfully!")
                return True
            except Exception as e:
                self._log(f"❌ Tesseract installation failed: {e}")
                return False
        
        elif os.path.exists("/etc/arch-release"):
            self._log("📦 Detected Arch Linux. Using pacman...")
            try:
                subprocess.check_call(["sudo", "pacman", "-S", "--noconfirm", "tesseract"])
                
                self._log("📦 Installing pytesseract...")
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "--quiet", "pytesseract"]
                )
                
                self._log("✅ Tesseract installed successfully!")
                return True
            except Exception as e:
                self._log(f"❌ Tesseract installation failed: {e}")
                return False
        
        else:
            self._log("⚠️  Unknown Linux distribution. Manual installation required.")
            self._log("📥 Visit: https://github.com/UB-Mannheim/tesseract/wiki/Downloads")
            return False
    
    def auto_install_ocr(self, background: bool = False) -> bool:
        """
        Automatically install best available OCR engine
        
        Args:
            background: If True, run in background thread
            
        Returns:
            True if installation successful, False otherwise
        """
        if background:
            thread = threading.Thread(target=self._auto_install_ocr_impl)
            thread.daemon = True
            thread.start()
            return True
        else:
            return self._auto_install_ocr_impl()
    
    def _auto_install_ocr_impl(self) -> bool:
        """Implementation of auto-install"""
        self._log("🚀 Starting automatic OCR engine installation...")
        self._log(f"📊 Detected platform: {self.system}")
        self._log("")
        
        # Try EasyOCR first (best choice for most users)
        self._log("✨ Attempting to install EasyOCR (recommended)...")
        if self.install_easyocr():
            self._log("🎉 OCR setup complete! You can now search images with text.")
            return True
        
        self._log("")
        self._log("ℹ️  EasyOCR installation did not work. Trying PaddleOCR...")
        if self.install_paddleocr():
            self._log("🎉 OCR setup complete! You can now search images with text.")
            return True
        
        self._log("")
        self._log("ℹ️  Attempting platform-specific OCR engines...")
        
        if self.is_windows:
            self._log("🪟 Windows detected.")
            if self.install_tesseract_windows():
                self._log("🎉 OCR setup complete!")
                return True
        
        elif self.is_macos:
            self._log("🍎 macOS detected.")
            if self.install_tesseract_macos():
                self._log("🎉 OCR setup complete!")
                return True
        
        elif self.is_linux:
            self._log("🐧 Linux detected.")
            if self.install_tesseract_linux():
                self._log("🎉 OCR setup complete!")
                return True
        
        self._log("")
        self._log("❌ All OCR installation attempts failed.")
        self._log("📚 Manual installation required.")
        self._log("")
        self._log("Manual Installation Options:")
        self._log("1. EasyOCR: pip install easyocr")
        self._log("2. PaddleOCR: pip install paddleocr")
        self._log("3. Tesseract: https://github.com/UB-Mannheim/tesseract/wiki")
        
        return False
    
    def check_installation(self) -> Tuple[bool, str]:
        """
        Check if any OCR engine is installed
        
        Returns:
            Tuple of (is_installed: bool, engine_name: str)
        """
        try:
            import easyocr
            return True, "EasyOCR"
        except ImportError:
            pass
        
        try:
            import paddleocr
            return True, "PaddleOCR"
        except ImportError:
            pass
        
        try:
            import pytesseract
            return True, "Tesseract"
        except ImportError:
            pass
        
        return False, "None"


def get_ocr_installer() -> OCRInstaller:
    """Get singleton OCR installer instance"""
    global _ocr_installer_instance
    if '_ocr_installer_instance' not in globals():
        _ocr_installer_instance = OCRInstaller()
    return _ocr_installer_instance


if __name__ == "__main__":
    # Test OCR installer
    installer = OCRInstaller()
    
    print("🔍 Testing OCR Installation Manager")
    print("=" * 50)
    print()
    
    # Check current status
    is_installed, engine = installer.check_installation()
    if is_installed:
        print(f"✅ OCR Already Installed: {engine}")
    else:
        print("❌ No OCR engine found")
    
    print()
    print("Available OCR Strategies:")
    for engine, info in OCRInstaller.INSTALL_STRATEGIES.items():
        print(f"  - {info['description']} (Priority: {info['priority']})")
