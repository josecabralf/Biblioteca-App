from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.dtos.SocioDTO import SocioDTO
from persistence.BDHelper import BDHelper
from persistence.RegistroNoEncontrado import RegistroNoEncontradoError

class SocioDAOImplSQL(ISocioDAO):
  tableName = "Socios"
  columnas = "(nombre, apellido, telefono, email)"
  values = "(?, ?, ?, ?)"
  updateValues = "nombre = ?, apellido = ?, telefono = ?, email = ?"
  pk = "id_socio"
  
  def create(self, socio: SocioDTO):
    datos = socio.asTuple()
    BDHelper().create(self.tableName, self.columnas, self.values, datos)
    
  def fetchById(self, id: int) -> SocioDTO:
    socio = BDHelper().fetchById(self.tableName, self.pk, (id,))
    if not socio: raise RegistroNoEncontradoError(f"No se encontró el socio con id {id}")
    return SocioDTO(socio[0][0], socio[0][1], socio[0][2], socio[0][3], socio[0][4])
  
  def fetchAll(self) -> list:
    socios = BDHelper().fetchAll(self.tableName)
    sociosDTO = []
    for socio in socios: sociosDTO.append(SocioDTO(socio[0], socio[1], socio[2], socio[3], socio[4]))
    return sociosDTO
  
  def update(self, socio: SocioDTO, id: int):
    self.fetchById(id)
    datos = socio.asTuple() + (id,)
    BDHelper().update(self.tableName, self.updateValues, self.pk, datos)
    
  def delete(self, id: int):
    self.fetchById(id)
    datos = (id,)
    BDHelper().delete(self.tableName, datos)