import random
filas = int(input('Ingresa el numero de filas: '))
while filas > 20:
    filas = int(input('La filas no pueden ser mayores a 20, Ingrese de nuevo: '))

columnas = int(input('Ingresa el numero de columnas: '))
while columnas > 20:
    columnas = int(input('La columnas no pueden ser mayores a 20, Ingrese de nuevo: '))

#Llenar la matriz
matriz = []
for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        numero_aleatorio = random.randint(1,50)
        valor = numero_aleatorio
        matriz[i].append(valor)
#Imprimir matriz
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
print()

comparar1 = 0
comparar2 = 0
print(matriz)
# Mayor en cada fila 
for fila in matriz:
    for elemento in fila:
        comparar1 = elemento
        if comparar1 > comparar2:
            comparar2 = comparar1
        else:
            continue
    print(f'el mas grande es {comparar2}')
    comparar2 = 0