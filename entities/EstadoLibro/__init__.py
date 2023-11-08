from abc import abstractmethod
from entities.Singleton.Singleton import Singleton

class EstadoLibro(Singleton):
  def __str__(self) -> str: return self.__class__.__name__
  
  def esDisponible() -> bool: return False
  def esExtraviado() -> bool: return False
  def esPerdido() -> bool: return False
  
  def prestar(libro): return
  def extraviar(libro): return
  def devolver(libro): return