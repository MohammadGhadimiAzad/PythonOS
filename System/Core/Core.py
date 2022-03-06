from asyncio.windows_events import NULL
import datetime
import platform
import json
import threading

from System.Core.FileSystem import fs_routines
from System.Core.KeysSystem import rg_routines
from System.Core.TaskSystem import ts_routines
from System.Utils.Utils import print_error, print_log, print_warning
from os.path import exists

Kernel_lvl = 8 # Main kernel variable, 8 by default

# Each screen has an ID
isBSOD = False        # Black screen of death 0
isRSOD = False        # Red screen of death 1
isGSOD = False        # Green screen of death 2

isBIOS = False        # bios screen 3
isINSTALLER = False   # installer screen 4

isBootloader = False  # Boot screen 5
isLogin = False       # Login screen 6
isDesktop = False     # Desktop screen 7
isBoot = False        # Boot the system 8

in_linux = False
in_windows = False
in_mac = False

# Start the boot order
def switch1(Kernel_lvl):
    if (Kernel_lvl == 0): isBSOD = True
    elif (Kernel_lvl == 1): isRSOD = True
    elif (Kernel_lvl == 2): isGSOD = True
    elif (Kernel_lvl == 3): isBIOS = True
    elif (Kernel_lvl == 4): isINSTALLER = True
    elif (Kernel_lvl == 5): isBootloader = True
    elif (Kernel_lvl == 6): isLogin = True
    elif (Kernel_lvl == 7): isDesktop = True
    elif (Kernel_lvl == 8): isBoot = True
    else:
        print_error("Invalid Kernel_lvl value, must be 0-8, STOPPING...")
        exit()
switch1(Kernel_lvl)

# Check base system (is running on linux, windows or mac)
def check_os():

    global in_linux, in_windows, in_mac

    if platform.system() == "Linux": in_linux = True
    elif platform.system() == "Windows": in_windows = True
    elif platform.system() == "Darwin": in_mac = True


# Routines, are the first tasks that are executed in the first seconds of system startup
def routines():

    check_os()

    print_log("----------- Starting system execution -----------")
    print_log("Started log at: " + str(datetime.datetime.now()))

    # In what os is running the system?
    if in_linux: print_log("Running on Linux")
    elif in_windows: print_log("Running on Windows")
    elif in_mac: print_log("Running on Mac")
    else: print_warning("Unknown OS, starting anyway...")

    # Load the registry.
    rg_routines()

    # Load the process system
    ts_routines()

    # Load the file system
    fs_routines()


def delete_logs():
    # Delete the files inside the Logs folder using the os module
    import os

    from System.Utils.Utils import print_info

    # Get the relative path of the Logs folder
    logs_path = os.path.join(os.getcwd(), "Logs")

    # Get the list of files inside the Logs folder
    logs_files = os.listdir(logs_path)

    # Print an information message
    print_info("Deleting files from the Logs folder")

    # Delete the files inside the Logs folder
    for file in logs_files:
        os.remove(os.path.join(logs_path, file))
        print(os.path.join(logs_path, file))


class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class GlobalObjects(metaclass=SingletonMeta):
    def save_setting(self, ip):
        settings_path = self.computer_name+".json"
        self.ip = ip

        with open(settings_path, 'w') as f:
            json.dump({
            "ip": ip
        }, f)
    
    def set_settings(self, computer_name = None, ip = None):
        self.computer_name = computer_name
        settings_path = computer_name+".json"
        self.os.title("Python OS [" + self.computer_name + "]")  # Window title.

        if (not exists(settings_path)):
            ip = input("Enter pc ip: ")
            self.save_setting(ip)
        else:
            f = open(settings_path)
            data = json.load(f)
            self.ip = data["ip"]
            f.close()

    def set_network(self, network : threading.Thread, port = None):
        if self.network == None:
            self.network = network

        if self.port == None:
            self.port = port
    
    def __init__(self, computer_name = None, ip = None):
        self.network = None
        self.port = None
        if computer_name != None:
            self.computer_name = computer_name
            settings_path = computer_name+".json"

            if (not exists(settings_path)):
                ip = input("Enter pc ip: ")
                self.save_setting(ip)
            else:
                f = open(settings_path)
                data = json.load(f)
                self.ip = data["ip"]
                f.close()
            
        import tkinter as tk
        self.os = tk.Tk()  # Create the window that will be the base of the program.
        self.os.title("Python OS")  # Window title.
        self.os.geometry("1024x600")  # Window size.
        self.os.resizable(False, False)  # Window resizing.


