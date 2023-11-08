import sqlite3
from config import path_bd
from entities.fabricacionPura.Singleton import Singleton

class BDHelper(Singleton):
  _base_datos = path_bd
    
  def __init__(self):
    self.conexion = sqlite3.connect(self._base_datos)
    self.cursor = self.conexion.cursor()