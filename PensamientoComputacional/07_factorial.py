def factorial(n):
    """Calcular el factorial de un numero

    Args:
        n (int): Numero mayor a 0

    Returns:
        int: Retorna n!
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input('Escribe el numero a saber su factorial: '))
print(factorial(n))