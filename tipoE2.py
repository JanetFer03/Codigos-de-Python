
def contar_palabras(texto, claves, archivo_salida):
    for signo in ".,;:¡!`^[]{}¿?\"'()-\n":
        texto = texto.replace(signo, " ")
    texto = texto.lower()
    lista = texto.split()

    resultado = {}
    for clave in claves:
        resultado[clave.lower()] = lista.count(clave.lower())

    with open(archivo_salida, "w", encoding="utf-8") as archivo:
        for palabra, veces in resultado.items():
            archivo.write(f"{palabra}: {veces}\n")

    return resultado
texto = """
Crimen y castigo. Dostoievski. Estas palabras pasaron fugazmente por un
rincón de mi cerebro, causándome un sobresalto. ¿No sería que Dostoievski
había colocado juntas estas palabras no como sinónimos sino como antónimos?
Crimen y castigo, dos palabras absolutamente incompatibles, tan diferentes como el hielo y el carbón. Me
pareció comprender el lago turbio y pestilente, el fondo del caos de
Dostoievski, que había pensado en crimen y castigo como antónimos. Estos
pensamientos cruzaron mi mente como caballos al galope.
—¡Eh! ¡Tremendas habas! ¡Ven!
La voz y el color de Horiki habían cambiado. No hacía ni un momento que
se había levantado tambaleante a más no poder y ya estaba aquí de nuevo.
—¿Qué diablos quieres?
Con una extraña sensación, ambos bajamos del tejado al primer piso, y ya
nos disponíamos a bajar a la planta baja cuando Horiki se detuvo de repente.
—¡Mira! —dijo en voz baja, señalando algo con el dedo.
La pequeña ventana de mi habitación estaba abierta, y desde el lugar en el que
estábamos se divisaba el interior, donde la luz encendida permitía ver dos animales.
—Así son los seres humanos. No hay nada de qué extrañarse —susurré
con la cabeza dándome vueltas y la respiración agitada. Olvidándome de lo
que le estaba aconteciendo a Yoshiko, me quedé inmóvil, de pie, en la escalera.
Horiki se aclaró ruidosamente la garganta. Subí de nuevo al tejado,
corriendo como si huyera de alguien, y me dejé caer al suelo. Levantando la
vista al cielo oscuro, cubierto de nubes de lluvia, no sentí ira ni repugnancia, ni
tampoco tristeza; sólo un miedo horrible. No era el temor que podrían
inspirar los fantasmas de un cementerio sino más bien el de encontrarse con un
dios vestido de blanco en el bosque de cipreses de un santuario sintoísta; uno de
los terribles miedos ancestrales que no pueden describirse con pocas palabras.
A partir de esa noche, me salieron las primeras canas prematuras. Perdí por
completo la seguridad en mí mismo, aumentaron mis sospechas hacia el ser
humano hasta profundidades inconmensurables, y se destruyeron todas las esperanzas, toda la alegría y
toda la simpatía hacia las personas para siempre jamás. De hecho, lo acontecido
aquella noche fue decisivo en mi vida. Se me había abierto un tajo entre las
cejas, y, a partir de entonces, esta herida me dolía cada vez que tenía que tratar
con un ser humano.
"""


claves = ["Dostoievski", "sinónimos", "Horiki", "humanos", "miedo", "palabras"]

archivo = "conteo_palabras.txt"

conteo = contar_palabras(texto, claves, archivo)

print("Conteo realizado:")
for palabra, veces in conteo.items():
    print(f"{palabra}: {veces}")