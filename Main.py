from DiaryActions.Insert import *
from DiaryActions.View import *
from DiaryActions.Delete import *
from DiaryActions.Search import *
from DiaryActions.Update import *
from EventsListsHandler import EventsListHandler
from DateValidation import DateValidation
from Event import Event
from File import File
from flask import Flask

app = Flask(__name__)
filepath='events.json'  #DB file path (local to app folder)
f = File(filepath)

#------------------------------------------------------------------
# localhost:5000/  - will show the API of the diary application
#------------------------------------------------------------------
@app.route("/")
def welcome():
    return """
    <b>Hello</b> <br>
    <b>This Is An Events Diary</b><br><br>
    The valid commands for this Diary are:<br><br>
    Insert New Event - /<b>insert</b> , date , title , description <br><br>
    Delete Existing Event - /<b>delete</b> , date , title<br><br>
    View Existing Event - /<b>view</b> , date , title<br><br>
    Update Existing Event - /<b>update</b> , date , title , newdate , newtitle , newdescription<br><br>
    Search By Date Range - /<b>search-by-dates</b> , min_date , max_date<br><br>
    Search By Content - /<b>search-by-content</b> , text<br><br>
    Search By Date Range Or Content - /<b>search-by-date-or-content</b> , min_date , max_date , text <br><br>
    Search By Date Range And Content - /<b>search-by-date-and-content</b> , min_date , max_date , text<br><br>
    Save Diary DB File - /<b>saveDB</b> , dest_filename<br>
    (Initilize Local diary DB)<br><br>
    Initilize Diary DB - /<b>cleanDB</b><br><br>
    <b>## Date Format is : DD-MM-YYYY ##</b><br><br>
    """
#-------------------------------------------------------
#localhost:5000/insert,<date>,<title>,<description>
#Insrt new event with date,title and description values
#-------------------------------------------------------
@app.route("/insert,<date>,<title>,<description>")
def insertEvent(date, title, description):
    if DateValidation.validateDate(date): #validate Date
        e = Event(date, title, description)
        return Insert.insertEvent2Json(e, filepath)
    else:
        return 'date not valid!'


#-------------------------------------------------------
#localhost:5000/delete,<date>,<title>
#delete event by date and title
#-------------------------------------------------------
@app.route("/delete,<date>,<title>")
def deleteEvent(date, title):
    DateValidation.validateDate(date)
    return Delete.deleteFromJson(date, title, filepath)

#-------------------------------------------------------
#localhost:5000/view,<date>,<title>
#view event by date and title
#-------------------------------------------------------
@app.route("/view,<date>,<title>")
def viewEvent(date , title):
    DateValidation.validateDate(date)
    return View.viewFromJson(date, title, filepath)


#-------------------------------------------------------
#localhost:5000/update,<date>,<title>,<newdate>,<newtitle>,<newdescription>
#update event by date and title, to new date,title and description values
#-------------------------------------------------------
@app.route("/update,<date>,<title>,<newdate>,<newtitle>,<newdescription>")
def updateEvent(date,title,newdate, newtitle, newdescription):
    DateValidation.validateDate(date)
    DateValidation.validateDate(newdate)
    return Update.updateEventInJson(date, title, newdate, newtitle, newdescription, filepath)


#-------------------------------------------------------
#localhost:5000/search-by-dates,<min_date>,<max_date>
#search and view events by date range
#-------------------------------------------------------
@app.route("/search-by-dates,<min_date>,<max_date>")
def searchByDate(min_date, max_date):
    DateValidation.validateDate(min_date)
    DateValidation.validateDate(max_date)
    if DateValidation.validateDateRange(min_date, max_date):
        result_list = Search.searchEventByDates(min_date, max_date, filepath)
        return EventsListHandler.eventsListToStr(EventsListHandler.eventsListToStr(result_list))
    else:
        return 'date range not valid!'

#-------------------------------------------------------
#localhost:5000/search-by-content,<str>
#search and view events by content text
#-------------------------------------------------------
@app.route("/search-by-content,<str>")
def searchByContentStr(str):
    result_list = Search.searchEventByContent(str, filepath)
    return EventsListHandler.eventsListToStr(EventsListHandler.eventsListToStr(result_list))

#-------------------------------------------------------
#localhost:5000/search-by-date-and-content,<min_date>,<max_date>,<str>
#search and view events by content text or date range
#-------------------------------------------------------
@app.route("/search-by-date-or-content,<min_date>,<max_date>,<str>")
def searchByDateOrContent(min_date, max_date, str):
    result_list1 = Search.searchEventByDates(min_date, max_date, filepath)
    result_list2 = Search.searchEventByContent(str, filepath)
    result_list = EventsListHandler.mergeLists(result_list1, result_list2)
    return EventsListHandler.eventsListToStr(result_list)


#-------------------------------------------------------
#localhost:5000/search-by-date-or-content,<min_date>,<max_date>,<str>
#search and view events by content text and date range
#-------------------------------------------------------
@app.route("/search-by-date-and-content,<min_date>,<max_date>,<str>")
def searchByDateAndContent(min_date, max_date, str):
    DateValidation.validateDate(min_date)
    DateValidation.validateDate(max_date)
    if DateValidation.validateDateRange(min_date, max_date):
        result_list = Search.searchEventByDatesAndContent(min_date, max_date, str, filepath)
        return EventsListHandler.eventsListToStr(result_list)
    else:
        return 'date range not valid!'

#-------------------------------------------------------
#localhost:5000/saveDB,<dest_path>
#saves local DB file to destenation path, local DB will be initilized
#-------------------------------------------------------
@app.route("/saveDB,<dest_path>")
def saveFileDB(dest_path):
    resultStr = f.fileSave(dest_path)
    f.fileInit()
    return resultStr


#-------------------------------------------------------
#localhost:5000/cleanDB
#initilized local DB
#-------------------------------------------------------
@app.route("/cleanDB")
def fileInitilize():
    return f.fileInit()
    
if __name__ == "__main__":
    app.run(debug=True)
