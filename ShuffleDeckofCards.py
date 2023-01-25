# WAP to shuffle a Deck of Cards distributed among 5 people

import random
import itertools

deck = list(itertools.product(range(1, 14), ["Spade", "Diamonds", "Club", "Hearts"]))
print("Original Deck of Cards")
print(deck)
random.shuffle(deck)
print("\nShuffled Deck of Cards")
print(deck)

for i in range(5):
    print(f' Person {i+1} => {deck[i][0]} of {deck[i][1]}')
