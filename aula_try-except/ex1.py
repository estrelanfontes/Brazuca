try: 
    s = int(input(f"Digite um numero inteiro:  "))
    print(s*2)
except ValueError:
    print("Você não inseriu um numero inteiro")

