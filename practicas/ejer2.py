numero = int(input('Ingrese un numero: '))

if numero % 2 == 1:
    print('Weird')
else:
    if numero >= 2 and numero <= 5:
        print("Not Weird")
    elif numero >= 6 and numero <= 20:
        print("Weird")
    else:
        print("Not Weird")
