from persistence.daos.interfaces.ILibroDAO import ILibroDAO
from persistence.dtos.LibroDTO import LibroDTO
from entities.Libro import Libro
from persistence.BDHelper import BDHelper
from exceptions.RegistroNoEncontrado import RegistroNoEncontradoError

class LibroDAOImplSQL(ILibroDAO):
  tableName = "Libros"
  columnas = "(titulo, precio_reposicion, id_estado)"
  updateValues = "titulo = ?, precio_reposicion = ?, id_estado = ?"
  values = "(?, ?, ?)"
  pk = "codigo_lib"
  
  def create(self, libro: Libro):
    libroDTO = LibroDTO.fromLibro(libro)
    datos = libroDTO.asTuple()
    BDHelper().create(self.tableName, self.columnas, self.values, datos)
    
  def fetchById(self, id: int) -> Libro:
    libro = BDHelper().fetchById(self.tableName, self.pk, (id,))
    if not libro: raise RegistroNoEncontradoError(f"No se encontró el libro con id {id}")
    libroDTO = LibroDTO(libro[0][0], libro[0][1], libro[0][2], libro[0][3])
    return libroDTO.asLibro()
  
  def fetchAll(self) -> list:
    librosDTO = BDHelper().fetchAll(self.tableName)
    libros = [LibroDTO(libro[0], libro[1], libro[2], libro[3]).asLibro() for libro in librosDTO]
    return libros
  
  def update(self, libro: Libro):
    self.fetchById(libro.getCodigo())
    libroDTO = LibroDTO.fromLibro(libro)
    datos = libroDTO.asTuple() + (libroDTO.getId(),)
    BDHelper().update(self.tableName, self.updateValues, self.pk, datos)
    
  def delete(self, id: int):
    self.fetchById(id)
    BDHelper().delete(self.tableName, self.pk, (id,))
  
  