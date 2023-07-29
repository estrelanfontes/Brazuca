#Crie uma função que receba um numero inteiro como entrada e retorne uma lista de todos os divisores desse numero
def f():
  n = int(input("Digite um numero inteiro: "))
  lista = []
  for i in range(1,9):
    if n%i == 0:
      lista.append(i)
  print(f"Os divisores desse numero são {lista}")
f()
