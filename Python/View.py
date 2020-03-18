import Graphics
import time
class View:
    def __init__(self):
        self.win = Graphics.GraphWin('Window',800,700)
        self.Grid = View.CreateGrid(7,6,Graphics.Point(0,0),Graphics.Point(800,700))
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
                gridList.append(View.GridBox(None,Graphics.Point(x1,y1),Graphics.Point(x2,y2)))
                x1 += eachWidth
                x2 += eachWidth
            y1 += eachHeight
            y2 += eachHeight
            x1 = topLeftPoint.getX()
            x2 = x1+eachWidth
        return gridList
    def draw(self):
        for i in self.Grid:
            i.draw(self.win)
    def undraw(self):
        pass
    class GridBox:
        def __init__(self,dayData,topLeftPoint,bottomRightPoint):
            self.Data = dayData # each day
            self.Items = []
            self.topLeftPoint = topLeftPoint
            self.bottomRightPoint = bottomRightPoint
            self.Rectangle = Graphics.Rectangle(self.topLeftPoint,self.bottomRightPoint)
            self.Label = Graphics.Text(Graphics.Point(bottomRightPoint.getX()-8,topLeftPoint.getY()+8),'22')
            self.Label.setSize(10)
        def SetData(self,data):
            self.Data = data
            self.Label.setText(str(data.Date.Day))
            self.CreateItems()
        def CreateItems(self):
            p1 = self.topLeftPoint.clone()
            p2 = Graphics.Point(self.bottomRightPoint.getX(),p1.getY()+10)
            for i in self.Data.Items:
                self.Items.append(ItemBox(i,p1,p2))
                p1 = Graphics.Point(p1.getX(),p1.getY()+10)
                p2 = Graphics.Point(p2.getX(),p2.getY()+10)
        def draw(self,win):
            self.Rectangle.draw(win)
            if(self.Label.getText() == '0'):
                self.Label.undraw()
            else:
                self.Label.draw(win)
        def undraw(self,win=None):
            self.Rectangle.undraw()
            self.Label.undraw()

        class ItemBox:
            def __init__(self,itemData,topLeftPoint,bottomRightPoint):
                self.Data = itemData # each item
                self.topLeftPoint = topLeftPoint
                self.bottomRightPoint = bottomRightPoint
                self.Label = Graphics.Text(Graphics.Point((topLeftPoint.getX()-bottomRightPoint.getX())/2,
                    (topLeftPoint.getY()-bottomRightPoint.getY())/2),self.Data.Name)
                self.Label.setSize(10)
                self.Rectangle = Graphics.Rectangle(self.topLeftPoint,self.bottomRightPoint)
                self.Rectangle.setBackground(self.Data.Class.Color)
            def draw(self,win):
                self.Rectangle.draw(win)
                self.Label.draw(win)
            def undraw(self,win=None):
                self.Rectangle.draw(win)
                self.Label.draw(win)



'''
g = Graphics.GraphWin('Window',800,700)
g.setBackground(Graphics.color_rgb(255,255,255))
x = View.CreateGrid(7,6,Graphics.Point(0,0),Graphics.Point(800,700))
for i in x:
    i.draw(g)
#while True:
    #time.sleep(.1)
input("press return to continue...")'''
