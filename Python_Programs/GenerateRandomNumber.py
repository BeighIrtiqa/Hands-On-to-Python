#to generate random numbers
import random

print('''1 - Random Integer
2 - Random Float
3 - Random word''')

choice = int(input('Enter your choice:    '))
if choice == 1:
    start = int(input ('Enter starting number :  '))
    end = int(input('Enter your limit:  '))
    print(random.randint(start, end))
elif choice == 2:
    start = float(input('Enter starting number:   '))
    end = float(input('Enter your limit:  '))
    print(random.uniform(start, end))
elif choice == 3:
    colors = ['red' 'blue', 'black', 'yellow', 'green', 'pink', 'cyan', 'white', 'grey']
    print(colors)
    print(random.choice(colors))
else:
    print('You have entered an Invalid Choice')
