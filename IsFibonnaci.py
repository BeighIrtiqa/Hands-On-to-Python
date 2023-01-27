# WAP to check if a given number is a fibonnaci number or not
# A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square


import math


def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
    else:
        check1 = 5 * n * n + 4
        check2 = 5 * n * n - 4
        return math.isqrt(check1) ** 2 == check1 or math.isqrt(check2) ** 2 == check2


# test the function
num = int(input('Enter any integer for check:   '))
if num < 0:
    print('Please enter any positive integer')
else:
    b = is_fibonacci(num)
    if b:
        print(f'{num} is a fibonnaci number')
    else:
        print(f'{num} is not a fibonnaci number')
