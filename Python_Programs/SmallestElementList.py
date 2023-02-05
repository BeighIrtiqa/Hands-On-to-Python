# WAP to find the smallest element and the largest element in the list in the list

n = int(input('Enter the number of elements in a list:  '))
lst =[]
print('Enter elements: ')
for i in range(n):
    lst.append(int(input()))

print(lst)
lst.sort()
print(f'The smallest element is {lst[0]}')
print(f'The largest element is {lst[-1]}')
print(f'The second largest element is {lst[-2]}')