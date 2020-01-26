'''
Created by Aidan Smith July 2018
Modified November 2018 for new application
Version 4
'''
from library.Graphics import *
from library.ReadWrite import *
from prefs import *

class CourseCreator:
    def __init__(self):
        #self.courses = listOfCourses
        self.screen = GraphWin("Class Chooser",350,500,autoflush = False)
        self.subjectList = SelectFromList(Point(0,180),175,20,15)

        # "Button" objects to check if colors are clicked on
        self.redSlider = Button('',10,Point(0,0),Point(255,50))
        self.greenSlider = Button('',10,Point(0,50),Point(255,100))
        self.blueSlider = Button('',10,Point(0,100),Point(255,150))
        # Displays the number of the color for each
        self.redLabel = Text(Point(300,25),'0')
        self.greenLabel = Text(Point(300,75),'0')
        self.blueLabel = Text(Point(300,125),'0')
        # Rectangle to display the test color
        self.testViewer = Rectangle(Point(255,0),Point(350,150))
        self.testViewer.draw(self.screen)
        # Display the current value on the slider
        self.redLoc = Line(Point(0,0),Point(0,50))
        self.redLoc.setFill(color_rgb(255,255,255))
        self.greenLoc = Line(Point(0,50),Point(0,100))
        self.greenLoc.setFill(color_rgb(255,255,255))
        self.blueLoc = Line(Point(0,100),Point(0,150))
        self.blueLoc.setFill(color_rgb(255,255,255))
        #Entry Box for the name
        self.entryBox = Entry(Point(100,165),15)

        # Buttons
        self.exitBTN = Button('X',20,Point(self.screen.getWidth()-25,self.screen.getHeight()-30),Point(self.screen.getWidth(),self.screen.getHeight()))
        self.exitBTN.draw(self.screen)
        self.addBTN = Button('+',20,Point(self.screen.getWidth()-50,self.screen.getHeight()-30),Point(self.screen.getWidth()-25,self.screen.getHeight()))
        self.addBTN.draw(self.screen)
        self.removeBTN = Button('-',20,Point(self.screen.getWidth()-75,self.screen.getHeight()-30),Point(self.screen.getWidth()-50,self.screen.getHeight()))
        self.removeBTN.draw(self.screen)

        # Show all objects
        self.redSlider.draw(self.screen)
        self.redLabel.draw(self.screen)
        self.greenSlider.draw(self.screen)
        self.greenLabel.draw(self.screen)
        self.blueSlider.draw(self.screen)
        self.blueLabel.draw(self.screen)

        self.redLoc.draw(self.screen)
        self.greenLoc.draw(self.screen)
        self.blueLoc.draw(self.screen)

        self.entryBox.draw(self.screen)


        #Create all of the different color lines
        lines = []
        for i in range(0,256,1):
            temp = Line(Point(i,0),Point(i,50))
            temp.setFill(color_rgb(i,0,0))

            temp1 = Line(Point(i,50),Point(i,100))
            temp1.setFill(color_rgb(0,i,0))

            temp2 = Line(Point(i,100),Point(i,150))
            temp2.setFill(color_rgb(0,0,i))

            lines.append(temp)
            lines.append(temp1)
            lines.append(temp2)

        for i in lines:
            i.draw(self.screen)

        self.createCoursesList()
        self.screen.autoflush = True
    def run(self):
        r = 0
        g = 0
        b = 0
        run = True
        while run:
            key = self.screen.checkKey()
            mouse = self.screen.checkMouse()
            if(mouse == None):
                mouse = Point(-1,-1)

            if(self.redSlider.pressed(mouse)):
                r = int(mouse.getX())
                self.redLabel.setText(str(r))
                self.redLoc.undraw()
                self.redLoc = Line(Point(r,0),Point(r,50))
                self.redLoc.setFill(color_rgb(255,255,255))
                self.redLoc.draw(self.screen)

            if(self.greenSlider.pressed(mouse)):
                g = int(mouse.getX())
                self.greenLabel.setText(str(g))
                self.greenLoc.undraw()
                self.greenLoc = Line(Point(g,50),Point(g,100))
                self.greenLoc.setFill(color_rgb(255,255,255))
                self.greenLoc.draw(self.screen)
            if(self.blueSlider.pressed(mouse)):
                b = int(mouse.getX())
                self.blueLabel.setText(str(b))
                self.blueLoc.undraw()
                self.blueLoc = Line(Point(b,100),Point(b,150))
                self.blueLoc.setFill(color_rgb(255,255,255))
                self.blueLoc.draw(self.screen)
            self.testViewer.setFill(color_rgb(r,g,b))

            self.subjectList.checkSelected(mouse)

            self.r = str(r)
            self.g = str(g)
            self.b = str(b)
            # Add current item to the list
            if(self.addBTN.pressed(mouse) or key == 'Return'):
                name = self.entryBox.getText()
                color = 'color_rgb(' + self.r + ',' + self.g + ','+self.b+')'

                if name != '':
                    self.saveCourse(name,color)
                self.entryBox.setText('')
                self.screen.autoflush = False
                self.updateCoursesList()
                self.screen.autoflush = True

            # remove the selected item from the list
            if(self.removeBTN.pressed(mouse) or key == 'BackSpace'):
                name = self.subjectList.getSelected()
                if name != []: # If nothing is selected doesn's crash
                    self.removeCourse(name[0])
                    self.screen.autoflush = False
                    self.subjectList.remove(name)
                    self.updateCoursesList()
                    self.screen.autoflush = True

            # Close the window
            if(key == 'Escape' or self.exitBTN.pressed(mouse)):
                run = False

        self.screen.close()


    def createCoursesList(self):
        classes = PREFS.CLASSES
        self.subjectList = SelectFromList(Point(0,180),175,20,15)
        for i in classes:
            self.subjectList.add(i,eval(PREFS.CLASSES[i]),serial=[i])

        self.subjectList.draw(self.screen)

    def updateCoursesList(self):
        self.subjectList.undraw()
        PREFS.updateClasses()
        self.createCoursesList()

    def saveCourse(self,label,color):
        file = ReadWrite(PREFS.CLASS_FILE)
        file.write(label+'\n'+color+'\n')

    def removeCourse(self,label):
        file = ReadWrite(PREFS.CLASS_FILE)
        data = file.read()
        temp = []
        for i in range(0,len(data)):
            x = data[i]
            if len(x) > 2 and x[:-1] == label:
                temp.append(x)
                temp.append(data[i+1])
        for i in temp:
            data.remove(i)
        file.overWrite('')
        for i in data:
            file.write(i)
