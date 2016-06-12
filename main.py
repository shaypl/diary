import json
from DiaryActions import insertEvent2Json
from DiaryActions import deleteFromJson
from DiaryActions import viewFromJson
from DiaryActions import updateEventInJson
from assist_functions import dateValidation
from event import Event
from flask import Flask
from File import File

app = Flask(__name__)
filepath='events.json'
f = File(filepath)

@app.route("/")
def welcome():
    return "Hello <br> this is an events diary"

@app.route("/insert,<date>,<title>,<description>")
def insertEvent(date,title,description):
    if (dateValidation(date) == 1):
        e = Event(date,title,description)
        return insertEvent2Json(e, filepath)
    else:
        return 'date not valid, please insert valid date in format DDMMYYYY'

@app.route("/delete,<date>,<title>")
def deleteEvent(date,title):
    return deleteFromJson(date,title,filepath)

@app.route("/view,<date>,<title>")
def viewEvent(date,title):
    return viewFromJson(date,title,filepath)

@app.route("/update,<date>,<title>,<newdate>,<newtitle>,<newdescription>")
def updateEvent(date,title,newdate,newtitle,newdescription):
    if dateValidation(newdate) == 1:
        return updateEventInJson(date,title,newdate,newtitle,newdescription,filepath)
    else:
        return 'new date to update not valid, please insert valid date in format DDMMYYYY'

@app.route("/cleanDB")
def fileInitilize():
    return f.fileInit()
    
if __name__ == "__main__":
    app.run(debug=True)
