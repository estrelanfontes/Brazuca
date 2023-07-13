import random
cpu=random.randint(0,5)
player=int(input("Digite um numero de 0 a 5: "))
if player==cpu:
    print("you win")
else:
    print("you lost, try again")