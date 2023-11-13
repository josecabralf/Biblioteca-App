import tkinter as tk
from tkinter import ttk, CENTER, RIGHT, Y, BOTH, Scrollbar
from boundaries.PantallasReportes.TemplatePantallaResultados import TemplatePantallaResultados

class PantallaPrestamosSocio(TemplatePantallaResultados):
  def asignarValores(self, kwargs):
    self.socio = kwargs["socio"]
    self.prestamos: list = kwargs["prestamos"]
     
  def crearVentana(self):
    super().crearVentana()
    self.ventana.title("Reporte Prestamos de Socio")
   
  def crearTitulo(self):
    self.frameTitulo = tk.Frame(self.ventana, background="#4c061d")
    lblTitulo = tk.Label(self.frameTitulo, text=f"Prestamos de {self.socio[1]} {self.socio[2]}", 
                         background="#4c061d", foreground="white", font=("Helvetica", 14, "bold"))
    lblTitulo.pack()
    return self.frameTitulo
  
  def crearResultados(self):
    self.frameResultados = tk.Frame(self.ventana, background="#4c061d")
    columns = ("ID", "Libro", "Fecha Inicio", "Días", "Fecha Fin")
    self.treeview = ttk.Treeview(self.frameResultados, columns=columns, show="headings", selectmode="browse")
    
    column_widths = {"ID": 50, "Libro": 300,
                       "Fecha Inicio": 150, "Días": 50, "Fecha Fin": 150}
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
    for p in self.prestamos: self.treeview.insert("", "end", values=p)
  
  def imprimir(self): self.gestor.imprimir(self, 3, (self.socio[0], self.prestamos))