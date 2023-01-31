# WAP to check the frequency of the words in a string
from collections import Counter

s = input('Enter a string: ')
print("The original string is : " + str(s))
res = Counter(s.split())
# printing result
print("The words frequency : " + str(dict(res)))
 