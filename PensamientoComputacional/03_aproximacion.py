def run():
    objetivo = int(input('Ingrese el numero a verificar la raiz cuadrada: '))
    #El margen de error es epsilon
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(respuesta**2,end=" ")
        print(objetivo,end=" ")
        print(abs(respuesta**2 - objetivo),respuesta)
        respuesta += paso
    print('---------------------------------')
    print(respuesta**2,end=" ")
    print(objetivo,end=" ")
    print(abs(respuesta**2 - objetivo),respuesta)
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada del {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

if __name__ == "__main__":
    run()