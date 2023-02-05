# WAP to check if an array is monotonic or not
# an array is said to be monotonic if it is either increasing or decreasing
# Array with elements <= 2 are always monotonic

def isMonotonic(A):
    if len(A) <= 2:
        return True
    else:
        difference = A[1] - A[0]
        for i in range(2, len(A)):
            if difference == 0:
                difference = A[i] - A[i - 1]
                continue
            elif (difference > 0 and A[i] >= A[i - 1]) or (difference < 0 and A[i] <= A[i - 1]):
                continue
            else:
                return False
        return True
#a = [6, 5, 4, 4]
#a = [3, 4, 4, 5, 10]
#a = [5, 15, 20, 10]
l = int(input('ENter length of the list:   '))
a = []
for i in range(l):
    a.append(int(input(f'Element {i+1}:  ')))
print(a)

print(f'Is the given list monotonic ? {isMonotonic(a)}')