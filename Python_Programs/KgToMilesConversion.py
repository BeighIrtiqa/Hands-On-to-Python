# 1 km = 0.621371 miles
# 1 mile = 1.60934 km

print('What do you want to convert')
print('''KM - to convert kilometer to miles
MK- to convert miles to kilometers''')

choice = input('Enter your choice:    ')
if choice == 'km':
    x = float(input('Enter the number of kilometers:   '))
    miles = x * 0.621371
    print(f'{x} km = {miles} miles')
elif choice == 'mk':
    x = float(input('Enter the number of miles:  '))
    kilometer = x * 1.60934
    print(f'{x} miles = {kilometer} kilometers')
else:
    print('Invalid input')

