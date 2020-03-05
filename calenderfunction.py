# Make a calender for the year

import calendar
b=int(input("Enter the year :"))
for i in range(1,13):
    print(calendar.month(b,i))
