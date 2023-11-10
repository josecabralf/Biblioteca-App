from entities.Socio import Socio

class SocioDTO:
  def __init__(self, id: int, nombre: str, apellido: str, telefono: str, email: str) -> None:
    self._id = id
    self._nombre = nombre
    self._apellido = apellido
    self._telefono = telefono
    self._email = email
  
  def getId(self) -> int: return self._id
  
  def asTuple(self) -> tuple:
    return (self._nombre, self._apellido, self._telefono, self._email)
  
  def asSocio(self) -> Socio:
    return Socio(self._id, self._nombre, self._apellido, self._telefono, self._email)
  
  @classmethod
  def toDTO(cls, socio: Socio) -> 'SocioDTO':
    return SocioDTO(socio.id, socio.nombre, socio.apellido, socio.telefono, socio.email)