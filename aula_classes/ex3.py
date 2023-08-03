class Aluno:
    def __init__(self, nome, nota):
        self.me = nome
        self.ta = nota
aluno1 = Aluno("Joao", 9)
aluno2 = Aluno("Ana,", 8)
if aluno1.ta > aluno2.ta:
    print(f"Aluno {aluno1.me} teve a maior nota")
else:
    print(f"Aluno {aluno2.me} teve a maior nota")