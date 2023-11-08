from entities.EstadoLibro import EstadoLibro
from entities.EstadoLibro.Disponible import Disponible


class Extraviado(EstadoLibro): 
  def esExtraviado() -> bool: True
  
  def devolver(libro): libro.setEstado(Disponible())