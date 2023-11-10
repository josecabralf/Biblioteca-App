from abc import ABC, abstractmethod
from persistence.dtos.PrestamoDTO import PrestamoDTO


class IPrestamoDAO(ABC):
  @abstractmethod
  def create(self, prestamo: PrestamoDTO): ...
  
  @abstractmethod
  def fetchById(self, id: int) -> PrestamoDTO: ... 
  
  @abstractmethod
  def fetchAll(self) -> list: ...
  
  @abstractmethod
  def update(self, prestamo: PrestamoDTO): ...
  
  @abstractmethod
  def delete(self, id: int): ...