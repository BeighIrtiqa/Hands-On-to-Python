# WAP TO REMOVE DUPLICATES FROM A STRING


def remove_duplicates(s):
    return "".join(sorted(set(s), key=s.index))


s = input('Enter a string:  ')
result = remove_duplicates(s)
print(result)

