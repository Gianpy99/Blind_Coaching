@echo off
echo ===============================================
echo    Blind Coaching App - Quick Installer
echo ===============================================
echo.

REM Check if Python is installed
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://python.org
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Check if pip is available
echo Checking pip...
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available
    echo Please ensure pip is installed with Python
    pause
    exit /b 1
)

echo [OK] pip found
echo.

REM Install Flask
echo Installing Flask...
pip install flask
if errorlevel 1 (
    echo [ERROR] Failed to install Flask
    pause
    exit /b 1
)

echo [OK] Flask installed
echo.

REM Install PyInstaller
echo Installing PyInstaller...
pip install pyinstaller
if errorlevel 1 (
    echo [ERROR] Failed to install PyInstaller
    pause
    exit /b 1
)

echo [OK] PyInstaller installed
echo.

REM Check if main script exists
if not exist "blind_coaching_standalone.py" (
    echo [ERROR] blind_coaching_standalone.py not found
    echo Please ensure all files are in the same directory
    pause
    exit /b 1
)

echo [OK] Main script found
echo.

REM Create executable
echo Creating standalone executable...
echo This may take a few minutes...
echo.

pyinstaller --onefile --name BlindCoachingApp --windowed blind_coaching_standalone.py

if errorlevel 1 (
    echo [ERROR] Failed to create executable
    pause
    exit /b 1
)

echo.
echo ===============================================
echo           BUILD SUCCESSFUL!
echo ===============================================
echo.
echo Your standalone application has been created:
echo Location: dist\BlindCoachingApp.exe
echo.
echo DISTRIBUTION INSTRUCTIONS:
echo 1. Copy BlindCoachingApp.exe to any Windows computer
echo 2. Double-click to run (no Python required!)
echo 3. The app will open in your web browser
echo 4. Complete your coaching session
echo 5. Download your session report
echo.
echo The executable is completely self-contained and
echo can be shared with anyone running Windows.
echo.
echo Press any key to run the application now...
pause >nul

if exist "dist\BlindCoachingApp.exe" (
    echo Starting application...
    start dist\BlindCoachingApp.exe
) else (
    echo Executable not found in expected location
)

echo.
echo Installation complete!
pause
