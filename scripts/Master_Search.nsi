; Master Search - NSIS Installer Script
; Creates Start Menu and Desktop shortcuts
; Generated automatically during build process

!include "MUI2.nsh"
!include "x64.nsh"

; Basic Settings
Name "Master Search"
OutFile "Master_Search-2025.11.20-win64.exe"
InstallDir "$PROGRAMFILES64\Master Search"
InstallDirRegKey HKLM "Software\Master Search" "InstallDir"

; UI Settings
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES

; Uninstall UI
!insertmacro MUI_UNPAGE_INSTFILES

; Language
!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "German"

; Version Information
VIProductVersion "2025.11.20.0"
VIAddVersionKey /LANG=${LANG_ENGLISH} "ProductName" "Master Search"
VIAddVersionKey /LANG=${LANG_ENGLISH} "CompanyName" "LOONY-TECH"
VIAddVersionKey /LANG=${LANG_ENGLISH} "FileDescription" "Professional file search tool"
VIAddVersionKey /LANG=${LANG_ENGLISH} "FileVersion" "2025.11.20"
VIAddVersionKey /LANG=${LANG_ENGLISH} "ProductVersion" "2025.11.20"

; Installation Sections
Section "Install"
    SetOutPath "$INSTDIR"
    
    ; Copy files
    File "Master_Search.exe"
    File "MasterSearch_CLI.exe"
    
    ; Store installation folder
    WriteRegStr HKLM "Software\Master Search" "InstallDir" "$INSTDIR"
    
    ; Create Start Menu shortcuts
    CreateDirectory "$SMPROGRAMS\Master Search"
    CreateShortcut "$SMPROGRAMS\Master Search\Master Search.lnk" "$INSTDIR\Master_Search.exe"
    CreateShortcut "$SMPROGRAMS\Master Search\Master Search CLI.lnk" "$INSTDIR\MasterSearch_CLI.exe"
    CreateShortcut "$SMPROGRAMS\Master Search\Uninstall.lnk" "$INSTDIR\uninstall.exe"
    
    ; Create Desktop shortcuts
    CreateShortcut "$DESKTOP\Master Search.lnk" "$INSTDIR\Master_Search.exe"
    CreateShortcut "$DESKTOP\Master Search CLI.lnk" "$INSTDIR\MasterSearch_CLI.exe"
    
    ; Add to PATH
    EnVar::AddValue "PATH" "$INSTDIR"
    
    ; Create uninstaller
    WriteUninstaller "$INSTDIR\uninstall.exe"
    
    ; Add/Remove Programs
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Master Search" "DisplayName" "Master Search v2025.11.20"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Master Search" "UninstallString" "$INSTDIR\uninstall.exe"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Master Search" "InstallLocation" "$INSTDIR"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Master Search" "DisplayVersion" "2025.11.20"
    WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Master Search" "Publisher" "LOONY-TECH"
    
SectionEnd

; Uninstall Section
Section "Uninstall"
    ; Remove files
    Delete "$INSTDIR\Master_Search.exe"
    Delete "$INSTDIR\MasterSearch_CLI.exe"
    Delete "$INSTDIR\uninstall.exe"
    
    ; Remove directories
    RMDir "$INSTDIR"
    
    ; Remove Start Menu shortcuts
    Delete "$SMPROGRAMS\Master Search\Master Search.lnk"
    Delete "$SMPROGRAMS\Master Search\Master Search CLI.lnk"
    Delete "$SMPROGRAMS\Master Search\Uninstall.lnk"
    RMDir "$SMPROGRAMS\Master Search"
    
    ; Remove Desktop shortcuts
    Delete "$DESKTOP\Master Search.lnk"
    Delete "$DESKTOP\Master Search CLI.lnk"
    
    ; Remove from PATH
    EnVar::DeleteValue "PATH" "$INSTDIR"
    
    ; Remove registry entries
    DeleteRegKey HKLM "Software\Master Search"
    DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\Master Search"
    
SectionEnd

; Language Strings
LangString DESC_MainProgram ${LANG_ENGLISH} "Master Search - Professional file search tool"
LangString DESC_MainProgram ${LANG_GERMAN} "Master Search - Professionelles Datei-Suchwerkzeug"
