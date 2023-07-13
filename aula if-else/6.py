s=float(input("Qual o salário? "))
if s>1250:
    aumento=s+15*s/100
    print(f"Você terá um aumento de {aumento}")
else:
    aumento=s+10*s/100
    print(f"Você terá um aumento de {aumento}")