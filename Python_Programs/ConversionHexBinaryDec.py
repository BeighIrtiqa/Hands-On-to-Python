# WAP to convert Decimal Number to Binary, Hexadecimal or Octal

num = int(input('Enter any number:   '))
print('''hex -> decimal to hexadecimal
bin -> decimal to binary
oct -> decimal to octal''')
ch = input('Enter your choice:   ')

if ch == 'hex':
    print(f'{num} in hexadecimal is {hex(num)}')
elif ch == 'oct':
    print(f'{num} in octal is {oct(num)}')
elif ch == 'bin':
    print(f'{num} in binary is {bin(num)}')
else:
    print('Invalid choice')
