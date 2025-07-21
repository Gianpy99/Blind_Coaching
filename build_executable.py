"""
Blind Coaching Standalone Application - Executable Version
A complete self-contained coaching application based on the GROW model

This script creates a Windows executable (.exe) file that can be distributed
without requiring Python installation on the target machine.

Requirements:
- PyInstaller: pip install pyinstaller
- Flask: pip install flask

Build Instructions:
1. Install requirements: pip install flask pyinstaller
2. Run this script to create the executable
3. The executable will be created in the 'dist' folder
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages."""
    packages = ['flask', 'pyinstaller']
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
            return False
    return True

def create_executable():
    """Create executable using PyInstaller."""
    script_name = "blind_coaching_standalone.py"
    
    if not os.path.exists(script_name):
        print(f"❌ {script_name} not found in current directory")
        return False
    
    print("🔨 Creating executable with PyInstaller...")
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--onefile',                    # Create a single executable file
        '--windowed',                   # No console window (for GUI apps)
        '--name', 'BlindCoachingApp',   # Name of the executable
        '--icon', 'NONE',               # No icon (can be added later)
        '--add-data', 'coaching_questions.txt;.',  # Include questions file if exists
        script_name
    ]
    
    # If coaching_questions.txt doesn't exist, remove the add-data option
    if not os.path.exists('coaching_questions.txt'):
        cmd = [c for c in cmd if not c.startswith('coaching_questions.txt')]
        cmd = [c for c in cmd if c != '--add-data']
    
    try:
        subprocess.check_call(cmd)
        print("✅ Executable created successfully!")
        print("📁 Location: dist/BlindCoachingApp.exe")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create executable: {e}")
        return False

def create_installer_batch():
    """Create a batch file for easy installation."""
    batch_content = """@echo off
echo Installing Blind Coaching Application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Install required packages
echo Installing Flask...
pip install flask

echo.
echo Creating executable...
python build_executable.py

echo.
echo Build complete! Check the 'dist' folder for BlindCoachingApp.exe
pause
"""
    
    try:
        with open('install.bat', 'w') as f:
            f.write(batch_content)
        print("✅ Created install.bat for easy installation")
    except Exception as e:
        print(f"❌ Failed to create install.bat: {e}")

def main():
    print("🎯 Blind Coaching - Executable Builder")
    print("=" * 40)
    
    print("This will create a standalone executable (.exe) file.")
    print("The executable can be run on any Windows machine without Python.")
    print()
    
    # Ask user if they want to install requirements
    response = input("Install required packages (flask, pyinstaller)? (y/n): ").lower()
    if response == 'y':
        if not install_requirements():
            print("❌ Failed to install requirements. Please install manually:")
            print("   pip install flask pyinstaller")
            return
    
    print()
    print("Creating executable...")
    
    if create_executable():
        print()
        print("🎉 Build successful!")
        print("📁 Your executable is located at: dist/BlindCoachingApp.exe")
        print()
        print("Distribution Instructions:")
        print("1. Copy BlindCoachingApp.exe to any Windows computer")
        print("2. Run the executable to start the coaching application")
        print("3. The app will open in your default web browser")
        print("4. No Python installation required on target machine!")
        
        # Create installer batch file
        create_installer_batch()
        
    else:
        print("❌ Build failed. Please check the error messages above.")

if __name__ == "__main__":
    main()
