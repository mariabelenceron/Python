numero = int(input('Ingrese el numero de N para formar la matriz identidad: '))
for i in range(numero):
    for j in range(numero):
        if i == j:
            print('1', end=" ")
        else:
            print('0',end=" ")
    print()