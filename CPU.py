# Restart the computer
# Shutdown the computer
# Get the CPU usage
# Get CPU battery

import pyttsx3
import os
import psutil
import time


def cpuUsage():
         usage=str(psutil.cpu_percent())
         pyttsx3.speak("Present CPU usage is "+usage)
         time.sleep(5)
    
def cpuBattery():
        battery=psutil.sensors_battery()
        pyttsx3.speak("Present CPU battery is")
        pyttsx3.speak(battery.percent)
        time.sleep(5)

def restart():
        pyttsx3.speak("Restarting system")
        os.system("shutdown /r /t 1")

def shutdown():
        pyttsx3.speak("Shutdown begins now")
        os.system("shutdown /s /t 1")

