v1 = int(input("Digite um numero inteiro: "))
v2 = int(input("Digite um numero inteiro: "))
v3 = int(input("Digite um numero inteiro: "))
v4 = int(input("Digite um numero inteiro: "))
v5 = int(input("Digite um numero inteiro: "))
lista = []
soma = 0
#para cada item na lista com tais valores
for v in [v1, v2, v3, v4, v5]:
    #Se o item for divisivel por 2
    if v % 2 == 0:
        #Adicione o item a lista
        lista.append(v)

#Para cada item na lista em que os valores são divisiveis por 2
for x in lista:
    #Adicione os valores na variavel soma
    soma = soma + x
#Printe a soma final de todos os valores
#Esse print está fora do "for" porque não precisa mostrar a soma de cada valor e sim a soma final
print(f"A soma de apenas numeros pares é: {soma}")