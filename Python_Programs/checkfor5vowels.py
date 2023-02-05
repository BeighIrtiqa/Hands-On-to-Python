# WAP to check if the string contains atleast 5 vowels or not
def check_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
        if count >= 5:
            return True
    return False


test_string = input('Enter a random string to check:  ')
print(f'Contains >= 5 vowels : {check_vowels(test_string)}')

