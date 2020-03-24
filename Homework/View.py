import Graphics
import time
from datetime import datetime
class View:
    def __init__(self,model):
        self.Win = Graphics.GraphWin('Window',800,700)
        self.Grid = View.CreateGrid(7,6,Graphics.Point(0,60),Graphics.Point(800,700))
        self.Model = model
        self.ViewMonth = datetime.now().month
        self.ViewYear = datetime.now().year
        self.Header = Header(self.Grid,self.ViewMonth,self.ViewYear)
        self.Classes = ClassesList(model.Classes)

    def AddItem(self):
        newItembox = AddItem(self.Model.Classes)
        return newItembox.run(self.Win)

    def CheckKey(self):
        return self.Win.checkKey()

    def CheckMouse(self):
        mouse = self.Win.checkMouse()
        for i in self.Grid:
            if i.Clicked(mouse):
                return i
            for j in i.Items:
                if j.Clicked(mouse):
                    return j
        return None
    
    def CheckMouseRight(self):
        mouse = self.Win.checkMouseRight()
        for i in self.Grid:
            for j in i.Items:
                if j.Clicked(mouse):
                    return j
        return None

    def CreateGrid(xBoxes,yBoxes,topLeftPoint,bottomRightPoint):
        eachHeight = (bottomRightPoint.getY() - topLeftPoint.getY())/yBoxes
        eachWidth = (bottomRightPoint.getX() - topLeftPoint.getX())/xBoxes
        x1 = topLeftPoint.getX()
        x2 = x1+eachWidth
        y1 = topLeftPoint.getY()
        y2 = y1 + eachHeight
        gridList = []
        for i in range(yBoxes):
            for j in range(xBoxes):
                gridList.append(GridBox(None,Graphics.Point(x1,y1),Graphics.Point(x2,y2)))
                x1 += eachWidth
                x2 += eachWidth
            y1 += eachHeight
            y2 += eachHeight
            x1 = topLeftPoint.getX()
            x2 = x1+eachWidth
        return gridList

    def ViewNextMonth(self):
        self.undraw()
        self.ViewMonth += 1
        if self.ViewMonth > 12:
            self.ViewYear += 1
            self.ViewMonth = 1
        self.LinkData()

    def ViewPrevMonth(self):
        self.undraw() 
        self.ViewMonth -= 1
        if self.ViewMonth < 1:
            self.ViewYear -= 1
            self.ViewMonth = 12
        self.LinkData()

    def LinkData(self):
        index = self.Model.Calendar.GetMonthIndex(self.ViewMonth,self.ViewYear)
        count = 0;
        for i in range(index,index+6):
            for j in self.Model.Calendar.CalendarDateList[i]:
                self.Grid[count].SetData(j)
                count+= 1

    def Update(self):
        self.undraw()
        self.Header = Header(self.Grid,self.ViewMonth,self.ViewYear)
        self.draw()

    def draw(self):
        self.Win.pause()
        self.LinkData()
        self.Header.draw(self.Win)
        self.Classes.draw(self.Win)
        for i in self.Grid:
            i.draw(self.Win)
        self.Win.resume()
    def undraw(self):
        self.Win.pause()
        self.Header.undraw()
        self.Classes.undraw()
        for i in self.Grid:
            i.undraw()
        self.Win.resume()

class AddItem:
    def __init__(self,classes):
        self.DrawableItems = []
        box = Graphics.Rectangle(Graphics.Point(0,0),Graphics.Point(200,250))
        box.setFill(Graphics.color_rgb(255,255,255))
        self.DrawableItems.append(box)

        self.Entry = Graphics.Entry(Graphics.Point(100,20),20)
        self.DrawableItems.append(self.Entry)

        #self.Submit = Graphics.Button("Submit",10,Graphics.Point(20,150),Graphics.Point(80,190))
        self.Cancel = Graphics.Button("Cancel",10,Graphics.Point(120,200),Graphics.Point(180,240))
        #self.DrawableItems.append(self.Submit)
        self.DrawableItems.append(self.Cancel)
        
        self.Classes = {}
        self.ClassBoxList = []
        count = 0
        for i in classes:
            item = Graphics.Button(i.Name,10,Graphics.Point(20, 40 + 20*count),Graphics.Point(180,60+ 20*count))
            count += 1
            item.setFill(i.Color)
            self.DrawableItems.append(item)
            self.Classes[item] = i
            self.ClassBoxList.append(item)

    def run(self,win):
        self.draw(win)
        selected = None
        running = True
        while running:
            mouse = win.checkMouse()
            if self.Cancel.pressed(mouse):
                break
            elif self.Entry.getText() != '':
                for i in self.ClassBoxList:
                    if i.pressed(mouse):
                        selected = self.Classes[i]
                        running = False
        self.undraw()
        return self.Entry.getText(),selected

    def draw(self,win):
        for i in self.DrawableItems:
            i.draw(win)

    def undraw(self):
        for i in self.DrawableItems:
            i.undraw()

class GridBox:
    def __init__(self,dayData,topLeftPoint,bottomRightPoint):
        self.Data = dayData # each day
        self.Items = []
        self.topLeftPoint = topLeftPoint
        self.bottomRightPoint = bottomRightPoint
        self.Rectangle = Graphics.Rectangle(self.topLeftPoint,self.bottomRightPoint)
        self.Label = Graphics.Text(Graphics.Point(bottomRightPoint.getX()-8,topLeftPoint.getY()+8),'0')
        self.Label.setSize(10)

    def SetData(self,data):
        self.Items = []
        self.Data = data
        self.Label.setText(str(data.Date.Day))
        self.CreateItems()

    def CreateItems(self):
        p1 = Graphics.Point(self.topLeftPoint.getX(),self.topLeftPoint.getY()+14)#self.topLeftPoint.clone()
        p2 = Graphics.Point(self.bottomRightPoint.getX(),p1.getY()+12)
        for i in self.Data.Items:
            self.Items.append(ItemBox(i,p1,p2))
            p1 = Graphics.Point(p1.getX(),p1.getY()+12)
            p2 = Graphics.Point(p2.getX(),p2.getY()+12)

    def Clicked(self,point):
        tl = self.topLeftPoint
        br = self.bottomRightPoint
        return tl.getY() < point.getY() < tl.getY() + 15 and br.getX() > point.getX() > br.getX() - 15

    def draw(self,win):
        self.Rectangle.draw(win)
        if(self.Label.getText() == '0'):
            self.Label.undraw()
        else:
            self.Label.draw(win)
        for i in self.Items:
            i.draw(win)

    def undraw(self,win=None):
        self.Rectangle.undraw()
        self.Label.undraw()
        for i in self.Items:
            i.undraw()

class Header:
    def __init__(self,Grid,viewMonth,viewYear):
        self.Items = []
        monthNames = ['null','January','February','March','April','May','June','July','August',
            'September','October','November','December']
        dayNames = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
        
        monthHeader = Graphics.Text(Graphics.Point(400,20),monthNames[viewMonth] + ' ' +str(viewYear))
        monthHeader.setSize(22)
        self.Items.append(monthHeader)
        
        count = 0
        for i in dayNames:
            grid = Grid[count]
            count += 1
            x = grid.topLeftPoint.getX()+(grid.bottomRightPoint.getX() - grid.topLeftPoint.getX())/2
            y = grid.topLeftPoint.getY()-10
            label = Graphics.Text(Graphics.Point(x,y),i)
            label.setSize(12)
            self.Items.append(label)
        
    def draw(self,win):
        for i in self.Items:
            i.draw(win)

    def undraw(self):
        for i in self.Items:
            i.undraw()

class ItemBox:
    def __init__(self,itemData,topLeftPoint,bottomRightPoint):
        self.Data = itemData # each item
        self.topLeftPoint = topLeftPoint
        self.bottomRightPoint = bottomRightPoint
        self.Label = Graphics.Text(Graphics.Point(topLeftPoint.getX()+(bottomRightPoint.getX()-topLeftPoint.getX())/2,
            topLeftPoint.getY()+(bottomRightPoint.getY()-topLeftPoint.getY())/2),self.Data.Name)
        self.Label.setSize(10)
        self.Rectangle = Graphics.Rectangle(self.topLeftPoint,self.bottomRightPoint)
        self.Rectangle.setFill(self.Data.Class.Color)

        self.CompletedRect = Graphics.Rectangle(Graphics.Point(self.topLeftPoint.getX()+10,self.topLeftPoint.getY()),self.bottomRightPoint)
        self.CompletedRect.setFill(Graphics.color_rgb(70,70,70))

    def Clicked(self,point):
        tl = self.topLeftPoint
        br = self.bottomRightPoint
        return tl.getY() < point.getY() < br.getY() and tl.getX() < point.getX() < br.getX()

    def draw(self,win):
        self.Rectangle.draw(win)
        if self.Data.Completed:
            self.CompletedRect.draw(win)
        self.Label.draw(win)

    def undraw(self,win=None):
        self.Rectangle.undraw()
        self.CompletedRect.undraw()
        self.Label.undraw()

class ClassesList:
    def __init__(self,classes):
        self.DrawableItems = []
        width = 70
        height = 13
        p1 = Graphics.Point(0,0)
        p2 = Graphics.Point(width,height)
        count = 1
        for i in classes:
            mpoint = Graphics.Point(p1.getX()+(p2.getX()-p1.getX())/2,p1.getY()+(p2.getY()-p1.getY())/2)
            rect = Graphics.Rectangle(p1,p2)
            rect.setFill(i.Color)
            label = Graphics.Text(mpoint,i.Name)
            label.setSize(10)
            self.DrawableItems.append(rect)
            self.DrawableItems.append(label)

            p1 = Graphics.Point(0 + (count%3 * width),0 + int(count/3)* height)
            p2 = Graphics.Point(width + (count%3 * width),p1.getY()+height)
            count += 1

    def draw(self,win):
        for i in self.DrawableItems:
            i.draw(win)
    def undraw(self):
        for i in self.DrawableItems:
            i.undraw()

