class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome 
        self.idade = idade 
        self.profissão = profissao 
        print(f" Nome: {nome} \n Idade: {idade}\n Profissão: {profissao}")
p: Pessoa(input("Qual o nome?  "), int(input("Qual a idade?  ")), input("Qual a profissão?  "))