# WAP to find the string greater than a given length
sentence = input('Enter any string:')
length = int(input('Enter any length: '))
print([word for word in sentence.split() if len(word) > length])
