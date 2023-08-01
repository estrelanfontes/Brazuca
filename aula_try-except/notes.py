#raise--criar um erro
while True:
    try:
        x = int(input("whats x: "))
    except ValueError:
        print("X invalid")
    else:
        break
print(f"X is {x}")


try:
    x = int(input("whats x: "))
except ValueError:
        print("X invalid")
else:
     print(f"X is {x}")


def main():
    z = get_int("whats z")
    x = get_int("whats x")
    print(f"X is {x}")

def get_int(msg):
    while True:
        try:
          return int(input(msg))
        except ValueError:
          pass
main()