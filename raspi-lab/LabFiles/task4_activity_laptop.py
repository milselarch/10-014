from libdw import pyrebase

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

"""
TO DO 4.1 With your partner decide what key your node should have
""" 

key = pass

while True: 

    """
    TO DO 4.2 Decide with your partner what values should represent the LED being on or off
    Then prompt the user with a message to ask for the desired action
    """

    action = input("fill in")

    """ 
    TO DO 4.3 if the value entered by the user is valid, upload the data to firebase to your node
    else, tell the user that an invalid value was entered 
    """
    pass 





