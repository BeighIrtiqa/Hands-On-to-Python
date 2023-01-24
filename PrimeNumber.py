# WAP to check whether a number is prime or not
# A prime number is a whole number greater than 1 whose only factors are 1 and itself.
# A factor is a whole number that can be divided evenly into another number.
# The first few prime numbers are 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29.
# Numbers that have more than two factors are called composite numbers.

num = int(input('Enter any number:   '))

if num == 0:
    print('0 is neither a prime nor a composite number')
elif num == 1:
    print('1 is not considered as prime')
else:
    flag = 0
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} is not a prime number !!!')
            break
    else:
        print(f'{num} is a prime number !!!')

