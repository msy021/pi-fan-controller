#!/usr/bin/env python3

import RPi.GPIO as GPIO # always needed with RPi.GPIO
GPIO_PIN = 4  # Which GPIO pin you're using to control the fan.

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
GPIO.setup(GPIO_PIN, GPIO.OUT) # set GPIO 25 as an output. You can use any GPIO port
p = GPIO.PWM(GPIO_PIN, 50)    # create an object p for PWM on port 25 at 50 Hertz  
                        # you can have more than one of these, but they need  
                        # different names for each port   
                        # e.g. p1, p2, motor, servo1 etc.
p.start(0)             # start the PWM on 50 percent duty cycle
p.stop()                # stop the PWM output  

GPIO.cleanup()          # when your program exits, tidy up after yourself  
