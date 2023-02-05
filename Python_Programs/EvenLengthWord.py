# WAP to print even length word in a string


n = input('ENter any string : ')
s = n.split(" ")
print(s)
for i in s:
    if len(i) % 2 == 0:
        print(i)

