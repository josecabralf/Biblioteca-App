from entities.fabricacionPura.Singleton import Singleton

class EstadoLibro(Singleton):
  #def __str__(self) -> str: return self.__class__.__name__
  
  def esDisponible() -> bool: return False
  def esExtraviado() -> bool: return False
  def esPrestado() -> bool: return False
  
  def prestar(libro): return
  def extraviar(libro): return
  def devolver(libro): return
  
  
class Disponible(EstadoLibro):
  def esDisponible() -> bool: return True
  def prestar(libro): libro.setEstado(Prestado())
  
  
class Extraviado(EstadoLibro): 
  def esExtraviado() -> bool: True
  def devolver(libro): libro.setEstado(Disponible())
  
  
class Prestado(EstadoLibro):
  def esPrestado() -> bool: return True
  def extraviar(libro): libro.setEstado(Extraviado())
  def devolver(libro): libro.setEstado(Disponible())