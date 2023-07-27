<<<<<<< HEAD
dados = {"nome": input("Qual o seu nome: "), "partidas": int(input("Quantas partidas ja jogou? "))}
a=0
lista = []
while dados["partidas"]!=0:
  gp = int(input("Quantos gols? "))
  a+=1
  lista.append(gp)
  if dados["partidas"]==a:
    break
dados["gols"] = lista
dados["soma"] = sum(lista)
print(dados)
print(dados["soma"])
=======
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
>>>>>>> 46f7a8e5c413536b46f99d94103049afe3ac471e
