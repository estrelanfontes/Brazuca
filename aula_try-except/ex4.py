def read_file():
    try:
        print(open(input("nome:  ")).read())
    except FileNotFoundError:
        print("The file don't exist")
read_file()
#C:/Users/brazuca/Desktop/Estrela/
   # meuArquivo = open('teste.txt')
    #print(meuArquivo.read())