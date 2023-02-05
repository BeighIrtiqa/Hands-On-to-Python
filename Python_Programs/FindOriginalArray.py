# WAP to Reconstruct the array by replacing arr[i] with (arr[i-1]+1) % M
# we will be given a modified array , where -1 indicates the modified value in the list,
# we have to generate the original value for the same and finally display the original array

#original_array = [-1, -1, 5, -1, -1, 14]
#M = 11
M = int(input("Enter value of M:  "))
l = int(input('Enter range of the array:  '))
original_array = []

for i in range(l):
    original_array.append(int(input(f'Enter element {i+1}:  ')))

print(original_array)
#logic
if original_array[0] == -1:
    for i in range(1, len(original_array)):
        if original_array[i] != -1:
            original_array[0] = original_array[i]
            break
for i in range(1, len(original_array)):
    if original_array[i] == -1:
        original_array[i] = (original_array[i-1] + 1) % M
print(original_array)

'''
the program first checks if the first element of the array is -1. 
If it is, it then runs a loop to find the first non-zero element in the array, 
and assigns it to the 0th index element.
Then it runs the previous loop to replace the remaining -1 elements 
with their corresponding values using the relationship a[i] = (a[i-1]+1) % M.
This will handle the case where the first element of the original array is -1 as well and construct the original array.
'''
