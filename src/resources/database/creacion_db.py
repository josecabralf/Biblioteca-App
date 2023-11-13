from config import pathDB

import sqlite3

def crearModeloDatos():
  conn = sqlite3.connect(pathDB)
  cursor = conn.cursor()

  cursor.execute('''
      CREATE TABLE Estados (
          id_estado INTEGER PRIMARY KEY,
          nombre TEXT(15) NOT NULL
      )
  ''')

  cursor.executemany('INSERT INTO Estados VALUES (?, ?)', [(1, 'Disponible'), (2, 'Prestado'), (3, 'Extraviado')])

  cursor.execute('''
      CREATE TABLE Libros (
          codigo_lib INTEGER PRIMARY KEY AUTOINCREMENT,
          titulo TEXT(50) NOT NULL,
          precio_reposicion REAL NOT NULL,
          id_estado INTEGER NOT NULL,
          FOREIGN KEY (id_estado) REFERENCES Estados(id_estado)
      )
  ''')

  cursor.execute('''
      CREATE TABLE Socios (
          id_socio INTEGER PRIMARY KEY AUTOINCREMENT,
          nombre TEXT(30) NOT NULL,
          apellido TEXT(30) NOT NULL,
          telefono TEXT(20) NOT NULL,
          email TEXT(30) NOT NULL
      )
  ''')

  cursor.execute('''
      CREATE TABLE Prestamos (
          id_prestamo INTEGER PRIMARY KEY AUTOINCREMENT,
          codigo_lib INTEGER NOT NULL,
          id_socio INTEGER NOT NULL,
          fecha_prest DATETIME NOT NULL,
          dias_prest INTEGER NOT NULL,
          fecha_fin DATETIME,
          FOREIGN KEY (codigo_lib) REFERENCES Libros(codigo_lib),
          FOREIGN KEY (id_socio) REFERENCES Socios(id_socio)
      )
  ''')

  conn.commit()
  conn.close()
  
def agregarDatosAModelo():
  conn = sqlite3.connect(pathDB)
  cursor = conn.cursor()

  cursor.executemany('INSERT INTO Libros (titulo, precio_reposicion, id_estado) VALUES (?, ?, ?)',
                    [('La Aventura del Tiempo', 29.99, 2), # 1: prestado
                      ('El Secreto de las Estrellas', 35.5, 2), #2: prestado
                      ('Viaje a lo Desconocido', 19.95, 2),
                      ('Los Mundos Perdidos', 22.0, 2),
                      ('El Misterio del Pasado', 18.75, 3),
                      ('Aventuras en la Luna', 30.99, 1),
                      ('El Camino de los Reyes', 29.99, 1)
                      ])

  cursor.executemany('INSERT INTO Socios (nombre, apellido, telefono, email) VALUES (?, ?, ?, ?)',
                    [('Luisa', 'Fernández', '555-1234', 'luisa@email.com'),
                      ('Pedro', 'Martínez', '555-5678', 'pedro@email.com'),
                      ('Santiago', 'Gutierrez', '555-6897', 'santiago@email.com')
                      ])

  cursor.executemany('INSERT INTO Prestamos (codigo_lib, id_socio, fecha_prest, dias_prest, fecha_fin) VALUES (?, ?, ?, ?, ?)',
                    [(1, 3, '2023-10-31 10:03:14', 6, None), # LIBRO NO DEVUELTO CON DEMORA
                      (2, 2, '2023-11-02 14:55:01', 6, '2023-11-8 14:18:33'), # DEVUELTO SIN DEMORA
                      #3 PRESTAMOS SIN DEVOLVER
                      (4, 1, '2023-11-8 11:45:00', 14, None),
                      (3, 1, '2023-11-10 09:30:00', 10, None), 
                      (2, 1, '2023-11-9 14:00:00', 21, None)])

  conn.commit()
  conn.close()
