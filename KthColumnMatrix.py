# WAP to display the Kth column from a given matrix

m = int(input('Enter the number of rows:  '))
n = int(input('Enter the number of columns:  '))

mat = []
print(f'The matrix is of {m} x {n} dimension')

for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input(f'Enter mat[{i}] [{j}] :  ')))
    mat.append(a)

print(f'Matrix {m} x {n} = {mat}')

# retrieve kth column
k = int(input('Enter the column: '))
if k <= n:
    res = [col[k] for col in mat]
    print("The Kth column of matrix is : " + str(res))
else:
    print(f'k should be less than or equal to {n}')
