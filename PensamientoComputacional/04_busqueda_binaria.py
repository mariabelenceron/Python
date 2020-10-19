def run():
    objetivo = int(input('Ingrese el numero a verificar la raiz cuadrada: '))
    #El margen de error es epsilon
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    print(respuesta)
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}, abs={abs(respuesta**2 - objetivo)}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2
    print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}, abs={abs(respuesta**2 - objetivo)}')
    print(f'La raiz cuadrada del {objetivo} es {respuesta}')

if __name__ == "__main__":
    run()