def run():
    numero = int(input('Ingrese el tamano de su linea: '))
    for i in range(numero):
        print('#', end="")
    print()

if __name__ == "__main__":
    run()