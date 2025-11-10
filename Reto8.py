
COMPONENTES_VALIDOS = ("Motor", "Sensor", "Batería", "Chasis")
base_de_partes = {}

def registrar_parte():
    sn = input("Ingresa el número de Serie (ej. SN-1001): ").strip()
    if sn in base_de_partes:
        print("Error: ese número de serie ya está registrado.")
        return

    tipo = input("Ingresa el tipo de componente: ").strip()
    if tipo not in COMPONENTES_VALIDOS:
        print("Error: tipo de componente no válido.")
        print("Tipos válidos:", COMPONENTES_VALIDOS)
        return

    resultados = []
    for i in range(1, 4):
        entrada = input(f"Ingresa el resultado de la prueba {i} (0-100): ").strip()
        try:
            valor = float(entrada)
            if 0 <= valor <= 100:
                resultados.append(valor)
            else:
                print("Error: el valor debe estar entre 0 y 100.")
                return
        except ValueError:
            print("Error: solo se permiten números.")
            return

    base_de_partes[sn] = {
        "tipo_componente": tipo,
        "resultados_pruebas": resultados,
        "estado": "Pendiente"
    }
    print("Se registro correctamente.")


def buscar_parte():
    sn = input("Número de Serie a buscar: ").strip()
    parte = base_de_partes(sn)
    if parte:
        print(f"Tipo: {parte['tipo_componente']}")
        print(f"Resultados: {parte['resultados_pruebas']}")
        print(f"Estado: {parte['estado']}")
    else:
        print("Error: esa parte no está registrada.")


def evaluar_parte():
    sn = input("Número de Serie a evaluar: ").strip()
    parte = base_de_partes(sn)
    if parte:
        promedio = sum(parte["resultados_pruebas"]) / 3
        nuevo_estado = "Aprobado" if promedio >= 90.0 else "Rechazado"
        parte["estado"] = nuevo_estado
        print(f"Evaluación completadada.Actualizacion {nuevo_estado}")
    else:
        print("Error: esa parte no está registrada.")


def ver_inventario():
    if base_de_partes:
        for sn, datos in base_de_partes.items():
            print(f"{sn} - {datos['tipo_componente']} - {datos['estado']}")
    else:
        print("No hay partes registradas.")

def contar_componentes(lista, tipo):
    return 0 if not lista else (lista[0]["tipo_componente"] == tipo) + contar_componentes(lista[1:], tipo)

def ejecutar_conteo():
    tipo = input("Tipo a contar: ").strip()
    if tipo in COMPONENTES_VALIDOS:
        total = contar_componentes(list(base_de_partes.values()), tipo)
        print(f"Hay {total} piezas tipo '{tipo}'.")
    else:
        print("Tipo no válido.")


def main():
    while True:
        print("\nHola, este es nuestro menú de opciones:")
        print("1. registrar")
        print("2. buscar")
        print("3. evaluar")
        print("4. ver_inventario")
        print("5. conteo")
        print("6. salir")

        opcion = input("¿Qué opción deseas?: ").lower().strip().replace(" ", "_")

        if opcion == "registrar" or opcion == "1":
            registrar_parte()
        elif opcion == "buscar" or opcion == "2":
            buscar_parte()
        elif opcion == "evaluar" or opcion == "3":
            evaluar_parte()
        elif opcion == "ver_inventario" or opcion == "4" or opcion == "verinventario":
            ver_inventario()
        elif opcion == "conteo" or opcion == "5":
            ejecutar_conteo()
        elif opcion == "salir" or opcion == "6":
            print("Cerrando sistema de QC...")
            break
        else:
            print("Opción no reconocida. Intenta de nuevo.")

if __name__ == "__main__":
    main()