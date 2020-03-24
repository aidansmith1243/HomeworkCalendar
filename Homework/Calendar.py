class Calendar:
    def __init__(self):
        import datetime

        self.FinalYear = datetime.datetime.now().year
        self.CalendarDateList = Calendar.CreateCalendar(self.FinalYear)
    def AddYear(self):
        import DataClasses
        self.FinalYear += 1
        temp = Calendar.CreateCalendar(self.FinalYear)
        for i in temp:
            self.CalendarDateList.append(i)
    def GetMonthIndex(self,month,year):
        '''
        Gives the index of the first week for the selected month
        '''
        count = 0
        for i in self.CalendarDateList:
            if(i[6].Date.Month == month and i[6].Date.Year == year):
                return count
            count += 1
        return -1
    def GetCurrentViewMonth(self,month,year):
        index = self.GetMonthIndex(month,year)
        temp = []
        for i in range(index,index + 6):
            temp.append(self.CalendarDateList[i])
        return temp
    def CreateCalendar(year):
        import calendar
        import DataClasses
        calendar.setfirstweekday(calendar.SUNDAY)
        fullCalendarList = []
        for month in range(1,13):
            cal = calendar.monthcalendar(year,month)
            for row in range(0,len(cal)):
                for col in range(0,len(cal[0])):
                    cal[row][col] = DataClasses.Day(DataClasses.Date(month,cal[row][col],year))
            for i in cal:
                fullCalendarList.append(i)
        return fullCalendarList
    def Clean(self):
        # ToDo remove calendar date from old years
        pass
