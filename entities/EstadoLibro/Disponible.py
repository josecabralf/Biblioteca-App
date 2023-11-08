from entities.EstadoLibro import EstadoLibro

class Disponible(EstadoLibro):
  def prestar(libro): ...
  
  def esDisponible() -> bool: return True