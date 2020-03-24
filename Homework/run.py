from Control import Control
app = Control()
while app.Running:
    try:
        app.CheckKeys()
        app.CheckMouse()
    except:
        break
app.Close()
