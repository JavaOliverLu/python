from PIL import Image
import cv2

path = 'output.txt'
f = open(path, 'w')

img = cv2.imread('2.png')
h,w,c= img.shape

im = Image.open('2.png')
pixels = list(im.getdata())
distance = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]

for flg in range(h*w):
  if((flg+1)%w==0):
    f.write(str('\n'))
  f.write(str(pixels[flg])+" ")
 
f.close()
