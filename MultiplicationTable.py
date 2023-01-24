# WAP to write a multiplication table
# 2 x 1 = 2

number = int(input('TABLE OF ??  :->   '))
limit = int(input('Enter the limit of the table:  '))
print(f'  TABLE OF {number}')


for i in range(1, limit + 1):
    print(f'{number} x {i}  =  {number * i}')
