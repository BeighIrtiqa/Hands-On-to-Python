# WAP to check whether a string is symmetrical (A string is said to be symmetrical if both the halves of the string are the same ) and palindrome

def palindrome(str):
    mid = (len(str) - 1) //2
    start = 0
    last = len(str) - 1
    flag = 0

    while start < mid:
        if str[start] == str[last]:
            start += 1
            last -= 1
        else:
            flag = 1
            break

    if flag == 0:
        print('String is palindrome')
    else:
        print('String is not palindrome')


def symmetrical(str):
    flag = 0
    if len(str) % 2:
        mid = len(str) // 2 + 1
    else:
        mid = len(str) // 2

    start1 = 0
    start2 = mid

    while (start1 < mid) and (start2 < len(str)):
        if str[start1] == str[start2]:
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break

    if flag == 0:
        print("String is symmetrical")
    else:
        print("String is not symmetrical")


#st = 'amaama'
st = 'khokho'
palindrome(st)
symmetrical(st)
