@echo off 
setlocal
cd /d %~dp0

if exist defaultbrightness.txt (
    set /p DEFAULT_BRIGHTNESS=<defaultbrightness.txt
    .venv\Scripts\python.exe -c "import screen_brightness_control as sbc; sbc.set_brightness(%DEFAULT_BRIGHTNESS%)"
    del defaultbrightness.txt
)

taskkill /F /FI "COMMANDLINE eq *eye_unslop.py*" /T > NUL 2>&1
exit