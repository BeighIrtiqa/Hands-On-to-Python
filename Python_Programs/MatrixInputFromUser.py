# WAP to create a user defined matrix

m = int(input('Enter the row dimension of matrix: '))
n = int(input('Enter the column dimension of matrix: '))

print(f'The input matrices should be of {m} x {n} dimensions')

l1 = []
l2 = []

print('Enter elements in list 1: ')
for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input(f'Enter l1[{i}] [{j}] :  ')))
    l1.append(a)

print('Enter elements in list 2: ')
for i in range(m):
    a = []
    for j in range(n):
        a.append(int(input(f'Enter l2[{i}] [{j}] :  ')))
    l2.append(a)

print('List 1 :')
for i in range(m):
    for j in range(n):
        print(l1[i][j], end=" ")
    print()

print('List 2:')
for i in range(m):
    for j in range(n):
        print(l2[i][j], end=" ")
    print()

