from entities.Libro import Libro
from entities.fabricacionPura.EstadoLibro import *

class LibroDTO:
  dictEstados = {
    1: Disponible(),
    2: Prestado(),
    3: Extraviado(),
  }
  
  def __init__(self, codigo, titulo, precio, estado) -> None:
    self._codigo : int = codigo
    self._titulo : str = titulo
    self._precio : float = precio
    self._estado : int  = estado
    
  def getId(self) -> int: return self._codigo  
  
  def asTuple(self) -> tuple:
    return (self._titulo, self._precio, self._estado)
  
  def asLibro(self) -> Libro:
    return Libro(self._codigo, self._titulo, self._precio, self.dictEstados[self._estado])
  
  @classmethod
  def toDTO(cls, libro: Libro) -> 'LibroDTO':
    estado = 0
    for idEstado, estadoLibro in LibroDTO.dictEstados.items():
        if estadoLibro == libro.getEstado(): estado = idEstado
    return LibroDTO(libro.codigo, libro.titulo, libro.precio, estado)
  