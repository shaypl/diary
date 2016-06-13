from DiaryActions.Insert import *
from DiaryActions.View import *
from DiaryActions.Delete import *
from DiaryActions.Search import *
from DiaryActions.Update import *
from EventsListsHandler import EventsListHandler
from DateValidation import DateValidation
from Event import Event
from File import File
import unittest

class TestDateValidation(unittest.TestCase):

    def setUp(self):
        self.true_date1 = '05-01-1986'
        self.true_date2 = '9-1-1986'
        self.false_date1 = '40-11-2016'
        self.false_date2 = '29-20-2016'
        self.false_date3 = '30-02-2016'

    def testValidateDate_trueDate1(self):
        self.assertEqual(DateValidation.validateDate(self.true_date1), 1)

    def testValidateDate_trueDate2(self):
        self.assertEqual(DateValidation.validateDate(self.true_date2), 1)

    def testValidateDate_falseDate1(self):
        self.assertEqual(DateValidation.validateDate(self.false_date1), 0)

    def testValidateDate_falseDate2(self):
        self.assertEqual(DateValidation.validateDate(self.false_date2), 0)

    def testValidateDate_falseDate3(self):
        self.assertEqual(DateValidation.validateDate(self.false_date3), 0)

    def testValidateDateRange_true (self):
        self.assertEqual(DateValidation.validateDateRange(self.true_date1,self.true_date2), 1)

    def testValidateDateRange_false (self):
        self.assertEqual(DateValidation.validateDateRange(self.true_date2,self.true_date1), 0)

class TestEventListHandler(unittest.TestCase):

    def setUp(self):
        self.emptylist = []
        self.list1 = [{"Description": "important", "Title": "meeting", "Date": "13-08-2016"}, {"Description": "free", "Title": "nothing", "Date": "24-07-1986"}]
        self.list2 = [{"Description": "important", "Title": "meeting", "Date": "13-08-2016"}, {"Description": "fun", "Title": "vacation", "Date": "24-07-1986"}]
        self.resultlist = [{"Description": "important", "Title": "meeting", "Date": "13-08-2016"}, {"Description": "free", "Title": "nothing", "Date": "24-07-1986"}, {"Description": "fun", "Title": "vacation", "Date": "24-07-1986"}]

    def testmergeLists_true (self):
        self.assertEqual(EventsListHandler.mergeLists(self.list1,self.list2), self.resultlist)

    def testmergeLists_true2 (self):
        self.assertEqual(EventsListHandler.mergeLists(self.list1,self.emptylist), self.list1)

    def testmergeLists_true3(self):
        self.assertEqual(EventsListHandler.mergeLists(self.emptylist, self.list1), self.list1)

    def testmergeLists_true3(self):
        self.assertEqual(EventsListHandler.mergeLists(self.emptylist, self.list1), self.list1)

    def testEventsListToStr_true1(self):
        self.assertEqual(EventsListHandler.eventsListToStr(self.emptylist), 'no events to show')

if __name__ == '__main__':
    unittest.main()
