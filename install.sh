#!/bin/bash

# Blind Coaching App - macOS/Linux Installer
# Creates a standalone executable for macOS and Linux systems

echo "==============================================="
echo "    Blind Coaching App - Quick Installer"
echo "==============================================="
echo

# Check if Python is installed
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo
    echo "Please install Python 3 from: https://python.org"
    echo "On macOS: brew install python3"
    echo "On Ubuntu/Debian: sudo apt install python3 python3-pip"
    echo "On CentOS/RHEL: sudo yum install python3 python3-pip"
    exit 1
fi

echo "[OK] Python 3 found"
echo

# Check if pip is available
echo "Checking pip..."
if ! command -v pip3 &> /dev/null; then
    echo "[ERROR] pip3 is not available"
    echo "Please install pip3"
    exit 1
fi

echo "[OK] pip3 found"
echo

# Install Flask
echo "Installing Flask..."
pip3 install flask
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install Flask"
    exit 1
fi

echo "[OK] Flask installed"
echo

# Install PyInstaller
echo "Installing PyInstaller..."
pip3 install pyinstaller
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install PyInstaller"
    exit 1
fi

echo "[OK] PyInstaller installed"
echo

# Check if main script exists
if [ ! -f "blind_coaching_standalone.py" ]; then
    echo "[ERROR] blind_coaching_standalone.py not found"
    echo "Please ensure all files are in the same directory"
    exit 1
fi

echo "[OK] Main script found"
echo

# Create executable
echo "Creating standalone executable..."
echo "This may take a few minutes..."
echo

# For macOS, create an app bundle; for Linux, create a binary
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    pyinstaller --onefile --name BlindCoachingApp --windowed blind_coaching_standalone.py
    APP_PATH="dist/BlindCoachingApp"
else
    # Linux
    pyinstaller --onefile --name BlindCoachingApp blind_coaching_standalone.py
    APP_PATH="dist/BlindCoachingApp"
fi

if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to create executable"
    exit 1
fi

echo
echo "==============================================="
echo "           BUILD SUCCESSFUL!"
echo "==============================================="
echo
echo "Your standalone application has been created:"
echo "Location: $APP_PATH"
echo

if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "DISTRIBUTION INSTRUCTIONS (macOS):"
    echo "1. Copy BlindCoachingApp to any macOS computer"
    echo "2. Double-click to run (no Python required!)"
    echo "3. The app will open in your web browser"
    echo "4. Complete your coaching session"
    echo "5. Download your session report"
    echo
    echo "Note: On first run, you may need to allow the app"
    echo "in System Preferences > Security & Privacy"
else
    echo "DISTRIBUTION INSTRUCTIONS (Linux):"
    echo "1. Copy BlindCoachingApp to any Linux computer"
    echo "2. Make executable: chmod +x BlindCoachingApp"
    echo "3. Run: ./BlindCoachingApp"
    echo "4. The app will open in your web browser"
    echo "5. Complete your coaching session"
    echo "6. Download your session report"
fi

echo
echo "The executable is completely self-contained and"
echo "can be shared with anyone running the same operating system."
echo
echo "Press Enter to run the application now..."
read

if [ -f "$APP_PATH" ]; then
    echo "Starting application..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open "$APP_PATH"
    else
        chmod +x "$APP_PATH"
        "$APP_PATH" &
    fi
else
    echo "Executable not found in expected location"
fi

echo
echo "Installation complete!"
