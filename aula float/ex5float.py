C=float(input("digite um valor em celsius: "))
F=float(input("digite um valor em fahrenheit: "))
K=float(input("digite um valor em kelvin: "))

kc=K-273.15
kf=(K-273.15)*9/5+32
fc=(F-32)*5/9+273.15
fk=(F-32)*5/9
ck=C+273.15
cf=(C*9/5)+32
print(f"o valor de celsius em kelvin é {ck}")
print(f"o valor de celsius em fahrenheit é {cf}")
print(f"o valor de fahrenheit em kelvin é {fk}")
print(f"o valor de fahrenheit em celsius é {fc}")
print(f"o valor de kelvin em celsius é {kc}")
print(f"o valor de kelvin em fahrenheit é {kf}")