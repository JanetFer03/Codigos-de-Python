
estudiantes = {}
materiasv= (
    "Resistencia de los materiales",
    "Control clásico",
    "Programación avanzada",
    "Matemáticas aplicadas",
    "Electrónica digital"
)


while True:
    print("\nHola, este es nuestro menú de opciones:")
    print("1. registrar")
    print("2. buscar")
    print("3. promedio")
    print("4. ver_todos")
    print("5. cursos_unicos")
    print("6. salir")

    opcion = input("¿Qué opción deseas? ").lower().strip()
    if opcion == "registrar" or opcion == "1":
        id_alumno = input("ID del alumno: ").strip()
        if id_alumno in estudiantes:
            print("Error: ese ID ya está registrado.")
            continue

        nombre = input("Nombre del alumno: ").strip()
        materia = input("Materia: ").strip()

        if materia not in materiasv:
            print("Error: materia no válida.")
            print("Materias válidas:", materiasv)
            continue


        calificaciones = []
        for i in range(1, 4):
            nota = input(f"Calificación {i}: ").strip()
            try:
                nota_float = float(nota)
                calificaciones.append(nota_float)
            except ValueError:
                print("Error: solo se permiten números.")
                break
        else:
            estudiantes[id_alumno] = {
                "nombre": nombre,
                "materia": materia,
                "calificaciones": calificaciones
            }
            print("Alumno registrado correctamente.")

    elif opcion == "buscar" or opcion == "2":
        id_buscar = input("ID del alumno a buscar: ").strip()
        if id_buscar in estudiantes:
            alumno = estudiantes[id_buscar]
            print("Nombre:", alumno["nombre"])
            print("Materia:", alumno["materia"])
            print("Calificaciones:", alumno["calificaciones"])
        else:
            print("El alumno no esta registrado.")

    elif opcion == "promedio" or opcion == "3":
        id_prom = input("ID del alumno: ").strip()
        if id_prom in estudiantes:
            notas = estudiantes[id_prom]["calificaciones"]
            promedio = sum(notas) / len(notas)
            print("Promedio:", round(promedio, 2))
        else:
            print("El alumno no esta registrado.")

    elif opcion == "ver_todos" or opcion == "4" or opcion == "ver todos" or opcion == "vertodos" :
        if not estudiantes:
            print("No hay estudiantes registrados.")
        else:
            for id_est, datos in estudiantes.items():
                print(f"ID: {id_est} | Nombre: {datos['nombre']}")

    elif opcion == "cursos_unicos" or opcion == "5" or opcion == "cursos unicos" or opcion == "cursosunicos":
        cursos = set()
        for datos in estudiantes.values():
            cursos.add(datos["materia"])
        print("Cursos únicos registrados:")
        for curso in cursos:
            print("-", curso)

    elif opcion == "salir" or opcion == "6":
        print("Hasta pronto.")
        break

    else:
        print("Intenta de nuevo.")