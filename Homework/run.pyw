from Control import Control
import time
app = Control()
testing = False
while app.Running:
    if not testing:
        try:
            app.CheckKeys()
            app.CheckMouse()
        except:
            break
    else:
        app.CheckKeys()
        app.CheckMouse()
    time.sleep(.1)
app.Close()
