def calcular_hora_a_segundos(hora):
    una_hora = 3600
    return una_hora * hora

def calcular_minuto_a_segundos(minuto):
    un_minuto = 60
    return un_minuto * minuto

if __name__ == "__main__":
    hora = int(input('Ingrese una hora: '))
    minuto = int(input('Ingrese los minutos: '))
    print(f'{hora}:{minuto} son {calcular_hora_a_segundos(hora) + calcular_minuto_a_segundos(minuto)} segundos')
    