@echo off
echo ===============================================
echo    Blind Coaching App - Anaconda Fix
echo ===============================================
echo.

echo Fixing Anaconda conflicts for PyInstaller...
echo.

REM Remove problematic pathlib package
echo Removing obsolete pathlib package...
conda remove pathlib -y 2>nul

REM Clean pip cache
echo Cleaning pip cache...
pip cache purge 2>nul

REM Try to fix the pyodbc issue too
echo Fixing pyodbc version issue...
conda remove pyodbc -y 2>nul
conda install pyodbc -y 2>nul

echo.
echo Anaconda environment cleaned.
echo Now running the executable builder...
echo.

.\build_exe.bat
