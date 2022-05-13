from libdw import pyrebase

projectid = "sutd-utational-project"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyCro0vqZ8o0vPK7CkmgAiefXhbZE47hpNQ"
email = "milselarch@gmail.com"
password = "potatopotato" 

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

key = "data"

print("The database is currently empty")
node = db.child(key).get(user['idToken']) 
print("key   :", node.key())
print("value :", node.val()) 

print("Now we upload a key-value pair")
value = input("Enter a value: ")
db.child(key).set(value, user['idToken'])
print("please go to the firebase console and have a look") 


print("Now that there is data in the database, we can download the data")
node = db.child(key).get(user['idToken']) 
print("key   :", node.key())
print("value :", node.val()) 


###my_stream.close()



