#define MyAppName "Master Search"
#define MyAppVersion "2025.11.13"
#define MyAppPublisher "LOONY-TECH"
#define MyAppURL "https://github.com/Loony2392/master-search"
#define MyAppExeName "MasterSearch.exe"
#define MyAppCliName "MasterSearchCLI.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{A1B2C3D4-E5F6-7890-ABCD-EF1234567890}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
LicenseFile=LICENSE
; Uncomment the following line to run in "modern" mode which adds an "I accept the license" checkbox and uses Modern UI styling.
; NOTE: This may not be compatible with versions prior to 2.0. Don't forget to also update the file extension in Output section below!
PrivilegesRequired=lowest
OutputBaseFilename=Master_Search_v{#MyAppVersion}_Windows_Setup
OutputDir=release_builds
Compression=lz4
SolidCompression=yes
WizardStyle=modern
UninstallDisplayIcon={app}\{#MyAppExeName}
SetupIconFile=media\master_search.ico
WizardSmallImageFile=media\wizard_small.bmp
WizardLargeImageFile=media\wizard_large.bmp

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "german"; MessagesFile: "compiler:Languages\German.isl"
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
; GUI Application
Source: "dist\MasterSearch.exe"; DestDir: "{app}"; Flags: ignoreversion
; CLI Application
Source: "dist\MasterSearchCLI.exe"; DestDir: "{app}"; Flags: ignoreversion
; Documentation
Source: "README.md"; DestDir: "{app}"; Flags: isreadme
Source: "CHANGELOG.md"; DestDir: "{app}"
Source: "LICENSE"; DestDir: "{app}"
; Additional files that may be needed
Source: "locales\*"; DestDir: "{app}\locales"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "media\*"; DestDir: "{app}\media"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{#MyAppName} CLI"; Filename: "{app}\{#MyAppCliName}"; Parameters: "--help"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]
procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // You can add post-installation code here if needed
    // For example: create shortcuts, register file types, etc.
  end;
end;

function PrepareToInstall(var NeedsRestart: Boolean): String;
begin
  // Check system requirements if needed
  Result := '';
end;

function ShouldSkipPage(PageID: Integer): Boolean;
begin
  Result := False;
end;
