from entities.Prestamo import Prestamo
from datetime import datetime
from entities.Libro import Libro
from entities.Socio import Socio

class PrestamoDTO:
  def __init__(self, id: int, libro: int, socio: int, fecha_ini: datetime, 
               dias: int, fecha_fin : datetime = None) -> None:
    self.id = id
    self.libro = libro
    self.socio = socio
    self.fecha_ini = fecha_ini
    self.dias = dias
    self.fecha_fin = fecha_fin
    
  def getId(self) -> int: return self.id  
  
  def asTuple(self):
    return (self.libro, self.socio, self.fecha_ini, self.dias, self.fecha_fin)
  
  def asPrestamo(self, libro: Libro, socio: Socio):
    return Prestamo(self.id, libro, socio, self.fecha_ini, self.dias, self.fecha_fin)
  
  @classmethod
  def toDTO(cls, prestamo: Prestamo):
    return cls(prestamo.getId(), prestamo.getLibro().getId(), prestamo.getSocio().getId(), 
               prestamo.getFechaIni(), prestamo.getDias(), prestamo.getFechaFin())
    
  def getLibro(self): return self.libro
  def getSocio(self): return self.socio