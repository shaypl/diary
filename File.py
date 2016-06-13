from shutil import copyfile

#----- Methods for file actions -----#
class File:
 def __init__(self, path):
     self.path = path


#----- copies source file to destination path -----#
 def fileSave (self,dest_path):
     try:
        dst_file = open(dest_path,'w')
        src_file = open(self.path,'a')
     except (IOError, OSError) as e:
         return 'File Open Error'
     copyfile(self.path,dest_path)
     return 'Diary DB saved to file: '+dest_path

#----- initilizes json file -----#
 def fileInit(self):
     f = open(self.path,'wb')
     f.close()
     return 'DB Initialized'





