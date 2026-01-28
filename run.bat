@echo off 
setlocal 
cd /d %~dp0

if not exist ".venv" (
    python -m venv .venv
    call .venv\Scripts\activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
) else (
    call .venv\Scripts\activate
)

start /b "" .venv\Scripts\pythonw.exe src\eye_unslop.py > NUL 2>&1
exit