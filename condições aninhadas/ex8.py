p=float(input("peso em kg: "))
a=float(input("altura em metros: "))
imc=p/a**2
if imc<18.5:
  print("abaixo do peso")
elif imc>=18.5 and imc<25:
  print("peso ideal")
  if imc>=25 and imc<30:
    print("sobrepeso")
elif imc>=30 and imc<40:
  print("obesidade")
else:
  print("obesidade mórbida")
