# WAP to find the factorial of any number using recursion

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


num = int(input('Enter any number:  '))
if num == 0:
    print('Factorial of 0 is undefined')
elif num < 0:
    print('Enter a positive integer')
else:
    print(f'Factorial of {num} is {fact(num)}')


