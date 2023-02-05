# WAP to find the indexes of list elements

# Solution 1 - using Enumerate method
l = [11, 22, 33, 44, 55, 66, 77, 88, 99]
print(l)
for index, value in enumerate(l, start=1):
    print(index, "->", value)


# Solution 2 -
# Using for loop

for i in range(len(l)):
    value = l[i]
    print(i, "->", value)

