from abc import abstractmethod
from entities.fabricacionPura.Singleton import Singleton
from datetime import date
from config import path_reportes

class ImprimirStrategy(Singleton):
    @abstractmethod
    def imprimir(self, data: tuple):pass
    
    
class ImprimirLibroEstados(ImprimirStrategy):
    def imprimir(self, data: dict):
        with open(f"{path_reportes}libroEstados_{date.today()}.csv", "w") as file:
            file.write("Estado,Cantidad\n")
            for estado, cantidad in data.items():
                file.write(f"{estado},{cantidad}\n")


class ImprimirRestock(ImprimirStrategy):
    def imprimir(self, data: tuple):
        with open(f"{path_reportes}restock_{date.today()}.csv", "w") as file:
            file.write("ID,Nombre,Precio\n")
            for id, nombre, precio in data:
                file.write(f"{id},{nombre},{precio}\n")
                

class ImprimirSolicitantesLibro(ImprimirStrategy):
    def imprimir(self, data: tuple):
        with open(f"{path_reportes}solicitantesLibro_{date.today()}.csv", "w") as file:
            file.write("ID,Nombre,Apellido,Fecha de Prestamo,Fecha de Devolucion\n")
            for id, nombre, apellido, fechaPrestamo, fechaDevolucion in data:
                file.write(f"{id},{nombre},{apellido},{fechaPrestamo},{fechaDevolucion}\n")
     
                
class ImprimirPrestamoSocio(ImprimirStrategy):
    def imprimir(self, data: tuple):
        with open(f"{path_reportes}prestamoSocio_{date.today()}.csv", "w") as file:
            file.write("ID,Nombre,Apellido,Fecha de Prestamo,Fecha de Devolucion\n")
            for id, nombre, apellido, fechaPrestamo, fechaDevolucion in data:
                file.write(f"{id},{nombre},{apellido},{fechaPrestamo},{fechaDevolucion}\n")
                
                

class ImprimirDemorados(ImprimirStrategy):
    def imprimir(self, data: tuple):
        with open(f"{path_reportes}demorados_{date.today()}.csv", "w") as file:
            file.write("ID,Nombre,Apellido,Fecha de Prestamo,Fecha de Devolucion\n")
            for id, nombre, apellido, fechaPrestamo, fechaDevolucion in data:
                file.write(f"{id},{nombre},{apellido},{fechaPrestamo},{fechaDevolucion}\n")