import random
j1 = random.randint(1,6)
j2 = random.randint(1,6)
j3 = random.randint(1,6)
j4 = random.randint(1,6)
n = j1,j2,j3,j4
d = {"jogador1": j1, "jogador2": j2,"jogador3":j3,"jogador4": j4}
d = dict(sorted(d.items(),key = lambda item: item[1], reverse=True))
print(d)

"""Maior e menor valor
for i in n:
    if i>=j1 and i>=j2 and i>=j3 and i>=j4:
        maior=i
for i in n:
    if i<=j1 and i<=j2 and i<=j3 and i<=j4:
        menor=i
print(maior)
print(menor)
"""