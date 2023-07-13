print("\nstart")
if False:
    print("False") #if false=algo que não aconteceu, os valores desse "if" foram ignorados
if True:
    print("True")

print("Is\n\n")

name = input("Say your name: ")
if name == "Star":
    print("You are Star")
elif name=="Flor":
    print("Hi Flor!")
else:
    print("You are not Star")
print(f"Nice to meet you")

"Por que não dois ifs?"
x = int(input("x= "))
if x > 2:
    print(f"{x}greater than 2")
else:
    print(f"{x} get greater than 2")

"EX 2:"
score = float(input("Qual a nota? "))
if score>9 and score<10:
    print("Vc ganhou um A")
if score > 7 and score<9:
    print("Vc ganhou um B")
else:
    print(f"{score} not greater than 2")

"EX 3:"
score = float(input("Qual a nota? "))
if score==10:
    print("wonderfull")
elif score==9 or 8:
    print("congratulations")
else:
    print("You get an F")

"Ex 4:"
name = input("Whats your name? ")
if name != "Star":
    print("Nice to meet you")
else:
    print("Hi")

"Ex 5:"
name = input("Whats your name? ")
if not name == "Star":
    print("Nice to meet you")
else:
    print("Hi")