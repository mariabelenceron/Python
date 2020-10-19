def validar_triangulo(a,b,c):
    """Validar si es un trinagulo o no

    Args:
        a (int): Primer lado
        b (int): Segundo lado
        c (int): Tercer lado
    """
    if (a+b) > c and a+c > b:
        print('Es un triangulo')
    else:
        print('No es un triangulo')

if __name__ == "__main__":
    validar_triangulo(3,3,3)