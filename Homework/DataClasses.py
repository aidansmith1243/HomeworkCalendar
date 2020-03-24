class Date:
    def __init__(self,m,d,y):
        self.Day = d
        self.Month = m
        self.Year = y

class Day:
    def __init__(self,date):
        self.Date = date
        self.Items = []
    def AddItem(self,item):
        self.Items.append(item)
    def RemoveItem(self,item):
        try:
            if self.Items != []:
                print(self.Items[0])
            self.Items.remove(item)
        except:
            pass

    def CompleteItem(self,item):
        item.Completeed = not item.Completed

class DailyItem:
    def __init__(self,name,c):
        self.Name = name
        self.Class = c
        self.Completed = False
    
class Class:
    def __init__(self,name, color):
        self.Name = name
        self.Color = color