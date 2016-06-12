import json
import os
from event import Event

#----------------------------------------------------------------------------------------------------
#This function inserts new event to Json file
#collects all the events which already in file, and dumps it again for handeling correct Json syntax
#----------------------------------------------------------------------------------------------------
def insertEvent2Json(event, filepath):
    e = event
    tempdict = {
        'Date': e.getDate(),
        'Title': e.getTitle(),
        'Description': e.getDescription()
    }
    f = open(filepath,'a')
    if os.path.getsize(filepath) == 0:    #if there is no event in file, just insert new event as dictionary
        json.dump(tempdict,f)
        f.close()
    else:
        filedata=json.loads(open(filepath,'r').read())
        if len(filedata) == 3 and type(filedata)==dict:            #if there is only one event, load it as dictionary,
            datalist=[filedata,tempdict]  # append new event and inserts as List of Dictionaries, and insert to file
            f = open(filepath, 'w')
            json.dump(datalist, f)
        else:
                                         #if in file are multiple events, load them as list of Dictionaries,
                                         #append new event to List and insert to file again
            filedata.append(tempdict)
            f = open(filepath, 'w')
            json.dump(filedata, f)
    f.close()
    return 'new event inserted: <br>date: '+ e.getDate()+'<br> Title: '+ e.getTitle()+'<br> Description: '+ e.getDescription()

#----------------------------------------------------------------------------------------------------
#
#
#----------------------------------------------------------------------------------------------------
def deleteFromJson(date, title, filepath):
    f = open(filepath, 'a')
    if os.path.getsize(filepath) == 0:  # if there is no event in file, no deletion needed
        f.close()
        return 'Events Diary Empty, no events to delete!'
    else:
        filedata = json.loads(open(filepath, 'r').read())
        if type(filedata)==dict:  # if there is only one event, json loads it as dictionary,
            if filedata["Date"] == date and filedata["Title"]==title:
                open(filepath,'w')
                f.close()
                return 'Event successfuly Deleted: <br>date: '+ date+'<br> Title: '+ title
            else:
                f.close()
                return 'Event was not found, delete was not successful'
        else:
            index = 0
            for event in filedata:
                if event["Date"] == date and event["Title"] == title:
                        filedata.pop(index)
                        if len(filedata) > 0:
                            f = open(filepath, 'w')
                            json.dump(filedata, f)
                        else:
                            f = open(filepath, 'w')
                        f.close()
                        return 'Event successfuly Deleted: <br>date: ' + date + '<br> Title: ' + title
                else:
                    index+=1
            f.close()
            return 'Event was not found, delete was not successful'
#----------------------------------------------------------------------------------------------------
#
#
#----------------------------------------------------------------------------------------------------
def viewFromJson(date, title, filepath):
    f = open(filepath, 'r')
    if os.path.getsize(filepath) == 0:  # if there is no event in file, no deletion needed
        return 'Events Diary Empty, no events to view!'
    else:
        filedata = json.loads(open(filepath, 'r').read())
        if type(filedata) == dict:  # if there is only one event, load it as dictionary,
            if filedata["Date"] == date and filedata["Title"] == title:
                f.close()
                return 'The Event Requested: <br>date: ' + date + '<br> Title: ' + title+ '<br> Description: ' + filedata['Description']
            else:
                f.close()
                return 'Not found requested event'
        else:
            for event in filedata:
                if event["Date"] == date and event["Title"] == title:
                    f.close()
                    return 'The Event Requested: <br>date: ' + date + '<br> Title: ' + title + '<br> Description: ' + event['Description']
            f.close()
            return 'Not found requested event'
#----------------------------------------------------------------------------------------------------
#
#
#----------------------------------------------------------------------------------------------------
def updateEventInJson(date,title,newdate,newtitle,newdescription,filepath):
    f = open(filepath, 'a')
    if os.path.getsize(filepath) == 0:  # if there is no event in file, no deletion needed
        f.close()
        return 'Events Diary Empty, no events to update!'
    else:
        filedata = json.loads(open(filepath, 'r').read())
        if type(filedata) == dict:  # if there is only one event, json loads it as dictionary
            if filedata["Date"] == date and filedata["Title"] == title:
                filedata["Date"] = newdate
                filedata["Title"] = newtitle
                filedata["Description"] = newdescription
                f = open(filepath, 'w')
                json.dump(filedata, f)
                f.close()
                return 'Event successfuly updated:<br>Date: '+ filedata["Date"] + '<br> Title: ' + filedata["Title"] + '<br> Description: ' + filedata["Description"]
            else:
                f.close()
                return 'Event was not found, Update was not successful'
        else:
            for event in filedata:
                if event["Date"] == date and event["Title"] == title:
                    event["Date"] = newdate
                    event["Title"] = newtitle
                    event["Description"] = newdescription
                    f = open(filepath, 'w')
                    json.dump(filedata, f)
                    f.close()
                    return 'Event successfuly updated:<br>Date: ' + event["Date"] + '<br> Title: ' + event["Title"] + '<br> Description: ' + event["Description"]
            f.close()
            return 'Event was not found, Update was not successful'