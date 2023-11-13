import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from config import png_aceptar, png_cancelar, png_search


class PantallaValidacionLibro:
  def __init__(self, gestor) -> None:
    self.ventana = tk.Toplevel()
    self.gestor = gestor
    self.ventana.configure(bg = "#4c061d")
    self.estilo = ttk.Style()
    self.estilo.theme_use('xpnative')
    self.setEstiloBotones()
    self.widgets = []
    self.crearVentana()
    self.imgSearch = PhotoImage(file=png_search).subsample(25)
    self.crearWidgets()
    self.ventana.mainloop() 
    
  def crearWidgets(self):
    self.widgets.append(self.crearTitulo())
    self.widgets.append(self.crearEntryLibro())
    self.widgets.append(self.crearBotonera())
    self.mostrarWidgets()
  
  def enableAceptar(self): self.btnAceptar.config(state=tk.NORMAL)
  
  def mostrarWidgets(self):
    for widget in self.widgets: widget.pack()  
    
  def validarLibro(self):
    if self.campoLibro.get() == "":
      self.mostrarError("Debe ingresar un titulo de libro")
      return
    try: self.libro = self.gestor.validarLibro(self.campoLibro.get())
    except Exception as e: 
      self.mostrarError(str(e))
      return
    self.disableLibro()
    self.crearDatosLibro()
    self.enableAceptar()
  
  def crearDatosLibro(self):
    lblNombre = tk.Label(self.frameDatosLibro, text=f"Titulo: {self.libro[1]}", background="#4c061d", foreground="white")
    lblNombre.pack()
    self.frameDatosLibro.pack()
    
  def mostrarError(self, message: str): messagebox.showerror("Error", message)
  
  def crearBotonera(self):
        self.frameBotonera = tk.Frame(self.ventana, background="#4c061d")
        self.imgAceptar = PhotoImage(file=png_aceptar).subsample(25)
        self.imgCancelar = PhotoImage(file=png_cancelar).subsample(25)
        self.btnAceptar = ttk.Button(self.frameBotonera, text="Aceptar", command=self.aceptar, 
                                image=self.imgAceptar, compound="left", style="Back.TButton", state=tk.DISABLED)
        btnCancelar = ttk.Button(self.frameBotonera, text="Cancelar", command=self.cancelar, 
                                  image=self.imgCancelar, compound="left", style="Back.TButton")
        self.btnAceptar.pack(side=tk.LEFT, padx=10)
        btnCancelar.pack(side=tk.LEFT, padx=10)
        return self.frameBotonera
      
  def cancelar(self): self.ventana.destroy()
    
  def aceptar(self):
    self.cancelar()   
    self.gestor.reportarSolicitantesLibro(self.libro)
    
  def crearTitulo(self):
      self.frameLblPregunta = tk.Frame(self.ventana, background="#4c061d")
      lblPregunta = tk.Label(self.frameLblPregunta, text="Titulo de Libro:", background="#4c061d", foreground="white")
      lblPregunta.pack(padx=10, pady=10)
      return self.frameLblPregunta  
  
  def crearEntryLibro(self):
    self.frameLibro = tk.Frame(self.ventana, background="#4c061d")
    self.frameEntryLibro = tk.Frame(self.frameLibro, background="#4c061d")
    lblLibro = tk.Label(self.frameEntryLibro, text="Titulo:", background="#4c061d", foreground="white")
    lblLibro.grid(row=0, column=0, padx=10, pady=10)
    self.varLibro = tk.StringVar()
    self.campoLibro = tk.Entry(self.frameEntryLibro, textvariable=self.varLibro)
    self.campoLibro.grid(row=0, column=1, padx=10, pady=10)
    self.btnValidarLibro = ttk.Button(self.frameEntryLibro, command=self.validarLibro, 
                              image=self.imgSearch, compound="left", style="Back.TButton")
    self.btnValidarLibro.grid(row=0, column=2, padx=10, pady=10)
    self.frameEntryLibro.pack()
    self.frameDatosLibro = tk.Frame(self.frameLibro, background="#4c061d")
    return self.frameLibro
  
  def setEstiloBotones(self):
      self.estilo.configure("Botones.TButton", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
      self.estilo.map('Back', background=[('active','#B0B0B0')])
  
  def crearVentana(self):
    self.ventana.title("Validar Titulo Libro")
    self.ventana.protocol("WM_DELETE_WINDOW", self.cancelar)
    self.ventana.resizable(False, False)
    
  def disableLibro(self):
    self.campoLibro.configure(state="disabled")
    self.btnValidarLibro.configure(state="disabled")