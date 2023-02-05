# WAP to check the occurrence of a number in the given list

n = int(input('Enter the number of elements in list:'))
lst = []
print('Enter list elements: ')
for i in range(n):
    lst.append(int(input()))

num = int(input('Enter the number to check for : '))

if num in lst:
    occur = lst.count(num)
    print(f'"{num}" occurs {occur} times in the list')
else:
    print(f'"{num}" is not present in the list')
