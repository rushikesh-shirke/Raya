@echo off
echo Uninstalling Raya...

:: Remove Registry Key
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "RayaApp" /f

:: Kill the process if running
taskkill /f /im Raya.exe

echo Raya has been removed from Windows Startup and killed.
pause
