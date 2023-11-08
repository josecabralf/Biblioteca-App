from entities.EstadoLibro import EstadoLibro
from entities.EstadoLibro.Extraviado import Extraviado
from entities.EstadoLibro.Disponible import Disponible

class Prestado(EstadoLibro):
  def esPrestado() -> bool: return True
  
  def extraviar(libro): libro.setEstado(Extraviado())
  
  def devolver(libro): libro.setEstado(Disponible())