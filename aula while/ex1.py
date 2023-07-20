import random


def rodaojogo():
 
    cpu=random.randint(0,5)
    player=int(input("Digite um numero de 0 a 5: "))
    i=0

    while player!=cpu:
        print("you lost, try again")
        i+= 1
        print(f"Você usou {i} tentativas")
        player=int(input("Digite um numero de 0 a 5: "))
   
        if player==cpu:
            i=i+1
            print("you win")
            print(f"Você usou {i} tentativas")
            break




rodaojogo()
