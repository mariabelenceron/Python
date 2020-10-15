import string

def run():
    frase = input('Ingrese una frase: ')
    frase = frase.lower()
    contador_espacios = 0
    contador_vocales = 0
    for i in frase:
        if i == " ":
            contador_espacios +=1
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            contador_vocales+=1
    print(f'La frase: "{frase}" tiene {contador_espacios} espacios y {contador_vocales} vocales')


if __name__ == "__main__":
    run()