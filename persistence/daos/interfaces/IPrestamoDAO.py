from abc import ABC, abstractmethod
from entities.Prestamo import Prestamo


class IPrestamoDAO(ABC):
  @abstractmethod
  def create(self, prestamo: Prestamo): ...
  
  @abstractmethod
  def fetchById(self, id: int) -> Prestamo: ... 
  
  @abstractmethod
  def fetchAll(self) -> list: ...
  
  @abstractmethod
  def update(self, prestamo: Prestamo): ...
  
  @abstractmethod
  def delete(self, id: int): ...
  
  @abstractmethod
  def fetchBySocio(self, idSocio: int) -> list: ...
  
  @abstractmethod
  def fetchByLibro(self, idLibro: int) -> Prestamo: ...