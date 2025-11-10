lista_inicial = ["leche", "pan", "manzanas"]

while True:
    print("Hola, este es nuestro menú de opciones para la lista. Escribe la opcion que deseas:")
    print("Añadir")
    print("Quitar")
    print("Revisar")
    print("Salir")

    opcion = input("¿Qué opción deseas? ").lower()

    if opcion == "añadir":
        nuevoart = input("¿Qué artículo deseas añadir? ").lower()
        lista_inicial.append(nuevoart)
        print(f"'{nuevoart}' se añadió correctamente.")
        print("Lista actual:", lista_inicial)

    elif opcion == "quitar":
        quitarart = input("¿Qué artículo deseas eliminar? ").lower()
        if quitarart in lista_inicial:
            lista_inicial.remove(quitarart)
            print(f"'{quitarart}' se ha eliminado correctamente.")
        else:
            print(f"'{quitarart}' no existe en la lista.")
        print("Lista actual:", lista_inicial)

    elif opcion == "revisar":
        print("Lista de compras:", lista_inicial)

    elif opcion == "salir":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intenta otra vez.")

