import math
a1=float(input("Qual o angulo? "))
a2=float(input("Qual o angulo? "))
a3=float(input("Qual o angulo? "))
#para ser um triangulo:
e = a3!=0 and a1!=0 and a2!=0
e = (a1+a2)>a3
e = (a1+a3)>a2
e = (a3+a2)>a1 
e = math.fabs(a3-a2)<a1 or math.fabs(a1-a2)<a3 or math.fabs(a3-a1)<a2 
if e==True:
    if a1==a2==a3:
      t="equilátero"
    elif a1!=a3 and a2!=a3 and a2!=a1:
      t="escaleno"
    else:
      t="isósceles"

    print(f"é um triângulo {t}")
    
else:
    print("não é um triangulo")
