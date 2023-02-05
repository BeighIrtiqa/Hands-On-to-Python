# WAP to calculate the roots of a Quadratic Equation of the form ax^2 + bx +c = 0
# a, b, c are Real numbers
# a!=0

import cmath
a = int(input('Enter any number (a):   '))
b = int(input('Enter any number (b):  '))
c = int(input('Enter any number (c):  '))
if a == 0:
    print('Invalid input')
    print('a cannot be equal to 0 according to rules')
    a = int(input('Please enter non- zero value of a:  '))
    print('')
print(f'The given Quadratic Equation is {a}x^2 + {b}x + {c} = 0')
print('')
# formula for finding discriminant
# d = b^2 -4ac
d = (b ** 2) - (4 * a * c)

# we will get 2 root (1 positive root and 1 negative root)
root1 = (-b - cmath.sqrt(d)) / (2*a)
root2 = (-b + cmath.sqrt(d)) / (2*a)

print(f' Root 1 = {root1}')
print(f' Root 2 = {root2}')


