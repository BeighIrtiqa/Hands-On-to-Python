# WAP to count the number of vowels in a string

str = input('Enter any strong:    ')
print(str)
vowels = "aeiou"
str = str.lower()
print(str)
count_dct = {}.fromkeys(vowels, 0)
print(count_dct)

for char in str:
    if char in count_dct:
        count_dct[char] += 1

print(count_dct)

'''
This code is a program that counts the number of vowels in a given string.

1.The string "Harry Potter and the Goblet of Fire" is assigned to the variable 'str'.
2.The string "aeiou" is assigned to the variable 'vowels'.
3.The string assigned to 'str' is converted to lowercase using the lower() method, so that the program can count vowels regardless of case. The lowercase version of the string is then reassigned to the 'str' variable.
4.The count dictionary is created using the fromkeys() method, with the keys being the characters in the 'vowels' string and all values being initialized to 0.
5.The for loop iterates over each character in the 'str' string.
6.The if statement checks if the character in the for loop is present in the count dictionary.
7.If the character is present in the count dictionary, its value is incremented by 1.
8. Finally, the count dictionary is printed, displaying the number of occurrences of each vowel in the input string.
'''