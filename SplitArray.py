# WAP to split an array and add the first part to the end of the array


def split_and_add(arr, k):
    first_part = arr[:k]
    # print("First part: ", first_part)
    second_part = arr[k:]
    # print("Second part", second_part)
    return second_part + first_part


a = []
x = int(input('Enter the length of an array:  '))
print(f'Enter {x} array elements of your choice:   ')
for i in range(x):
    a.append(int(input(f'Enter {i + 1} element: ')))

t = int(input('Enter the number of times you want to rotate the array:  '))
print(a)
print(split_and_add(a, t))
