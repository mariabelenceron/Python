calificacion_alumnos = [2,5,8,4,6,10,9,2,5,6,7,9,8,0]
promedio_general = 0
alumnos_aprobados = 0
alumnos_reprobados = 0
total_alumnos = len(calificacion_alumnos)

for i in calificacion_alumnos:
    promedio_general += i

for i in calificacion_alumnos:
    if i >= 8:
        alumnos_aprobados += 1
    else:
        alumnos_reprobados +=1


print(f'El promedio general del grupo es: {round(promedio_general/len(calificacion_alumnos),2)}')
print(f'Hay {alumnos_aprobados} alumnos aprobados y {alumnos_reprobados} alumnos reprobados')
print(f'De los {total_alumnos} alumnos, el {round((alumnos_aprobados / total_alumnos)*100,2)}% aprobaron y el {round((alumnos_reprobados / total_alumnos)*100,2)}% reprobaron')
print(f'Hay {alumnos_aprobados} alumnos cuyas calificaciones son mayores o iguales a 8')