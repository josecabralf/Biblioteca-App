from abc import ABC, abstractmethod
from entities.Libro import Libro


class ILibroDAO(ABC):
  @abstractmethod
  def create(self, libro: Libro): ...
  
  @abstractmethod
  def fetchById(self, id: int) -> Libro: ... 
  
  @abstractmethod
  def fetchAll(self) -> list: ...
  
  @abstractmethod
  def update(self, libro: Libro): ...
  
  @abstractmethod
  def delete(self, id: int): ...
  
  @abstractmethod
  def fetchByTitulo(self, titulo: str) -> Libro: ...