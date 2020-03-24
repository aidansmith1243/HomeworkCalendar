import DataClasses
from Calendar import Calendar
import pickle
class Model:
    def __init__(self,saveFile):
        self.Calendar = Calendar()
        self.Classes = []
        self.SaveFile = saveFile
    def AddClass(self,c):
        self.Classe.append(c)
    def RemoveClass(self,c):
        try:
            self.Classes.remove(c)
        except:
            pass
    def Save(self):
        '''
        Saves the current state of this object to the SaveFile as binary
        '''
        by = pickle.dumps(self)
        file = open(self.SaveFile,'wb')
        file.write(by)
        file.close
    def Import(file):
        '''
        Gets the Calendar object in the SaveFile.

        :return: the new Calendar object
        '''
        file = open(file,'rb')
        fileContents = file.read()
        temp = pickle.loads(fileContents)
        if isinstance(temp,Model):
            return temp
        else:
            print('ERROR Loading file')
            return None
