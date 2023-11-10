from persistence.daos.interfaces.IPrestamoDAO import IPrestamoDAO
from persistence.dtos.PrestamoDTO import PrestamoDTO
from persistence.BDHelper import BDHelper
from persistence.RegistroNoEncontrado import RegistroNoEncontradoError


class PrestamoDAOImplSQL(IPrestamoDAO):
  tableName = "Prestamos"
  columnas = "(codigo_lib, id_socio, fecha_prest, dias_prest, fecha_fin)"
  values = "(?, ?, ?, ?, ?)"
  updateValues = "codigo_lib = ?, id_socio = ?, fecha_prest = ?, dias_prest = ?, fecha_fin = ?"
  pk = "id_prestamo"
  
  def create(self, prestamo: PrestamoDTO):
    datos = prestamo.asTuple()
    BDHelper().create(self.tableName, self.columnas, self.values, datos)
    
  def fetchById(self, id: int) -> PrestamoDTO:
    prestamo = BDHelper().fetchById(self.tableName, self.pk, (id,))
    if not prestamo: raise RegistroNoEncontradoError(f"No se encontró el prestamo con id {id}")
    return PrestamoDTO(prestamo[0][0], prestamo[0][1], prestamo[0][2], prestamo[0][3], prestamo[0][4], prestamo[0][5])
  
  def fetchAll(self) -> list:
    prestamos = BDHelper().fetchAll(self.tableName)
    prestamosDTO = []
    for prestamo in prestamos: prestamosDTO.append(PrestamoDTO(prestamo[0], prestamo[1], prestamo[2], prestamo[3], prestamo[4], prestamo[5]))
    return prestamosDTO
  
  def update(self, prestamo: PrestamoDTO, id: int):
    self.fetchById(id)
    datos = prestamo.asTuple() + (id,)
    BDHelper().update(self.tableName, self.updateValues, self.pk, datos)
    
  def delete(self, id: int):
    self.fetchById(id)
    datos = (id,)
    BDHelper().delete(self.tableName, datos)