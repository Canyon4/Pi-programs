import tm1637
import RPi.GPIO as GPIO
import time
import sys

display = tm1637.TM1637(clk=24, dio=18)

try:
    while True:
        user_input = sys.argv[1]
        time.sleep(1)
        display.scroll("Hello "+str(user_input), delay=250)
        display.clear()
        time.sleep(2)
except KeyboardInterrupt:

    GPIO.cleanup()
    
