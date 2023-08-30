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
from detecta import detect_peaks

import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import csv
from itertools import zip_longest


a = Tk()
a.title("使用自動化偏振光學方法預測PM2.5")
hello = Label(a, text="使用自動化偏振光學方法預測PM2.5", width="30", height="5")
hello.pack()
hello1 = Label(a, text="研究者:王培宇 陶德愷 陸紹祺", width="30", height="5")
hello1.pack()
hello1 = Label(a, text="程式設計:陸紹祺", width="30", height="5")
hello1.pack()
def mfileopen():
	file1 = filedialog.askopenfile()
	label = Label(text=file1).pack()
	if file1:
		filepath1 = os.path.abspath(file1.name)
		return filepath1
def mfileopen2():
	file2 = filedialog.askopenfile()
	label2 = Label(text=file2).pack()
	if file2:
		filepath2 = os.path.abspath(file2.name)
		return  filepath2



button = Button(text="請開啟沒有偏振的照片",width = 30,command= mfileopen).pack()
button2 = Button(text="請開啟有偏振的照片",width = 30,command= mfileopen2).pack()

im = Image.open(mfileopen())
width = im.size[0]
height = im.size[1]

im2 = Image.open(mfileopen2())
width2 = im2.size[0]
height2 = im2.size[1]

im3 = Image.open(mfileopen2())

im = im.convert('RGB')
im2 = im2.convert('RGB')

for x in range(width):
	for y in range(height):
		r, g, b = im.getpixel((x, y))
		r2, g2, b2 = im2.getpixel((x, y))
		im3.putpixel((x, y), (r - r2, g - g2, b - b2))

im3.save("temp.jpg")
im3.show()

tmp = Image.open('temp.jpg')
tmpwidth = tmp.size[0]
tmpheight = tmp.size[1]
rarray=[]
garray=[]
barray=[]
cntfor=0
for x in range(tmpwidth):
    for y in range(tmpheight):
        rt, gt, bt = tmp.getpixel((x,y))
        if(rt>10):
          rarray.append(rt)
          cntfor+=1
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

plt1.plot(z,frer)
plt1.xlabel('r值')
plt1.xticks(range ( 0 , 256 , 20 ))
plt1.ylabel('次數')
plt1.title('R')

plt2.plot(z,freg)
plt2.xticks(range ( 0 , 256 , 20 ))
plt2.xlabel('g值')
plt2.ylabel('次數')
plt2.title('G')

plt3.plot(z,freb)
plt3.xticks(range ( 0 , 256 , 20 ))
plt3.xlabel('b值')
plt3.ylabel('次數')
plt3.title('B')

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

x=(realpeakr*0.299+realpeakg*0.587 +realpeakb*0.114)
y=-0.8152*x+89.872
BigString="預估pm2.5濃度為: "+str(y)+"(μg/m3)"
messagebox.showinfo("預估pm2.5濃度",BigString)


a.mainloop()


