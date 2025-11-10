
print("Bienvenido, este programa es para analizar las calidifiaciones de tu curso")
alumca = int(input("Ingresa el numero de alumnos que deseas registrar: "))

nombres=[]
calificaciones=[]

for i in range(alumca):
    nombre = input (f"Ingresa el nombre del alumno {i+1} : ").lower()
    calificacion = float (input(f"Ingresa la calificacion de {nombre}: "))
    nombres.append(nombre)
    calificaciones.append(calificacion)


aprobados=[]
reprobados=[]
exelentes=[]

promediog = sum(calificaciones)/alumca

for i in range(alumca):
    nota = calificaciones[i]
    nombre = nombres [i]

    if nota == 10:
        exelentes.append(nombre)
    
    elif nota > 6:
        aprobados.append(nombre)
    
    elif nota < 5:
        reprobados.append(nombre)

print("REPORTE FINAL")
print(f"Total de estudiantes: {alumca}")
print(f"Promeduo general: {promediog}")
print(f"Calificacion mas alta: {max(calificaciones)}")
print(f"Calificacion mas baja: {min(calificaciones)}")
print(f"Estudiantes con calificacion exelentes: {exelentes}")
print(f"Estudiantes aprobados: {aprobados}")
print(f"Estudiantes reprobados: {reprobados}")
print("HASTA LUEGO")



