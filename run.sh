#!/bin/bash

cd "$(dirname "$0")"

if [ ! -d .venv ]; then
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

else 
    source .venv/bin/activate

fi

nohup python3 src/eye_unslop.py > /dev/null 2>&1 &