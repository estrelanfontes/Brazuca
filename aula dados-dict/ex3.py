dados = {"n": input("Qual o seu nome: "), "p": int(input("Quantas partidas ja jogou? "))}
a=0
lista = []
while dados["p"]!=0:
  gp = int(input("Quantos gols? "))
  a+=1
  lista.append(gp)
  if dados["p"]==a:
    break
print(lista)
#Falta colocar a lista no dicionário
