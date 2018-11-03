from ReadWrite import *

def color_rgb(r,g,b):
    """r,g,b are intensities of red, green, and blue in range(256)
    Returns color specifier string for the resulting color"""
    return "#%02x%02x%02x" % (r,g,b)

DATA_FILE = 'lib/data/data.txt'
CLASS_FILE = 'lib/data/classes.txt'

DARK_MODE = False;

MONTH_NAMES = {1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
DAY_HEADER = ['SUN','MON','TUE','WED','THU','FRI','SAT']
CLASSES = importClasses(CLASS_FILE)

# GRAY = color_rgb(200,200,200)
if not DARK_MODE:
    COMPLETED_ITEM_TEXT_COLOR = color_rgb(100,100,100)
    COMPLETED_ITEM_COLOR = color_rgb(150,150,150)
    
    BLACK = color_rgb(0,0,0)
    WHITE = color_rgb(255,255,255)
    
    TODAY_COLOR = color_rgb(230,230,230)
    OTHER_MONTH_COLOR = color_rgb(150,150,150)
else:
    COMPLETED_ITEM_TEXT_COLOR = color_rgb(100,100,100)
    i=75
    COMPLETED_ITEM_COLOR = color_rgb(i,i,i)
    i=75
    TODAY_COLOR = color_rgb(i,i,i)
    i=35
    OTHER_MONTH_COLOR = color_rgb(i,i,i)
    i=200
    BLACK = color_rgb(i,i,i)
    
    WHITE = color_rgb(0,0,0)

""" My Methods 

def createLegend():
    legend = []
    width = 80
    height = 13
    count = 0
    for i in CLASSES:
        x1 = 0 + count/3 * width
        x2 = width + count/3 * width
        y1 = 0 + count%3 * height
        y2 = height + count%3 * height
        
        temp = Button(i,11,Point(x1,y1),Point(x2,y2))
        temp.setFill(eval(CLASSES[i]))
        legend.append(temp)
        count+=1
    return legend
def createDayHeader():
    arr = []
    width = 800
    w = width/7
    count = 0
    for i in DAY_HEADER:
        temp = Text(Point((width/14)+count*w,50),i)
        temp.setSize(12)
        temp.setTextColor(BLACK)
        arr.append(temp)
        count+=1 
    return arr
    """