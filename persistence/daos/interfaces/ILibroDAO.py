from abc import ABC, abstractmethod
from persistence.dtos.LibroDTO import LibroDTO


class ILibroDAO(ABC):
  @abstractmethod
  def create(self, libro: LibroDTO): ...
  
  @abstractmethod
  def fetchById(self, id: int) -> LibroDTO: ... 
  
  @abstractmethod
  def fetchAll(self) -> list: ...
  
  @abstractmethod
  def update(self, libro: LibroDTO): ...
  
  @abstractmethod
  def delete(self, id: int): ...