# WAP to make a calculator for 4 principal operations

print("Press 1 for Addition \n Press 2 for Subtraction \n Press 3 for Multiplication \n Press 4 for Division")
x = int(input('Enter number 1:  '))
y = int(input('Enter number 2:   '))
ch = int(input('Enter your choice from (1 - 4):   '))

if ch == 1:
    print(f' {x} + {y} = {x + y}')
elif ch == 2:
    print(f' {x} - {y} = {x - y}')
elif ch == 3:
    print(f' {x} * {y} = {x * y}')
elif ch == 4:
    print(f' {x} / {y} = {x / y}')
else:
    print("Invalid key pressed.....")
