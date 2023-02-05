# WAP to print even numbers and odd numbers within a given range


start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
e = []
o = []

if start <= 0 or end <= 0:
    print('Please Enter positive integers')
elif start > end:
    print('Start should be less than end')
else:
    # iterating each number in list
    for num in range(start, end + 1):

        # checking condition
        if num % 2 == 0:
            e.append(num)
        else:
            o.append(num)

    print("Even list: ", e)
    print("Odd List: ", o)
