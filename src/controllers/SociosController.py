from boundaries.PantallasSocios.PantallaSocios import PantallaSocios
from boundaries.PantallasSocios.PantallaCamposSocio import PantallaCamposSocio

from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.daos.implementations.SocioDAO import SocioDAOImplSQL
from persistence.daos.interfaces.IPrestamoDAO import IPrestamoDAO
from persistence.daos.implementations.PrestamoDAO import PrestamoDAOImplSQL

from persistence.BDHelper import BDHelper
from persistence.dtos.SocioDTO import SocioDTO
from entities.Socio import Socio

class SociosController:
  def __init__(self, backToMain, dao: ISocioDAO = SocioDAOImplSQL(), 
               prestamoDao: IPrestamoDAO = PrestamoDAOImplSQL()) -> None:
    self.pantalla = PantallaSocios(self, backToMain)
    BDHelper().suscribir(self.pantalla)
    self.dao = dao
    self.prestamoDao = prestamoDao
    self.loadSocios()
    
  def loadSocios(self):
    self.socios = dict()
    for s in self.dao.fetchAll(): self.socios[s.getId()] = s
    self.pantalla.setSocios([(s.getId(),) + s.asTuple() for s in self.socios.values()])
    
  def search(self, id: int):
    if id == -1: 
      self.loadSocios()
      return
    try: socio = self.socios[id]
    except:
      self.pantalla.setSocios([])
      return
    self.pantalla.setSocios([(socio.getId(),) + socio.asTuple()])
    
  def desuscribir(self, observer): BDHelper().desuscribir(observer)
  
  def desbloquearPantalla(self): 
    self.pantalla.desbloquear()
    self.idSocio = None
  def bloquearPantalla(self): self.pantalla.bloquear()
  
  def volver(self):
    self.desuscribir(self.pantalla)
    self.pantalla.destruir()
    self.pantalla.volver()
  
  def create(self, socio: Socio): 
    socio.setNombre(socio.getNombre().upper())
    socio.setApellido(socio.getApellido().upper())
    self.dao.create(socio)
  
  def update(self, socio: Socio):
    socio._id = self.idSocio
    socio.setNombre(socio.getNombre().upper())
    socio.setApellido(socio.getApellido().upper())
    self.dao.update(socio)
    self.idSocio = None
    
  def delete(self):
    if self.validarSocioSinPrestamos():
      self.dao.delete(self.idSocio)
      self.idSocio = None
  
  def validarSocioSinPrestamos(self):
    prestamos = self.prestamoDao.fetchBySocio(self.idSocio)
    if prestamos:
      socio = self.socios[self.idSocio]
      socio.setPrestamos(prestamos)
      if socio.tienePrestamosVigentes():
        self.pantalla.showErrorMessage(f"No se puede eliminar socio: tiene prestamos sin devolver")
        return False
    return True
  
  def openCreateWindow(self):
    self.bloquearPantalla()
    self.crearPantallaCamposSocio(None, "C")
    
  def openReadWindow(self, data: tuple):
    self.bloquearPantalla()
    self.crearPantallaCamposSocio(data[1:], "R")
  
  def openUpdateWindow(self, data: tuple):
    self.bloquearPantalla()
    self.idSocio = int(data[0])
    self.crearPantallaCamposSocio(data[1:], "U")
    
  def openDeleteWindow(self, data: tuple):
    self.bloquearPantalla()
    self.idSocio = int(data[0])
    self.crearPantallaCamposSocio(data[1:], "D")
    
  def crearPantallaCamposSocio(self, data, operacion): PantallaCamposSocio(self, data, operacion)