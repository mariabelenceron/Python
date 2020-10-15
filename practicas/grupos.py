def run():
    nombre = input('Cual es su nombre?: ')
    mensaje_genero = """
    Cual es su genero?
    H - Hombre
    M - Mujer
    (H/M):
    """
    genero = input(mensaje_genero)
    genero = genero.lower()
    if (genero == 'm' and nombre.lower() < 'm') or (genero == 'h' and nombre.lower() > 'n'):
        print("Su grupo es A")
    else:
        print("Su grupo es B")

if __name__ == "__main__":
    run()