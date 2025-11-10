
class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = 0
        self._encendido = False  

    def arrancar(self):
        if not self._encendido:
            self._encendido = True
            print(f"El {self.marca} {self.modelo} ha arrancado.")
        else:
            print("El vehículo ya estaba en marcha.")

    def apagar(self):
        if self._encendido:
            self._encendido = False
            print(f"El {self.marca} {self.modelo} se ha apagado.")

    def get_kilometraje(self):
        return self.kilometraje

    def mostrar_info_base(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")


class Coche(Vehiculo):
    def __init__(self, marca, modelo, anio, num_puertas):
        super().__init__(marca, modelo, anio)
        self.num_puertas = num_puertas

    def conducir(self, km):
        if self._encendido:
            self.kilometraje += km
            print(f"Conduciendo {km} km...")
        else:
            print("Error: El coche debe estar arrancado para conducir.")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, anio, capacidad_carga_kg):
        super().__init__(marca, modelo, anio)
        self.capacidad_carga_kg = capacidad_carga_kg
        self.__carga_actual_kg = 0  

    def cargar(self, kilos):
        if self.__carga_actual_kg + kilos <= self.capacidad_carga_kg:
            self.__carga_actual_kg += kilos
            print("Carga exitosa.")
        else:
            print("Error: Sobrecarga.")

    def descargar(self, kilos):
        if kilos <= self.__carga_actual_kg:
            self.__carga_actual_kg -= kilos
            print(f"Descargados {kilos} kg.")
        else:
            print("Error: No hay suficiente carga para descargar.")

    def get_carga_actual(self):
        return self.__carga_actual_kg


mi_coche = Coche("Toyota", "V", 2022, 4)
mi_camion = Camion("Volvo", "FH", 2020, 5000)

mi_coche.conducir(50)  
mi_coche.arrancar()
mi_coche.conducir(100)
mi_coche.apagar()
print("Kilometraje del coche:", mi_coche.get_kilometraje())


mi_camion.cargar(3000)
mi_camion.cargar(3000)  
mi_camion.descargar(1000)
print("Carga actual del camión:", mi_camion.get_carga_actual())