abecedario = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

mensaje = 'CLAVEEJEM'
nuevo_arreglo = []
#range(len(mensaje)) = Tamaño del arreglo
for i in range(len(mensaje)):
    for j in range(len(abecedario)):
        if mensaje[i] == abecedario[j]:
            #.append(j) = agregar al arreglo la posición de la letra
            nuevo_arreglo.append(j)
#print() para imprimir el arreglo
print(nuevo_arreglo)
