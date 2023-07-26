def termos():
  termos=int(input(f"Quantos termos a mais? "))
  while termos!=0:
    termos=int(input(f"Quantos termos a mais? "))
    if termos==0:
     break

v=2
f=0
q=39
print(f"Primeiro termo: {f}")
print("Os primeiros 20 numeros: ", end="")
for p in range(f,q,v):
    print(p,end=", ")
print("")
print(f"A razão: {v}")
termos()
#pequeno detalhe: eu só pergunto quantos termos ele quer ver a mais, mas eu não mostro os termos