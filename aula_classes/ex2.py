class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
retangulo = Retangulo(float(input("Largura:  ")), float(input("Altura:  ")))
def area():
    print(f"Area:  {Retangulo.altura*Retangulo.largura}")
area()