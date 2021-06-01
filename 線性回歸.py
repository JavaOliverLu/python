import matplotlib.pyplot as plt
import numpy as np
xa=[4,3,2.67,2.5,2.4,2.33,2.29,2.25,2.22,2.2,2.18,2.17,2.15,2.14,2.13,2.13,2.12,2.11,2.11,2.1]
ya=[-162,-89,-42,0,35.2,69,98.8,126,151.7,174.9,196.3,216,234,253.6,270.6,287,302.2,317,330,343]
 
 
N=20
 
 
x_sum=0
y_sum=0
x2_sum=0
xy_sum=0
 
# 計算各總和
for i in range(0,N):
   x_sum=xa[i]+x_sum
   y_sum=ya[i]+y_sum
   x2_sum=xa[i]*xa[i]+x2_sum
   xy_sum=xa[i]*ya[i]+xy_sum
 
 
x_avg=x_sum/N
y_avg=y_sum/N
x2_avg=x2_sum/N
xy_avg=xy_sum/N
 
#計算 a b
a= (xy_avg-x_avg*y_avg)/(x2_avg-x_avg*x_avg)
b= y_avg - a* x_avg
print('y=%6.2fx+' % a,'%6.2f' % b )
 
x = np.arange(-5,5, 2)
y = x*a +b
plt.plot(x,y)
plt.axhline(y=0)
plt.axvline(x=0)
plt.title("The relation between ratio of hydrogen and carbon and Boiling point temperature", fontsize=10)
plt.xlabel("ratio of hydrogen and carbon", fontsize=15)
plt.ylabel("Boiling point temperature", fontsize=15)
for flag in range(20):
 plt.scatter(xa[flag],ya[flag])
plt.show()
