import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from config import png_aceptar, png_csv

class PantallaLibroEstados:
  def __init__(self, gestor, dictFrecuenciaEstado) -> None:
    self.ventana = tk.Toplevel()
    self.gestor = gestor
    self.ventana.configure(bg = "#4c061d")
    self.estilo = ttk.Style()
    self.estilo.theme_use('xpnative')
    self.setEstiloBotones()
    self.widgets = []
    self.crearVentana()
    self.dictFrecuenciaEstado: dict = dictFrecuenciaEstado
    self.crearWidgets()
    self.ventana.mainloop()
    
  def setEstiloBotones(self):
    self.estilo.configure("Botones.TButton", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
    self.estilo.map('Back', background=[('active','#B0B0B0')])   
     
  def crearVentana(self):
    self.ventana.title("Reporte Libros Por Estado")
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
    lblTitulo = tk.Label(self.frameTitulo, text="Libros Por Estado", background="#4c061d", foreground="white", font=("Helvetica", 14, "bold"))
    lblTitulo.pack()
    return self.frameTitulo
  
  def crearResultados(self):
    self.frameResultados = tk.Frame(self.ventana, background="#4c061d")
    
    lblEstado = tk.Label(self.frameResultados, text="Estado", background="#4c061d", foreground="white")
    lblResultado = tk.Label(self.frameResultados, text="Cantidad", background="#4c061d", foreground="white")
    
    lblEstado.grid(row=0, column=0, padx=10, pady=10)
    lblResultado.grid(row=0, column=1, padx=10, pady=10)
    
    i = 1
    for estado, cantidad in self.dictFrecuenciaEstado.items():
      estado = tk.Label(self.frameResultados, text=estado, background="#4c061d", foreground="white")
      cantidad = tk.Label(self.frameResultados, text=cantidad, background="#4c061d", foreground="white")
      estado.grid(row=i, column=0, padx=10, pady=10)
      cantidad.grid(row=i, column=1, padx=10, pady=10)
      i += 1
    return self.frameResultados
  
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
  
  def imprimir(self): self.gestor.imprimir(self, 0, self.dictFrecuenciaEstado)
  
  def showInfo(self, msg): messagebox.showinfo(message=msg)