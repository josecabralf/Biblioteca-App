from datetime import datetime

from boundaries.PantallasPrestamos.PantallaPrestamos import PantallaPrestamos
from boundaries.PantallasPrestamos.PantallaRegistrarDevolucion import PantallaRegistrarDevolucion
from boundaries.PantallasPrestamos.PantallaRegistrarPrestamo import PantallaRegistrarPrestamo

from exceptions.RegistroNoEncontrado import RegistroNoEncontradoError
from exceptions.SocioConInfraccion import PrestamoConDemora, MasDeTresPrestamos
from exceptions.LibroNoDisponible import LibroNoDisponible

from persistence.daos.interfaces.IPrestamoDAO import IPrestamoDAO
from persistence.daos.implementations.PrestamoDAO import PrestamoDAOImplSQL
from persistence.daos.interfaces.ILibroDAO import ILibroDAO
from persistence.daos.implementations.LibroDAO import LibroDAOImplSQL
from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.daos.implementations.SocioDAO import SocioDAOImplSQL

from persistence.BDHelper import BDHelper

from entities.Prestamo import Prestamo

class PrestamosController:
  def __init__(self, backToMain, dao: IPrestamoDAO = PrestamoDAOImplSQL(), libroDao: ILibroDAO = LibroDAOImplSQL(),
               socioDao: ISocioDAO = SocioDAOImplSQL()) -> None:
    self.pantalla = PantallaPrestamos(self, backToMain)
    BDHelper().suscribir(self.pantalla)
    self.dao = dao
    self.libroDao = libroDao
    self.socioDao = socioDao
    self.libroPrestamo = None
    self.socioPrestamo = None
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
    self.idPrestamo = None
  def bloquearPantalla(self): self.pantalla.bloquear()
  
  def validarSocio(self, idSocio: int):
    socio = self.socioDao.fetchById(idSocio)
    socio.setPrestamos(self.dao.fetchBySocio(idSocio))
    if socio.tieneMasDeTresPrestamosVigentes(): raise MasDeTresPrestamos()
    if socio.tienePrestamoConDemora(): raise PrestamoConDemora()
    self.socioPrestamo = socio
    return self.socioPrestamo.asTuple()
  
  def validarLibro(self, idLibro: int):
    libro = self.libroDao.fetchById(idLibro)
    if not libro.estaDisponible(): raise LibroNoDisponible()
    self.libroPrestamo = libro
    return self.libroPrestamo.asTuple()
  
  def devolver(self):
    prestamo: Prestamo = self.prestamos[self.idPrestamo]
    prestamo.setFechaFin(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    libro = prestamo.getLibro()
    libro.devolver()
    self.libroDao.update(libro)
    self.dao.update(prestamo)
    self.idPrestamo = None
  
  def create(self, cantDias: int):
    prestamo = Prestamo(0, self.libroPrestamo, self.socioPrestamo, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cantDias, None)
    self.libroPrestamo.prestar()
    self.libroDao.update(self.libroPrestamo)
    self.dao.create(prestamo)
  
  def openPrestamoWindow(self):
    self.bloquearPantalla()
    self.crearPantallaRegistrarPrestamo()
    
  def crearPantallaRegistrarPrestamo(self): PantallaRegistrarPrestamo(self)
    
  def openDevolucionWindow(self, data: tuple):
    self.bloquearPantalla()
    self.idPrestamo = int(data[0])
    self.crearPantallaRegistrarDevolucion(data[1:])
    
  def crearPantallaRegistrarDevolucion(self, data: tuple): PantallaRegistrarDevolucion(self, data)
    
  def resetCamposTransaccion(self):
    self.libroPrestamo = None
    self.socioPrestamo = None