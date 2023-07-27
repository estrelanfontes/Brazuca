def test(x):
    if x%2 == 0:
        print("é par")
    else:
        print("é impar")
    return f"O dobro de {x} é {x*2}"
v = test(5)
print(v)

def test(msg):
    print(msg)
def dumb():
    return test
v = dumb()
print(v)
print(type(v))
v("rodrigo")

def test():
    return "rodrigo", "paiva"
nome, sobrenome = test()
print(nome, sobrenome)

def test(*args):
    print(args)
test(1, 2, 3, 4, "rodrigo")

def test(*args):
    for i in args:
        print(i)
test(1, 2, 3, 4, "rodrigo", 5)

lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, *n)  #empacota os valores restantes de lista, no caso [3,4,5]
print(lista)
print(*lista)  #desempacota os valores existentes na lista
# o sinal: * qnd usado em lista tem a funcionalidade de desempacotar valores
# qnd usado em variaveis tem a funcionalidade de empacotar valores

def test(*args):
    print(args)

    args[0] = 99
    print(args)

n = int()
print(f"O valor de n é {n}")

def test(*args): #args = Arguments
    print(args) #*args Recebe parametros indefinidamente no formto de lista (não precisam de chaves, só recebem valores)
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
test(*lista, *lista2)

def test(*args, **kwargs): #kwargs = key words arguments. Recebe argumentos no formato de chaves: valores (dicionarios)
    print(args)
    print(kwargs["nome"], kwargs["idade"])

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
test(*lista, *lista2, nome = "rodrigo", idade = 21)
#td q se repete é arg
#td q é opcional é kwarg