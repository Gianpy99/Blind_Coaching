@echo off
echo ===============================================
echo  Blind Coaching App - Executable Builder
echo      (Anaconda-friendly version)
echo ===============================================
echo.

REM Check if Python is installed
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [OK] Python found
echo.

REM Check if main script exists
if not exist "blind_coaching_standalone.py" (
    echo [ERROR] blind_coaching_standalone.py not found
    pause
    exit /b 1
)

echo [OK] Main script found
echo.

REM Test Flask first
echo Testing Flask...
python -c "import flask" 2>nul
if errorlevel 1 (
    echo [INFO] Attempting to install Flask...
    
    REM Try different installation methods
    echo Trying: pip install flask --user
    pip install flask --user >nul 2>&1
    
    if errorlevel 1 (
        echo Trying: conda install flask -y
        conda install flask -y >nul 2>&1
    )
    
    REM Test again
    python -c "import flask" 2>nul
    if errorlevel 1 (
        echo [ERROR] Could not install Flask
        echo.
        echo Please install Flask manually:
        echo   Method 1: pip install flask --user
        echo   Method 2: conda install flask
        echo   Method 3: pip install flask --force-reinstall --no-deps
        echo.
        echo Then run this script again.
        pause
        exit /b 1
    )
)

echo [OK] Flask is available
echo.

REM Test/Install PyInstaller
echo Testing PyInstaller...
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [INFO] Installing PyInstaller...
    
    REM Try user installation first (safer with Anaconda)
    pip install pyinstaller --user
    if errorlevel 1 (
        echo Trying alternative installation...
        conda install pyinstaller -c conda-forge -y
        if errorlevel 1 (
            echo [ERROR] Could not install PyInstaller
            echo.
            echo Please install PyInstaller manually:
            echo   pip install pyinstaller --user
            echo   or: conda install pyinstaller -c conda-forge
            echo.
            pause
            exit /b 1
        )
    )
)

echo [OK] PyInstaller is available
echo.

REM Create executable
echo ===============================================
echo           CREATING EXECUTABLE
echo ===============================================
echo.
echo This will create a standalone .exe file that can be
echo distributed to any Windows computer without Python.
echo.
echo Building... (this may take 3-5 minutes)
echo.

REM Clean previous builds
if exist "build" rmdir /s /q "build" 2>nul
if exist "dist" rmdir /s /q "dist" 2>nul
if exist "*.spec" del "*.spec" 2>nul

REM Build with PyInstaller
pyinstaller --onefile --name "BlindCoachingApp" --windowed blind_coaching_standalone.py

if errorlevel 1 (
    echo.
    echo [ERROR] Build failed!
    echo.
    echo This might be due to:
    echo 1. PyInstaller conflicts with Anaconda
    echo 2. Antivirus blocking the build process
    echo 3. Insufficient permissions
    echo.
    echo ALTERNATIVE: Run the Python script directly
    echo   python blind_coaching_standalone.py
    echo.
    pause
    exit /b 1
)

REM Check if executable was created
if not exist "dist\BlindCoachingApp.exe" (
    echo [ERROR] Executable not found after build
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
echo Size: 
dir dist\BlindCoachingApp.exe | findstr BlindCoachingApp.exe
echo.
echo TESTING THE EXECUTABLE:
echo.
echo Press Enter to test the executable now...
pause >nul

echo Starting BlindCoachingApp.exe...
start dist\BlindCoachingApp.exe

echo.
echo If the application opened in your browser, the build was successful!
echo.
echo DISTRIBUTION:
echo - Copy dist\BlindCoachingApp.exe to any Windows computer
echo - No Python installation required on target machines
echo - The app will open in the default web browser
echo.
echo BUILD COMPLETE!
pause
