import numpy as np
import matplotlib.pyplot as plt

x1=-20
x2=20
y1=-10
y2=10
plt.axis([x1,x2,y1,y2])

a=int(input("輸入第一個x座標"))
b=int(input("輸入第一個y座標"))
c=int(input("輸入第二個x座標"))
d=int(input("輸入第二個y座標"))
o=((d-b)/(c-a))
print("斜率=",o)
plt.plot([a,b],[c,d],linewidth=3,color='blue')

plt.axis('on')
plt.grid(False)

plt.show()
