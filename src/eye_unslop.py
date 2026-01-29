import platform
from time import sleep, monotonic
import atexit
from logging.handlers import RotatingFileHandler
import logging
import signal
import sys
import types

import screen_brightness_control as sbc
from playsound3 import playsound
from notifypy import Notify

from linux_backend import is_screen_locked

from config import (SOUND_PATH, LOG_PATH, LOG_SIZE, TARGET_REDUCTION,
                    BREAK_INTERVAL, SLEEP_INTERVAL, BREAK_DURATION, FALLBACK_BRIGHTNESS)

                    
handler_ = RotatingFileHandler(
    LOG_PATH,
    maxBytes=LOG_SIZE,
    backupCount=0
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[handler_]
)

logging.info("[RUNNING]")

logging.getLogger('screen_brightness_control').setLevel(logging.CRITICAL)

def display_notification(message: str, urgency: str = "normal", title: str = "An error occured.") -> None:
    """
    Notify the user when something goes wrong with the program.
    
    Makes sure the user knows what error occured instead of blindly
    terminating the program.
    """
    
    notification = Notify(default_notification_application_name="EyeUn-Slop")
    notification.title = title
    notification.message = message
    notification.urgency = urgency
    notification.send()
    
display_notification("Protecting your eyes from the background", title="EyeUn-Slop started.")    
    
try:
    #Get user's current screen brightness
    default_brightness = sbc.get_brightness(display=0)[0] 
    
except Exception as e:
    default_brightness = FALLBACK_BRIGHTNESS
    display_notification("Can't get current screen bightness....")
    logging.info(f"[ERROR][PASS 1] Can't get current brightness")

def is_idle() -> bool:
    """
    Check if the user or session is idle.
    
    For Linux: Evaluates idleness based on whether the screen
    is locked or not.
    
    .. note::
       Windows implementation is a placeholder and 
       will always return 'False'. Mac is not supported.
    """
    
    if platform.system() == "Linux":
        return is_screen_locked()
    
    if platform.system() == "Windows":
        return False

        #TODO: Add Windows user idleness detection system using key-logging.
    
    return False

def transient_dimming() -> None:
    """
    Dim brightness low for 20 seconds as a visual reminder with a 
    gentle notification sound.
    """
    
    global default_brightness
    
    # Updates the brightness if the user changes the brightness
    # during the working of the program
    try:
        default_brightness = sbc.get_brightness()[0]
    except:
        display_notification("Couldn't get current screen brightness....")
        logging.info("[ERROR][PASS 2] Can't get current screen brighteness")
    
    try:
        playsound(str(SOUND_PATH), block=False)
    except Exception as e:
        logging.info(f"[ERROR] {e}")
    
    # Won't let the brightness shift to a negative value
    target_brightness = max(0, (default_brightness - TARGET_REDUCTION)) 
    try:
        sbc.set_brightness(target_brightness)
        sleep(BREAK_DURATION)
        sbc.set_brightness(default_brightness)
        playsound(str(SOUND_PATH), block=False)
        
    except Exception as e:
        display_notification("Can't make any changes brightness. It's break time.", title="EyeUn-Slop time!")
        logging.info(f"[ERROR] {e}")
        
def main() -> None:
    """
    Execute the primary application loop for 20-20-20 rule.
    
    Uses the 'time.monotonic()' to get the accurate elapsed time
    which is not influenced by the system time. It sets a reminder
    every 20 minutes following the 20-20-20 rule.
    """
    
    next_dip = monotonic() + BREAK_INTERVAL
    
    while True:
            if is_idle():
                next_dip = monotonic() + BREAK_INTERVAL
            
            elif monotonic() >= next_dip:
                logging.info("Eye break time.")
                transient_dimming()
                logging.info("Eye break ends.")
                
                next_dip = monotonic() + BREAK_INTERVAL
                
            sleep(SLEEP_INTERVAL)
        
def at_exit(exit_msg: str = "Program terminated successfully.") -> None:
    """
    Exit the program safely by turning the brightness back to normal
    and display a termination notification.
    """
        
    sbc.set_brightness(default_brightness)
    display_notification(exit_msg, title="Program terminated.")   
    logging.info("[STOPPED]")
    
def signal_handler(signum: int, frame: types.FrameType) -> None:
    """Ensure safe termination of the program to execute the exit notificaiton"""
    sys.exit()
    
atexit.register(at_exit)

# Handling exit signals for linux
signals_to_handle = [signal.SIGTERM, signal.SIGHUP, signal.SIGINT]

for signal_ in signals_to_handle:
    try:
        signal.signal(signal_, signal_handler)
    except:
        #If the operating system is windows, then do nothing
        pass
        
if __name__ == "__main__":
    logging.info("Program started.")
    main()