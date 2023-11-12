from datetime import datetime

from boundaries.PantallasExtravios.PantallaExtravios import PantallaExtravios
from boundaries.PantallasExtravios.PantallaEncontrarLibro import PantallaEncontrarLibro
from boundaries.PantallasExtravios.PantallaNuevoExtravio import PantallaNuevoExtravio

from persistence.daos.interfaces.ILibroDAO import ILibroDAO
from persistence.daos.implementations.LibroDAO import LibroDAOImplSQL
from persistence.daos.interfaces.IPrestamoDAO import IPrestamoDAO
from persistence.daos.implementations.PrestamoDAO import PrestamoDAOImplSQL

from persistence.BDHelper import BDHelper

from exceptions.LibroNoDisponible import LibroNoDisponible

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
    self.libroExtraviado: Libro = None
    self.loadLibros()
    
  def loadLibros(self):
    self.librosExtraviados = dict()
    for l in self.libroDao.fetchAll(): 
      if l.estaExtraviado(): 
        self.librosExtraviados[l.getCodigo()] = l
    self.pantalla.setLibros([(l.getCodigo(),)+l.asTuple() for l in self.librosExtraviados.values()])
  
  def desbloquearPantalla(self): 
    self.pantalla.desbloquear()
    self.resetCamposTransaccion()
    
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
    prestamosLibro: Prestamo = [
      p for p in self.prestamoDao.fetchByLibro(self.libroEncontrado.getCodigo()) if p.estaVigente()]
    for p in prestamosLibro:
      p.setFechaFin(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
      self.prestamoDao.update(p)
    self.libroDao.update(self.libroEncontrado)
    self.pantalla.showInfo("Registrado Libro Encontrado")
    self.libroEncontrado = None
    self.loadLibros()
    
  def nuevoExtravio(self):
    self.libroExtraviado.extraviar()
    self.libroDao.update(self.libroExtraviado)
    self.pantalla.showInfo("Registrado Nuevo Extravio")
    
  def registrarNuevoExtravio(self):
    self.pantalla.showInfo("Registrado Nuevo Extravio")
    self.loadLibros()
    
  def validarLibro(self, idLibro: int):
    self.libroExtraviado = self.libroDao.fetchById(idLibro)
    return self.libroExtraviado.asTuple()
  
  def openEncontrarWindow(self, libro):
    self.bloquearPantalla()
    self.libroEncontrado = self.librosExtraviados[int(libro[0])]
    PantallaEncontrarLibro(self, libro[1:])
    
  def openNuevoExtravioWindow(self):
    self.bloquearPantalla()
    PantallaNuevoExtravio(self)
    
  def resetCamposTransaccion(self):
    self.libroEncontrado = None
    self.libroExtraviado = None