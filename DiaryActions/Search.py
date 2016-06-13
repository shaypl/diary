import os
import json
import datetime

#-----SEARCH EVENTS IN DIARY-----#
class Search:
    # ----------------------------------------------------------------------------------------------------
    # This function searches events from Json file
    # load to list all the events which already in file,
    # searches by the date range the requested events, and inserts them to result list
    # ----------------------------------------------------------------------------------------------------
    def searchEventByDates(min_date,max_date,filepath):
        min_date = datetime.datetime.strptime(min_date, '%d-%m-%Y')
        max_date = datetime.datetime.strptime(max_date, '%d-%m-%Y')
        f = open(filepath, 'r')
        results = []
        if os.path.getsize(filepath) == 0:  # if there is no event in file, no deletion needed
            return results
        else:
            filedata = json.loads(open(filepath, 'r').read())
            if type(filedata) == dict:  # if there is only one event, load it as dictionary (json syntax)
                date = filedata["Date"]
                date = datetime.datetime.strptime(date, '%d-%m-%Y')
                if date >= min_date and date <= max_date:
                    results.append(filedata)
                else:
                    return results
            else:               #if multiple events in file, load them to list
                for event in filedata:
                    date = event["Date"]
                    date = datetime.datetime.strptime(date, '%d-%m-%Y')
                    if date >= min_date and date <= max_date:
                        results.append(event)
        f.close()
        return results

    # ----------------------------------------------------------------------------------------------------
    # This function searches events from Json file
    # load to list all the events which already in file,
    # searches by string the requested events, and inserts them to result list
    # ----------------------------------------------------------------------------------------------------
    def searchEventByContent(search_str,filepath):
        f = open(filepath, 'r')
        results = []
        if os.path.getsize(filepath) == 0:  # if there is no event in file, no deletion needed
            return results
        else:
            filedata = json.loads(open(filepath, 'r').read())
            if type(filedata) == dict:  # if there is only one event, load it as dictionary (jscn sysntax)
                title = filedata["Title"]
                description = filedata["Description"]
                if search_str in title or search_str in description:
                    results.append(filedata)
                else:
                    return results
            else:                      #if multiple events in file, load them to list
                for event in filedata:
                    title = event["Title"]
                    description = event["Description"]
                    if search_str in title or search_str in description:
                        results.append(event)
        f.close()
        return results
    # ----------------------------------------------------------------------------------------------------
    # This function searches events from Json file
    # load to list all the events which already in file,
    # searches by string and date range the requested events, and inserts them to result list
    # ----------------------------------------------------------------------------------------------------
    def searchEventByDatesAndContent(min_date, max_date,search_str, filepath):
        min_date = datetime.datetime.strptime(min_date, '%d-%m-%Y')
        max_date = datetime.datetime.strptime(max_date, '%d-%m-%Y')
        f = open(filepath, 'r')
        results = []
        if os.path.getsize(filepath) == 0:  # if there is no event in file, no events to search
            return results
        else:
            filedata = json.loads(open(filepath, 'r').read())
            if type(filedata) == dict:  # if there is only one event, load it as dictionary (jscn sysntax)
                date = filedata["Date"]
                date = datetime.datetime.strptime(date, '%d-%m-%Y')
                title = filedata["Title"]
                description = filedata["Description"]
                if (date >= min_date and date <= max_date) and (search_str in title or search_str in description):
                    results.append(filedata)
                else:
                    return results
            else:                  #if multiple events in file, load them to list
                for event in filedata:
                    date = event["Date"]
                    date = datetime.datetime.strptime(date, '%d-%m-%Y')
                    title = event["Title"]
                    description = event["Description"]
                    if (date >= min_date and date <= max_date) and (search_str in title or search_str in description):
                        results.append(event)
        f.close()
        return results

