def eliminar_duplicados_orden(lista):
    resultado = []
    vistos = set()
    for elemento in lista:
        if elemento not in vistos:
            resultado.append(elemento)
            vistos.add(elemento)
    return resultado


lista = [1, 8, 9, 7, 52, 78, 37, 13, 32, 2, 3, 8, 1, 44, 2, 9, 53, 54, 52, 7, 2, 1, 37, 13, 0, 1, 2, 3]

lista_sin_duplicados = eliminar_duplicados_orden(lista)

print(lista_sin_duplicados)