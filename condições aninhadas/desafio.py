p1=str(input("pedra papel ou tesoura? Player 1:  "))
p2=str(input("pedra papel ou tesoura? Player 2:  "))
if p1=="pedra" and p2=="tesoura" or p1=="papel" and p2=="pedra" or p1=="tesoura" and p2=="papel":
  print("Player 1 ganhou")
elif p1==p2:
  print("Empate")
else:
  print("Player 2 ganhou")
