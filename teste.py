dados = {"nome": input("Qual o seu nome: "), "partidas": int(input("Quantas partidas ja jogou? "))}
lista = []
for e in dados["partidas"]:
  gp = int(input(f"Quantos gols na partida {e+1}? "))
  lista.append(gp)
dados["gols"] = lista
dados["soma"] = sum(lista)
print(dados)
print(dados["soma"])