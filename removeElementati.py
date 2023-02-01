# WAP to remove element at ith position

string = input('Enter any string: ')
i = int(input('Enter the index : '))

a = string[:i]
b = string[i+1:]
print(a+b)
