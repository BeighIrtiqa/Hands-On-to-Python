# WAP to demonstrate the set operations in Sets

x = int(input('Enter number of elements in set 1:  '))
y = int(input('Enter number of elements in set 2:  '))
s1 = set()
s2 = set()

print('Enter set 1 ')
for i in range(x):
    temp = int(input(f'Enter element {i+1}:   '))
    s1.add(temp)

print('Enter set 2 ')
for i in range(y):
    temp = int(input(f'Enter element {i+1}:   '))
    s2.add(temp)

print(s1)
print(s2)

# Operations
print("1 for Union \t 2 for Intersection \t 3 for Difference \t 4 for Symmetric Difference")
o = int(input('Enter the operation to be performed:  '))
if o == 1:
    print(f'Union of {s1} and {s2} is   {s1 | s2}')
elif o == 2:
    print(f'Intersection of {s1} and {s2} is   {s1 & s2}')
elif o == 3:
    print(f'Difference between {s1} and {s2} is   {s1 - s2}')
elif o == 4:
    print(f'Symmetric Difference between {s1} and {s2} is   {s1 ^ s2}')
else:
    print('Invalid choice')