def run():
    frase = input('Ingrese su correo: ')
    contador = 0
    for i in frase:
        if i == '@':
            contador +=1
    if contador > 1:
        print('Su correo es invalido')
    else:
        print('Su correo es valido')


if __name__ == "__main__":
    run()