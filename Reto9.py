
TIPOS_ENTRADA_VALIDOS = ("Observación", "Prueba", "Error", "Mantenimiento")
ARCHIVO_LOG = "laboratorio.txt"

def registrar_entrada():
    tipo = input("Ingresa el tipo de entrada (Observación, Prueba, Error, Mantenimiento): ").strip().capitalize()
    if tipo not in TIPOS_ENTRADA_VALIDOS:
        print("Error: tipo no válido.")
        print("Tipos válidos:", TIPOS_ENTRADA_VALIDOS)
        return

    descripcion = input("Ingresa la descripción de lo que se hizo: ").strip()
    if not descripcion:
        print("Error: la descripción no puede estar vacía.")
        return

    entrada = f"TIPO: {tipo} - DESCRIPCIÓN: {descripcion}\n"

    try:
        with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
            archivo.write(entrada)
        print("Entrada registrada correctamente.")
    except Exception as e:
        print("Error al guardar la entrada:", e)

def ver_log():
    try:
        with open(ARCHIVO_LOG, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            if contenido:
                print("\n--- CUADERNO DE LABORATORIO ---")
                print(contenido)
            else:
                print("El log está vacío.")
    except FileNotFoundError:
        print("El log está vacío o no se ha creado.")
    except Exception as e:
        print("Error al leer el archivo:", e)

def main():
    while True:
        print("\nHola, este es nuestro menú de opciones:")
        print("1. registrar")
        print("2. ver_log")
        print("3. salir")

        opcion = input("Qué opción deseas? ").lower().strip()

        if opcion == "registrar" or opcion == "1":
            registrar_entrada()
        elif opcion == "ver_log" or opcion == "2" or opcion == "verlog" or opcion == "ver log":
            ver_log()
        elif opcion == "salir" or opcion == "3":
            print("Cerrando...")
            break
        else:
            print("Intenta de nuevo.")

if __name__ == "__main__":
    main()