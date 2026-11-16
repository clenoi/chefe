@echo off
cd /d C:\Time3IA
start /min pythonw bracos.py
timeout /t 3 /nobreak >nul
start "" "time3-final.html"
exit