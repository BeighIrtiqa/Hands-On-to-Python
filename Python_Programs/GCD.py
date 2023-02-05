# WAP to find the Greatest Common Divisor of any two numbers


def calcGCD(x, y):
    gcd = 0
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


num1 = int(input('Enter first number:  '))
num2 = int(input('Enter second number:  '))
res = calcGCD(num1, num2)

# test cases
if num1 == 0 and num2 == 0:
    print('''The GCD of 0 and 0 is undefined. Because in mathematics, 
0 and 0 are not considered as a valid input for GCD.
GCD can be calculated between two or more positive integers.''')
elif (num1 == 0 and num2 == 1) or (num1 == 1 or num2 == 0) or (num1 == 1 and num2 == 1):
    print(f'The GCD of {num1} and {num2} is 1')
else:
    print(f'The GCD of {num1} and {num2} is {res}')
