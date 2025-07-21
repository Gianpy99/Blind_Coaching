@echo off
echo ===============================================
echo  Blind Coaching App - Console Test Version
echo ===============================================
echo.

echo Creating test executable (with console)...
echo This version will show a console window for debugging.
echo.

REM Activate virtual environment
call venv_build\Scripts\activate.bat

REM Clean previous builds
if exist "build" rmdir /s /q "build" 2>nul
if exist "dist" rmdir /s /q "dist" 2>nul
if exist "*.spec" del "*.spec" 2>nul

REM Create executable without windowed flag (shows console)
pyinstaller --onefile --name "BlindCoachingApp_Console" blind_coaching_standalone.py

call deactivate

if errorlevel 1 (
    echo [ERROR] Build failed
    pause
    exit /b 1
)

echo.
echo Test executable created: dist\BlindCoachingApp_Console.exe
echo.
echo This version includes a console window for debugging.
echo If it works, we can create the windowed version later.
echo.

pause
