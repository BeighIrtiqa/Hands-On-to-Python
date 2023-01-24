# WAP to find the factors of a given number

num = int(input('Enter the number:  '))
lst = []

if num == 0:
    print('Factor of 0 is undefined')

for i in range(1, num + 1):
    if num % i == 0:
        lst.append(i)

print(f'Factor of {num} are {lst}')
