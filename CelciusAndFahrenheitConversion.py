# WAP to convert Celcius to Fahreheit and vice versa
# F = C x 9/5 + 32
# C = 5/9 ( F - 32 )

print('To convert from F to C -> Press 0')
print('To convert from C to F -> Press 1')

ch = int(input('Enter Your Choice:    '))

if ch == 0:
    f = float(input('Enter the temperature in Fahrenheit:   '))
    c = (5/9) * (f - 32)
    print(f'{f} F = {c} C')
elif ch == 1:
    c = float(input('Enter the temperature in Celsius:   '))
    f = (c * (9/5)) + 32
    print(f'{c} C = {f} F')
else:
    print(f'{ch} is an Invalid Argument')
