n=float(input("Digite um numero: "))
if n==3 or n==5 or n==7:
  print("É um numero primo")
elif n==2:
  print("Não é um numero primo")
if n%2!=0 and n%3!=0 and n%5!=0 and n%7!=0:
  print("É um número primo")
else:
  print("Não é um numero primo")