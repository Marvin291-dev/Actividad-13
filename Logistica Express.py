class Repartidor:
    def __init__(self, Nombre, Paquete, Zona):
        self.Nombre = Nombre
        self.Paquete = Paquete
        self.Zona = Zona

    def __str__(self):
        return (f"{self.Nombre} - {self.Paquetes} paquetes - Zona: {self.Zona}")
