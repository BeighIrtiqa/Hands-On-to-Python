# WAP to compute matrix multiplication

print('Give dimensions for Matrix 1')
rMat1 = int(input('Enter number of rows in Matrix 1:  '))
cMat1 = int(input('Enter number of columns in Matrix 1:  '))
print('Give dimensions for Matrix 2')
rMat2 = int(input('Enter number of rows in Matrix 2:  '))
cMat2 = int(input('Enter number of columns in Matrix 2:  '))

# checking "Compatibility condition"
if cMat1 != rMat2:
    print('Matrix multiplication is not possible')
    print('if Matrix1 is of m x n , the matrix 2 should be of n x p. so that, Resultant matrix could be m x p')
else:
    # inputting the values for MATRIX 1:
    A = [[0 for j in range(cMat1)] for i in range(rMat1)]
    print('Enter values for MATRIX 1:  ')
    for i in range(rMat1):
        for j in range(cMat1):
            A[i][j] = int(input(f'Enter value in A[{i}][{j}] =  '))

    # inputting the values for MATRIX 2:
    B = [[0 for j in range(cMat2)] for i in range(rMat2)]
    print('Enter values for MATRIX 2:  ')
    for i in range(rMat2):
        for j in range(cMat2):
            B[i][j] = int(input(f'Enter value of B[{i}][{j}]:   '))

    # Printing the input matrices A and B
    print('INPUT MATRIX 1 :  ')
    for a in A:
        print(a)
    print('INPUT MATRIX 2 :  ')
    for b in B:
        print(b)

    R = [[0 for j in range(cMat2)] for i in range(rMat1)]
    # Matrix multiplication
    for i in range(rMat1):
        for j in range(cMat2):
            for k in range(rMat2):
                R[i][j] = A[i][k] + B[k][j]
    print('Resultant Matrix: ')
    for r in R:
        print(r)