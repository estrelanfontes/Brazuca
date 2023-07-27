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