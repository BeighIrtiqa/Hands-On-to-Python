# WAP to find the n largest elements in the list

def largest_n_elements(arr, N):
    if N == 0:
        return 0
    arr.sort(reverse=True)
    return arr[:N]


n = int(input('Enter the length of list:  '))
lst = []
for i in range(n):
    lst.append(int(input()))

max = int(input('How many largest elements do you want to display:  '))

print(f'Input List is {lst}')
print(f'The {max} largest elements present in the list are {largest_n_elements(lst, max)}')
