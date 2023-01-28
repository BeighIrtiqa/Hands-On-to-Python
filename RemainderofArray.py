# (a * b) mod n = ((a mod n) * (b mod n)) mod n.
# Find remainder of array multiplication divided by n

m = int(input('Enter the length of array: '))
arr = []
for i in range(m):
    arr.append(int(input(f'Enter element {i + 1}:  ')))

n = int(input('Enter the number to divide with: '))
mul = 1
for i in range(m):
    mul = (mul * (arr[i] % n)) % n
print(mul % n)
