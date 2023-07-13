import random
list = []

a=str(input("digite o nome do aluno: "))
b=str(input("digite o nome do aluno: "))
c=str(input("digite o nome do aluno: "))
d=str(input("digite o nome do aluno: "))

list.append(a)
list.append(b)
list.append(c)
list.append(d)

r = random.choice(list)
print(r)