# WAP to calculate compound interest annually is given by:
# A = P(1 + R/100) t
# Compound Interest = Amount – Principal  Where,
# A is amount
# P is the principal amount
# R is the rate and
# T is the time span


def CompoundInterest(p, r, t):
    a = p * (pow((1 + r / 100), t))
    ci = a - p
    return ci


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
print(f'The Compound Interest will be  {CompoundInterest(principal, rate, time)}')
