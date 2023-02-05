# WAP TO MULTIPLY ALL THE ELEMENTS IN A LIST


n = int(input('Enter the number of elements in a list: '))
lst = []
print(f'Enter {n} elements in list: ')
for i in range(n):
    lst.append(int(input()))
result = 1
for i in range(n):
    result *= lst[i]

print(f'The given list is {lst}')
print(f'the product of elements in the list are : {result}')