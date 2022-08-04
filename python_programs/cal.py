import os
import calendar  as cal
os.system('cls')

#cal month()
"""
print("the calendar for jan 2022 is : ")
print(cal.month(2022,1))
"""

#cal calendar() (year,w,l,,m)
"""
print(cal.calendar(2022,1,1,1,4))
"""

#cal calender() 2
"""
weekdayvalues=cal.Calendar(firstweekday=2)
for i in weekdayvalues.iterweekdays():
    print("the current week day is :", i)
"""

#cal calender 3
"""
inyear=int(input("please enter the required year : "))
calendarobj=cal.Calendar()
for i in calendarobj.itermonthdates(inyear,4):
    print("the current date is :",i)
"""

#cal calendar 4
"""
inyear=int(input("please enter the required year : "))
inmonth=int(input("please enter the required month : "))
inweekday=int(input("please enter the required weekday : "))
calendarobj=cal.Calendar(firstweekday=inweekday)
for i in calendarobj.itermonthdays(inyear,inmonth):
    print("the current day is :",i)
    """
    
#cal calendar 5
"""
inyear=int(input("please enter the required year : "))
inmonth=int(input("please enter the required month : "))

calendarobj=cal.Calendar()
for i in calendarobj.itermonthdays2(inyear,inmonth):
    print("the current day is :",i)
    """
    
#cal calendar() 6
"""
inyear=int(input("please enter the required year : "))
inmonth=int(input("please enter the required month : "))
calendarobj=cal.Calendar()
print(calendarobj.monthdatescalendar(inyear,inmonth))
    """
    
#cal calendar() 7
"""
inyear=int(input("please enter the required year : "))
inmonth=int(input("please enter the required month : "))
calendarobj=cal.Calendar()
for i in calendarobj.monthdays2calendar(inyear,inmonth):
    print(i)
    """
    
#cal calendar()7
"""
inyear=int(input("please enter the required year : "))
inmonth=int(input("please enter the required month : "))
calendarobj=cal.Calendar()
print(calendarobj.monthdayscalendar(inyear,inmonth))
"""

#cal calendar()8
"""
inyear=int(input("please enter the required year : "))

calendarobj=cal.Calendar()
print(calendarobj.yeardatescalendar(inyear))
"""

#cal textcalendar()
"""
htmlTextCalendar=cal.TextCalendar(firstweekday=0)
inyear=int(input("please enter the required year: "))
inmonth=int(input("please enter the required month: "))
print(htmlTextCalendar.formatmonth(inyear,inmonth))
"""

#cal isleap()
"""
inyear=int(input("please enter the required year : "))
print("leap year status : ",cal.isleap(inyear))
"""

#cal leapday()
"""
instartyear=int(input("please enter the starting year : "))
inendyear=int(input("please enter the endding year : "))
print("the total number of leap days : ",cal.leapdays(instartyear,inendyear))
"""

#cal prmonth()
"""
inyear=int(input("please enter the required year : "))
inmonth=int(input("please enter the required month : "))
print(cal.prmonth(inyear,inmonth))
"""

#cal,dt,month
#error
"""
import datetime
from calendar import monthrange

birthdate=datetime.date(2002,1,30)
ndaysinmonth=cal.monthrange(2002,1)
datesinbetween=[(birthdate+datetime.timedelta(dateindex) for dateindex in range(ndaysinmonth[1]))]
nsundays=0
for weekday in datesinbetween:
    nsundays+=int(weekday.isoweekday()==6)
print("the total sundays in the month of the given date is :",nsundays)"""