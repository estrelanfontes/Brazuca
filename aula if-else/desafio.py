#Faça um programa que leia 3 retas do usuário e diga se elas podem formar um triângulo


a1=float(input("Qual a medida? "))
a2=float(input("Qual a medida? "))
a3=float(input("Qual a medida? "))

if (a1+a2)<a3 and (a1+a3)<a2 and (a3+a2)<a1 or a1==a2==a3:
    print("é um triângulo")
else:
    print("não é um triangulo")