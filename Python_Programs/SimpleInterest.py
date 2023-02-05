# WAP to calculate simple interest
# Simple interest formula is given by:
# Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate

p = int(input('Enter your principal amount: '))
t = int(input('enter the time:  '))
r = int(input('Enter the rate: '))

si = (p * t * r)/100
print(f'The Simple Interest on given input will be:  {si}')