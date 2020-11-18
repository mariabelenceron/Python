# Ejercicio 1

meses = [12,30,23,40,13,50,12,28,19,20,20,33]
promedio_anual = 0
meses_cosechas_superiores = 0
meses_cosechas_inferiores = 0

for i in meses:
    promedio_anual += i

promedio_anual = promedio_anual / len(meses)

for mes in meses:
    if mes > promedio_anual:
        meses_cosechas_superiores += 1
    else: 
        meses_cosechas_inferiores += 1

print(f'El promedio anual de toneladas cosechadas es: {promedio_anual}')
print(f'Meses con cosechas superiores al promedio anual: {meses_cosechas_superiores} meses')
print(f'Meses con cosechas inferiores al promedio anual: {meses_cosechas_inferiores} meses')