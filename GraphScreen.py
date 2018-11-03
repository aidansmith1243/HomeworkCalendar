import Graphics as g
# from GraphScreen import *
from Graphics import *
from AddItem import *
from Calendar import *
from prefs import *
import time
import datetime

def null():
    pass

class GraphScreen:
    '''
    This class is used as a template for easy creation of graphic
    applets
    '''
    
    def __init__(self,name,width,height):
        '''
        For any sub classes use "GraphScreen.__init__(self)" to
        initiate variables
        '''
        self.isOpen = False
        self.items = {}
        self.actions = {}
        
        self.g = g
        self.win = g.GraphWin(name,width,height)
        self.win.setBackground(PREFS.WHITE)
        
    def __str__(self):
        return str([self.isOpen,self.items,self.actions])
    
    def open(self):#,name,height,width):
        '''
        Generates and opens the window with all items drawn on screen
        '''
        if self.isOpen:
            return;
        self.isOpen = True
        
        self.draw()

    def isRunning(self):
        return self.isOpen
    
    def close(self):
        '''
        Closes the graphic window and changes isOpen to False
        '''
        self.win.close()
        self.isOpen = False
        
    def draw(self,x=0):
        '''
        Draws every item in "items" to the window

        x - Does nothing, only used to match the method from other
        classes
        '''
        self.win.pause()
        #print self.items
        for i in self.items:
            try:
                if type(self.items[i]) == list:
                    for x in self.items[i]:
                        try:
                            x.draw(self.win)
                        except:
                            for y in x:
                                y.draw(self.win)
                else:
                    self.items[i].draw(self.win)
            except:
                print 'ERROR DRAWING ITEM: ' + str(i)
        
        self.win.resume()
        

    def undraw(self):
        '''
        Undraws every item in items from the window
        '''
        self.win.pause()

        for i in self.items:
            try:
                if type(self.items[i]) == list:
                    for x in self.items[i]:
                        try:
                            x.undraw()
                        except:
                            for y in x:
                                y.undraw()
                else:
                    self.items[i].undraw()
            except:
                print 'ERROR UNDRAWING ITEM: ' + str(i)
        
        self.win.resume()
        
    def run(self):
        '''
        Overwrite in sub class to complete main functions
        '''
        if self.isOpen:
            pass
    def createItems(self):
        '''
        Overwrite in sub class and call during constructor to generate
        all of the items
        '''
        pass
    def addAction(self,key,method = null):
        '''
        Creates an action for when the key is pressed it will
        complete the method given otherwise will only give the key
        name.
        
        Currently only works for the keyboard
        '''
        self.actions[key] = method
    def addItem(self,name,item):
        '''
        Add the graphic item to the collection
        '''
        self.items[name] = item
    def removeItem(self,name):
        del self.items[name]
        
    def undrawItem(self,name):
        self.win.pause()
        try:
            if type(self.items[name]) == list:
                for x in self.items[name]:
                    try:
                        x.undraw()
                    except:
                        for y in x:
                            y.undraw()
            else:
                self.items[name].undraw()
        except:
            print 'ERROR UNDRAWING ITEM: ' + str(x)
        self.win.resume()
        
    def drawItem(self,name):
        self.win.pause()
        try:
            if type(self.items[name]) == list:
                for x in self.items[name]:
                    try:
                        x.draw(self.win)
                    except:
                        for y in x:
                            y.draw(self.win)
            else:
                self.items[name].draw(self.win)
        except:
            print 'ERROR DRAWING ITEM: ' + str(x)
        self.win.resume()
        
    def checkButtons(self):
        '''
        Called in the main loop to check if buttons or the mouse
        has been pressed

        returns - blank string if nothing pressed
                - string title in "actions" to be used if needed

        Currently only works for the keyboard
        '''
        if not self.isOpen:
            return ''
        self.win.resetKey()
        key = self.win.checkKey()

        for i in self.actions:
            if key == i:
                self.actions[i]()
                return i

        return ''
        
class Window(GraphScreen):
    def __init__(self,name,width,height):
        GraphScreen.__init__(self,name,width,height)

        # Variables
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.day = self.now.day

        self.addItemWin = False
        self.newItem = ''
        
        self.height = height
        self.width = width
        
        self.savedItem = []
        self.selectedItem = []
        self.dayClicked = []

        self.lastTime = time.time()
        self.lastMouse = Point(-1,-1)

        self.viewMonth = True
        
        self.createActions()        
        self.createItems()
        self.updateCalendar()
        
        
    def run(self):
        if self.isOpen:
            mouse = self.win.checkMouse()
            
            # Remove any previous selected daily items
            if mouse.getX() != -1 and mouse.getY()!= -1:
                self.calendar.uncheckSelected()
                
                # Add a new item to the calendar when double click on a day  
                self.dayClicked = self.calendar.getDayClicked(mouse)
                # Double clicking to add an item
                if(time.time() - self.lastTime < .4):
                    addDay = self.calendar.getDayClicked(self.lastMouse)
                    addDay2 = self.calendar.getDayClicked(mouse) 
                    if(addDay == addDay2 and addDay != []):
                        self.add(addDay)    
                self.lastMouse = mouse
                self.lastTime = time.time()
                
            # Select an item if it is clicked
            self.selectedItem = self.calendar.getSelected(mouse)
            

        return self.isOpen
    
    def createItems(self):
        self.calendar = Month(self.month,self.day,self.year,Point(0,60),Point(self.width,self.height))
        self.title = Text(Point(self.width/2,25),str(PREFS.MONTH_NAMES[self.month]) + " " + str(self.year))
        self.title.setSize(25)
        self.title.setTextColor(PREFS.BLACK)
        self.header = createDayHeader()
        self.legend = createLegend()
        
    def createActions(self):
        self.addAction('Escape',self.close)
        self.addAction('space',self.add)
        self.addAction('BackSpace',self.remove)
        self.addAction('Return',self.complete)
        self.addAction('t',self.viewToday)
        self.addAction('v',self.paste)
        self.addAction('c',self.copy)
        self.addAction('x',self.cut)
        self.addAction('Right',self.nextMonth)
        self.addAction('Left',self.prevMonth)
        self.addAction('d',self.darkMode)

    def updateCalendar(self):
        self.win.pause()
        
        self.win.setBackground(PREFS.WHITE)
        
        # undraw Items
        self.calendar.undraw()
        self.title.undraw()
        for i in self.header:
            i.undraw()
        for i in self.legend:
            i.undraw()
        
        # update items
        self.createItems()
        
        # redraw Items
        self.calendar.draw(self.win)
        self.title.draw(self.win)
        for i in self.header:
            i.draw(self.win)
        for i in self.legend:
            i.draw(self.win)
            
        self.win.resume()

    '''-----------------------------'''
    ''' All Keyboard Button Actions '''
    
    def add(self,date = [0,0,0]):
        self.addWin = AddItem(date)
        self.addWin.run()
        self.updateCalendar()
        
    
    def remove(self):
        removeItem(PREFS.DATA_FILE, self.selectedItem)
        self.updateCalendar()
        
    def complete(self):
        completeItem(PREFS.DATA_FILE, self.selectedItem)
        self.updateCalendar()
        
    def viewToday(self):
        self.year = self.now.year
        self.month = self.now.month
        self.updateCalendar()
        
    def paste(self):
        #Fix
        if len(self.savedItem) > 0:
            temp = self.savedItem
            temp[1] = str(self.dayClicked[0])
            temp[2] = str(self.dayClicked[1])
            temp[3] = str(self.dayClicked[2])
            addItem(PREFS.DATA_FILE, temp)
            self.updateCalendar()
        
    def cut(self):
        self.savedItem = self.selectedItem
        self.remove()
        self.updateCalendar()
        
    def copy(self):
        self.savedItem = self.selectedItem
        
    def nextMonth(self):
        self.month,self.year = monthConversion(self.month+1, self.year)
        self.updateCalendar()    
        
    def prevMonth(self):
        self.month,self.year = monthConversion(self.month-1, self.year)
        self.updateCalendar()
            
    def darkMode(self):
        
        if PREFS.DARK_MODE:
            PREFS.setDarkMode(False)
        else:
            PREFS.setDarkMode(True)
        self.updateCalendar()
        
    ''' All Keyboard Button Actions '''
    '''-----------------------------'''
    


