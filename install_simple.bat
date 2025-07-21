@echo off
echo ===============================================
echo    Blind Coaching App - Simple Installer
echo      (For environments with pip issues)
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

REM Check if main script exists
if not exist "blind_coaching_standalone.py" (
    echo [ERROR] blind_coaching_standalone.py not found
    echo Please ensure all files are in the same directory
    pause
    exit /b 1
)

echo [OK] Main script found
echo.

REM Test if Flask is available
echo Testing Flask availability...
python -c "import flask; print('Flask version:', flask.__version__)" 2>nul
if errorlevel 1 (
    echo [WARNING] Flask not detected, but the app might still work
    echo The application has fallback mechanisms
) else (
    echo [OK] Flask is available
)

echo.

REM Try to run the application directly
echo ===============================================
echo        RUNNING APPLICATION DIRECTLY
echo ===============================================
echo.
echo Starting Blind Coaching Application...
echo If Flask is properly installed, the app will open in your browser.
echo If not, you'll see instructions for manual Flask installation.
echo.
echo Press Ctrl+C to stop the application when done.
echo.

python blind_coaching_standalone.py

echo.
echo ===============================================
echo           APPLICATION STOPPED
echo ===============================================
echo.
echo If the application worked correctly, you're all set!
echo.
echo If you saw Flask-related errors, please install Flask manually:
echo   pip install flask
echo   or try: python -m pip install flask
echo   or try: conda install flask (if using Anaconda)
echo.
echo Then run this installer again or run the app directly:
echo   python blind_coaching_standalone.py
echo.
pause
