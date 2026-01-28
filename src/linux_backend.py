import os
import subprocess

def is_screen_locked() -> bool:
    """
    Check if the screen is locked.
    
    This function is Linux exclusive. Since Wayland, which is more modern and 
    advanced that X11, doesn't support keylogging, it monitors the 
    whether the screen is locked or not due to user inactivity to know
    if the user is AFK or not.
    
    :return: Returns 'True' if the screen lock is active, otherwise 'False'.
    :rtype: bool
    """
    
    # Gets the linux desktop environment
    desktop = os.environ.get("XDG_CURRENT_DESKTOP", "").upper()
    
    if "KDE" in desktop:
        # KDE exclusive command
        cmd = [
            "busctl", "--user", "call",
            "org.freedesktop.ScreenSaver",
            "/org/freedesktop/ScreenSaver",
            "org.freedesktop.ScreenSaver",
            "GetActive"
        ]
        
        # Runs command in the terminal and returns and output
        out = subprocess.run(cmd, capture_output=True, text=True) 
        
        return "true" in out.stdout.strip().lower()
    
    elif "GNOME" in desktop:
        # GNOME exclusive command
        cmd = [
            "busctl", "--user", "call",
            "org.gnome.ScreenSaver",
            "/org/gnome/ScreenSaver",
            "org.gnome.ScreenSaver",
            "GetActive"
        ]
        
        out = subprocess.run(cmd, capture_output=True, text=True)
        
        return "true" in out.stdout.strip().lower()
    
    else:
        return False
    
    #TODO: Include support for other famous distro environments 
    #like XFCE, Cinnamon, etc.
        