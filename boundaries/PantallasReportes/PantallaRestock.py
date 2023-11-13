import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox, CENTER, RIGHT, Y, BOTH, Scrollbar
from config import png_aceptar, png_csv

class PantallaRestock:
  def __init__(self, gestor, libros, precioReposicion) -> None:
    self.ventana = tk.Toplevel()
    self.gestor = gestor
    self.ventana.configure(bg = "#4c061d")
    self.estilo = ttk.Style()
    self.estilo.theme_use('xpnative')
    self.setEstiloBotones()
    self.widgets = []
    self.crearVentana()
    self.libros: list = libros
    self.precioReposicion: float = precioReposicion
    self.crearWidgets()
    self.ventana.mainloop()
    
  def setEstiloBotones(self):
    self.estilo.configure("Botones.TButton", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
    self.estilo.map('Back', background=[('active','#B0B0B0')])   
     
  def crearVentana(self):
    self.ventana.title("Reporte Precios de Reposicion")
    self.ventana.protocol("WM_DELETE_WINDOW", self.aceptar)
    self.ventana.resizable(False, False)
    
  def crearWidgets(self):
    self.widgets.append(self.crearTitulo())
    self.widgets.append(self.crearResultados())
    self.widgets.append(self.crearBotonera())
    self.mostrarWidgets()
    
  def mostrarWidgets(self):
      for i in range(len(self.widgets)): self.widgets[i].grid(row=i, column=0, padx=10, pady=10, sticky="nsew")
   
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
    self.treeview.delete(*self.treeview.get_children())  # Limpiar la grilla
    for libro in self.libros:
        self.treeview.insert("", "end", values=libro)
    self.treeview.insert("", "end", values=("Total", "", self.precioReposicion))
  
  def crearBotonera(self):
    self.frameBotonera = tk.Frame(self.ventana, background="#4c061d")
    self.imgAceptar = PhotoImage(file=png_aceptar).subsample(15)
    self.imgPrintCSV = PhotoImage(file=png_csv).subsample(5)
    btnAceptar = ttk.Button(self.frameBotonera, text="Aceptar", command=self.aceptar, 
                            image=self.imgAceptar, compound="left", style="Back.TButton")
    btnCancelar = ttk.Button(self.frameBotonera, text="Guardar CSV", command=self.imprimir, 
                              image=self.imgPrintCSV, compound="left", style="Back.TButton")
    self.frameBotonera.columnconfigure(0, weight=1)
    self.frameBotonera.columnconfigure(1, weight=1)
    btnAceptar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    btnCancelar.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
    return self.frameBotonera
  
  def aceptar(self): self.ventana.destroy()
  
  def imprimir(self): self.gestor.imprimir(self, 1, (self.libros, self.precioReposicion))
  
  def showInfo(self, msg): messagebox.showinfo(message=msg)