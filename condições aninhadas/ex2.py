import math
n=int(input("digite um numero inteiro: "))
print("escolha a base de conversão:")
print("digite '1' para binário")
print("digite '2' para octal")
print("digite '3' para hexadecimal")
d=input("Digite: ")
#transformando um numero para binario
if d=="1":
 print(bin(n))
#transformando um numero para octal
elif d=="2":
 print(oct(n))
#transformando um numero para hexadecimal
elif d=="3":
 print(hex(n))
else:
 print("tente de novo")