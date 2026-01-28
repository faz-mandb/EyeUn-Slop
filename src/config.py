from pathlib import Path

#---------------Program Config------------------

TARGET_REDUCTION = 20
BASE_DIR = Path(__file__).resolve().parent.parent 
SOUND_PATH = BASE_DIR / "assets" / "notification.mp3"
LOG_PATH = BASE_DIR / "linux_ecr.log"
LOG_SIZE = 1_000_000 #bytes
BREAK_INTERVAL = 20 * 60 #sec
SLEEP_INTERVAL = 1 #sec
BREAK_DURATION = 20 #sec
FALLBACK_BRIGHTNESS = 50

#-----------------------------------------------