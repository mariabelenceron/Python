def run():
    numero = int(input('Ingrese el tamano del cuadrado: '))
    for i in range(numero):
        for j in range(numero):
            print('#', end="")
        print()

if __name__ == "__main__":
    run()