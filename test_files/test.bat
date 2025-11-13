@echo off
REM This is a test batch file
echo Running test script
set TEST_VAR=test_value
if "%TEST_VAR%"=="test_value" (
    echo Test passed
) else (
    echo Test failed
)
pause