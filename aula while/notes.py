p = int(input("sua idade: "))
while p != 0:
    print(f"Você digitou {p}")
    p = int(input("sua idade: "))
print("Fim")


p = str(input("qual o seu sexo (M/F): ")).upper().strip()
while p not in "MF":
    print("Digite um valor valido")
    p = str(input("qual o seu sexo: "))
print(f"seu sexo é {p}")


pares = list()
impares = []
while True:
    n = int(input("Digite um valor: "))
    if n == 0:
     break
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print(pares)
print("")
print(impares)


def dobra(x):
    print(f"O valor dobrado é {x*2}")
dobra(2)


def dobra(x=1):
    return x*2
numero_dobrado = dobra(4)
print(numero_dobrado)


def main():
    numero_dobrado = dobra(4)
    print(f"o numero dobrado é {numero_dobrado}")
def dobra(x=1):
    return x*2
main()