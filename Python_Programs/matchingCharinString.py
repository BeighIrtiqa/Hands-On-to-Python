# WAP to count the number of matching characters in a pair of two string


def count_matching_characters(s1, s2):
    count = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            count += 1
    return count


st1 = input('Enter string 1:  ')
st2 = input('Enter string 2:  ')
print("Number of Matching characters: ", count_matching_characters(st1, st2))
# print(result) # Output: 2


'''
The min function is used to determine the length of the shorter string, 
which is then used as the range for the for loop. 
This ensures that the loop only iterates as many times as there are characters in the shorter string.
If the loop were to iterate based on the length of the longer string,
it would result in an IndexError when trying to access characters in the shorter string that don't exist.
'''