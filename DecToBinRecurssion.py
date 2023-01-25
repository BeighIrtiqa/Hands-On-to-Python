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


'''
Here is how it works:

At the first call, the input decimal number is 15, so n % 2 is 1 and n // 2 is 7.
The function then recursively calls itself with the argument n // 2 (7), and the result of the modulo operation (1) is appended to the binary_num variable.
The second recursive call is made with the argument n // 2 (3), and the result of the modulo operation (1) is again appended to the binary_num variable.
Similarly, the recursive call is made with the argument n // 2 (1), and the result of the modulo operation (1) is again appended to the binary_num variable.
The final recursive call is made with the argument n // 2 (0), and the function returns the final binary representation of the decimal number in reverse order (i.e. binary_num)
The final binary representation is obtained by concatenating the results of the recursive calls and the modulo operation. The + sign is used for concatenation.
'''