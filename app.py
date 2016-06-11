from event import Event
from flask import Flask
from File import File

app = Flask(__name__)
filepath="events.xml"
f = File(filepath)

@app.route("/")
def welcome():
    return "Hello <br> this is an events diary"

@app.route("/insert,<date>,<title>,<description>")
def input(date,title,description):
    e = Event(date,title,description)
    e.saveEvent2Xml(filepath)

@app.route("/view,<date>,<title>,<description>")
def input(date, title, description):
    e = Event(date, title, description)
    e.saveEvent2Xml(filepath)

@app.route("/cleanDB")
def fileInitilize():
    f.fileInit()
    
if __name__ == "__main__":
    app.run(debug=True)
