def run():
    numero = int(input('Ingrese el tamano del cuadrado: '))
    for i in range(numero):
        if i == (numero-1) or i == 0:
            print('#'* (numero), end="")
        else:
            for j in range(numero):
                if j == (numero-1) or j == 0:
                    print('#',end="")
                else:
                    print(' ',end="")
        print()
if __name__ == "__main__":
    run()