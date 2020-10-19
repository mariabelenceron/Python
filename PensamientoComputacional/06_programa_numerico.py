def enumaracion_exhaustiva(objetivo):
    """Es un tipo de metodo sobre buscar diferentes o todos los posibles resultados de lo que se esta buscando

    Args:
        objetivo (int): Recive el numero que se desea calcular la raiz cuadrada
    """
    respuesta = 0
    while respuesta ** 2 < objetivo:
        respuesta += 1
    if respuesta ** 2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')

def aproximacion(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada del {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')

def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    print(respuesta)
    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo) / 2
    print(f'La raiz cuadrada del {objetivo} es {respuesta}')

if __name__ == "__main__":
    mensaje = """
    Bienvenido al programa de calculo de raiz cuadrada usando 3 metodos distintos:
    1. Enumeracion Exhaustiva
    2. Aproximacion
    3. Busqueda Binaria
    4. Salir
    Escoge una opcion: """
    

    while True:
        opcion = int(input(mensaje))
        
        if opcion == 1:
            enumaracion_exhaustiva(objetivo)
            objetivo = int(input('Ingrese el numero a calcular su raiz cuadrada:'))
        elif opcion == 2:
            objetivo = int(input('Ingrese el numero a calcular su raiz cuadrada:'))
            aproximacion(objetivo)
        elif opcion == 3:
            objetivo = int(input('Ingrese el numero a calcular su raiz cuadrada:'))
            busqueda_binaria(objetivo)
        elif opcion == 4:
            break

