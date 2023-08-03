import sys #biblioteca sys--Parâmetros e funções específicas do sistema (possui a lista argv)
print("hello my name is", sys.argv[1])#argv--lista de todos os parametros executados no terminal

import sys 
if len(sys.argv) == 2:
    print("hello my name is", sys.argv[1])
else:
    sys.exit("Too many arguments")#função exit() encerra o programa e consegue printar str 
#sys.path()--acessa o caminho de um arquivo
#OBS listas:  [:] inicio ao fim,,,[1:] posição um ao fim,,,[:-1] inicio ao fim,,,[5,-2,8] posição 5 ao antepenultimo de 8 em 8
import time
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
        print(f"f: {f}\nc: {c}")
        time.sleep(1)#função da biblioteca time que manipula o tempo de execução
    return f
#O modulo importa as funçoes que você criou em outro arquivo. EX:
"""import modulo
print(modulo.fatorial(5))
print(modulo.dobro(5))
OU
from modulo import fatorial, dobro"""

"from aulas import sys"