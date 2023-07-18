ano=int(input("Qual seu ano de nascimento? "))
if ano==18:
  print("Hora de se alistar")
elif ano<18:
  f=18-ano
  print(f"ainda não é hora de se alistar. Faltam {f} anos")
else:
  p=ano-18
  print(f"passou da hora de se alistar. Você tem {p} anos a mais")
