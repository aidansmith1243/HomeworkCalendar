from Graphics import *
import calendar

def monthConversion(month,year):
        if(month > 12):
            year+=1
            month = 1
        if(month < 1):
            year-=1
            month = 12
        return month,year
# used internally to know where the current month starts
def getStartingIndex(dates):
    index = 0
    for i in dates[0]:
        if i == 1:
                break
        '''
        if type(i) == str:
            if i == ' 1':
                break
        else:
            if i.getText() == ' 1':
                break
        '''
        index +=1
    return index

# used internally to know where the current month ends
def getEndingIndex(dates):
    index = 0
    for i in dates[4]:
        if i == 1:
                break
        '''
        if type(i) == str:
            if i == ' 1':
                break
        else:
            if i.getText() == ' 1':
                break
        '''
        index +=1
    return index
def createDatesGrid(monthGrid,month,day,year):
        datesGrid = []
        dates = createDates(month,day,year)
        week = []
        mod = 12
        r=0
        c=0
        for i in monthGrid:
            for x in i:
                pt = Point(x.getP2().getX()-mod,x.getP1().getY()+mod)
                data = Text(pt,dates[r][c])
                week.append(data)
                c+=1
            datesGrid.append(week)
            week=[]
            r+=1
            c=0
        return datesGrid
def createDates(month,day,year):
        if day == 0:
                day = 1
        
        month = month
        year = year
        dm = DateMaker()
        thisMonth = dm.createDatesList(year,month)
        index = 0;
        for i in thisMonth[0]:
            if i != '  ':
                break
            index+=1
        startingIndex = index
        # Find the previous month and create the month
        lmth = month-1
        lyr = year
        if(month == 1):
            lmth = 12
            lyr = year-1
        lastMonth = dm.createDatesList(lyr,lmth)
        # Find the next month and create the month
        nmth = month+1
        nyr = year
        if(month == 12):
            nmth = 1
            nyr = year+1
        nextMonth = dm.createDatesList(nyr,nmth)
        # Remove any empty weeks
        for i in lastMonth:
            if i[0] == '':
                lastMonth.remove(i)
                
        for i in thisMonth:
            if i[0] == '':
                thisMonth.remove(i)
        
        for i in nextMonth:
            if i[0] == '':
                nextMonth.remove(i)
        # Combine the three months into a single array
        comb,startIndex = dm.combineMonths(lastMonth,thisMonth)
        comb,i = dm.combineMonths(comb,nextMonth)
        # Final Data that holds the month info
        temp = comb[startIndex:startIndex+5]
        for r in range(len(temp)):
                for c in range(len(temp[r])):
                        temp[r][c] = int(temp[r][c])
        return temp
        
class DateMaker:
    def createDatesList(self,year,month):
        # Create the calendar object where the week starts on Monday
        #cal = calendar.TextCalendar(calendar.MONDAY)
        cal = calendar.TextCalendar(calendar.SUNDAY)

        # Create a str for the month
        month = cal.formatmonth(year, month)

        # Hold days in order
        a = ['','','','','','','','']

        # Run through the string and seperate weeks
        aCoord = 0;
        i = 0;
        while i < len(month):
            if(month[i] == '\n'):
                aCoord+=1;
            else:
                a[aCoord]+=month[i]
            i+=1
        a = a[2:]

        # Run through the lines and seperate the days
        i = 0;
        for x in a:
            b = [x[0:2],x[3:5],x[6:8],x[9:11],x[12:14],x[15:17],x[18:20]] 
            a[i] = b
            i+=1
        return a
    
    def combineMonths(self,first,second):
        returnIndex = len(first)-1
        if(first[len(first)-1][6] == ''):
            lastWeek = first[len(first)-1]
            spot = 0;
            for i in lastWeek:
                if i == '':
                    break
                spot+=1

            while spot < 7:
                first[len(first)-1][spot] = second[0][spot]
                spot+=1
            second = second[1:len(second)]
        
        else:
            returnIndex +=1
        return first+second,returnIndex
    def createYear(self,year):
        all = []
        for i in range(1,13):
            temp = self.createDatesList(year,i)
            for x in range(len(temp)):
                for y in range(7):
                    if temp[x][y] != '' and temp[x][y] != '  ':
                        temp[x][y] = [i,int(temp[x][y]),year]
            
            if len(all) > 0:
                index = 7
                for z in range(7):
                    if all[len(all)-1][z] == '':
                        index = z
                        break
                for z in range(index,7):
                    all[len(all)-1][z] = temp[0][z]
                if index != 7:
                    temp.remove(temp[0])
            
            for z in temp:
                all.append(z)
            try:
                all.remove(['','','','','','',''])
            except:
                pass
            
        for i in range(len(all)):
            for x in range(7):
                if all[i][x] != '' and all[i][x] != '  ':
                    all[i][x][0] = int(all[i][x][0])
                else:
                    all[i][x] = [0,0]
        return all #[day,month,year]
        
