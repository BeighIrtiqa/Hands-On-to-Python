# WAP to find the factorial of a number using recursion

def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)


numb = int(input('Enter any number:   '))
if numb < 0:
    print('Invalid argument')
result = factorial(numb)
print(f'The factorial of {numb} is {result}')
