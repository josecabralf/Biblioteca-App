import tkinter as tk
from tkinter import ttk, CENTER, RIGHT, Y, BOTH, Scrollbar
from boundaries.PantallasReportes.TemplatePantallaResultados import TemplatePantallaResultados

class PantallaSolicitantes(TemplatePantallaResultados):
  def asignarValores(self, kwargs):
    self.libro = kwargs["libro"]
    self.solicitantes: list = kwargs["solicitantes"]
     
  def crearVentana(self):
    super().crearVentana()
    self.ventana.title("Reporte Solicitantes de Libro")
   
  def crearTitulo(self):
    self.frameTitulo = tk.Frame(self.ventana, background="#4c061d")
    lblTitulo = tk.Label(self.frameTitulo, text=f"Solicitantes de {self.libro}", background="#4c061d", 
                         foreground="white", font=("Helvetica", 14, "bold"))
    lblTitulo.pack()
    return self.frameTitulo
  
  def crearResultados(self):
    self.frameResultados = tk.Frame(self.ventana, background="#4c061d")
    columns = ("Id", "Nombre", "Apellido")
    self.treeview = ttk.Treeview(self.frameResultados, columns=columns, show="headings", selectmode="browse")
    column_widths = {"Id": 50, "Nombre": 150, "Apellido": 150}
    
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
    for socio in self.solicitantes: self.treeview.insert("", "end", values=socio)
  
  def imprimir(self): self.gestor.imprimir(self, 2, (self.libro, self.solicitantes))