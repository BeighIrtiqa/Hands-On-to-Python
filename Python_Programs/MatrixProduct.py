# WAP to perform matrix product - get the product of all the elements present in the matrix
from itertools import chain


def prod(val):
    mult = 1
    for i in val:
        mult *= i
    return mult


lst = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
print(f'The original list is : {lst}')
res = prod(list(chain(*lst)))  # [1, 4, 5, 7, 3, 4, 46, 7, 3] - flatten
print(f'The total element product of lists is {res}')


'''
chain function in the itertools module takes a number of iterables as arguments
and returns a single iterable that produces the elements of each argument in sequence.
chain(*test_list) is used to flatten a nested list into a single iterable.
The prod function then takes the iterable produced by chain and calculates the product of all the elements in the list.
'''