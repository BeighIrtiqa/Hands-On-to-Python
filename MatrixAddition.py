# Program to add two matrices using list comprehension

# Ask user for number of rows and columns
num_rows = int(input('Enter the number of rows: '))
num_columns = int(input('Enter the number of columns: '))


# Initialize empty matrices X and Y
X = [[0 for j in range(num_columns)] for i in range(num_rows)]
Y = [[0 for j in range(num_columns)] for i in range(num_rows)]


# Populate matrix X with user-defined values
print(f'Enter the values in a {num_rows} x {num_columns} dimensional matrix X:  ')
for i in range(num_rows):
    for j in range(num_columns):
        X[i][j] = int(input(f'Enter value for X[{i}][{j}]: '))


# Print Matrix X
print('MATRIX X: ')
for x in X:
    print(x)


# Populate matrix Y with user-defined values
print(f'Enter the values in a {num_rows} x {num_columns} dimensional matrix Y:  ')
for i in range(num_rows):
    for j in range(num_columns):
        Y[i][j] = int(input(f'Enter value for Y[{i}][{j}]: '))


# Print Matrix Y
print('MATRIX Y: ')
for y in Y:
    print(y)


# Perform matrix addition
result = [[X[i][j] + Y[i][j] for j in range(num_columns)] for i in range(num_rows)]


# Print the result
print(' RESULTANT MATRIX: ')
for r in result:
    print(r)
