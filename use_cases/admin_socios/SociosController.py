from boundaries.PantallasSocios.PantallaSocios import PantallaSocios
from persistence.RegistroNoEncontrado import RegistroNoEncontradoError
from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.daos.implementations.SocioDAO import SocioDAOImplSQL
from persistence.BDHelper import BDHelper

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