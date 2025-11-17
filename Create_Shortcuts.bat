@echo off
REM Master Search - Create Shortcuts Batch Script
REM Double-click this file after installing Master Search to create shortcuts

echo [INFO] Creating Master Search shortcuts...
echo.

REM Get Python executable path
for /f "delims=" %%i in ('where python') do set PYTHON_PATH=%%i

if "%PYTHON_PATH%"=="" (
    echo [ERROR] Python not found in PATH
    echo Please make sure Python is installed and added to PATH
    pause
    exit /b 1
)

echo [INFO] Using Python: %PYTHON_PATH%
echo.

REM Get the script directory (one level up from this batch file)
cd /d "%~dp0"

REM Run the shortcut creation script
"%PYTHON_PATH%" scripts\create_shortcuts.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Failed to create shortcuts
    echo Please try running as Administrator
    pause
    exit /b 1
) else (
    echo.
    echo [OK] Shortcuts created successfully!
    echo You can now find Master Search in:
    echo   - Start Menu
    echo   - Desktop
    pause
    exit /b 0
)
