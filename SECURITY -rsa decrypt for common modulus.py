from libnum import*
print("This program is use to solve RSA problem")
print("\033[31mBefore using,Please install libnum . THE script is below \033[0m")
print("\033[34mpip install  libnum\033[0m")
print("This program Only use when the modulus (n) is common. and you have two public key (e) and ciphertext (c)")
print("\033[0;31;42mENCRYPT!!\033[0m")
n=eval(input("Please enter your  modulus (n) "))
e1=eval(input("Please enter your  public key1 (e1) "))
e2=eval(input("Please enter your  public key2 (e2) "))
c1=eval(input("Please enter your  ciphertext1 (c1) "))
c2=eval(input("Please enter your  ciphertext2 (c2) "))

x,y,gcd=xgcd(e1,e2)
x=abs(x)
y=abs(y)
m1=pow(c1,x,n)
m2=invmod(pow(c2,y,n),n)
print(n2s(m1*m2%n))
