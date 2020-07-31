#!/usr/bin/env python3

import subprocess
import time
import RPi.GPIO as GPIO # always needed with RPi.GPIO

#from gpiozero import OutputDevice


#ON_THRESHOLD = 65  # (degrees Celsius) Fan kicks on at this temperature.
#OFF_THRESHOLD = 55  # (degress Celsius) Fan shuts off at this temperature.
TARGETTEMP = 60       # TEMPERATURA PENTRU PWM50%
HIST = 10              # histerezis temperatura
SLEEP_INTERVAL = 5  # (seconds) How often we check the core temperature.
GPIO_PIN = 4  # Which GPIO pin you're using to control the fan.

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
GPIO.setup(GPIO_PIN, GPIO.OUT)# set GPIO pin as an output. You can use any GPIO port
p = GPIO.PWM(GPIO_PIN, 50)    # create an object p for PWM at 50 Hertz  
                        # you can have more than one of these, but they need  
                        # different names for each port   
                        # e.g. p1, p2, motor, servo1 etc.
p.start(0)             # start the PWM on 0 percent duty cycle


def get_temp():
    """Get the core temperature.

    Run a shell script to get the core temp and parse the output.

    Raises:
        RuntimeError: if response cannot be parsed.

    Returns:
        float: The core temperature in degrees Celsius.
    """
    output = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True)
    temp_str = output.stdout.decode()
    try:
        return float(temp_str.split('=')[1].split('\'')[0])
    except (IndexError, ValueError):
        raise RuntimeError('Could not parse temperature output.')


if __name__ == '__main__':
    # Validate the on and off thresholds
    #if OFF_THRESHOLD >= ON_THRESHOLD:
    #    raise RuntimeError('OFF_THRESHOLD must be less than ON_THRESHOLD')

    #fan = OutputDevice(GPIO_PIN)
    
    lastduty=0

    while True:
        temp = get_temp()

        # Start the fan if the temperature has reached the limit and the fan
        # isn't already running.
        # NOTE: `fan.value` returns 1 for "on" and 0 for "off"
        #if temp > ON_THRESHOLD and not fan.value:
            fan.on()

        # Stop the fan if the fan is running and the temperature has dropped
        # to 10 degrees below the limit.
        #elif fan.value and temp < OFF_THRESHOLD:
        #    fan.off()
        
        duty=(temp-(TARGETTEMP-HIST))*(100/(2*HIST))
        #print (duty)
        if duty < 0 :
            duty = 0
        elif duty <30 :
            duty = lastduty
        elif duty > 100 :
            duty = 100
        lastduty = duty
            
        p.ChangeDutyCycle(duty)
        
        
        time.sleep(SLEEP_INTERVAL)
