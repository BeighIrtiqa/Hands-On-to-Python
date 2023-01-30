# WAP to check if a number exists in a list or not

n = int(input('Enter length of list: '))
test_list = []
print('Enter LIST elements:')
for i in range(n):
    test_list.append(int(input()))

num = int(input('Enter element which you want to find:  '))
print("Given List is:  ", test_list)

# Checking if number exists in list
for i in test_list:
    if i == num:
        print("Element Exists")
        break
else:
    print("Element does not exist")
