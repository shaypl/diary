import json
import os

#-----INSERT EVENT TO DIARY-----#
class Insert:

    # ----------------------------------------------------------------------------------------------------
    # This function inserts new event to Json file
    # collects all the events which already in file, and dumps it again for handeling correct Json syntax
    # ----------------------------------------------------------------------------------------------------
    def insertEvent2Json(event, filepath):
        e = event
        tempdict = {
            'Date': e.getDate(),
            'Title': e.getTitle(),
            'Description': e.getDescription()
        }
        f = open(filepath, 'a')
        if os.path.getsize(filepath) == 0:  # if there is no event in file, just insert new event as dictionary
            json.dump(tempdict, f)
            f.close()
        else:
            filedata = json.loads(open(filepath, 'r').read())
            if type(filedata) == dict:  # if there is only one event, load it as dictionary (json syntax)
                datalist = [filedata, tempdict]
                f = open(filepath, 'w')
                json.dump(datalist, f)
            else:
                # if in file are multiple events, load them as list of Dictionaries,
                # append new event to List and insert list back to file
                filedata.append(tempdict)
                f = open(filepath, 'w')
                json.dump(filedata, f)
        f.close()
        return 'new event inserted: <br>date: ' + e.getDate() + '<br> Title: ' + e.getTitle() + '<br> Description: ' + e.getDescription()