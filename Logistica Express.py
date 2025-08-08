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

    def Ordenar(self):
        def QuickSort(lista):
            if len(lista) <= 2:
                return lista
            pivote = lista[0]
            mayores = [x for x in lista[1:] if x.Paquete > pivote.Paquete]
            iguales = [x for x in lista[1:] if x.Paquete == pivote.Paquete]
            menores = [x for x in lista[1:] if x.Paquete < pivote.Paquete]

            return QuickSort(mayores) + [pivote] + iguales + QuickSort(menores)