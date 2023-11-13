import sqlite3
from config import pathDB
from entities.fabricacionPura.Singleton import Singleton
from entities.fabricacionPura.Observer import IObserver, ISubject

class BDHelper(Singleton, ISubject):
  _base_datos = pathDB
  observers = []
  
  def __init__(self):
    self.conexion = sqlite3.connect(self._base_datos)
    self.cursor = self.conexion.cursor()
    
  def create(self, tableName: str, columns: str, values: str, datos: tuple):
    sql = f"INSERT INTO {tableName} {columns} VALUES {values}"
    self.cursor.execute(sql, datos)
    self.conexion.commit()
    self.notificar(f"{tableName}: registro creado exitosamente")
    
  def fetchById(self, tableName: str, pk: str, datos: tuple) -> list:
    sql = f"SELECT * FROM {tableName} WHERE {pk} = ?"
    self.cursor.execute(sql, datos)
    return self.cursor.fetchall()
  
  def fetchAll(self, tableName: str) -> list:
    sql = f"SELECT * FROM {tableName}"
    self.cursor.execute(sql)
    return self.cursor.fetchall()
  
  def update(self, tableName: str, updateValues: str, pk:str, datos: tuple):
    sql = f"UPDATE {tableName} SET {updateValues} WHERE {pk} = ?"
    self.cursor.execute(sql, datos)
    self.conexion.commit()
    self.notificar(f"{tableName}: registro actualizado exitosamente")
    
  def delete(self, tableName: str, pk: str, datos: tuple):
    sql = f"DELETE FROM {tableName} WHERE {pk} = ?"
    self.cursor.execute(sql, datos)
    self.conexion.commit()
    self.notificar(f"{tableName}: registro eliminado exitosamente")
    
  def fetchByColumn(self, tableName: str, column: str, datos: tuple) -> list:
    sql = f"SELECT * FROM {tableName} WHERE {column} = ?"
    self.cursor.execute(sql, datos)
    return self.cursor.fetchall()
    
  def suscribir(self, observer: IObserver): self.observers.append(observer)
    
  def desuscribir(self, observer: IObserver): self.observers.remove(observer)
    
  def notificar(self, message):
    for observer in self.observers: observer.actualizar(message)
