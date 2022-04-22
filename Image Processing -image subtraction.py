from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


im = Image.open('1.JPG')
width = im.size[0]
height = im.size[1]

im2 = Image.open('2.JPG')
width2 = im2.size[0]
height2 = im2.size[1]

im3 = Image.open('3.jpg')

im = im.convert('RGB')
im2 = im2.convert('RGB')



for x in range(width):
    for y in range(height):
        r, g, b = im.getpixel((x,y))
        r2, g2, b2 = im2.getpixel((x,y))
        im3.putpixel((x,y),(0,0,b-b2))

im3.save("temp.jpg")
im3.show()
         


