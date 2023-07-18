#pra cada item na lista print move
for i in [0,1,2]:
    print("move")

for i in range(3):
    print("move")

for i in [0,1,2]:
    print(i)

#printa de 0 a 9
for i in range(10):
    print(i)

#print de 0 a 9 de 2 em 2
for i in range(0,10,2):
    print(i)

start = int(input("start: "))
end =  int(input("end: "))
step = int(input("step: "))
for i in range(start, end, step):
    if i % 10 == 0:
        print(i)

#Só pode usar o for quando tiver um objeto interável
#O range só trabalha com valores inteiros

#len significa posição
#aluno+1 representa a posição dos valores de "alunos"
#alunos[aluno] mostra os valores dentro de "alunos"
alunos = ["rodrigo", "antonio", "pedro"]
for aluno in range(len(alunos)):
    print(aluno+1, alunos[aluno])

