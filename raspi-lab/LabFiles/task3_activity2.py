import RPi.GPIO as GPIO
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED and GPIO12 for switch
led = 23
switch = 12

# Set GPIO23 as output.
GPIO.setup(led, GPIO.OUT)

# Set GPIO12 as input
GPIO.setup(switch, GPIO.IN, GPIO.PUD_DOWN)

"""
TO DO 3.4 
this function turns on the LED at led 
waits for duration t
turns off the LED
waits for duration t
"""

def blink( t, led ):
    pass 

    
frequency = float(input("enter the frequency of blinks in cycles per second"))

while True:
 
    """
    TO DO 3.5 from the frequency, calculate the period 
    TO DO 3.6 if the switch is closed, execute the function blink,
                else, switch off the led 
    """ 
    pass 



