from boundaries.PantallasExtravios.PantallaExtravios import PantallaExtravios
from boundaries.PantallasExtravios.PantallaEncontrarLibro import PantallaEncontrarLibro

from persistence.daos.interfaces.ILibroDAO import ILibroDAO
from persistence.daos.implementations.LibroDAO import LibroDAOImplSQL
from persistence.daos.interfaces.IPrestamoDAO import IPrestamoDAO
from persistence.daos.implementations.PrestamoDAO import PrestamoDAOImplSQL

from persistence.BDHelper import BDHelper

from entities.Libro import Libro
from entities.Prestamo import Prestamo

class ExtraviosController:
  def __init__(self, backToMain, libroDao: ILibroDAO = LibroDAOImplSQL(), 
               prestamoDao: IPrestamoDAO = PrestamoDAOImplSQL()) -> None:
    self.pantalla = PantallaExtravios(self, backToMain)
    BDHelper().suscribir(self.pantalla)
    self.libroDao = libroDao
    self.prestamoDao = prestamoDao
    self.libroEncontrado: Libro = None
    self.loadLibros()
    
  def loadLibros(self):
    self.librosExtraviados = dict()
    for l in self.libroDao.fetchAll(): 
      if l.estaExtraviado(): 
        self.librosExtraviados[l.getCodigo()] = l
    self.pantalla.setLibros([(l.getCodigo(),)+l.asTuple() for l in self.librosExtraviados.values()])
  
  def desbloquearPantalla(self): 
    self.pantalla.desbloquear()
    self.libroEncontrado = None
  def bloquearPantalla(self): self.pantalla.bloquear()
  
  def search(self, id: int):
    if id == -1: 
      self.loadLibros()
      return
    try: libro = self.librosExtraviados[id]
    except:
      self.pantalla.setLibros([])
      return
    self.pantalla.setLibros([(libro.getCodigo(),) + libro.asTuple()])
    
  def desuscribir(self, observer): BDHelper().desuscribir(observer)
  
  def volver(self):
    self.desuscribir(self.pantalla)
    self.pantalla.destruir()
    self.pantalla.volver()
  
  def buscarNuevosExtravios(self): 
    prestamos = [p for p in self.prestamoDao.fetchAll() if p.tieneLibroExtraviado()]
    if prestamos == []: 
      self.pantalla.showInfo("No hay nuevos libros extraviados")
      return
    for p in prestamos: 
      l: Libro = p.getLibro()
      l.extraviar()
      self.libroDao.update(l)
    self.pantalla.showInfo(f"Hay {len(prestamos)} libros extraviados nuevos")
  
  def aparecioLibro(self):
    self.libroEncontrado.aparecer()
    self.libroDao.update(self.libroEncontrado)
    self.pantalla.showInfo("Registrado Libro Encontrado")
    self.libroEncontrado = None
    self.loadLibros()
  
  def openEncontrarWindow(self, libro):
    self.bloquearPantalla()
    self.libroEncontrado = self.librosExtraviados[int(libro[0])]
    PantallaEncontrarLibro(self, libro[1:])