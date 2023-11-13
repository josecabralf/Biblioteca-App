from persistence.daos.interfaces.IPrestamoDAO import IPrestamoDAO
from persistence.dtos.PrestamoDTO import PrestamoDTO
from entities.Prestamo import Prestamo

from persistence.daos.implementations.LibroDAO import LibroDAOImplSQL
from persistence.daos.implementations.SocioDAO import SocioDAOImplSQL

from persistence.BDHelper import BDHelper
from exceptions.RegistroNoEncontrado import RegistroNoEncontradoError


class PrestamoDAOImplSQL(IPrestamoDAO):
  tableName = "Prestamos"
  columnas = "(codigo_lib, id_socio, fecha_prest, dias_prest, fecha_fin)"
  values = "(?, ?, ?, ?, ?)"
  updateValues = "codigo_lib = ?, id_socio = ?, fecha_prest = ?, dias_prest = ?, fecha_fin = ?"
  pk = "id_prestamo"
  
  def create(self, prestamo: Prestamo):
    prestamoDTO = PrestamoDTO.toDTO(prestamo)
    datos = prestamoDTO.asTuple()
    BDHelper().create(self.tableName, self.columnas, self.values, datos)
    
  def fetchById(self, id: int) -> Prestamo:
    prestamo = BDHelper().fetchById(self.tableName, self.pk, (id,))
    if not prestamo: raise RegistroNoEncontradoError(f"No se encontró el prestamo con id {id}")
    prestamo = self.fromResultsToPrestamo(prestamo)[0]
    return prestamo
  
  def fetchAll(self) -> list:
    res = BDHelper().fetchAll(self.tableName)
    return self.fromResultsToPrestamo(res)
  
  def update(self, prestamo: Prestamo):
    self.fetchById(prestamo.getId())
    prestamoDTO = PrestamoDTO.toDTO(prestamo)
    datos = prestamoDTO.asTuple() + (prestamoDTO.getId(),)
    BDHelper().update(self.tableName, self.updateValues, self.pk, datos)
    
  def delete(self, id: int):
    self.fetchById(id)
    BDHelper().delete(self.tableName, self.pk, (id,))
    
  def fetchBySocio(self, idSocio: int) -> list:
    res = BDHelper().fetchByColumn(self.tableName, "id_socio", (idSocio,))
    return self.fromResultsToPrestamo(res)
  
  def fromResultsToPrestamo(self, res):
    prestamosDTO = [PrestamoDTO(p[0], p[1], p[2], p[3], p[4], p[5]) for p in res]
    prestamos = [p.asPrestamo(LibroDAOImplSQL().fetchById(p.getLibro()), 
                              SocioDAOImplSQL().fetchById(p.getSocio())) for p in prestamosDTO]
    return prestamos
  
  def fetchByLibro(self, idLibro: int) -> Prestamo:
    res = BDHelper().fetchByColumn(self.tableName, "codigo_lib", (idLibro,))
    return self.fromResultsToPrestamo(res)