# WAP to print the positive numbers and the negative numbers in the list

n = int(input('Enter the length of list:  '))
lst = []
pos = []
neg = []
for i in range(n):
    lst.append(int(input()))

print(f'The given list of numbers is {lst}')
for i in lst:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)

print(f'{pos} are the positive numbers in the given list')
print(f'{neg} are the negative numbers in the given list')
