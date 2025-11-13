#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Master Search - MSI Build Script
================================
Automated MSI Creation for Master Search

Author: Loony2392
Company: LOONY-TECH
Email: info@loony-tech.de
"""

import subprocess
import sys
import os
import shutil
from pathlib import Path
import time

# Force UTF-8 output on Windows
if sys.platform == 'win32':
    import io
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except:
        pass

class MSIBuilder:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.dist_folder = self.project_root / 'dist'
        self.build_folder = self.project_root / 'build'
        
    def print_colored(self, text, emoji=''):
        """Simple text output (ASCII-safe)."""
        try:
            print(f"{emoji} {text}")
        except UnicodeEncodeError:
            # Fallback for cp1252 console
            try:
                safe_text = text.encode('utf-8', errors='replace').decode('ascii', errors='replace')
                print(f"{emoji} {safe_text}")
            except:
                print(emoji + " " + str(text))
    
    def print_separator(self, char='=', length=60):
        """Print separator line (ASCII-safe)."""
        try:
            print(char * length)
        except UnicodeEncodeError:
            print('=' * length)
    
    def check_requirements(self):
        """Check if all dependencies are installed."""
        self.print_colored('Checking system requirements...', '[*]')
        
        # Check Python Version
        if sys.version_info < (3, 7):
            self.print_colored(f'Python 3.7+ required! Current: {sys.version}', '[ERROR]')
            return False
        
        self.print_colored(f'Python Version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}', '[OK]')
        
        # Check Windows
        if os.name != 'nt':
            self.print_colored('MSI creation is only possible on Windows!', '[ERROR]')
            return False
        
        self.print_colored('Windows system detected', '[OK]')
        
        return True
    
    def install_dependencies(self):
        """Install required build dependencies."""
        self.print_colored('Installing build dependencies...', '[*]')
        
        dependencies = [
            'cx_Freeze>=6.15.0',
            'colorama>=0.4.6',
        ]
        
        # Optional: psutil
        try:
            import psutil
            self.print_colored('psutil already installed', '[OK]')
        except ImportError:
            dependencies.append('psutil>=5.9.0')
        
        for dep in dependencies:
            try:
                self.print_colored(f'Installing {dep}...', '[*]')
                subprocess.check_call([
                    sys.executable, '-m', 'pip', 'install', dep
                ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                self.print_colored(f'{dep} successfully installed', '[OK]')
            except subprocess.CalledProcessError as e:
                self.print_colored(f'Error installing {dep}: {e}', '[ERROR]')
                return False
        
        return True
    
    def clean_build_directories(self):
        """Clean old build directories."""
        self.print_colored('Cleaning build directories...', '[*]')
        
        for folder in [self.build_folder, self.dist_folder]:
            if folder.exists():
                try:
                    shutil.rmtree(folder)
                    self.print_colored(f'{folder.name} cleaned', '[OK]')
                except PermissionError as e:
                    self.print_colored(f'Permission denied cleaning {folder.name} - trying alternative...', '[WARN]')
                    # Try using Windows command
                    try:
                        import subprocess
                        subprocess.call(['rmdir', '/s', '/q', str(folder)], shell=True)
                        self.print_colored(f'{folder.name} cleaned (via cmd)', '[OK]')
                    except:
                        self.print_colored(f'Could not clean {folder.name}, will proceed anyway', '[WARN]')
                except Exception as e:
                    self.print_colored(f'Could not clean {folder.name}: {e}', '[WARN]')
    
    def build_executable(self):
        """Create the executable file."""
        self.print_colored('Creating executable file...', '[*]')
        
        try:
            subprocess.check_call([
                sys.executable, 'setup_msi.py', 'build'
            ])
            self.print_colored('Executable file created', '[OK]')
            return True
        except subprocess.CalledProcessError as e:
            self.print_colored(f'Error creating EXE: {e}', '[ERROR]')
            return False
    
    def build_msi(self):
        """Create the MSI installer."""
        self.print_colored('Creating MSI installer...', '[*]')
        
        try:
            subprocess.check_call([
                sys.executable, 'setup_msi.py', 'bdist_msi'
            ])
            self.print_colored('MSI file created', '[OK]')
            return True
        except subprocess.CalledProcessError as e:
            self.print_colored(f'Error creating MSI: {e}', '[ERROR]')
            return False
    
    def show_results(self):
        """Display build results."""
        self.print_separator('=')
        self.print_colored('BUILD COMPLETED SUCCESSFULLY', '[SUCCESS]')
        self.print_separator('=')
        
        # Find MSI files
        msi_files = list(self.dist_folder.glob('*.msi'))
        exe_files = list(Path('build').rglob('*.exe'))
        
        if msi_files:
            msi_file = msi_files[0]
            file_size = msi_file.stat().st_size / (1024 * 1024)  # MB
            
            self.print_colored('MSI FILE DETAILS:', '[*]')
            self.print_colored(f'File: {msi_file.name}', '[*]')
            self.print_colored(f'Path: {msi_file.absolute()}', '[*]')
            self.print_colored(f'Size: {file_size:.1f} MB', '[*]')
            
            print()
            self.print_colored('INSTALLATION:', '[*]')
            self.print_colored('1. Double-click the MSI file', '[*]')
            self.print_colored('2. Follow the installation wizard', '[*]')
            self.print_colored('3. Master Search will be installed', '[*]')
            self.print_colored('4. Start program from Start menu', '[*]')
            
            print()
            self.print_colored('DISTRIBUTION:', '[*]')
            self.print_colored('The MSI file can be distributed without additional dependencies', '[*]')
            self.print_colored('No Python installation required on target system', '[OK]')
        
        if exe_files:
            print()
            self.print_colored(f'Additionally: {len(exe_files)} EXE file(s) created', '[*]')
    
    def run(self):
        """Run the complete build process."""
        print()
        self.print_separator('=')
        self.print_colored('MASTER SEARCH - MSI BUILDER', '[BUILD]')
        self.print_separator('=')
        self.print_colored('Automated MSI Creation Tool', '[*]')
        self.print_colored('Author: Loony2392 - LOONY-TECH', '[*]')
        print()
        
        # Schritt 1: Systemprüfung
        if not self.check_requirements():
            return False
        
        print()
        
        # Schritt 2: Abhängigkeiten installieren
        if not self.install_dependencies():
            return False
        
        print()
        
        # Schritt 3: Bereinigung
        self.clean_build_directories()
        
        print()
        
        # Schritt 4: EXE erstellen
        if not self.build_executable():
            return False
        
        print()
        
        # Schritt 5: MSI erstellen
        if not self.build_msi():
            return False
        
        print()
        
        # Schritt 6: Ergebnisse anzeigen
        self.show_results()
        
        return True

def main():
    """Main entry point."""
    builder = MSIBuilder()
    
    try:
        success = builder.run()
        
        if success:
            print()
            builder.print_colored('MSI build completed successfully!', '[SUCCESS]')
            
            # Optional: Open MSI file
            msi_files = list(Path('dist').glob('*.msi'))
            if msi_files:
                try:
                    os.startfile(str(msi_files[0].parent))
                    builder.print_colored('Dist folder opened', '[OK]')
                except:
                    pass
        else:
            builder.print_colored('MSI build failed!', '[ERROR]')
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\nBuild cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()