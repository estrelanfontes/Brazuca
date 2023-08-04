import math
class Circulo:
    def __init__(self, raio):
        area = math.pi*raio**2
        print(f"Area:  {area}")
c: Circulo(float(input("Raio:  ")))#Aqui eu defini o valor da propriedade "raio"