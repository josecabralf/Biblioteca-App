import tkinter as tk
from tkinter import ttk, CENTER, RIGHT, Y, BOTH, Scrollbar
from boundaries.PantallasReportes.TemplatePantallaResultados import TemplatePantallaResultados


class PantallaDemorados(TemplatePantallaResultados):
  def asignarValores(self, kwargs):
    self.prestamos: list = kwargs["prestamos"]
    
  def setEstiloBotones(self):
    self.estilo.configure("Botones.TButton", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
    self.estilo.map('Back', background=[('active','#B0B0B0')])   
     
  def crearVentana(self):
    super().crearVentana()
    self.ventana.title("Reporte Prestamos Demorados")
   
  def crearTitulo(self):
    self.frameTitulo = tk.Frame(self.ventana, background="#4c061d")
    lblTitulo = tk.Label(self.frameTitulo, text="Prestamos Demorados", background="#4c061d", 
                         foreground="white", font=("Helvetica", 14, "bold"))
    lblTitulo.pack()
    return self.frameTitulo
  
  def crearResultados(self):
    self.frameResultados = tk.Frame(self.ventana, background="#4c061d")
    columns = ("ID", "Libro", "Socio", "Fecha Inicio", "Días Solicitado")
    self.treeview = ttk.Treeview(self.frameResultados, columns=columns, show="headings", selectmode="browse")
    column_widths = {"ID": 50, "Libro": 300, "Socio": 300, "Fecha Inicio": 150, "Días Solicitado": 150}
    
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
  
  def imprimir(self): self.gestor.imprimir(self, 4, (self.prestamos,))