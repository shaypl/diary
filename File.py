class File:
 def __init__(self, path):
     self.path = path

 def fileInit(self):
     f = open(self.path,'wb')
     f.close()






