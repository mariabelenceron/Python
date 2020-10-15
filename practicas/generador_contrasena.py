import random
import string

def generar_contrasena():
    caracteres = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

    # mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    # simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    # numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    # caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    #Para poder transformar de lista a string
    contrasena = "".join(contrasena)
    return contrasena

def run():
    contrasena = generar_contrasena()
    print(f'Tu nueva contraseña es: {contrasena}')

    #Pruebas
    # caracteres = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase
    # print(caracteres)
    # lista = list(string.ascii_letters)
    # print(lista)

if __name__ == "__main__":
    run()