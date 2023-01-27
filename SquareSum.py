# WAP to find sum of square of first n natural numbers

def squareness(n):
    return n * (n + 1) * (2 * n + 1) // 6


# Driven Program
num = int(input('Enter any number: '))
print(squareness(num))
