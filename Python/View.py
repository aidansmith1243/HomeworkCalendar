import Graphics
import time
class View:
    def __init__(self):
        pass
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
                gridList.append(View.GridBox(Graphics.Point(x1,y1),Graphics.Point(x2,y2)))
                x1 += eachWidth
                x2 += eachWidth
            y1 += eachHeight
            y2 += eachHeight
            x1 = topLeftPoint.getX()
            x2 = x1+eachWidth
        return gridList

    class GridBox:
        def __init__(self,topLeftPoint,bottomRightPoint):
            self.Items = []
            self.topLeftPoint = topLeftPoint
            self.bottomRightPoint = bottomRightPoint
            self.Rectangle = Graphics.Rectangle(self.topLeftPoint,self.bottomRightPoint)
            self.Label = Graphics.Text(Graphics.Point(bottomRightPoint.getX()-8,topLeftPoint.getY()+8),'22')
            self.Label.setSize(10)
        def SetDate(self,day):
            self.Label.setText(str(day))
        def draw(self,win):
            self.Rectangle.draw(win)
            if(self.Label.getText() == '0')
                self.Label.undraw()
            else:
                self.Label.draw(win)
        def undraw(self,win=None):
            self.Rectangle.undraw()
            self.Label.undraw()
        class ItemBox:
            def __init__(self,):
                pass
            def draw(self,win):
                pass
            def undraw(self,win=None):
                pass




g = Graphics.GraphWin('Window',800,700)
g.setBackground(Graphics.color_rgb(255,255,255))
x = View.CreateGrid(7,6,Graphics.Point(0,0),Graphics.Point(800,700))
for i in x:
    i.draw(g)
#while True:
    #time.sleep(.1)
input("press return to continue...")
