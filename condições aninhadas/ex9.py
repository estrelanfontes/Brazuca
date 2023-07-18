p=float(input("Preço do produto: "))
print("OPÇÕES DE PAGAMENTO")
print("à vista dinheiro/cheque--10% de desconto--digite: 1")
print("à vista no cartão--5% de desconto--digite: 2")
print("em até 2x no cartão--preço formal--digite: 3")
print("3x ou mais no cartão--20% de juros--digite: 4")
f=str(input("Forma de pagamento: "))

if f=="1":
  a=p-p*0.1
  print(f"Total a pagar: {a}")
elif f=="2":
  a=p-p*0.05
  print(f"Total a pagar: {a}")
elif f=="3":
  a=a/2
  print(f"Total a pagar: Até duas vezes {a}")
elif f=="4":
  q=int(input("quantas vezes? "))
  j=p*0.2
  a=p/q
  print(f"Total a pagar: {a+j/q}")
