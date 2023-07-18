lista = []
soma = 0
for n in range(1,501):
   if n % 3 == 0:
      lista.append(n)
print(f"Valores dentro da lista: {lista}")

for x in range(len(lista)):
   soma = soma + lista[x]
print(f"Soma de todos os valores multiplos de 3: {soma}")
print(f"Quantos números são divisíveis? {len(lista)}")