from entities.fabricacionPura.EstadoLibro import EstadoLibro

class Libro:
  def __init__(self, codigo, titulo, precio, estado) -> None:
    self._codigo : int = codigo
    self._titulo : str = titulo
    self._precio : float = precio
    self._estado : EstadoLibro = estado
  
  def __str__(self) -> str:
    return f"Libro: {self.codigo} - {self.titulo} - {self.precio} - {self.estado}"
  
  # PROPERTIES
  @property
  def codigo(self) -> int: return self._codigo
  @codigo.setter
  def codigo(self, codigo: int) -> None: self._codigo = codigo
  
  @property
  def titulo(self) -> str: return self._titulo
  @titulo.setter
  def titulo(self, titulo: str) -> None: self._titulo = titulo
  
  @property
  def precio(self) -> float: return self._precio
  @precio.setter
  def precio(self, precio: float) -> None: self._precio = precio
  
  @property
  def estado(self) -> EstadoLibro: return self._estado
  @estado.setter
  def estado(self, estado: EstadoLibro) -> None: self._estado = estado
  
  # GETTERS Y SETTERS
  def getCodigo(self) -> int: return self.codigo
  def setCodigo(self, codigo: int) -> None: self.codigo = codigo
  
  def getTitulo(self) -> str: return self.titulo
  def setTitulo(self, titulo: str) -> None: self.titulo = titulo
  
  def getPrecio(self) -> float: return self.precio
  def setPrecio(self, precio: float) -> None: self.precio = precio
  
  def getEstado(self) -> EstadoLibro: return self.estado
  def setEstado(self, estado: EstadoLibro) -> None: self.estado = estado
  
  # COMPORTAMIENTO ASOCIADO A ESTADO
  def prestar(self): self.estado.prestar(self)
  def devolver(self): self.estado.devolver(self)
  def extraviar(self): self.estado.extraviar(self)
  
  def estaDisponible(self) -> bool: return self.estado.esDisponible()
  def estaExtraviado(self) -> bool: return self.estado.esExtraviado()
  def estaPerdido(self) -> bool: return self.estado.esPerdido()