from library.ReadWrite import *

def color_rgb(r,g,b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color"""
    return "#%02x%02x%02x" % (r,g,b)

class prefs:
    def __init__(self):
        self.SETTINGS_FILE = 'settings/settings.txt'
        self.DATA_FILE = getSetting(self.SETTINGS_FILE, "DATA_FILE")
        self.CLASS_FILE = getSetting(self.SETTINGS_FILE, "CLASS_FILE")
        
        self.MONTH_NAMES = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
        self.DAY_HEADER = ['SUN','MON','TUE','WED','THU','FRI','SAT']
        self.CLASSES = importClasses(self.CLASS_FILE)

        self.setDarkMode(bool(getSetting(self.SETTINGS_FILE, 'PREFS.DARK_MODE')=='True'))

    def setDarkMode(self,val):
        self.DARK_MODE = val
        if not self.DARK_MODE:
            # Regular Mode Colors
            self.COMPLETED_ITEM_TEXT_COLOR = color_rgb(100,100,100)
            self.COMPLETED_ITEM_COLOR = color_rgb(150,150,150)
            
            self.BLACK = color_rgb(0,0,0)
            self.WHITE = color_rgb(255,255,255)
            
            self.TODAY_COLOR = color_rgb(230,230,230)
            self.OTHER_MONTH_COLOR = color_rgb(150,150,150)
        else:
            # Dark Mode Colors
            i = 80;  self.COMPLETED_ITEM_TEXT_COLOR = color_rgb(i,i,i)
            i = 80;  self.COMPLETED_ITEM_COLOR = color_rgb(i,i,i)
            
            i = 80;  self.TODAY_COLOR = color_rgb(i,i,i)
            i = 0;   self.OTHER_MONTH_COLOR = color_rgb(i,i,i)
            
            i = 200; self.BLACK = color_rgb(i,i,i)
            i = 30;  self.WHITE = color_rgb(i,i,i)
    def updateClasses(self):
        self.CLASSES = importClasses(self.CLASS_FILE)
                
PREFS = prefs()

