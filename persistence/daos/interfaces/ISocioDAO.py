from abc import ABC, abstractmethod
from persistence.dtos.SocioDTO import SocioDTO


class ISocioDAO(ABC):
  @abstractmethod
  def crearSocio(self, socio: SocioDTO): ...
  
  @abstractmethod
  def buscarSocio(self, id: int) -> SocioDTO: ... 
  
  @abstractmethod
  def buscarSocios(self) -> list: ...
  
  @abstractmethod
  def actualizarSocio(self, socio: SocioDTO): ...
  
  @abstractmethod
  def eliminarSocio(self, id: int): ...