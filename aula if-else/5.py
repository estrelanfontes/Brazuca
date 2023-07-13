v1=float(input("Digite um numero inteiro: "))
v2=float(input("Digite um numero inteiro: "))
v3=float(input("Digite um numero inteiro: "))

if v3==v2 or v3==v1 or v2==v1:
    print("não pode ter valores iguais")
else:
 if v1>v2 and v1>v3:
    print(f"{v1} é o maior numero")
 if v2>v1 and v2>v3:
    print(f"{v2} é o maior numero")
 if v3>v2 and v3>v1:
    print(f"{v3} é o maior numero")
 if v1<v2 and v1<v3:
    print(f"{v1} é o menor numero")
 if v2<v1 and v2<v3:
    print(f"{v2} é o menor numero")
 if v3<v2 and v3<v1:
    print(f"{v3} é o menor numero")