# WAP to check of the number is a perfect number or not
# A number is a perfect number if is equal to sum of its proper divisors,
# that is, sum of its positive divisors excluding the number itself


def is_perfect_number(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        return True
    else:
        return False


# 6, 8128, 28, 496 are some examples of perfect numbers
n = int(input('Enter any number for check:  '))
b = is_perfect_number(n)
if b:
    print(f'{n} is a perfect number')
else:
    print(f'{n} is not a perfect number')

