from abc import ABC, abstractmethod
from entities.Socio import Socio


class ISocioDAO(ABC):
  @abstractmethod
  def create(self, socio: Socio): ...
  
  @abstractmethod
  def fetchById(self, id: int) -> Socio: ... 
  
  @abstractmethod
  def fetchAll(self) -> list: ...
  
  @abstractmethod
  def update(self, socio: Socio): ...
  
  @abstractmethod
  def delete(self, id: int): ...