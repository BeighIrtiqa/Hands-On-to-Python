# Swap two numbers

a = int(input('Enter any number :   '))
b = int(input('Enter another number:  '))

print(f'BEFORE SWAP :->  Value of a = {a} and value of b = {b} ')
choice = input('''Enter Your choice ->
                    1.for using third variable write true 
                    2.without using third variable (False)''')
choice = True if choice.lower() == 'true' else False

if choice:
    print('METHOD 1 - using third variable')
    temp = a
    a = b
    b = temp
else:
    print('METHOD 2 - without using third variable')
    a, b = b, a
print(f'AFTER SWAP :->  Value of a = {a} and value of b = {b} ')

