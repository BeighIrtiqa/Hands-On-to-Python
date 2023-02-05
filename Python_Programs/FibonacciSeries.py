# WAP to print the fibonacci series
# 0, 1, 1, 2, 3, 5, 8, 13....


limit = int(input('Enter the limit until you want to print the series:    '))
a = 0
b = 1
i = 0
print(a, end='\t')
print(b, end='\t')


while i <= limit:
    c = a + b
    print(c, end='\t')
    a = b
    b = c
    i = i + 1


