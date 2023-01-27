# WAP to find the area of shapes

def Circle(r):
    PI = 3.14
    return PI * (r ** 2)


def Triangle(b, h):
    return 0.5 * b * h


def Square(s):
    return s ** 2


def Rectangle(lngt, w):
    return lngt * w


print("Press c for circle \n Press t for Triangle \n Press s for square \n Press r for rectangle")

choice = input('ENTER YOUR CHOICE:  ')

if choice == "c":
    radius = float(input('Enter the radius of circle:     '))
    print(f'The area of circle with radius {radius} = {Circle(radius)}')
elif choice == "t":
    base = float(input('Enter the base of triangle: '))
    height = float(input('Enter the height of triangle: '))
    print(f'The are of Triangle where base is {base} and height is {height} = {Triangle(base, height)}')
elif choice == "s":
    side = float(input('Enter the side:  '))
    print(f'The area of square with side {side} = {Square(side)}')
elif choice == "r":
    length = float(input('Enter length of rectangle:   '))
    width = float(input('Enter width of rectangle:  '))
    print(f'The area of rectangle with length {length} and width {width} = {Rectangle(length, width)}')
else:
    print('Invalid Choice')
