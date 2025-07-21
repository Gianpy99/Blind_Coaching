@echo off
echo ===============================================
echo  Blind Coaching App - Clean Environment
echo    (Creates executable without conflicts)
===============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Create clean virtual environment
echo Creating clean virtual environment...
if exist "venv_build" rmdir /s /q "venv_build"
python -m venv venv_build

if errorlevel 1 (
    echo [ERROR] Could not create virtual environment
    pause
    exit /b 1
)

echo [OK] Virtual environment created
echo.

REM Activate virtual environment and install packages
echo Installing packages in clean environment...
call venv_build\Scripts\activate.bat

pip install flask
if errorlevel 1 (
    echo [ERROR] Could not install Flask
    call deactivate
    pause
    exit /b 1
)

pip install pyinstaller
if errorlevel 1 (
    echo [ERROR] Could not install PyInstaller
    call deactivate
    pause
    exit /b 1
)

echo [OK] Packages installed in clean environment
echo.

REM Create executable
echo Creating executable...
echo This will take a few minutes...
echo.

REM Clean previous builds
if exist "build" rmdir /s /q "build" 2>nul
if exist "dist" rmdir /s /q "dist" 2>nul
if exist "*.spec" del "*.spec" 2>nul

pyinstaller --onefile --name "BlindCoachingApp" --windowed blind_coaching_standalone.py

call deactivate

if errorlevel 1 (
    echo [ERROR] Build failed even in clean environment
    echo.
    echo Your system might have specific conflicts.
    echo.
    echo RECOMMENDED SOLUTION:
    echo Run the Python script directly (it works perfectly):
    echo   python blind_coaching_standalone.py
    echo.
    echo The app will work exactly the same, just needs Python installed.
    pause
    exit /b 1
)

REM Check if executable was created
if not exist "dist\BlindCoachingApp.exe" (
    echo [ERROR] Executable not found
    pause
    exit /b 1
)

echo.
echo ===============================================
echo           BUILD SUCCESSFUL!
echo ===============================================
echo.
echo Standalone executable created: dist\BlindCoachingApp.exe
echo.

REM Test the executable
echo Testing executable...
start dist\BlindCoachingApp.exe

echo.
echo If the app opened in your browser, the build was successful!
echo.
echo The .exe file can now be distributed to any Windows computer.
echo No Python installation required on target machines.
echo.

REM Clean up build environment
echo Cleaning up build environment...
rmdir /s /q "venv_build" 2>nul
rmdir /s /q "build" 2>nul

echo.
echo BUILD COMPLETE!
echo Location: dist\BlindCoachingApp.exe
echo.
pause
