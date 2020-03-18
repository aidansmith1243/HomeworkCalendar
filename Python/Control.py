import Calendar
class Control:
    def __init__(self):
        self.Calendar = Calendar.Calendar()

index = x.GetMonthIndex(13,2020)
print(index)
for i in range(index,index +6):
    for j in x.CalendarDateList[i]:
        print(j.Date.Day,end=', ')
    print('')
