from boundaries.PantallasPrestamos.PantallaPrestamos import PantallaPrestamos
from boundaries.PantallasPrestamos.PantallaRegistrarDevolucion import PantallaRegistrarDevolucion
from boundaries.PantallasPrestamos.PantallaRegistrarPrestamo import PantallaRegistrarPrestamo
from persistence.RegistroNoEncontrado import RegistroNoEncontradoError

from persistence.daos.interfaces.IPrestamoDAO import IPrestamoDAO
from persistence.daos.implementations.PrestamoDAO import PrestamoDAOImplSQL
from persistence.daos.interfaces.ILibroDAO import ILibroDAO
from persistence.daos.implementations.LibroDAO import LibroDAOImplSQL
from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.daos.implementations.SocioDAO import SocioDAOImplSQL

from persistence.BDHelper import BDHelper
from persistence.dtos.PrestamoDTO import PrestamoDTO
from persistence.dtos.LibroDTO import LibroDTO

class PrestamosController:
  def __init__(self, backToMain, dao: IPrestamoDAO = PrestamoDAOImplSQL(), libroDao: ILibroDAO = LibroDAOImplSQL(),
               socioDao: ISocioDAO = SocioDAOImplSQL()) -> None:
    self.pantalla = PantallaPrestamos(self, backToMain)
    BDHelper().suscribir(self.pantalla)
    self.dao = dao
    self.libroDao = libroDao
    self.socioDao = socioDao
    self.loadPrestamos()
  
  def desuscribir(self, observer): BDHelper().desuscribir(observer)
  
  def volver(self): 
    self.desuscribir(self.pantalla)
    self.pantalla.destruir()
    self.pantalla.volver()
  
  def loadPrestamos(self, vigentes : bool = False):
    self.prestamos = dict()
    for p in self.dao.fetchAll(): self.prestamos[p.getId()] = p
    if not vigentes: aCargar = self.prestamos.values()
    else: aCargar = [p for p in self.prestamos.values() if p.estaVigente()]
    self.pantalla.setPrestamos([(p.getId(),) + p.asTuple() for p in aCargar])
    
  def search(self, id: int, vigentes : bool = False):
    if id == -1: 
      self.loadPrestamos(vigentes)
      return
    try: prestamo = self.dao.fetchById(id)
    except RegistroNoEncontradoError:
      self.pantalla.setPrestamos([])
      return
    if vigentes and not prestamo.estaVigente(): 
        self.pantalla.setPrestamos([])
        return
    self.pantalla.setPrestamos([(prestamo.getId(),) + prestamo.asTuple()])
  
  def desbloquearPantalla(self): 
    self.pantalla.desbloquear()
    self.idSocio = None
  def bloquearPantalla(self): self.pantalla.bloquear()
  
  def devolver(self, id: int, prestamo: PrestamoDTO):
    prestamo.id = id
    libro = self.libroDao.fetchById(prestamo.libro).asLibro()
    libro.devolver()
    self.libroDao.update(LibroDTO.fromLibro(libro))
    self.dao.update(prestamo)
  
  def openPrestamoWindow(self):
    self.bloquearPantalla()
    PantallaRegistrarDevolucion(self)
    
  def openDevolucionWindow(self, data: tuple):
    self.bloquearPantalla()
    self.idPrestamo = data[0]
    PantallaRegistrarPrestamo(self, data[1:])