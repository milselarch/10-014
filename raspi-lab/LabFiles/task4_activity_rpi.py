from libdw import pyrebase
import RPi.GPIO as GPIO
from time import sleep



projectid = "fill in"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "fill in"
email = "fill in"
password = "fill in"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
user = auth.refresh(user['refreshToken']) 


# Use the BCM GPIO numbers as the numbering scheme
GPIO.setmode(GPIO.BCM)

# Use GPIO23 for LED
led = 23

# Set GPIO23 as output.
GPIO.setup(led, GPIO.OUT)


"""
TO DO 4.4 With your partner decide the key of your node. See TO DO 4.1. 
""" 
key = pass 

while True: 

    """
    TO DO 4.5 Write code to retrieve the value from the node
    using the key. 
    """ 
    """
    TO DO 4.6 Check the datatype of the value and 
    display the value on the screen
    """ 

    """
    TO DO 4.7 Using the value obtained, 
    turn on or turn off the switch
    """ 

    """
    TO DO 4.8 Pause execution for a short period e.g. 1 sec
    """ 
    pass 
    


    
