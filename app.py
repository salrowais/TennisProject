from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
#from pymongo import MongoClient
#from datetime import datetime

#cluster = MongoClient("mongodb+srv://admin:23s242@cluster0.m94jrrj.mongodb.net/?retryWrites=true&w=majority")
#db = cluster["bookings"]
#users = db["users"]
#orders = db["orders"]

app = Flask(__name__)

@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")  # to get the body of the message
    number = request.form.get("From")  # to get the sender number
    number = number.replace("whatsapp:", "")  # to remove the word "whatsapp" form the variable {number)
    res = MessagingResponse()
 #   user = users.find_one({"number": number})

    if "Hi" in text:
        res.message("Hello2!")
    else:
        res.message("I don't know what to say2!")

    return str(res)

if __name__ == "__main__":
    app.run()

