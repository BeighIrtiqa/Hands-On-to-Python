import numpy as np


def rotate_left(arr, k):
    return np.roll(arr, -k)


a = []
x = int(input('Enter the length of an array:  '))
print(f'Enter {x} array elements of your choice:   ')
for i in range(x):
    a.append(int(input(f'Enter {i + 1} element: ')))

t = int(input('Enter the number of times you want to rotate the array:  '))

print(a)
print(rotate_left(a, t))
# [3, 4, 5, 1, 2]
