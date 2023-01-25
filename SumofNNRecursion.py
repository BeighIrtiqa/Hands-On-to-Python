# WAP to find the sum of 'n' Natural numbers using Recursion

def NaturalSum(n):
    if n <= 1:
        return n
    else:
        return n + NaturalSum(n-1)


terms = int(input('Enter the number of terms:  '))
if terms <= 0:
    print('Enter any positive integer')
else:
    print(f'Sum of first {terms} terms = {NaturalSum(terms)}')
