from GraphScreen import *
from Graphics import *
import time
'''
c = color_rgb(200,40,50)
c2 = color_rgb(90,40,30)

win = GraphWin("Test",500,500)
out = Rectangle(Point(30,30),Point(160,160))
out.setFill(c)

inner = Rectangle(Point(31,31),Point(159,50))
inner.setFill(c)
inner.setOutline(c)

out.draw(win)
inner.draw(win)
inner.setFill(c2)

while True:
    if win.checkKey() == 'Escape':
        break
win.close()
'''
# Main running for the calendar 
win = Window("Calendar",800,700)
win.open()
while(win.isRunning()):
    win.run()
    win.checkButtons()
    time.sleep(.1)
