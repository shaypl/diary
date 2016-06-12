from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET

class File:
 def __init__(self, path):
     self.path = path

 def fileInit(self):
     f = open(self.path,'wb')
     f.close()
     return 'DB Initialized'





