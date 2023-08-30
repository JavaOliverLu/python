import os
from tkinter import *
from tkinter import colorchooser, filedialog,messagebox
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from PIL import Image
import scipy
import numpy as np
import cv2
import numpy as np
import matplotlib.pyplot as plt
from detecta import detect_peaks

import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import csv
from itertools import zip_longest

#layout1
a = Tk()
a.title("使用自動化偏振光學方法預測PM2.5")
hello = Label(a, text="使用自動化偏振光學方法預測PM2.5", width="30", height="5")
hello.pack()
hello1 = Label(a, text="研究者:洪仕良 陸紹祺", width="30", height="5")
hello1.pack()
hello1 = Label(a, text="程式設計:陸紹祺", width="30", height="5")
hello1.pack()
def mfileopen():
	file1 = filedialog.askopenfile()
	label = Label(text=file1).pack()
	if file1:
		filepath1 = os.path.abspath(file1.name)
		print(filepath1)
		return filepath1
def mfileopen2():
	file2 = filedialog.askopenfile()
	label2 = Label(text=file2).pack()
	if file2:
		filepath2 = os.path.abspath(file2.name)
		return  filepath2



button = Button(text="請開啟沒有偏振的照片",width = 30,command= mfileopen).pack()
button2 = Button(text="請開啟有偏振的照片",width = 30,command= mfileopen2).pack()

#open
im = Image.open(mfileopen())
width = im.size[0]
height = im.size[1]
im.save("im.jpg")
im2 = Image.open(mfileopen2())
width2 = im2.size[0]
height2 = im2.size[1]
im3 = Image.open(mfileopen2())


#過濾第一章
img = cv2.imread("im.jpg", 1)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
white = np.array([255, 255, 255])
lowerBound = np.array([90,90,90])
mask = cv2.inRange(hsv, lowerBound, white)
res = cv2.bitwise_and(img, img, mask=mask)
cv2.imwrite("fixed1.jpg", res)


#過濾第二章

img2 = cv2.imread("im2.jpg", 1)
hsv=cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
white = np.array([255, 255, 255])
lowerBound = np.array([90,90,90])
mask = cv2.inRange(hsv, lowerBound, white)
res2 = cv2.bitwise_and(img2, img2, mask=mask)
cv2.imwrite("fixed2.jpg",res2)


im = Image.open('fixed1.jpg')
width = im.size[0]
height = im.size[1]
im2 = Image.open('fixed2.jpg')
width2 = im2.size[0]
height2 = im2.size[1]

im = im.convert('RGB')
im2 = im2.convert('RGB')

for x in range(width):
    for y in range(height):
        r, g, b = im.getpixel((x,y))
        r2, g2, b2 = im2.getpixel((x,y))
        if(r2<10and r>20):
          im3.putpixel((x,y),(0,0,0))
        else:
          im3.putpixel((x,y),(r-r2,g-g2,b-b2))
im3.save("temp.jpg")

tmp = Image.open('temp.jpg')
tmpwidth = tmp.size[0]
tmpheight = tmp.size[1]
rarray=[]
garray=[]
barray=[]

for x in range(tmpwidth):
    for y in range(tmpheight):
        rt, gt, bt = tmp.getpixel((x,y))
        if(rt>10):
          rarray.append(rt)
        if(gt>10):
          garray.append(gt)
        if(bt>10):
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

onediffr=[]
turnpointr=0
for runar in range(255):
  xaar=frer[runar+1]-frer[runar]
  onediffr.append(xaar)
for runbr in range(54,255):
  if(onediffr[254-runbr]<-300):
    turnpointr=254-runbr
    break


onediffg=[]
turnpointg=0
for runag in range(255):
  xaag=freg[runag+1]-freg[runag]
  onediffg.append(xaag)
for runbg in range(54,255):
  if(onediffg[254-runbg]<-300):
    turnpointg=254-runbg
    break

onediffb=[]
turnpointb=0
for runab in range(255):
  xaab=freb[runab+1]-freb[runab]
  onediffb.append(xaab)
for runbb in range(54,255):
  if(onediffb[254-runbb]<-300):
    turnpointb=254-runbb
    break

orir = detect_peaks(frer)
temparear=[]
peakr=[]
for xr in range(len(orir)):
  if(orir[xr]>18):
    temparear.append(orir[xr])
    peakr.append(frer[orir[xr]])
max_r = max(peakr)
realpeakr=temparear[(peakr.index(max_r))]

orig = detect_peaks(freg)
tempareag=[]
peakg=[]
for xg in range(len(orig)):
  if(orig[xg]>18):
    tempareag.append(orig[xg])
    peakg.append(freg[orig[xg]])
max_g = max(peakg)
realpeakg=tempareag[(peakg.index(max_g))]

orib = detect_peaks(freb)
tempareab=[]
peakb=[]
for xb in range(len(orib)):
  if(orib[xb]>18):
    tempareab.append(orib[xb])
    peakb.append(freb[orib[xb]])
max_b = max(peakb)
realpeakb=tempareab[(peakb.index(max_b))]
thevaalue=-0.07*turnpointr-1.72*turnpointb+1.84*realpeakg+1.77*realpeakb-3.07*(turnpointr-realpeakr)-5.06*(turnpointg-realpeakg)+8.33*(turnpointr*0.299+turnpointg*0.587+turnpointb*0.114)-10.61*(realpeakr*0.299 + realpeakg*0.587 + realpeakb*0.114)-1.48*((turnpointr-realpeakg)*0.299 + (turnpointg-realpeakg)*0.587 + (turnpointb-realpeakb)*0.114)
BigString="預估pm2.5濃度為: "+str(thevaalue)+"(μg/m3)"
messagebox.showinfo("預估pm2.5濃度",BigString)
print(turnpointr,turnpointg,turnpointb,realpeakr,realpeakg,realpeakb,(turnpointr-realpeakr),(turnpointg-realpeakg),turnpointb-realpeakb,(turnpointr*0.299+turnpointg*0.587+turnpointb*0.114),(realpeakr*0.299 + realpeakg*0.587 + realpeakb*0.114),(turnpointr-realpeakg)*0.299 + (turnpointg-realpeakg)*0.587 + (turnpointb-realpeakb)*0.114)

a.mainloop()
