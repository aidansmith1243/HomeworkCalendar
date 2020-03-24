from Model import Model
from View import View
from View import GridBox
from View import ItemBox
import random
import DataClasses
import Graphics
from datetime import datetime
class Control:
    def __init__(self):
        self.Running = True
        self.Model = Model.Import("data.txt")
        if self.Model == None:
            self.Model = Model("data.txt")

        self.View = View(self.Model)

        self.View.draw()
    def CheckKeys(self):
        key = self.View.CheckKey()
        if key != '':
            if key == 'Escape':
                pass
                #self.Running = False
            elif key == 'Down':
                self.View.ViewNextMonth()
                self.View.Update()
            elif key == 'Up':
                self.View.ViewPrevMonth()
                self.View.Update()

    def CheckMouse(self):
        clicked = self.View.CheckMouse()
        if clicked != None:
            if isinstance(clicked, GridBox):
                name,tempClass = self.View.AddItem()
                if tempClass != None:
                    clicked.Data.AddItem(DataClasses.DailyItem(name,tempClass))
                    self.View.Update()
            elif isinstance(clicked,ItemBox):
                clicked.Data.Completed = not clicked.Data.Completed
                self.View.Update()
        rightClicked = self.View.CheckMouseRight()
        if rightClicked != None:
            if isinstance(rightClicked,ItemBox):
                for i in self.Model.Calendar.CalendarDateList:
                    for x in i:
                        x.RemoveItem(rightClicked.Data)
            self.View.Update()

    def Close(self):
        self.View.Win.close()
        self.Model.Save()

