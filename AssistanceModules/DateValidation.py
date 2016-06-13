import datetime

#-----Methods for date validation-----#
class DateValidation:

    def __init__(self):
        pass

    # -----Validate that date is in correct date format-----#
    def validateDate (date):
        valid = 1
        try:
            datetime.datetime.strptime(date, '%d-%m-%Y')
        except ValueError:
            valid = 0
            raise ValueError("Incorrect date format, should be DD-MM-YYYY")
        finally:
            return valid

    # -----Validate that date ramge [min_range - max_range is correct (min_date < max_date)-----#
    def validateDateRange(min_date, max_date):
        return datetime.datetime.strptime(min_date, '%d-%m-%Y') < datetime.datetime.strptime(max_date, '%d-%m-%Y')

























