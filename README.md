# 👀 EyeUn-Slop
**What the hell is this?** A no-bullshit eye break reminder program built on Python for developers and users who are concerned about their eye health but can't tolerate annoying alarms every 20 minutes.

## ✨ Why is this special?
It is special because of the following features:

* **Focus-Oriented**: The most important feature of this program is that it is not *annoying*. Instead of shocking the user with a sudden *beep* or an alarm, it simply reduces the brightness of the first monitor of the user by 10 percent with a gentle notification sound for 20 seconds, and then turns it back to normal. In this way, it gently notifies the user to take a break, instead of occasionally giving the user a unwanted shot of adrenaline affecting the focus of the user.

* **Notification System**: It sends a notification if things go wrong, instead of silently failing in the background.

* **Linux-Exclusive:** On Linux KDE and GNOME desktop environments, it keeps checking whether the screen is locked or not. If the screen is locked in the current session due to user inactivity, it updates the break-reminder timer, such that the user gets the break exactly after 20 minutes after returning from AFK.

## 📋 Prerequisites
The **DDC/CI** should be enabled in the monitor settings, for the brightness change to happen.

#### Windows:
Nothing specific is needed on Windows for this program.

#### Linux:
For Debian/Mint/Ubuntu users:

`sudo apt install light libnotify-bin gstreamer1.0-plugins-base`

For Fedora/Red Hat (RHEL)/CentOS users:

`sudo dnf install light libnotify gstreamer1-plugins-base`

For Arch/Manjaro users:

`sudo pacman -S light libnotify gst-plugins-base`

## 🛠️ Installation

### Step 1: Clone the repository
First you need to clone the repository:

`git clone https://github.com/faz-mandb/EyeUn-Slop.git`

### Step 2: Running EyeUn-Slop
#### In Windows:
Navigate to the *"EyeUn-Slop"* folder and double click on the *"run.bat"* file. Initialization is confirmed via a system notification upon startup. To stop the program, just double click on the *"stop.bat"* in the *"EyeUn-Slop"* folder.
#### In Linux:
Navigate to the *"EyeUn-Slop"* folder and open terminal there. Then type:

`chmod +x ./run.sh && chmod +x ./stop.sh`

Then to start the script, type:

`./run.sh`

Initialization is confirmed via a system notification upon startup. To stop the *EyeUn-Slop* program, just execute the *"stop.sh"* shell script in the *"EyeUn-Slop"* folder by opening the terminal there and typing:

`./stop.sh`

## 🚨 Important

* In Linux, it is recommended to use **Screen Locking** in the desktop environment for the working of the idleness detector. Modern compositors like *Wayland* do not support key-logging, so the only way to make the idleness detector to work is to check the *screen locked state* to detect user idleness. It is also better to reduce the screen lock intervals to 10 minutes or 5 minutes for the smooth working of the program.

* This program was created and tested on Linux Fedora KDE. So issues may be expected in Windows or other distros and desktop environments.

## 🚧 To-do

* The **Windows idleness detector** to check the idleness of the user by keylogging.

* The **idleness detector** support for other popular distribution like XFCE, Cinnamon, etc.

* A **system-tray icon** for *EyeUn-Slop*.

## 🤝 Contributing
Since this project is still in progress. Help with any of the goals in the *To-do* list will be appreciated.

## 🐞 Found a bug?
If the app is acting up or the "slop" has hit the fan, please report it so I can fix it.

To help me out, please include:
* **Your OS** (e.g., Windows 11, Ubuntu 24.04)
* **Desktop Environment** (e.g., KDE Plasma, GNOME, XFCE)
* **Error output** (They will be printed in the .log file in the project directory.)

👉 **[Click here to open an issue](https://github.com/faz-mandb/EyeUn-Slop/issues)**

## 📄 License
Distributed under the MIT license.


