import json
import os

#-----UPDATE EVENTS IN DIARY-----#

class Update:
    # ----------------------------------------------------------------------------------------------------
    # This function updates events from Json file
    # load to list all the events which already in file,
    # searches by the date and title the requested events,
    # updates it values and inserts them to result list
    # ----------------------------------------------------------------------------------------------------
    def updateEventInJson(date, title, newdate, newtitle, newdescription, filepath):
        f = open(filepath, 'a')
        if os.path.getsize(filepath) == 0:  # if there is no event in file, no events to update
            f.close()
            return 'Events Diary Empty, no events to update!'
        else:
            filedata = json.loads(open(filepath, 'r').read())
            if type(filedata) == dict:  # if there is only one event, loads it as dictionary (json syntax)
                if filedata["Date"] == date and filedata["Title"] == title:
                    filedata["Date"] = newdate
                    filedata["Title"] = newtitle
                    filedata["Description"] = newdescription
                    f = open(filepath, 'w')
                    json.dump(filedata, f)
                    f.close()
                    return 'Event successfuly updated:<br>Date: ' + filedata["Date"] + '<br> Title: ' + filedata[
                        "Title"] + '<br> Description: ' + filedata["Description"]
                else:
                    f.close()
                    return 'Event was not found, Update was not successful'
            else:                     #if multiple events in file, load them to list
                for event in filedata:
                    if event["Date"] == date and event["Title"] == title:
                        event["Date"] = newdate
                        event["Title"] = newtitle
                        event["Description"] = newdescription
                        f = open(filepath, 'w')
                        json.dump(filedata, f)
                        f.close()
                        return 'Event successfuly updated:<br>Date: ' + event["Date"] + '<br> Title: ' + event[
                            "Title"] + '<br> Description: ' + event["Description"]
                f.close()
                return 'Event was not found, Update was not successful'