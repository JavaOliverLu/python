from PIL import Image
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4

tmp = Image.open('problem6.jpg')
image_hsv = tmp.convert('HSV')

tmpwidth = tmp.size[0]
tmpheight = tmp.size[1]
rarray=[]
garray=[]
barray=[]
cntfor=0
for x in range(tmpwidth):
    for y in range(tmpheight):
        rt, gt, bt = image_hsv.getpixel((x,y))
        if(rt>1):
          rarray.append(rt)
        if(gt>1):
          garray.append(gt)
        if(bt>1):
          barray.append(bt)

frer=[]
freg=[]
freb=[]
peakr=[]
z=[]
for i in range(256):
  frer.append(rarray.count(i))
  freg.append(garray.count(i))
  freb.append(barray.count(i))
  z.append(i)

plt1.plot(z,frer)
plt1.xlabel('h值')
plt1.xticks(range ( 0 , 256 , 20 ))
plt1.ylabel('次數')
plt1.title('h')

plt2.plot(z,freg)
plt2.xticks(range ( 0 , 256 , 20 ))
plt2.xlabel('s值')
plt2.ylabel('次數')
plt2.title('s')

plt3.plot(z,freb)
plt3.xticks(range ( 0 , 256 , 20 ))
plt3.xlabel('v值')
plt3.ylabel('次數')
plt3.title('v')
