
class Componente:
    def __init__(self, numero_serie, tipo_componente, costo):
        self.numero_serie = numero_serie
        self.tipo = tipo_componente
        self.costo = costo
        self.historial_revisiones = [] 
        self.esta_activo = True         

c1 = Componente("MTR-1001", "Motor", 550.75)
c2 = Componente("SNR-2050", "Sensor", 80.20)


c1.historial_revisiones.append("2025-10-25")
c1.historial_revisiones.append("2025-11-08")

c2.esta_activo = False


print("Reporte de Componente 1:")
print("Número de serie:", c1.numero_serie)
print("Tipo:", c1.tipo)
print("Costo:", c1.costo)
print("Historial de revisiones:", c1.historial_revisiones)
print("¿Está activo?:", c1.esta_activo)

print(" Reporte de Componente 2:")
print("Número de serie:", c2.numero_serie)
print("Tipo:", c2.tipo)
print("Costo:", c2.costo)
print("Historial de revisiones:", c2.historial_revisiones)
print("¿Está activo?:", c2.esta_activo)