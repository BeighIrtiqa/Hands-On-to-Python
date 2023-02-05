# lst = [10, 20, 30, 40, 50]
n = int(input('Enter the number of elements in list:'))
lst = []
print('Enter list elements: ')
for i in range(n):
    lst.append(int(input()))

cum_list = []
j = 0
for i in range(0, len(lst)):
    j += lst[i]
    cum_list.append(j)

print(cum_list)

