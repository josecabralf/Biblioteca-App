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

from persistence.dtos.PrestamoDTO import PrestamoDTO
from persistence.dtos.LibroDTO import LibroDTO

class PrestamosController:
  def __init__(self, backToMain, dao: IPrestamoDAO = PrestamoDAOImplSQL(), libroDao: ILibroDAO = LibroDAOImplSQL(),
               socioDao: ISocioDAO = SocioDAOImplSQL()) -> None:
    self.pantalla = PantallaPrestamos(self, backToMain)
    self.dao = dao
    self.libroDao = libroDao
    self.socioDao = socioDao
    self.loadPrestamos()
    
  def loadPrestamos(self):
    prestamos = self.dao.fetchAll()
    prestamos = [p.asPrestamo(self.libroDao.fetchById(p.libro).asLibro(), self.socioDao.fetchById(p.socio).asSocio()) for p in prestamos]
    self.pantalla.setPrestamos([(p.getId(),) + p.asTuple() for p in prestamos])
    
  def search(self, id: int):
    if id == -1: 
      self.loadPrestamos()
      return
    try: prestamo = self.dao.fetchById(id)
    except RegistroNoEncontradoError:
      self.pantalla.setPrestamos([])
      return
    prestamo = prestamo.asPrestamo(self.libroDao.fetchById(prestamo.libro).asLibro(), 
                                   self.socioDao.fetchById(prestamo.socio).asSocio())
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
    
  def openDevolucionWindow(self):
    self.bloquearPantalla()
    PantallaRegistrarPrestamo(self)