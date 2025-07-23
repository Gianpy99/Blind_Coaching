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
echo [1] Run Application Now
echo [2] Edit Coaching Questions
echo [3] View Documentation
echo [4] Exit
echo.
set /p choice="Choose an option (1-4): "

if "%choice%"=="1" goto run_app
if "%choice%"=="2" goto edit_questions
if "%choice%"=="3" goto docs
if "%choice%"=="4" goto exit

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

:edit_questions
echo.
echo ===============================================
echo           EDIT COACHING QUESTIONS
echo ===============================================
echo.
echo Opening coaching_questions.txt for editing...
echo.
echo You can modify the coaching questions and save the file.
echo The changes will be applied immediately when you restart the app.
echo.
if exist "coaching_questions.txt" (
    notepad coaching_questions.txt
) else (
    echo coaching_questions.txt not found
)
goto menu

:docs
echo.
echo ===============================================
echo             DOCUMENTATION
echo ===============================================
echo.
echo Opening README.md - Complete documentation and guide
echo.
if exist "README.md" (
    notepad README.md
) else (
    echo README.md not found
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
echo QUICK TIPS:
echo - Modify coaching_questions.txt to customize questions
echo - Use Option 2 to easily edit questions with Notepad
echo - The app runs in your web browser at localhost:5000
echo - Press Ctrl+C in the terminal to stop the application
echo.
echo For support: Check the documentation files
echo.
pause

:start
cls
goto :eof
