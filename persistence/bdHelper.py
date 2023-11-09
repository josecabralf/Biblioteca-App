import sqlite3
from config import pathDB
from entities.fabricacionPura.Singleton import Singleton


class BDHelper(Singleton):
  _base_datos = pathDB
    
  def __init__(self):
    self.conexion = sqlite3.connect(self._base_datos)
    self.cursor = self.conexion.cursor()
    
  def crearRegistro(self, tableName: str, columns: str, values: str, datos: tuple):
    sql = f"INSERT INTO {tableName} {columns} VALUES {values}"
    self.cursor.execute(sql, datos)
    self.conexion.commit()
    
  def fetchById(self, tableName: str, pk: str, datos: tuple) -> list:
    sql = f"SELECT * FROM {tableName} WHERE {pk} = ?"
    self.cursor.execute(sql, datos)
    return self.cursor.fetchall()
  
  def fetchAll(self, tableName: str) -> list:
    sql = f"SELECT * FROM {tableName}"
    self.cursor.execute(sql)
    return self.cursor.fetchall()
  
  def actualizarRegistro(self, tableName: str, updateValues: str, pk:str, datos: tuple):
    sql = f"UPDATE {tableName} SET {updateValues} WHERE {pk} = ?"
    self.cursor.execute(sql, datos)
    self.conexion.commit()
    
  def eliminarRegistro(self, tableName: str, datos: tuple):
    sql = f"DELETE FROM {tableName} WHERE id = ?"
    self.cursor.execute(sql, datos)
    self.conexion.commit()