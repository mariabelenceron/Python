mensaje = """
Bienvenido al juego de Piedra, Papel o Tijera
Que gane el mejor!!
"""
print(mensaje)
nombre_jugador_1 = input('Nombre del jugador 1: ')
nombre_jugador_2 = input('Nombre del jugador 2: ')
contador_jugador_1 = 0
contador_jugador_2 = 0
bandera = True

while bandera:
    print('--------------------------------------------')
    jugador_1 = input(f'Turno de {nombre_jugador_1}: ').lower()
    jugador_2 = input(f'Turno de {nombre_jugador_2}: ').lower()

    if (jugador_1 == 'piedra' and jugador_2 == 'papel') or (jugador_1 == 'tijera' and jugador_2 == 'piedra') or (jugador_1 == 'papel' and jugador_2 == 'tijera'):
        contador_jugador_2 += 1
        print(f'Ganó {nombre_jugador_2}')
    elif (jugador_1 == 'papel' and jugador_2 == 'piedra') or (jugador_1 == 'piedra' and jugador_2 == 'tijera') or (jugador_1 == 'tijera' and jugador_2 == 'papel'):
        contador_jugador_1 += 1 
        print(f'Ganó {nombre_jugador_1}')
    elif jugador_1 == jugador_2:
        print(f'Empate')
    else:
        print('Opción no valida, Inténtalo de nuevo')

    if contador_jugador_1 == 3:
        print('--------------------------------------------\n--------------------------------------------')
        print(f'Felicidades {nombre_jugador_1} has ganado!!')
        bandera = False
    elif contador_jugador_2 == 3:
        print('--------------------------------------------\n--------------------------------------------')
        print(f'Felicidades {nombre_jugador_2} has ganado!!')
        bandera = False
