valor=float(input("qual o valor da casa? "))
salario=float(input("qual o seu salário? ")) # 1000
anos=float(input("quantos anos vai pagar? "))

sl = salario * 0.3
prestação = valor/anos*12

if prestação>sl:
    print("emprestimo negado")
elif prestação<=sl:
    print("emprestimo aprovado")