from Model import Model
from View import View
from datetime import datetime
class Control:
    def __init__(self):
        self.Running = True
        self.Model = Model("data.txt")
        # import model
        self.View = View()
        self.ViewMonth = datetime.now().month
        self.ViewYear = datetime.now().year
        self.LinkMonth(self.ViewMonth,self.ViewYear)
        self.View.draw()
    def CheckKeys(self):
        pass
    def LinkMonth(self,month,year):
        count = 0
        for i in self.Model.Calendar.GetCurrentViewMonth(month,year):
            for j in i:
                self.View.Grid[count].SetData(j)
                count += 1
