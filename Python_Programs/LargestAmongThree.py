# WAP to find the greatest number among three numbers

x = int(input('Enter the first number:   '))
y = int(input('Enter the second number:   '))
z = int(input('Enter the third number:   '))

print(f'{x}, {y}, {z} are three numbers for comparison')

if x > y and x > z :
    print(f'{x} is greatest !!!')
elif y > x and y > z:
    print(f'{y} is greatest !!!')
else:
    print(f'{z} is greatest !!!')
