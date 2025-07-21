@echo off
echo ===============================================
echo          BLIND COACHING APP v1.0
echo            Distribution Package
echo ===============================================
echo.
echo Welcome to the Blind Coaching Application!
echo.
echo This package contains everything you need to run
echo a professional coaching session using the GROW model.
echo.
echo ===============================================
echo             QUICK START OPTIONS
echo ===============================================
echo.
echo [1] Run Application (Requires Python)
echo [2] Install and Create Executable
echo [3] Run Simple Installer
echo [4] View Documentation
echo [5] Exit
echo.
set /p choice="Choose an option (1-5): "

if "%choice%"=="1" goto run_app
if "%choice%"=="2" goto create_exe
if "%choice%"=="3" goto simple_install
if "%choice%"=="4" goto docs
if "%choice%"=="5" goto exit

:run_app
echo.
echo ===============================================
echo         RUNNING APPLICATION DIRECTLY
echo ===============================================
echo.
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found
    echo Please install Python from https://python.org
    pause
    goto menu
)
echo Starting Blind Coaching Application...
echo The app will open in your web browser.
echo Press Ctrl+C to stop when done.
echo.
python blind_coaching_standalone.py
goto menu

:create_exe
echo.
echo ===============================================
echo        CREATING STANDALONE EXECUTABLE
echo ===============================================
echo.
echo This will create BlindCoachingApp.exe that can run
echo on any Windows computer without Python installed.
echo.
pause
call build_clean.bat
goto menu

:simple_install
echo.
echo ===============================================
echo           SIMPLE INSTALLATION
echo ===============================================
echo.
echo This will install Flask and run the application.
echo.
pause
call install_simple.bat
goto menu

:docs
echo.
echo ===============================================
echo             DOCUMENTATION FILES
echo ===============================================
echo.
echo Opening documentation...
if exist "README_Standalone.md" (
    notepad README_Standalone.md
) else (
    echo README_Standalone.md not found
)
if exist "PROJECT_SUCCESS.md" (
    notepad PROJECT_SUCCESS.md
) else (
    echo PROJECT_SUCCESS.md not found
)
goto menu

:menu
echo.
echo ===============================================
echo.
set /p continue="Return to menu? (y/n): "
if /i "%continue%"=="y" goto start
goto exit

:exit
echo.
echo Thank you for using Blind Coaching App!
echo.
echo For support or questions:
echo - Check the documentation files
echo - Review the Python script comments
echo - Modify coaching_questions.txt for custom questions
echo.
pause

:start
cls
goto :eof
