from datetime import datetime
from entities.Libro import Libro
from entities.Socio import Socio

class Prestamo:
  def __init__(self, id: int, libro: Libro, socio: Socio, fecha_ini: str, 
               dias: int, fecha_fin : str = None) -> None:
    self._id = id
    self._libro = libro
    self._socio = socio
    self._fecha_ini = fecha_ini
    self._dias = dias
    self._fecha_fin = fecha_fin
  
  def __str__(self) -> str:
    string =  f"Prestamo: {self.id} \n{self.libro}\n{self.socio}\nDesde: {self.fecha_ini}\nDías Solicitado: {self.dias}\n"
    if not self.estaVigente(): string += f"Finalizado: {self.fecha_fin}\n"
    return string
  
  def asTuple(self):
    fecha_fin = self.fecha_fin if self.fecha_fin is not None else ""
    return (self.libro.getTitulo(), f"{self.socio.getNombre()} {self.socio.getApellido()}", 
            self.fecha_ini, self.dias, fecha_fin)
  
  # PROPERTIES
  @property
  def id(self) -> int: return self._id
  @id.setter
  def id(self, id: int) -> None: self._id = id
  
  @property
  def libro(self) -> Libro: return self._libro
  @libro.setter
  def libro(self, libro: Libro) -> None: self._libro = libro
  
  @property
  def socio(self) -> Socio: return self._socio
  @socio.setter
  def socio(self, socio: Socio) -> None: self._socio = socio
  
  @property
  def fecha_ini(self) -> str: return self._fecha_ini
  @fecha_ini.setter
  def fecha_ini(self, fecha_ini: str) -> None: self._fecha_ini = fecha_ini
  
  @property
  def dias(self) -> int: return self._dias
  @dias.setter
  def dias(self, dias: int) -> None: self._dias = dias
  
  @property
  def fecha_fin(self) -> str: return self._fecha_fin
  @fecha_fin.setter
  def fecha_fin(self, fecha_fin: str) -> None: self._fecha_fin = fecha_fin
  
  # GETTERS Y SETTERS
  def getId(self) -> int: return self.id
  def setId(self, id: int) -> None: self.id = id
  
  def getLibro(self) -> Libro: return self.libro
  def setLibro(self, libro: Libro) -> None: self.libro = libro
  
  def getSocio(self) -> Socio: return self.socio
  def setSocio(self, socio: Socio) -> None: self.socio = socio
  
  def getFechaIni(self) -> str: return self.fecha_ini
  def setFechaIni(self, fecha_ini: str) -> None: self.fecha_ini = fecha_ini
  
  def getDias(self) -> int: return self.dias
  def setDias(self, dias: int) -> None: self.dias = dias
  
  def getFechaFin(self) -> str: return self.fecha_fin
  def setFechaFin(self, fecha_fin: str) -> None: self.fecha_fin = fecha_fin
  
  # COMPORTAMIENTO
  def estaVigente(self) -> bool: return self.fecha_fin is None
  
  def estaDemorado(self) -> bool:
    if not self.estaVigente(): return False
    fecha_ini_dt = datetime.strptime(self.fecha_ini, "%Y-%m-%d %H:%M:%S")
    return (datetime.now() - fecha_ini_dt).days > self.dias

  def calcularDemora(self):
    if not self.estaVigente(): return 0
    fecha_ini_dt = datetime.strptime(self.fecha_ini, "%Y-%m-%d %H:%M:%S")
    return (datetime.now() - fecha_ini_dt).days - self.dias
  
  def tieneLibroExtraviado(self) -> bool: return (self.calcularDemora() > 30)
  
  def finalizar(self) -> None: self.fecha_fin = datetime.now()
  
  def extraviarLibro(self) -> None: self.libro.extraviar()