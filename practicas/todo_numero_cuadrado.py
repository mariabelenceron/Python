def square_digits(num):
    num = str(num)
    num = list(num)
    resultado = 0
    guardar_numeros = []
    for i in num:
        resultado = int(i)**2
        guardar_numeros.append(str(resultado))
    guardar_numeros = "".join(guardar_numeros)
    guardar_numeros = int(guardar_numeros)
    return guardar_numeros

def run():
    print(square_digits(9119)) 

if __name__ == "__main__":
    run()