!pip install  pycryptodome
!pip install  libnum
from libnum import*
from Crypto.Util.number import inverse,long_to_bytes

print("This program is use to solve RSA problem")
print("\033[31mBefore using,Please install pycryptodome . THE script is below \033[0m")
print("\033[34mpip install  pycryptodome\033[0m")
print("This program Only use when the public key (e) is very small")
print("\033[0;31;42mENCRYPT!!\033[0m")

n=eval(input("Please enter your  modulus (n) "))
e=eval(input("Please enter your little public key (e) "))
c=eval(input("Please enter your  ciphertext (c) "))


print(n2s(nroot(n,(e))))
