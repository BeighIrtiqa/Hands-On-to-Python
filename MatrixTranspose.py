# WAP to transpose a matrix

# input dimensions of matrix => rows x columns
rows = int(input('Enter number of rows:  '))
cols = int(input('enter number of columns: '))

# initialize the matrix to 0's
A = [[0 for j in range(cols)] for i in range(rows)]

# input the values in the matrix from user
for i in range(rows):
    for j in range(cols):
        A[i][j] = int(input(f'Enter value in A[{i}][{j}] =  '))

# Print the input matrix A
print('INPUT MATRIX: ')
for a in A:
    print(a)

# transpose of a matrix
T = [[0 for j in range(rows)] for i in range(cols)]
for i in range(cols):
    for j in range(rows):
        T[i][j] = A[j][i]

print('TRANSPOSED MATRIX: ')
for t in T:
    print(t)

