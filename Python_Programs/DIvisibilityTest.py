# WAP too check if the certain numbers are divisible by any given number

num = int(input('Divisibility for :  '))
limit = int(input('How many numbers do you want to check for:  '))
lst = []
print(f'Enter {limit} random numbers')
for i in range(limit):
    r = int(input())
    lst.append(r)
print('The given number are:  ')
print(lst)

result = set(filter(lambda x: x % num == 0, lst))

print(f'The numbers divisible by {num} are {result}')

