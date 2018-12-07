from library.Graphics import *
from library.ReadWrite import *
from prefs import *
import datetime

def addItem(string):
    file = ReadWrite(PREFS.DATA_FILE)
    data = file.write(string+'\n')

class AddItem:
    
    def __init__(self,date = [0,0,0]):
        now = datetime.datetime.now()
        if date == [0,0,0]:
            month = now.month
            day = now.day
            year = now.year
        else:
            month = date[0]
            day = date[1]
            year = date[2]

        
        screen = GraphWin("New Item",250,400,autoflush=False)
        screen.pause()
        screen.setBackground(color_rgb(255,255,255))
        
        self.exitBTN = Button("x",20,Point(screen.getWidth()-25,0),Point(screen.getWidth(),25))
        #self.exitBTN.draw(screen)
        self.submitBTN = Button("Submit",15,Point(screen.getWidth()-60,screen.getHeight()-25),Point(screen.getWidth(),screen.getHeight()))
        #self.submitBTN.draw(screen)

        self.dateMonth = EntryBox(screen,'',5,30,20,False)
        self.dateMonth.setText(month)
        
        self.dateDay = EntryBox(screen,'',5,90,20,False)
        self.dateDay.setText(day)
        
        self.dateYear = EntryBox(screen,'',5,150,20,False)
        self.dateYear.setText(year)

        self.title = EntryBox(screen,'',28,-21,50,False)

        self.dateDay.draw(screen)
        self.dateMonth.draw(screen)
        self.dateYear.draw(screen)
        self.title.draw(screen)
        
        
        self.subjectList = SelectFromList(Point(30,80),175,20,15)
        #classes,colors = importClasses()
        for i in PREFS.CLASSES:
            self.subjectList.add(i,eval(PREFS.CLASSES[i]))
        
        self.subjectList.draw(screen)
        
        
        self.screen = screen
        self.screen.resume()
        self.screen.resetKey()
    def run(self):
        myStr = ''
        running = True
        while running:
            mouseClick = self.screen.checkMouse()
            key = self.screen.checkKey()
            if(mouseClick == None):
                mouseClick = Point(-1,-1)

            self.subjectList.checkSelected(mouseClick)
            
            # Exit the screen
            if(self.exitBTN.pressed(mouseClick) or key == 'Escape'):
                running = False
                
            # Add to the list and exit
            if (self.submitBTN.pressed(mouseClick) or key == 'Return') and (len(self.title.getText()) > 1 and self.subjectList.getSelectedLabel() != '' and not "," in self.title.getText()):
                running = False
                myStr = self.createOutput()
            if(key == 'Up'):
                self.screen.pause()
                self.subjectList.selectPrevItem()
                self.screen.resume()
            if(key == 'Down'):
                self.screen.pause()
                self.subjectList.selectNextItem()
                self.screen.resume()

            txt = ''
            for c in self.title.getText():
                if(ord(c)<123):
                    txt += c
            self.title.setText(txt)
            self.screen.resetKey()
        self.screen.close()
        if myStr != '':
            addItem(myStr)
        
        return myStr
    def createOutput(self):
        myStr = self.subjectList.getSelectedLabel() + ','
        myStr += self.dateMonth.getText() + ',' + self.dateDay.getText() + ',' + self.dateYear.getText() + ','
        myStr += self.title.getText() + ','
        return myStr
    

class AddTimedItem(AddItem):
    def __init__(self,date=[0,0,0]):
        AddItem.__init__(self,date)

        self.startDate = EntryBox(self.screen,'',5,10,350,False)
        self.endDate = EntryBox(self.screen,'',5,90,350,False)

        self.am_pm_start = SelectFromList(Point(60,350),20,10,10)
        self.am_pm_start.add("AM",PREFS.WHITE)
        self.am_pm_start.add("PM",PREFS.WHITE)

        self.am_pm_end = SelectFromList(Point(140,350),20,10,10)
        self.am_pm_end.add("AM",PREFS.WHITE)
        self.am_pm_end.add("PM",PREFS.WHITE)

        self.startDate.draw(self.screen)
        self.endDate.draw(self.screen)
        self.am_pm_start.draw(self.screen)
        self.am_pm_end.draw(self.screen)
        
    def createOutput(self):
        myStr = self.subjectList.getSelectedLabel() + ','
        myStr += self.dateMonth.getText() + ',' + self.dateDay.getText() + ',' + self.dateYear.getText() + ','
        myStr += self.title.getText() + ',' 
        return myStr        
