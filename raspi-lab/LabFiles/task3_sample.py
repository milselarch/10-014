import RPi.GPIO as GPIO
from time import sleep

# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED
led = 23

# Set GPIO23 as output.
GPIO.setup(led, GPIO.OUT)


while True:

    command = input("turn the switch on or off? [on/off/exit]")
    
    if command == "on":  
        GPIO.output(led, GPIO.HIGH)  # turn on the LED
    elif command == "off":
        GPIO.output(led, GPIO.LOW)  # turn off the LED
    else:
        print("Invalid command")

    sleep(1)


