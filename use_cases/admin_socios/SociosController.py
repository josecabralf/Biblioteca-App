from boundaries.PantallasSocios.PantallaSocios import PantallaSocios
from boundaries.PantallasSocios.PantallaCamposSocio import PantallaCamposSocio
from persistence.RegistroNoEncontrado import RegistroNoEncontradoError
from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.daos.implementations.SocioDAO import SocioDAOImplSQL
from persistence.BDHelper import BDHelper
from persistence.dtos.SocioDTO import SocioDTO
from entities.Socio import Socio

class SociosController:
  def __init__(self, backToMain, dao: ISocioDAO = SocioDAOImplSQL()) -> None:
    self.pantalla = PantallaSocios(self, backToMain)
    BDHelper().suscribir(self.pantalla)
    self.dao = dao
    self.loadSocios()
    
  def loadSocios(self):
    socios = self.dao.fetchAll()
    self.pantalla.setSocios([s.asSocio() for s in socios])
    
  def search(self, id: int):
    if id == -1: 
      self.loadSocios()
      return
    try: socio = self.dao.fetchById(id)
    except RegistroNoEncontradoError:
      self.pantalla.setSocios([])
      return
    self.pantalla.setSocios([socio.asSocio()])
    
  def desuscribir(self, observer): BDHelper().desuscribir(observer)
  
  def desbloquearPantalla(self): 
    self.pantalla.desbloquear()
    self.idSocio = None
  def bloquearPantalla(self): self.pantalla.bloquear()
  
  def create(self, socio: Socio):
    socioDTO = SocioDTO.fromSocio(socio)
    self.dao.create(socioDTO)
  
  def update(self, socio: Socio):
    socioDTO = SocioDTO.fromSocio(socio)
    socioDTO._id = self.idSocio
    self.dao.update(socioDTO)
    self.idSocio = None
    
  def delete(self):
    self.dao.delete(self.idSocio)
    self.idSocio = None
    
  def openCreateWindow(self):
    self.bloquearPantalla()
    PantallaCamposSocio(self, None, "C")
    
  def openReadWindow(self, data: tuple):
    self.bloquearPantalla()
    PantallaCamposSocio(self, data[1:], "R")
  
  def openUpdateWindow(self, data: tuple):
    self.bloquearPantalla()
    self.idSocio = data[0]
    PantallaCamposSocio(self, data[1:], "U")
    
  def openDeleteWindow(self, data: tuple):
    self.bloquearPantalla()
    self.idSocio = data[0]
    PantallaCamposSocio(self, data[1:], "D")