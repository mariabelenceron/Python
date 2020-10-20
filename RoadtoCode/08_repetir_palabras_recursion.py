def repetir_palabra(palabra, numero_repeticion):
    if numero_repeticion == 1:
        return palabra
    return palabra + repetir_palabra(palabra, numero_repeticion - 1)

if __name__ == "__main__":
    palabra = input('Ingrese la palabra a repetir: ')
    numero_repeticion = int(input('Ingrese el numero de veces a repetir: '))
    print(repetir_palabra(palabra, numero_repeticion))