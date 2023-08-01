n = input("Digite seu nome  ")
try:
  i = int(input("digite sua idade  "))
  print(f"Seu nome é {n} e sua idade é {i}")
except ValueError:
  print("Digite um numero inteiro para idade")
  pass

