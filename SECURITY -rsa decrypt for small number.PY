!pip install  pycryptodome
from Crypto.Util.number import inverse,long_to_bytes
print("This program is use to solve RSA problem")
print("\033[31mBefore using,Please install pycryptodome . THE script is below \033[0m")
print("\033[34mpip install  pycryptodome\033[0m")
print("This program Only use when the modulus (n), public key (e) and ciphertext (c) are very small")
print("\033[0;31;42mENCRYPT!!\033[0m")

n=eval(input("Please enter your little modulus (n) "))
e=eval(input("Please enter your little public key (e) "))
c=eval(input("Please enter your little ciphertext (c) "))


print(long_to_bytes(pow(n,(1/e))))
