def run():
    objetivo = int(input('Ingrese el numero a verificar la raiz cuadrada:'))
    respuesta = 0

    while respuesta ** 2 < objetivo:
        print(respuesta,end=" ")
        print(respuesta ** 2)
        respuesta += 1
    print(respuesta)
    if respuesta ** 2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

if __name__ == "__main__":
    run()