
@echo off
:: Token Pressure Sandbox launcher

set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT=%SCRIPT_DIR%sandbox.py
set TEST_FILE=%SCRIPT_DIR%test_prompt.txt

if not exist "%PYTHON_SCRIPT%" (
    echo ERROR: sandbox.py not found in %SCRIPT_DIR%
    pause
    exit /b 1
)

echo Running Token Pressure Sandbox on test_prompt.txt...
python "%PYTHON_SCRIPT%" "%TEST_FILE%" --save-report
pause
