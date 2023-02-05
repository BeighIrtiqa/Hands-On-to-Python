# WAP to swap any two elements in a list

# Swap function
def swapPositions(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst


# Driver function
l = int(input('Enter the length of list: '))
List = []
print(f'Enter {l} elements: ')
for i in range(l):
    List.append(int(input()))

p1 = int(input('Enter the first position to be swapped:  '))
p2 = int(input('Enter the second position to be swapped:  '))
print(f'Original list is {List}')
print(f'The swapped list is : {swapPositions(List, p1, p2)}')
