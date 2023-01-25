# WAP to display a calendar of any month in any year
import calendar

year = int(input('Enter any year:   '))
month = int(input('Enter any month:  '))

calender = calendar.month(year, month)
print(calender)

