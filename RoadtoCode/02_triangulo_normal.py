def run():
    numero = int(input('Ingrese el tamano del triangulo: '))
    for i in range(numero + 1):
        print('#'*i)

if __name__ == "__main__":
    run()