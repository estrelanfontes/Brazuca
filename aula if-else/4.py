km=float(input("Quantos km? "))
if km<200 or km==200:
    cobrar=km*0.5
    print(f"Você pagará {cobrar} reais")
else:
    cobrar=km*0.45
    print(f"Você pagará {cobrar} reais")