
nombre = input("Escribe tu nombre: ")
nacimiento = int(input("¿Escribe tu año de nacimiento? "))
videojuegos= input("Escribe tus tres videojuegos favoritos (separados por comas): ")

perfil=[nombre]
edad= 2025-nacimiento
perfil.append(edad)

videojuegos = videojuegos.split()
perfil.extend(videojuegos)

perfil.insert(0,True)
juego_favorito = perfil.pop(3)

es_mayor_de_edad = edad >=18
nombre_largo = len (nombre) > 10
es_gamer_retro = "pacman" in perfil
print ("Perfil final:", perfil)
print("Juego favorito:", juego_favorito)
print("¿Es mayor de edad?", es_mayor_de_edad)
print("¿Tiene nombre largo?", nombre_largo)
print("¿Es gamer retro?", es_gamer_retro)
