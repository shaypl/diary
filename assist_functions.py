def parseDate(date):
    tempdict = {}
    int_date = int(date)
    tempdict["year"] = int_date%10000
    int_date = int(int_date/10000)
    tempdict["month"] = int_date % 100
    int_date = int(int_date / 100)
    tempdict["day"] = int_date % 100
    if int(int_date / 100) == 0:
        return tempdict
    else:
        return 0


def dateValidation(date):
    date_dict = parseDate(date)
    if date_dict == 0:
        return 0
    elif date_dict["month"] > 7 and date_dict["month"]%2 == 1 and date_dict["day"]>30:
        return 0
    elif date_dict["month"] <= 7 and date_dict["month"]%2 == 0 and date_dict["day"]>30:
        return 0
    elif date_dict["month"] == 2 and date_dict["day"]>29:
        return 0
    elif date_dict["month"]<0 or date_dict["month"] > 12 or date_dict["day"]< 0 or date_dict["day"] > 31 or date_dict["year"] < 0:
        return 0
    else:
        return 1