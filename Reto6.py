
# INVENTARIO DE UNA ESTACIÓN ESPACIAL
inventario = ["comida", "botiquín", "herramientas", "suministros"]

while True:
    print("\nHola, este es nuestro menú de opciones")
    print("1. Añadir")
    print("2. Quitar")
    print("3. Ver")
    print("4. Inspeccionar")
    print("5. Salir")

    opcion = input("¿Qué opción deseas? ").lower().strip()

    if opcion == "añadir" or opcion == "1":
        nuevoart = input("¿Qué artículo deseas añadir? ").lower()
        inventario.append(nuevoart)
        print(f"'{nuevoart}' se añadió correctamente.")
        print("Inventario actual:", inventario)

    elif opcion == "quitar" or opcion == "2":
        quitarart = input("¿Qué artículo deseas eliminar? ").lower()
        if quitarart in inventario:
            inventario.remove(quitarart)
            print(f"'{quitarart}' se ha eliminado correctamente.")
        else:
            print(f"'{quitarart}' no existe en la lista.")
        print("Inventario actual:", inventario)

    elif opcion == "ver" or opcion == "3":
        if not inventario:
            print("El inventario está vacío.")
        else:
            print("Inventario actual:")
            for i, item in enumerate(inventario, start=1):
                print(f"{i}. {item}")

    elif opcion == "inspeccionar" or opcion == "4":
        if not inventario:
            print("No hay ítems para inspeccionar.")
        else:
            numero = input("¿Qué número de ítem quieres inspeccionar?: ")
            if numero.isdigit():
                numero = int(numero)
                if 1 <= numero <= len(inventario):
                    print(f"Ítem #{numero}: {inventario[numero - 1]}")
                else:
                    print("Número fuera de rango.")
            else:
                print("Inválido. Escribe un número.")

    elif opcion == "salir" or opcion == "5":
        print("Cerrando inventario.")
        break

    else:
        print(" Intenta de nuevo.")