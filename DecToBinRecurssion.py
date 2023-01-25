# WAP to convert Decimal number in its Binary equivalent

def DecToBin(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        binary_num = ''
        binary_num += str(n % 2)
        return DecToBin(n // 2) + binary_num


num = int(input('Enter any number:  '))
print(DecToBin(num))

