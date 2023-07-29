p=(int(input("Sequencia fibonacci até o numero: ")))
def fib():
  n1=1
  n2=1
  N=n1+n2
  while p>N:
    N=n1+n2
    n1=n2
    n2=N
  if p<N:
    print(f"O numero {p} não pertence a sequencia")
  else:
      print(p)
fib()
