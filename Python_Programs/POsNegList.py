# Python program to print positive Numbers in given range

#start, end = -4, 19
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

pos = []
neg = []
# iterating each number in list
for num in range(start, end + 1):

    # checking condition
    if num >= 0:
        pos.append(num)
    else:
        neg.append(num)

print(pos)
print(neg)
