p1 = float(input("Qual o peso? "))
p2 = float(input("Qual o peso? "))
p3 = float(input("Qual o peso? "))
p4 = float(input("Qual o peso? "))
p5 = float(input("Qual o peso? "))
v=p1,p2,p3,p4,p5
for i in (v):
  if i>=p1 and i>=p2 and i>=p3 and i>=p4 and i>=p5:
    r=i
  if i<=p1 and i<=p2 and i<=p3 and i<=p4 and i<=p5:
    s=i
print(f"{r} é o maior numero")
print(f"{s} é o menor numero")