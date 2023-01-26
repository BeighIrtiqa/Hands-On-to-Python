# WAP to find the resolution of any image
import PIL
from PIL import Image

img = PIL.Image.open(r'C:\Users\IRTIQA\Desktop\EfficientNet\mildew.jpg')
# img.show()

width, height = img.size

print(f'Dimensions of a given image are : {width} x {height} ')