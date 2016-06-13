import json
import os

#-----DELETE EVENT FROM DIARY-----#

class Delete:

    # ----------------------------------------------------------------------------------------------------
    # This function deletes existing event to Json file
    # collects all the events which already in file to list,
    # deletes the requested event from list
    # and dumps the list to json file without deleted event
    # ----------------------------------------------------------------------------------------------------
    def deleteFromJson(date, title, filepath):
        f = open(filepath, 'a')
        if os.path.getsize(filepath) == 0:  # if there is no event in file, no deletion needed
            f.close()
            return 'Events Diary Empty, no events to delete!'
        else:
            filedata = json.loads(open(filepath, 'r').read())
            if type(filedata) == dict:  # if there is only one event, load it as dictionary (json syntax)
                if filedata["Date"] == date and filedata["Title"] == title:
                    open(filepath, 'w')
                    f.close()
                    return 'Event successfuly Deleted: <br>date: ' + date + '<br> Title: ' + title
                else:
                    f.close()
                    return 'Event was not found, delete was not successful'
            else:                #if multiple events in file, load them to list
                index = 0
                for event in filedata:
                    if event["Date"] == date and event["Title"] == title:  #find event to delete, and pop it from list
                        filedata.pop(index)
                        if len(filedata) > 0:
                            f = open(filepath, 'w')
                            json.dump(filedata, f)       #dump list back to file
                        else:
                            f = open(filepath, 'w')
                        f.close()
                        return 'Event successfuly Deleted: <br>date: ' + date + '<br> Title: ' + title
                    else:
                        index += 1
                f.close()
                return 'Event was not found, delete was not successful'