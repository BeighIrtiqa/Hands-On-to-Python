# WAP to merge two dictionaries

choice = int(input('Enter your choice:  '))
print("press 1 for solution 1 \n press 2 for solution 2 \n press 3 for solution 3")
records = int(input('Enter number of records in dictionary 1:  '))

print('Enter Dictionary 1:')
d1 = {}
for i in range(records):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d1[key] = value

records = int(input('Enter number of records in dictionary 2:  '))

print('Enter Dictionary 2:')
d2 = {}
for i in range(records):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d2[key] = value

print(d1)
print(d2)

if choice == 1:
    # using UNION operator
    print(d1 | d2)
elif choice == 2:
    # Using ** operator
    print(**d1, **d2)
elif choice == 3:
    # using a third dictionary
    d3 = d2.copy()
    d3.update(d1)
    print(d3)
else:
    print('Invalid choice')


