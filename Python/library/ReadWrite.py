import datetime
def importSettings(fileName):
    file = ReadWrite(fileName)
    data = file.read()
    temp = []
    for i in data:
        temp.append(seperate(i,'='))
    data = temp
    for i in data:
        i[-1] = i[-1].strip()
    return data
def getSetting(fileName, setting):
    file = importSettings(fileName)
    for i in file:
        if i[0] == setting:
                return i[1]
    return ""
def setSetting(fileName,setting,val):
    '''
    file = importSettings(fileName)
    for i in file:
        if i[0] == setting:
            i[1] = str(val)
    string = ''
    for i in file:
        string += i[0] + '=' + i[1]
    file = ReadWrite(fileName)
    file.overWrite(string)
    '''
    file = importSettings(fileName)
    for i in file:
        if i[0] == setting:
            i[1] = str(val)
    string = ''
    for i in file:
        if len(i) > 1:
            string += i[0] + '=' + i[1] + '\n'
        else:
            string += i[0] + '\n'     
    file = ReadWrite(fileName)
    file.overWrite(string)
    
def importData(fileName):
    file = ReadWrite(fileName)
    data = file.read()
    temp = []
    for i in data:
        temp.append(seperate(i,',')[0:-1])
    data = temp
    return data

def importClasses(fileName):
    file = ReadWrite(fileName)
    data = file.read()
    temp = {}
    for i in range(0,len(data),2):
        temp[data[i][0:-1]] = data[i+1][0:-1]
    data = temp
    return data

def seperate(string,sep):
    '''
    Returns a list that is created from a string that is
    seperated by a single character 'sep'.
    '''
    a = []
    item = ''
    for i in string:
        if i == sep:
            a = a + [item]
            item = ''
        else:
            item += i
    if item != '':
        a = a + [item]
    return a
def completeItem(fileName, com):
    data = importData(fileName)
    newData = ''
    for i in data:
        temp = ''
        if(i == com):
            if i[-1] != '/':
                for x in i:
                    temp += x + ','
                temp += '/,'
            else: # Removes the completed item signature
                for x in range(len(i)-1):
                    temp += i[x] + ','
        else:
            for x in i:
                temp += x + ','
        temp += '\n'
        newData += temp
    file = ReadWrite(fileName)
    file.overWrite(newData)

def removeItem(fileName, rem):
    data = importData(fileName)
    newData = ''
    for i in data:
        temp = ''
        if(i == rem):
            if i[0] != '/':
                temp += '/,'
                for x in i:
                    temp += x + ','
            else: # Will re-add the item if I want to add this later
                for x in range(len(i)-1):
                    temp += i[x+1] + ','
        else:
            if i[0] != '/' and int(i[3]) != datetime.datetime.now().year - 2:
                for x in i:
                    temp += x + ','
        if i[0] != '/' and int(i[3]) != datetime.datetime.now().year - 2:
            temp += '\n'
            newData += temp
    file = ReadWrite(fileName)
    file.overWrite(newData)
def addItem(fileName, add):
    file = ReadWrite(fileName)
    temp = ''
    for i in add:
        temp += i + ','
    temp += '\n'
    file.write(temp)
def monthConversion(month,year):
    """
    This method will check to see if going to the next or previous month will change the
    year and returns the corrected month and year.

    month - the month to see if it is in the same year
    year - the year that you are checking

    return month,year - the corrected values of each
    """
    if(month > 12):
        year+=1
        month = 1
    if(month < 1):
        year-=1
        month = 12
    return month,year

class ReadWrite:
    '''
    Class to read and write to a text file.
    '''
    def __init__(self,fileName):
        '''
        Create an object based on the name of the file

        fileName - The name of the file in the same folder with the extension
        '''
        self.fileName = fileName

    def read(self):
        '''
        Reads the data from the file and stores each line in an array.

        return - gives an array with each line in a new element.
        '''
        file = open(self.fileName,"r+")
        data = file.readlines()
        file.close()
        return data

    def write(self,data):
        '''

        '''
        file = open(self.fileName,"a+")
        file.write(data)
        file.close()
    # Removes all data in the file and starts writing the data
    def overWrite(self,data):
        file = open(self.fileName,"w+")
        file.write(data)
        file.close()
