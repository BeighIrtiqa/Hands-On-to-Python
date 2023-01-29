# WAP to print the even numbers and the odd numbers in the list

n = int(input('Enter the length of list:  '))
lst = []
even = []
odd = []
for i in range(n):
    lst.append(int(input()))

print(lst)
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

choice = int(input("Press 1 for Even numbers \t Press 0 for odd numbers : "))
if choice == 1:
    print(even)
elif choice == 0:
    print(odd)
else:
    print('Invalid choice ')