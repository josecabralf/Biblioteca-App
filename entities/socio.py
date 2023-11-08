class Socio:
  def __init__(self, id: str, nombre: str, apellido: str, telefono: str, email: str) -> None:
    self._id = id
    self._nombre = nombre
    self._apellido = apellido
    self._telefono = telefono
    self._email = email
    self._prestamos = []
  
  def __str__(self) -> str:
    return f"Socio: {self.id} - {self.nombre} - {self.apellido} - {self.telefono} - {self.email}"
  
  # PROPERTIES
  @property
  def id(self) -> str: return self._id
  @id.setter
  def id(self, id: str) -> None: self._id = id
  
  @property
  def nombre(self) -> str: return self._nombre
  @nombre.setter
  def nombre(self, nombre: str) -> None: self._nombre = nombre
  
  @property
  def apellido(self) -> str: return self._apellido
  @apellido.setter
  def apellido(self, apellido: str) -> None: self._apellido = apellido
  
  @property
  def telefono(self) -> str: return self._telefono
  @telefono.setter
  def telefono(self, telefono: str) -> None: self._telefono = telefono
  
  @property
  def email(self) -> str: return self._email
  @email.setter
  def email(self, email: str) -> None: self._email = email
  
  @property
  def prestamos(self) -> list: return self._prestamos
  @prestamos.setter
  def prestamos(self, prestamos: list) -> None: self._prestamos = prestamos
  
  # GETTERS Y SETTERS
  def getId(self) -> str: return self.id
  def setId(self, id: str) -> None: self.id = id
  
  def getNombre(self) -> str: return self.nombre
  def setNombre(self, nombre: str) -> None: self.nombre = nombre
  
  def getApellido(self) -> str: return self.apellido
  def setApellido(self, apellido: str) -> None: self.apellido = apellido
  
  def getTelefono(self) -> str: return self.telefono
  def setTelefono(self, telefono: str) -> None: self.telefono = telefono
  
  def getEmail(self) -> str: return self.email
  def setEmail(self, email: str) -> None: self.email = email
  
  def getPrestamos(self) -> list: return self.prestamos
  def setPrestamos(self, prestamos: list) -> None: self.prestamos = prestamos