from entities.EstadoLibro import EstadoLibro

class Libro:
  def __init__(self, codigo, titulo, precio, estado) -> None:
    self._codigo : str = codigo
    self._titulo : str = titulo
    self._precio : float = precio
    self._estado : EstadoLibro = estado
  
  def __str__(self) -> str:
    return f"Libro: {self.codigo} - {self.titulo} - {self.precio} - {self.estado}"
  
  @property
  def codigo(self) -> str: return self._codigo
  @codigo.setter
  def codigo(self, codigo) -> None: self._codigo = codigo
  def get_codigo(self) -> str: return self.codigo
  def set_codigo(self, codigo) -> None: self.codigo = codigo
  
  @property
  def titulo(self) -> str: return self._titulo
  @titulo.setter
  def titulo(self, titulo) -> None: self._titulo = titulo
  def get_titulo(self) -> str: return self.titulo
  def set_titulo(self, titulo) -> None: self.titulo = titulo
  
  @property
  def precio(self) -> float: return self._precio
  @precio.setter
  def precio(self, precio) -> None: self._precio = precio
  def get_precio(self) -> float: return self.precio
  def set_precio(self, precio) -> None: self.precio = precio
  
  @property
  def estado(self) -> EstadoLibro: return self._estado
  @estado.setter
  def estado(self, estado) -> None: self._estado = estado
  def get_estado(self) -> EstadoLibro: return self.estado
  def set_estado(self, estado) -> None: self.estado = estado
  
  # COMPORTAMIENTO ASOCIADO A ESTADO
  def prestar(self): self.estado.prestar(self)
  def devolver(self): self.estado.devolver(self)
  def extraviar(self): self.estado.extraviar(self)
  
  def estaDisponible(self) -> bool: return self.estado.esDisponible()
  def estaExtraviado(self) -> bool: return self.estado.esExtraviado()
  def estaPerdido(self) -> bool: return self.estado.esPerdido()