from boundaries.PantallasReportes.PantallaReportes import PantallaReportes

from boundaries.PantallasReportes.Reportes.PantallaLibroEstados import PantallaLibroEstados
from boundaries.PantallasReportes.Reportes.PantallaRestock import PantallaRestock
from boundaries.PantallasReportes.Reportes.PantallaDemorados import PantallaDemorados
from boundaries.PantallasReportes.Reportes.PantallaSolicitantes import PantallaSolicitantes
from boundaries.PantallasReportes.Reportes.PantallaPrestamosSocio import PantallaPrestamosSocio

from boundaries.PantallasReportes.Validaciones.PantallaValidacionLibro import PantallaValidacionLibro
from boundaries.PantallasReportes.Validaciones.PantallaValidacionSocio import PantallaValidacionSocio

from persistence.daos.interfaces.IPrestamoDAO import IPrestamoDAO
from persistence.daos.implementations.PrestamoDAO import PrestamoDAOImplSQL
from persistence.daos.interfaces.ILibroDAO import ILibroDAO
from persistence.daos.implementations.LibroDAO import LibroDAOImplSQL
from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.daos.implementations.SocioDAO import SocioDAOImplSQL

from entities.fabricacionPura.ImprimirStrategy import *

class ReportesController:
  def __init__(self, backToMain, prestamoDao: IPrestamoDAO = PrestamoDAOImplSQL(),
               libroDao: ILibroDAO = LibroDAOImplSQL(), socioDao: ISocioDAO = SocioDAOImplSQL()) -> None:
    self.pantalla = PantallaReportes(self, backToMain)
    self.prestamoDao = prestamoDao
    self.libroDao = libroDao
    self.socioDao = socioDao
    
  def reportarLibrosEstado(self):
    dictFrecuenciaEstado = self.calcularCantidadLibrosPorEstado()
    self.crearPantallaLibrosEstado(dictFrecuenciaEstado)
    
  def calcularCantidadLibrosPorEstado(self):
    libros = self.libroDao.fetchAll()
    dictFrecuenciaEstado = {
      "Disponible": 0,
      "Prestado": 0,
      "Extraviado": 0}
    for l in libros: dictFrecuenciaEstado[str(l.getEstado())] += 1
    return dictFrecuenciaEstado
  
  def reportarRestock(self):
    libros = self.buscarLibrosExtraviados() #[(id, nombre, precio)]
    precioReposicionTotal = round(sum([l[2] for l in libros]), 2)
    self.crearPantallaRestock(libros, precioReposicionTotal)
  
  def buscarLibrosExtraviados(self):
    return [(l.getCodigo(),) + l.asTuple()[0:2] for l in self.libroDao.fetchAll() if l.estaExtraviado()]
  
  def openValidarLibro(self):
    self.crearPantallaValidacionLibro()
  
  def validarLibro(self, titulo):
    libro = self.libroDao.fetchByTitulo(titulo.upper())
    return (libro.getCodigo(),)+(libro.asTuple()[0],)
  
  def reportarSolicitantesLibro(self, libro: tuple): #(id, titulo)
    socios = self.buscarSolicitantesLibro(libro[0])
    self.crearPantallaSolicitantes(libro[1], socios)
    
  def buscarSolicitantesLibro(self, idLibro):
    socios = [p.getSocio() for p in self.prestamoDao.fetchAll() if p.getLibro().getCodigo() == idLibro]
    return [(s.getId(),) + s.asTuple()[0:2] for s in socios]
  
  def openValidarSocio(self):
    self.crearPantallaValidacionSocio()
    
  def validarSocio(self, id):
    socio = self.socioDao.fetchById(id)
    return (socio.getId(),) + socio.asTuple()
  
  def reportarPrestamoSocio(self, socio: tuple): 
    prestamos = self.buscarPrestamosSocio(socio[0])
    self.crearPantallaPrestamoSocio(socio, prestamos)
    
  def buscarPrestamosSocio(self, idSocio):
    prestamos = [p for p in self.prestamoDao.fetchAll() if p.getSocio().getId() == idSocio]
    return [(p.getId(),) + (p.asTuple()[0],) + p.asTuple()[2:5] for p in prestamos]
  
  def reportarDemorados(self): 
    prestamos = [(p.getId(),) + p.asTuple()[0:4] for p in self.prestamoDao.fetchAll() if p.estaDemorado()]
    self.crearPantallaDemorados(prestamos)
  
  def volver(self):
    self.pantalla.destruir()
    self.pantalla.volver()
    
  def imprimir(self, pantalla, strategy, data): 
    self.determinarStrategyImprimir(strategy).imprimir(data)
    pantalla.showInfo("Reporte generado con exito")
  
  def crearPantallaLibrosEstado(self, dictFrecuenciaEstado): 
    PantallaLibroEstados(self, dictFrecuenciaEstado = dictFrecuenciaEstado)
    
  def crearPantallaRestock(self, libros, precioReposicionTotal): 
    PantallaRestock(self, libros=libros, precioReposicion=precioReposicionTotal)
  
  def crearPantallaDemorados(self, prestamos): 
    PantallaDemorados(self, prestamos=prestamos)
    
  def crearPantallaValidacionLibro(self): 
    PantallaValidacionLibro(self)
    
  def crearPantallaSolicitantes(self, libro, socios):
    PantallaSolicitantes(self, libro=libro, solicitantes=socios)
    
  def crearPantallaValidacionSocio(self):
    PantallaValidacionSocio(self)
  
  def crearPantallaPrestamoSocio(self, socio, prestamos):
    PantallaPrestamosSocio(self, socio=socio, prestamos=prestamos)
  
  def determinarStrategyImprimir(self, strategy):
    strategies = {
      0: ImprimirLibroEstados(),
      1: ImprimirRestock(),
      2: ImprimirSolicitantesLibro(),
      3: ImprimirPrestamoSocio(),
      4: ImprimirDemorados()
    }
    return strategies[strategy]