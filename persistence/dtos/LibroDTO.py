from entities.Libro import Libro
from entities.fabricacionPura.EstadoLibro import *

class LibroDTO:
  dictEstados = {
    1: Disponible(),
    2: Prestado(),
    3: Extraviado(),
  }
  
  def __init__(self, codigo, titulo, precio, estado) -> None:
    self.codigo : int = codigo
    self.titulo : str = titulo
    self.precio : float = precio
    self.estado : int  = estado
    
  def asTuple(self) -> tuple:
    return (self.codigo, self.titulo, self.precio, self.estado)
  
  def asLibro(self) -> Libro:
    return Libro(self.codigo, self.titulo, self.precio, self.dictEstados[self.estado])
  
  @classmethod
  def toDTO(cls, libro: Libro) -> 'LibroDTO':
    return LibroDTO(libro.codigo, libro.titulo, libro.precio, libro.estado.idEstado)