def quitar_vocales(parrafo):
    nuevo_parrafo = ''
    for i in parrafo:
        if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U':
            continue
        nuevo_parrafo += i

    return nuevo_parrafo

if __name__ == "__main__":
    parrafo = input('Ingrese un parrafo: ')
    print(quitar_vocales(parrafo))