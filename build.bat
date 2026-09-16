@echo off
echo Installing PyInstaller just in case...
py -m pip install pyinstaller
echo Building Raya...
py -m PyInstaller --onefile --windowed --name Raya src\main.py
if exist dist\Raya.exe (
    move /Y dist\Raya.exe .
    rmdir /S /Q build
    rmdir /S /Q dist
    del Raya.spec
    echo Build complete! Raya.exe is now in the current directory.
) else (
    echo Build failed. See output above.
)
pause
