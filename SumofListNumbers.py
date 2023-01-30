# WAP to find the sum of the digits of a number [12 = 1+2 = 3] in a list

#lst = [12, 67, 98, 34]
n = int(input('Enter length of list: '))
lst = []
print('Enter LIST elements:')
for i in range(n):
    lst.append(int(input()))

print(f'Input List : {lst}')
res = []
for i in lst:
    s = 0
    for j in str(i):
        s += int(j)
    res.append(s)

print(f'Summed List : {res}')
