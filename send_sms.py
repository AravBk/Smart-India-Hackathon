# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACa0300108284e312d43651ac6ec6f59aa", "e569a7e0d7decd8fcdbb5f2cb7099e60")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+919940261858", 
                       from_="+17755719965", 
                       body="Hello from Python!")
