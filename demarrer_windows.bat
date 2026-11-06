@echo off
cd /d "%~dp0"
echo.
echo Mandarin Integral - 30 lecons
where python >nul 2>&1
if %errorlevel% equ 0 (python -m http.server 8000) else (py -m http.server 8000)
pause
