# Check if given array is Monotonic
def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if x == A or y == A:
        return True
    return False


# Driver program
l = int(input('ENter length:  '))
a = []
print('enter array elements')
for i in range(l):
    a.append(int(input()))

# Print required result
print(isMonotonic(a))
