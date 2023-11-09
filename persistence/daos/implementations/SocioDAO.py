from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.dtos.SocioDTO import SocioDTO
from persistence.BDHelper import BDHelper
from persistence.RegistroNoEncontrado import RegistroNoEncontradoError

class SocioDAOImplSQL(ISocioDAO):
  tableName = "Socios"
  columnas = "(nombre, apellido, telefono, email)"
  values = "(?, ?, ?, ?)"
  update = "nombre = ?, apellido = ?, telefono = ?, email = ?"
  pk = "id_socio"
  
  def crearSocio(self, socio: SocioDTO):
    datos = socio.asTuple()[1:]
    BDHelper().crearRegistro(self.tableName, self.columnas, self.values, datos)
    
  def buscarSocio(self, id: int) -> SocioDTO:
    socio = BDHelper().fetchById(self.tableName, self.pk, (id,))
    if not socio: raise RegistroNoEncontradoError(f"No se encontró el socio con id {id}")
    return SocioDTO(socio[0][0], socio[0][1], socio[0][2], socio[0][3], socio[0][4])
  
  def buscarSocios(self) -> list:
    socios = BDHelper().fetchAll(self.tableName)
    sociosDTO = []
    for socio in socios: sociosDTO.append(SocioDTO(socio[0], socio[1], socio[2], socio[3], socio[4]))
    return sociosDTO
  
  def actualizarSocio(self, socio: SocioDTO):
    datos = socio.asTuple()[1:] + (socio.getId(),)
    BDHelper().actualizarRegistro(self.tableName, self.update, self.pk, datos)
    
  def eliminarSocio(self, id: int):
    datos = (id,)
    BDHelper().eliminarRegistro(self.tableName, datos)