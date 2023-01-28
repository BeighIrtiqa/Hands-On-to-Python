# WAP to swap first element of an array with the last element of the array

def swap(arr, num):
    if num == 1:
        return arr
    else:
        temp = arr[0]
        arr[0] = arr[num-1]
        arr[num-1] = temp
        return arr


n = int(input('Enter the length of the array: '))
a = []
print('Enter array elements below: ')
for i in range(n):
    a.append(int(input()))

print(f'Original array is: {a}')
print(f'The swapped array is : {swap(a, n)}')
