from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.dtos.SocioDTO import SocioDTO
from entities.Socio import Socio
from persistence.BDHelper import BDHelper
from exceptions.RegistroNoEncontrado import RegistroNoEncontradoError

class SocioDAOImplSQL(ISocioDAO):
  tableName = "Socios"
  columnas = "(nombre, apellido, telefono, email)"
  values = "(?, ?, ?, ?)"
  updateValues = "nombre = ?, apellido = ?, telefono = ?, email = ?"
  pk = "id_socio"
  
  def create(self, socio: Socio):
    socioDTO = SocioDTO.fromSocio(socio)
    datos = socioDTO.asTuple()
    BDHelper().create(self.tableName, self.columnas, self.values, datos)
    
  def fetchById(self, id: int) -> Socio:
    socio = BDHelper().fetchById(self.tableName, self.pk, (id,))
    if not socio: raise RegistroNoEncontradoError(f"No se encontró el socio con id {id}")
    return SocioDTO(socio[0][0], socio[0][1], socio[0][2], socio[0][3], socio[0][4]).asSocio()
  
  def fetchAll(self) -> list:
    sociosDTO = BDHelper().fetchAll(self.tableName)
    socios = [SocioDTO(socio[0], socio[1], socio[2], socio[3], socio[4]).asSocio() for socio in sociosDTO]
    return socios
  
  def update(self, socio: Socio):
    self.fetchById(socio.getId())
    socioDTO = SocioDTO.fromSocio(socio)
    datos = socioDTO.asTuple() + (socioDTO.getId(),)
    BDHelper().update(self.tableName, self.updateValues, self.pk, datos)
    
  def delete(self, id: int):
    self.fetchById(id)
    BDHelper().delete(self.tableName, self.pk, (id,))