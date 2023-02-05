# WAP to remove punctuations from a string

str = input('Enter any string:  ')

# use a list comprehension to filter out non-alphabetic characters
no_pun = ''.join([c for c in str if c.isalpha() or c.isspace()])
print(no_pun)

'''
This program uses a list comprehension to iterate over each character in the input string,
and only keeps the characters that are alphabetic or whitespaces. 
The isalpha() method returns True if the character is an alphabetic character and False otherwise. 
The join() method is used to join the remaining characters into a single string.
'''

