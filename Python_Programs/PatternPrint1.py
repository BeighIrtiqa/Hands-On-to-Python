# WAP TO PRINT A PATTERN
# Input : 41325 Output : |**** |* |*** |** |*****

num = input('Enter any number for pattern : ')

for i in num:
    print("|", end="")
    print("*" * int(i))

