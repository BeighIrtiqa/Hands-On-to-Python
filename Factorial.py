# WAP to find the factorial of a given number
# 5! = 5 x 4 x 3 x 2 x 1 =120

num = int(input('Enter any Number:   '))
fact = 1

if num < 0:
    print('Factorial of negative numbers does not exist')
elif num == 0:
    print('Factorial of 0 is 1')
elif num == 1:
    print('Factorial of 1 is 1')
else:
    for i in range(1, num+1):
        fact = fact * i
    print(f'Factorial of {num} is {fact}')
