def div():
    a = float(input("a: "))
    b = float(input("b: "))
    try:
        return print(a/b)
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
div()