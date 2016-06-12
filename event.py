from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
import json

class Event:
  
 def __init__(self, date, title, description):
     self.date = date
     self.title = title
     self.description = description

 def getDate(self):
     return self.date

 def getTitle(self):
     return self.title
    
 def getDescription(self):
     return self.description

 def setDate(self, date):
     self.date = date

 def setTitle(self, title):
     self.title = title
    
 def setDescription(self, description):
     self.description = description


