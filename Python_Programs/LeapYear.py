# Python program to check if year is a leap year or not
# Criteria:
#           if the year is a century year (means ending with 00 )  (divide by 100)
#           century year is divided by 400 is a leap year
#           but if the year is not a century year
#           then check by division of 4

x = input("Enter a year : ")
count = 0
for i in x:
    count += 1

if count == 4:
    year = int(x)
    if (year % 400 == 0) and (year % 100 == 0):
        print(f'{year} is a leap year !!!')

    elif (year % 4 == 0) and (year % 100 != 0):
        print(f'{year} is a leap year !!!')

    else:
        print(f'{year} is not a leap year  :(')
else:
    print('Please Enter The Year in YYYY Format')
