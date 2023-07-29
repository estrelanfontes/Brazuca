#Escreva uma função que receba uma lista de strings como entrada e retorne um dicionario onde as chaves sao as strings e os valores sao os numeros 

l2 = []
p = 0
l = [input(""), input(""), input("")]
for i in l:
  p +=1
  l2.append(i)
  l2.append(p)

def Convert(a):
    it = iter(a) # iter() leva um objeto arbitrário e tenta retornar um iterador que retornará os conteúdos ou elementos do objeto
    res_dct = dict(zip(it, it)) #Combinar várias listas em uma única lista de tuplas usando o zip() 
    return res_dct

print(Convert(l2))
