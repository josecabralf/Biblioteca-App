from abc import abstractmethod
from entities.fabricacionPura.Singleton import Singleton
from datetime import date
from config import path_reportes

class ImprimirStrategy(Singleton):
    dir: str = ...
    @abstractmethod
    def imprimir(self, data: tuple):pass
    
    
class ImprimirLibroEstados(ImprimirStrategy):
    dir = "libroEstados/"
    def imprimir(self, data: dict):
        with open(f"{path_reportes}{self.dir}libroEstados_{date.today()}.csv", "w") as file:
            file.write("Estado,Cantidad\n")
            for estado, cantidad in data.items():
                file.write(f"{estado},{cantidad}\n")


class ImprimirRestock(ImprimirStrategy):
    dir = "precioReposicion/"
    def imprimir(self, data: tuple):
        with open(f"{path_reportes}{self.dir}precioReposicion_{date.today()}.csv", "w") as file:
            file.write("ID,Nombre,Precio\n")
            for id, nombre, precio in data[0]:
                file.write(f"{id},{nombre},{precio}\n")
            file.write(f"Total,,{data[1]}\n")
            

class ImprimirSolicitantesLibro(ImprimirStrategy):
    def imprimir(self, data: tuple):
        with open(f"{path_reportes}{self.dir}solicitantesLibro_{date.today()}.csv", "w") as file:
            file.write("ID,Nombre,Apellido,Fecha de Prestamo,Fecha de Devolucion\n")
            for id, nombre, apellido, fechaPrestamo, fechaDevolucion in data:
                file.write(f"{id},{nombre},{apellido},{fechaPrestamo},{fechaDevolucion}\n")
     
                
class ImprimirPrestamoSocio(ImprimirStrategy):
    def imprimir(self, data: tuple):
        with open(f"{path_reportes}{self.dir}prestamoSocio_{date.today()}.csv", "w") as file:
            file.write("ID,Nombre,Apellido,Fecha de Prestamo,Fecha de Devolucion\n")
            for id, nombre, apellido, fechaPrestamo, fechaDevolucion in data:
                file.write(f"{id},{nombre},{apellido},{fechaPrestamo},{fechaDevolucion}\n")
                
                

class ImprimirDemorados(ImprimirStrategy):
    dir = "prestamosDemorados/"
    def imprimir(self, data: tuple):
        with open(f"{path_reportes}{self.dir}demorados_{date.today()}.csv", "w") as file:
            file.write("ID,Libro,Socio,Fecha Inicio,Dias Solicitado\n")
            for id, libro, socio, fechaIni, cantDias in data[0]:
                file.write(f"{id},{libro},{socio},{fechaIni},{cantDias}\n")