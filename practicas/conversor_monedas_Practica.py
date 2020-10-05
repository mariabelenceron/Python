pesos_mexicanos = input("Cuantos pesos mexicanos tienes?: ")
pesos_mexicanos = float(pesos_mexicanos)
valor_dolar = 22.10
dolares = pesos_mexicanos / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("Estos son los dolares que tienes: " + dolares)

dolares_eu = input("Cuantos dolares tienes?: ")
dolares_eu = float(dolares_eu)
valor_peso = 22.10
pesos_mex = dolares_eu * valor_peso
pesos_mex = round(pesos_mex,2)
pesos_mex = str(pesos_mex)
print("Estos son los pesos_mex que tienes: " + pesos_mex)