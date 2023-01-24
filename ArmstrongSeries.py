# WAP to find the All the Armstrong numbers between the given series

begin = int(input('Enter the start of series:  '))
limit = int(input('Enter the limit of series:  '))
print(f'THE ARMSTRONG SERIES BETWEEN THE RANGE {begin} AND {limit} IS: ')
for num in range(begin, limit + 1):
    total = 0
    temp = num
    count = len(str(temp))
    while temp > 0:
        digit = temp % 10
        power = digit ** count
        total += power
        temp //= 10
    if num == total:
        print(num, end='\t')

