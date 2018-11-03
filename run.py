from GraphScreen import *
from Graphics import *
import time

# Main running for the calendar 
win = Window("Calendar",800,700)
win.open()
while(win.isRunning()):
    win.run()
    win.checkButtons()
    time.sleep(.1)
