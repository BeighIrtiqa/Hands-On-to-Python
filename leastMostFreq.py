# WAP to find the least and the most frequent character in a string

def frequent_chars(s):
    char_freq = {}
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    choice = int(input('Enter 0 for least freq and 1 for most freq: '))
    if choice == 0:
        least_freq(char_freq)
    elif choice == 1:
        most_freq(char_freq)


def least_freq(char_freq):
    min_freq = min(char_freq.values())
    least_freq_chars = [char for char, freq in char_freq.items() if freq == min_freq]
    print("Least Frequent characters = ", least_freq_chars)


def most_freq(char_freq):
    max_freq = max(char_freq.values())
    most_freq_chars = [char for char, freq in char_freq.items() if freq == max_freq]
    print("Most Frequent characters = ", most_freq_chars)


str = "hello"
frequent_chars(str)
