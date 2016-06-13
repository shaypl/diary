import json
import os

#-----VIEW EVENTS FROM DIARY-----#

class View:
    # ----------------------------------------------------------------------------------------------------
    # This function view requested event from json file
    # collects all the events which already in file, and returns requested event
    # ----------------------------------------------------------------------------------------------------
    def viewFromJson(date, title, filepath):
        f = open(filepath, 'r')
        if os.path.getsize(filepath) == 0:  # if there is no event in file, no deletion needed
            return 'Events Diary Empty, no events to view!'
        else:
            filedata = json.loads(open(filepath, 'r').read())
            if type(filedata) == dict:  # if there is only one event, load it as dictionary (json syntax)
                if filedata["Date"] == date and filedata["Title"] == title:
                    f.close()
                    return 'The Event Requested: <br>date: ' + date + '<br> Title: ' + title + '<br> Description: ' + \
                           filedata['Description']
                else:
                    f.close()
                    return 'Not found requested event'
            else:                #if multiple events in file, load them to list
                for event in filedata:
                    if event["Date"] == date and event["Title"] == title:
                        f.close()
                        return 'The Event Requested: <br>date: ' + date + '<br> Title: ' + title + '<br> Description: ' + \
                               event['Description']
                f.close()
                return 'Not found requested event'