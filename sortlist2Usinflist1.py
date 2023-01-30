# WAP to sort one list using the other list


def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)
    z = [i for _, i in sorted(zipped_pairs)]
    return z


'''
It generates a new list where only the second element (the value from list1)
of each sorted pair is taken from sorted(zipped_pairs) and stored in the resulting list z.
The first element of each pair (the value from list2) is ignored and discarded using the underscore _.
This is a common practice in Python when iterating over a list of pairs,
and only one element of the pair is needed. 
The underscore acts as a placeholder for the unused value and helps to clearly indicate that the value is not used in the code.
'''


x = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Harper']
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))

