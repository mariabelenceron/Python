numero = int(input('Escribe el numero hasta el que quieres que imprima: '))
resultado = 1
potencia = 1
contador = 1

for i in range(1,numero):
    resultado = str(resultado)
    if resultado[len(resultado)-1] == '9':
        if i >= 8 and i <= 100:
            potencia = 2
        elif i >= 100 and i <= 1000:
            potencia = 3
    resultado = int(resultado)
    aux = resultado*(10**potencia)
    resultado = aux + i + 1
    
print(resultado)

#Solucion corta
# numero = int(input('Escribe el numero hasta el que quieres que imprima: '))
# for i in range(1, numero+1):
#     print(i, end="")
