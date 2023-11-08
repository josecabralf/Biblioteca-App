from entities.EstadoLibro import EstadoLibro
from entities.EstadoLibro.Prestado import Prestado


class Disponible(EstadoLibro):
  def esDisponible() -> bool: return True
  
  def prestar(libro): libro.setEstado(Prestado())