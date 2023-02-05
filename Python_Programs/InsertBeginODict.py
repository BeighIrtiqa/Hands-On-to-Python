# WAP to insert at the beginning of the ordered dictionary
'''The move_to_end method in Python dictionaries is used to change the order of an item in a dictionary
by moving it to either the end of the dictionary (if the last argument is set to True)
or the beginning of the dictionary (if the last argument is set to False).
The item is specified by its key and the order of the other items in the dictionary remains unchanged.'''

from collections import OrderedDict

Salary = OrderedDict([('Alice', 1000), ('Bob', 2000), ('Ben', 3000)])
Salary.update({'Tim': 3500})
Salary.move_to_end('Tim', last=False)

print("Resultant Dictionary : " + str(Salary))
