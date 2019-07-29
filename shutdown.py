# This file needs to be start with root rights or as user pi with sudo at boot
#
#The script listens to GPIO 22 wheter the attached wemos pulls up D5 for shutting down the Rpi
#
# ToDo: atreboot handler should be written

import RPi.GPIO as GPIO
import time
from subprocess import call
GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while True: 
    if (GPIO.input(24) == True):
        count = count + 1
        time.sleep(.1)
        if (count > 3):
            from subprocess import call
            call("sudo shutdown -h now", shell=True)
    else:
        count = 0
    time.sleep(.5);



