def calculadora(num_1, operador, num_2):
    if operador == '+':
        return num_1 + num_2
    elif operador == '-':
        return num_1 - num_2
    elif operador == 'x':
        return num_1 * num_2
    elif operador == '/':
        return num_1 / num_2
    else:
        return f'Operador no valido'

if __name__ == "__main__":
    num_1 = int(input('Ingrese el numero 1: '))
    operador = input('Ingrese el operador: ')
    num_2 = int(input('Ingrese el numero 2: '))
    
    print(f'{num_1} {operador} {num_2} = {calculadora(num_1, operador, num_2)}')