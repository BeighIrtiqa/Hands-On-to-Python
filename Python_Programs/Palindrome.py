# WAP check whether a string is palindrome or not

str = input('Enter any word:   ')
rev = str[::-1]     #string slicing

if str == rev:
    print(f'{str} is a palindrome')
else:
    print(f'{str} is not a palindrome')