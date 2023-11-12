from boundaries.PantallasReportes.PantallaReportes import PantallaReportes

from persistence.daos.interfaces.IPrestamoDAO import IPrestamoDAO
from persistence.daos.implementations.PrestamoDAO import PrestamoDAOImplSQL
from persistence.daos.interfaces.ILibroDAO import ILibroDAO
from persistence.daos.implementations.LibroDAO import LibroDAOImplSQL
from persistence.daos.interfaces.ISocioDAO import ISocioDAO
from persistence.daos.implementations.SocioDAO import SocioDAOImplSQL

class ReportesController:
  def __init__(self, backToMain, prestamoDao: IPrestamoDAO = PrestamoDAOImplSQL(),
               libroDao: ILibroDAO = LibroDAOImplSQL(), socioDao: ISocioDAO = SocioDAOImplSQL()) -> None:
    self.pantalla = PantallaReportes(self, backToMain)
    self.prestamoDao = prestamoDao
    self.libroDao = libroDao
    self.socioDao = socioDao
    
  def reportarLibrosEstado(self):
    libros = self.libroDao.fetchAll()
    dictEstados = {
      "Disponible": 0,
      "Prestado": 0,
      "Extraviado": 0}
    for l in libros: dictEstados[str(l.getEstado())] += 1
    self.crearPantallaLibrosEstado("Libros por Estado", dictEstados)
  
  def reportarRestock(self): pass
  
  def reportarSolicitantesLibro(self): pass
  
  def reportarPrestamoSocio(self): pass
  
  def reportarDemorados(self): pass
  
  def volver(self):
    self.pantalla.destruir()
    self.pantalla.volver()
    
  def desbloquearPantalla(self): self.pantalla.desbloquear()
  def bloquearPantalla(self): self.pantalla.bloquear()