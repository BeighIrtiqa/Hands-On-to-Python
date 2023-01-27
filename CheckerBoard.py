# WAP to crete a check board

import numpy as np


def printCheckBoard(n):
    print('CheckBoard Pattern :')
    # create an n x n matrix
    x = np.zeros((n, n), dtype=int)
    #print(x)

    # pattern using list slicing
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1

    # print the pattern
    for i in range(n):
        for j in range(n):
            print(x[i][j], end=" ")
        print()


num = int(input('Enter the dimensions of check board:  '))
printCheckBoard(num)
