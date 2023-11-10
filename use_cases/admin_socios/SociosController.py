from boundaries.PantallasSocios.PantallaSocios import PantallaSocios
from entities.Socio import Socio
from persistence.dtos.SocioDTO import SocioDTO
from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.daos.implementations.SocioDAO import SocioDAOImplSQL

class SociosController:
  def __init__(self, backToMain, dao: ISocioDAO = SocioDAOImplSQL()) -> None:
    self.pantalla = PantallaSocios(self, backToMain)
    self.dao = dao
    self.loadSocios()
    
  def loadSocios(self):
    socios = self.dao.fetchAll()
    self.pantalla.setSocios(socios)
    
  def search():
    pass