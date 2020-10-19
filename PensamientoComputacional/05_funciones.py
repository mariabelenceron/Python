def nombre_completo(nombre,apellido,inverso = False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

if __name__ == "__main__":
    saludo = """
    Hola que tal
    asi pueden escribir en varias lineas
    """
    print(saludo)
    print(nombre_completo('Belen','Ceron')) #El tercer valor se queda con False
    print(nombre_completo('Belen','Ceron',inverso=True))
    print(nombre_completo(apellido='Ceron',nombre='Belen'))