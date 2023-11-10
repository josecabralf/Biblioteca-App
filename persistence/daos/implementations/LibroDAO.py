from persistence.daos.interfaces.ILibroDAO import ILibroDAO
from persistence.dtos.LibroDTO import LibroDTO
from persistence.BDHelper import BDHelper
from persistence.RegistroNoEncontrado import RegistroNoEncontradoError

class LibroDAOImplSQL(ILibroDAO):
  tableName = "Libros"
  columnas = "(titulo, precio_reposicion, id_estado)"
  values = "titulo = ?, precio_reposicion = ?, id_estado = ?"
  updateValues = "(?, ?, ?)"
  pk = "codigo_lib"
  
  def create(self, libro: LibroDTO):
    datos = libro.asTuple()
    BDHelper().create(self.tableName, self.columnas, self.values, datos)
    
  def fetchById(self, id: int) -> LibroDTO:
    libro = BDHelper().fetchById(self.tableName, self.pk, (id,))
    if not libro: raise RegistroNoEncontradoError(f"No se encontró el libro con id {id}")
    return LibroDTO(libro[0][0], libro[0][1], libro[0][2], libro[0][3])
  
  def fetchAll(self) -> list:
    libros = BDHelper().fetchAll(self.tableName)
    librosDTO = []
    for libro in libros: librosDTO.append(LibroDTO(libro[0], libro[1], libro[2], libro[3]))
    return librosDTO
  
  def update(self, libro: LibroDTO, id: int):
    self.fetchById(id)
    datos = libro.asTuple() + (id,)
    BDHelper().update(self.tableName, self.updateValues, self.pk, datos)
    
  def delete(self, id: int):
    self.fetchById(id)
    BDHelper().delete(self.tableName, (id,))
  
  