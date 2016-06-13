
#-----Methods for list handeling-----#
class EventsListHandler:

    def __init__(self):
        pass
#-----merges 2 Lists to one list with no distinct items-----#
    def mergeLists(events_list1, events_list2):
        if len(events_list1) == 0:
            return events_list2
        elif len(events_list2) == 0:
            return events_list1
        else:
            resultList = []
            for event1 in events_list1:
                #index = 0
                for event2 in events_list2:
                    #index += 1
                    if event1["Date"] == event2["Date"] and event1["Title"] == event2["Title"] and event1["Description"] == event2["Description"]:
                        events_list2.remove(event2)
            for event in events_list1:
                resultList.append(event)
            for event in events_list2:
                resultList.append(event)
            return resultList
#-----return str of list with events (for printing events from list)-----#
    def eventsListToStr(events_list):
        if len(events_list) > 0:
            str=''
            for event in events_list:
                str +=event["Date"]+'<br>'+event["Title"]+'<br>'+event["Description"]+'<br><br>'
            return str
        else:
            return 'no events to show'
