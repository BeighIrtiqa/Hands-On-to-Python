# WAP to find the sum of digits of a number

num = int(input('Enter any number:   '))
temp = num
Sum = 0
if num < 0:
    print('Please enter a positive integer :(')
elif num == 0:
    print(f'Sum of {num} = {Sum}')
else:
    while num >= 0:
        Sum += num
        num -= 1
    print(f'Sum of digits of {temp} = {Sum}')
