from library.Graphics import *
from library.DateMaker import *
from library.ReadWrite import *
import prefs
import datetime
from prefs import *

class Month:
    def __init__(self,month,day,year,topLeftPoint,bottomRightPoint,row = 0):

        self.month = month
        self.day = day
        self.year = year

        dm = DateMaker()
        self.dates = dm.createYear(year)
        self.row = row

        if self.row == 0:
            for r in self.dates:
                for c in r:
                    if c[0] == month and c[1] == day and c[2] == year:
                        break
                if c[0] == month and c[1] == day and c[2] == year:
                    break
                self.row += 1

        self.calendar = []
        height = bottomRightPoint.getY() - topLeftPoint.getY()
        x1 = topLeftPoint.getX()
        x2 = bottomRightPoint.getX()
        y1 = topLeftPoint.getY()-height/5
        y2 = topLeftPoint.getY()
        for i in range(self.row-1,self.row+5):
            tempW = []
            tempD = []
            tempY = []

            for j in range(7):
                tempW.append(self.dates[i][j][0])
                tempD.append(self.dates[i][j][1])
                tempY.append(self.dates[i][j][2])

            y1 += height/5
            y2 += height/5
            self.calendar.append(Week(tempW,tempD,tempY,month,Point(x1,y1),Point(x2,y2)))
        try: # if there is a data file found in the location it will use it
            data = importData(PREFS.DATA_FILE)
            for i in data:
                self.addItem(i)
        except: # no data file is located and it will create one in the designated location
            pass
    def addItem(self,i):
        for x in self.calendar:
            x.addItem(i)
    def getRow(self):
        return self.row

    def draw(self,win):
        '''
        Draw the Month calendar to the window.
        '''
        self.win = win
        for i in self.calendar:
            i.draw(win)

    def undraw(self):
        '''
        Undraws all of the month info from the window.
        '''
        #win.pause()
        for i in self.calendar:
            i.undraw()
        #win.resume()
    def uncheckSelected(self):
        self.win.pause()
        for i in self.calendar:
            i.uncheckSelected()
        self.win.resume()
    def getSelected(self,mouse):
        self.win.pause()
        item = ''
        for i in self.calendar:
            temp = i.getSelected(mouse)
            if temp != '':
                item = temp
        self.win.resume()
        return item

    def getDayClicked(self,mouse):
        day = [0,0,0]
        for i in self.calendar:
            temp = i.getDayClicked(mouse)
            if temp != [0,0,0]:
                day = temp
        return day

class Week:
    def __init__(self,month,day,year,viewMonth,topLeftPoint,bottomRightPoint):
        week = []
        width = bottomRightPoint.getX() - topLeftPoint.getX()
        y1 = topLeftPoint.getY()
        y2 = bottomRightPoint.getY()
        x1 = topLeftPoint.getX()-width/7
        x2 = topLeftPoint.getX()
        for i in range(7):
            x1 += width/7
            x2 += width/7
            week.append(Day(month[i],day[i],year[i],viewMonth,Point(x1,y1),Point(x2,y2)))
        self.week = week

    def draw(self,win):
        for i in self.week:
            i.draw(win)
    def undraw(self):
        for i in self.week:
            i.undraw()
    def addItem(self,i):
        for x in self.week:
            x.addItem(i)
    def uncheckSelected(self):
        for i in self.week:
            i.uncheckSelected()
    def getSelected(self,mouse):
        item = ''
        for i in self.week:
            temp = i.getSelected(mouse)
            if temp != '':
                item = temp
        return item
    def getDayClicked(self,mouse):
        day = [0,0,0]
        for i in self.week:
            temp = i.getDayClicked(mouse)
            if temp != [0,0,0]:
                day = temp
        return day
class Day:
    def __init__(self,month,day,year,viewMonth,topLeftPoint,bottomRightPoint):
        self.month = month
        self.day = day
        self.year = year
        self.box = Button('',5,topLeftPoint,bottomRightPoint)
        now = datetime.datetime.now()
        if now.day == day and now.year == year and now.month == month:
            self.box.setFill(PREFS.TODAY_COLOR)
        elif(self.month != viewMonth or self.year != now.year):
            self.box.setFill(PREFS.OTHER_MONTH_COLOR)
        self.dayLabel = Text(Point(bottomRightPoint.getX()-10,topLeftPoint.getY()+8),str(day))
        self.list = SelectFromList(Point(topLeftPoint.getX(),topLeftPoint.getY()+15),bottomRightPoint.getX()-topLeftPoint.getX(),13,10)
        if(self.day == 1):
            self.firstLabel = Text(Point((topLeftPoint.getX()+(bottomRightPoint.getX()-topLeftPoint.getX())/2),topLeftPoint.getY()+7),PREFS.MONTH_NAMES[month])
        else:
            self.firstLabel = Text(Point((topLeftPoint.getX()+(bottomRightPoint.getX()-topLeftPoint.getX())/2),topLeftPoint.getY()+7),'')
        self.firstLabel.setSize(10)
        self.firstLabel.setTextColor(PREFS.BLACK)



    def addItem(self,i):
        """
        Adds the given item to the list of items for the current day.
        """
        if(i[0] != '/'):
            if(self.day == int(i[2]) and self.month == int(i[1]) and self.year == int(i[3])):
                try:
                    if i[-1] != '/':
                        self.list.add(i[-1], eval(PREFS.CLASSES[i[0]]),i)
                    else:
                        self.list.add(i[-2], eval(PREFS.CLASSES[i[0]]),i,complete=True)
                except:
                    pass # Used to deal with classes that are not found

    def uncheckSelected(self):
        self.list.uncheckSelected()
    def getSelected(self,mouse):

        self.list.checkSelected(mouse)
        t =  self.list.getSelected()
        return t
    def getDayClicked(self,mouse):
        day = [0,0,0]
        temp = self.box.pressed(mouse)
        if temp:
            day = [self.month,self.day,self.year]
        return day

    def draw(self,win):
        """
        Draws the day to the window.
        """
        self.box.setOutline(PREFS.BLACK)
        self.dayLabel.setTextColor(PREFS.BLACK)


        self.box.draw(win)
        self.dayLabel.draw(win)
        self.list.draw(win)
        if(self.day == 1):
            self.firstLabel.draw(win)
    def undraw(self):
        self.box.undraw()
        self.dayLabel.undraw()
        self.list.undraw()
        if(self.day == 1):
            self.firstLabel.undraw()



def createLegend():
    legend = []
    width = 80
    height = 13
    count = 0
    for i in PREFS.CLASSES:
        x1 = 0 + (int)(count/3) * width
        x2 = width + (int)(count/3) * width
        y1 = 0 + count%3 * height
        y2 = height + count%3 * height
        
        temp = Button(i,10,Point(x1,y1),Point(x2,y2))
        temp.setFill(eval(PREFS.CLASSES[i]))
        legend.append(temp)
        count+=1
    return legend
def createDayHeader():
    arr = []
    width = 800
    w = width/7
    count = 0
    for i in PREFS.DAY_HEADER:
        temp = Text(Point((width/14)+count*w,50),i)
        temp.setSize(12)
        temp.setTextColor(PREFS.BLACK)
        arr.append(temp)
        count+=1
    return arr
