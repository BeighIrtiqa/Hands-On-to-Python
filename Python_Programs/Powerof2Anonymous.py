# WAP to find the power of 2 using lambda function
print('POWER OF 2')
num = int(input('Enter the number of terms:    '))
result = list(map(lambda x: 2 ** x, range(num + 1)))

for i in range(num + 1):
    print(f'The power of {i} is {result[i]}')
