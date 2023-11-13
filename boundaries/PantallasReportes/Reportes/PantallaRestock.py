import tkinter as tk
from tkinter import ttk, CENTER, RIGHT, Y, BOTH, Scrollbar
from boundaries.PantallasReportes.TemplatePantallaResultados import TemplatePantallaResultados


class PantallaRestock(TemplatePantallaResultados): 
  def asignarValores(self, kwargs):
    self.libros: list = kwargs["libros"]
    self.precioReposicion: float = kwargs["precioReposicion"]
     
  def crearVentana(self):
    super().crearVentana()
    self.ventana.title("Reporte Precios de Reposicion")
   
  def crearTitulo(self):
    self.frameTitulo = tk.Frame(self.ventana, background="#4c061d")
    lblTitulo = tk.Label(self.frameTitulo, text="Precios de Reposicion", background="#4c061d", 
                         foreground="white", font=("Helvetica", 14, "bold"))
    lblTitulo.pack()
    return self.frameTitulo
  
  def crearResultados(self):
    self.frameResultados = tk.Frame(self.ventana, background="#4c061d")
    columns = ("Codigo", "Titulo", "Precio")
    self.treeview = ttk.Treeview(self.frameResultados, columns=columns, show="headings", selectmode="browse")
    column_widths = {"Codigo": 50, "Titulo": 300, "Precio": 50}
    
    for col in columns:
      self.treeview.heading(col, text=col)
      width = column_widths.get(col, 100)
      self.treeview.column(col, width=width, anchor=CENTER)
      
    scrollbar = Scrollbar(self.frameResultados, orient="vertical", command=self.treeview.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    self.treeview.config(yscrollcommand=scrollbar.set)
    self.treeview.pack(fill=BOTH, expand=True)
    self.loadTable()
    return self.frameResultados
    
  def loadTable(self):
    for libro in self.libros: self.treeview.insert("", "end", values=libro)
    self.treeview.insert("", "end", values=("Total", "", self.precioReposicion))
  
  def imprimir(self): self.gestor.imprimir(self, 1, (self.libros, self.precioReposicion))