# WAP to write all the prime numbers between given two numbers

Lower = int(input('Enter the lower limit:  '))
Upper = int(input('Enter the upper limit:   '))
series = []
# Test Case 1
if Lower == 0 and Upper == 0:
    print('0 is neither prime nor composite')
# Test Case 2
elif Upper == 0:
    print('By the usual definition of prime for integers, number less than cannot be prime')
# Test Case 3
elif (Lower == 1 and Upper == 1) or (Lower == 0 and Upper == 1):
    print('''1 is not considered a prime number. A prime number is defined as a positive integer greater than 
1 that has no positive integer divisors other than 1 and itself
Since 1 has only one positive integer divisor (1), it is not considered prime.
    ''')
# Test Case 4
elif Lower < 0 or Upper < 0:
    print('By the usual definition of prime for integers, negative numbers cannot be prime')

else:
    for num in range(Lower, Upper+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                if Lower == 2 or Lower == 1 or Lower == 0:
                    series.append(2)
                series.append(num)
                series = list(dict.fromkeys(series))
    print(f'The Prime numbers between {Lower} and {Upper} is:')
    print(series)
