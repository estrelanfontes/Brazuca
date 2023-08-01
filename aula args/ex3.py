def m():
  l = [input("digite o elemento 1: "), input("digite o elemento 2: "), input("digite o elemento 3: ")]
  lis = []
  for i in l:
    if len(i) == 5:
      lis.append(i)
  print(f"A lista com elementos de 5 carcteres: {lis}")
m()
