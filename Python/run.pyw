#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from GraphScreen import *
from library.Graphics import *
import time

# Main running for the calendar
win = Window("Calendar",800,700)
win.open()
while(win.isRunning()):
    win.run()
    win.checkButtons()
    time.sleep(.1)
