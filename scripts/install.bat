@echo off
echo Installing Raya to Windows Startup...

:: Get the directory of the script and resolve the path to the executable
set "SCRIPT_DIR=%~dp0"
set "EXE_PATH=%SCRIPT_DIR%..\Raya.exe"

if not exist "%EXE_PATH%" (
    echo Error: Raya.exe not found at %EXE_PATH%.
    echo Please run build.bat first to build the executable.
    pause
    exit /b
)

:: Add Registry Key
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "RayaApp" /t REG_SZ /d "\"%EXE_PATH%\"" /f
if %errorLevel% == 0 (
    echo Raya has been added to Windows Startup successfully!
) else (
    echo Failed to add Raya to Windows Startup.
)
pause
