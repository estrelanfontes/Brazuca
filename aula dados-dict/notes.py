lista = list() == []#Função que guarda valores
dicionarios = dict() == {}#Possui uma chave e um valor ex: "chave": "valor"
tuplas = tuple() == ()#Lista imutável
conjuntos = set()#Dicionario com um valor

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dobra = [n for n in lista if n % 2 == 0]
dobra = [n if n % 2 == 0 else None for n in lista]
print(dobra)

nomes = ["Rodrigo", " Pedro", "Antonio" ]
lista_modificada = [nome for nome in nomes]
print(lista_modificada)

filme1 = {"Nome": "Vingadores", "ano": 2013}
filme2 = {"Nome": "a ilha", "ano": 2033}
locadora = [filme1, filme2]
print(locadora[0]["ano"])

filme1 = {"Nome": "Vingadores", "ano": 2013, "chave": "valor"}
for k, v in filme1.values():
    print(k, v)
for k, v in filme1.items():
    print(k, v)
for k, v in filme1.keys():
    print(k, v)

lista = [1, 2, 3, 4]
d1 = {v for v in lista}