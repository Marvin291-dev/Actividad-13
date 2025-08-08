class Repartidor:
    def __init__(self, Nombre, Paquete, Zona):
        self.Nombre = Nombre
        self.Paquete = Paquete
        self.Zona = Zona

    def __str__(self):
        return (f"{self.Nombre} - {self.Paquetes} paquetes - Zona: {self.Zona}")

class Mensajeria:
    def __init__(self):
        self.Repartidors = []

    def AgregarRepartidor(self, Repartidor):
        for i in self.Repartidors:
            if i.Nombre.lower() == Repartidor.Nombre.lower():
                print(f"Ya existe este repartidor {Repartidor.Nombre}")
                return
            self.Repartidors.append(Repartidor)
            print("Repartidor agregado correctamente")