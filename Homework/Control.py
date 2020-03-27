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
        self.Model = Model.Import("data")
        if self.Model == None:
            self.Model = Model("data")
        '''
        colors = {}
        colors['Purple'] = Graphics.color_rgb(153,51,255)
        colors['Red'] = Graphics.color_rgb(255,51,51)
        colors['Grey'] = Graphics.color_rgb(192,192,192)
        colors['Blue'] = Graphics.color_rgb(51,51,255)
        colors['Green'] = Graphics.color_rgb(0,204,0)
        colors['Yellow'] = Graphics.color_rgb(255,255,51)
        colors['Orange'] = Graphics.color_rgb(255,128,0)
        self.Model.AddClass(DataClasses.Class("ENGL 200",colors['Green']))
        self.Model.AddClass(DataClasses.Class("STAT 510",colors['Red']))
        self.Model.AddClass(DataClasses.Class("CIS 450",colors['Blue']))
        self.Model.AddClass(DataClasses.Class("CIS 501",colors['Purple']))
        '''
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
            if isinstance(clicked, GridBox) and clicked.Data.Date.Day != 0:
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

