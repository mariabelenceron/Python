def run():
    nombre_1 = input('Cual es su nombre?: ')
    edad_1 = int(input('Cual es su edad?: '))
    nombre_2 = input('Cual es su nombre?: ')
    edad_2 = int(input('Cual es su edad?: '))

    if edad_1 > edad_2:
        print(f'{nombre_1} es mayor que {nombre_2}')
    else:
        print(f'{nombre_2} es mayor que {nombre_1}')


if __name__ == "__main__":
    run()