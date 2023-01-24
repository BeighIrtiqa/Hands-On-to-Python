# WAP to check whether a number is an Armstrong number or not
# 153 = (1 X 1 X 1) + (5 x 5 x 5) + (3 x 3 x 3) = 153 [is an armstrong number]

# count digits
def digits(n):
    c = 0
    while n:
        c = c + 1
        n = n // 10
    return c


# Check for armstrong
def armstrong(n, c):
    total = 0
    while n > 0:
        digit = n % 10
        power = digit ** c
        total = total + power
        n = n // 10
    return total


# input from user
num = int(input('Enter the number for check:   '))
temp = num
count = digits(temp)
ans = armstrong(temp, count)

if num == ans:
    print(f'{num} is an Armstrong number !!!')
else:
    print(f'{num} is not an Armstrong number :(')
