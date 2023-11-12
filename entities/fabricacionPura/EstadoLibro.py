from entities.fabricacionPura.Singleton import Singleton

class EstadoLibro(Singleton):
  def __str__(self) -> str: return self.__class__.__name__
  
  def esDisponible(self) -> bool: return False
  def esExtraviado(self) -> bool: return False
  def esPrestado(self) -> bool: return False
  
  def prestar(self, libro): return
  def extraviar(self, libro): return
  def devolver(self, libro): return
  def aparecer(self, libro): return
  

class Disponible(EstadoLibro):
  def esDisponible(self) -> bool: return True
  def prestar(self, libro): libro.setEstado(Prestado())
  def extraviar(self, libro): libro.setEstado(Extraviado())
  
  
class Extraviado(EstadoLibro): 
  def esExtraviado(self) -> bool: return True
  def aparecer(self, libro): libro.setEstado(Disponible())
  
  
class Prestado(EstadoLibro):
  def esPrestado(self) -> bool: return True
  def extraviar(self, libro): libro.setEstado(Extraviado())
  def devolver(self, libro): libro.setEstado(Disponible())