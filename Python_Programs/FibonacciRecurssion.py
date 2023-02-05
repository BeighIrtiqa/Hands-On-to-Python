# WAP to write a recursive function to print the Fibonacci series

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


num = int(input('Enter the number of terms to be displayed:   '))

if num <= 0:
    print('Enter any positive Integer')
else:
    print('The fibonacci Series is: ')
    for i in range(num):
        res = fibo(i)
        print(res,  end="\t")
