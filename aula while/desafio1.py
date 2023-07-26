p=(int(input("Sequencia fibonacci até o numero: ")))
def fib():
  n1=1
  n2=1
  N=n1+n2
  print(n1)
  print(n2)
  while p>N:
    N=n1+n2
    n1=n2
    n2=N
    if p<N:
      break
    else:
      print(N)
fib()