# WAP to sort the string in Alphabetic Order

str = input('Enter any string:  ')
# str = 'Harry Potter and Goblet of Fire'
word = str.split()
print(word)

for i in range(len(word)):
    word[i] = word[i].lower()

# print(word)
word.sort()
print(word)
