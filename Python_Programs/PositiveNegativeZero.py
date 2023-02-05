# WAP to check if the number is a Positive number , or a Negative number, or a Zero

num = int(input('Enter any number of your choice:   '))

if num > 0:
    print(f'{num} is a positive number')
elif num < 0:
    print(f'{num} is a negative number')
else:
    print(f'You have entered a {num}')
