import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from config import png_aceptar, png_cancelar, png_search
from entities.Socio import Socio


class PantallaNuevoExtravio:
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
    self.validezLibro = False
    self.ventana.mainloop() 
    
  def crearWidgets(self):
    self.widgets.append(self.crearLblPregunta())
    self.widgets.append(self.crearEntryLibro())
    self.widgets.append(self.crearBotonera())
    self.mostrarWidgets()
  
  def enableAceptar(self): self.btnAceptar.config(state=tk.NORMAL)
  
  def checkAceptar(self):
    if self.validezLibro: self.enableAceptar()
  
  def mostrarWidgets(self):
    for widget in self.widgets: widget.pack()  
    
  def validarLibro(self):
    if self.campoLibro.get() == "":
      self.mostrarError("Debe ingresar un id de libro")
      return
    try: libro = self.gestor.validarLibro(int(self.campoLibro.get()))
    except Exception as e: 
      self.mostrarError(str(e))
      return
    self.disableLibro()
    self.crearDatosLibro(libro)
    self.validezLibro = True
    self.checkAceptar()
  
  def crearEntryCantidadDias(self):
    self.frameEntryCantidadDias = tk.Frame(self.ventana, background="#4c061d")
    lblCantidadDias = tk.Label(self.frameEntryCantidadDias, text="Cantidad de dias:", background="#4c061d", foreground="white")
    lblCantidadDias.grid(row=0, column=0, padx=10, pady=10)
    self.varCantidadDias = tk.StringVar()
    self.varCantidadDias.trace_add("write", self.validateInputCantDias)
    self.campoCantidadDias = tk.Entry(self.frameEntryCantidadDias, textvariable=self.varCantidadDias)
    self.campoCantidadDias.grid(row=0, column=1, padx=10, pady=10)
    return self.frameEntryCantidadDias
    
  def crearDatosSocio(self, socio: Socio):
    lblDatosSocio = tk.Label(self.frameDatosSocio, text="Datos del Socio:", background="#4c061d", foreground="white")
    lblDatosSocio.pack(padx=10, pady=10)
    lblNombre = tk.Label(self.frameDatosSocio, text=f"Nombre: {socio[0]}", background="#4c061d", foreground="white")
    lblNombre.pack()
    lblApellido = tk.Label(self.frameDatosSocio, text=f"Apellido: {socio[1]}", background="#4c061d", foreground="white")
    lblApellido.pack()
    lblTelefono = tk.Label(self.frameDatosSocio, text=f"Telefono: {socio[2]}", background="#4c061d", foreground="white")
    lblTelefono.pack()
    lblEmail = tk.Label(self.frameDatosSocio, text=f"Email: {socio[3]}", background="#4c061d", foreground="white")
    lblEmail.pack()
    self.frameDatosSocio.pack()
  
  def crearDatosLibro(self, libro):
    lblDatosLibro = tk.Label(self.frameDatosLibro, text="Datos del Libro:", background="#4c061d", foreground="white")
    lblDatosLibro.pack(padx=10, pady=10)
    lblNombre = tk.Label(self.frameDatosLibro, text=f"Titulo: {libro[0]}", background="#4c061d", foreground="white")
    lblNombre.pack()
    lblPrecio = tk.Label(self.frameDatosLibro, text=f"Precio: {libro[1]}", background="#4c061d", foreground="white")
    lblPrecio.pack()
    lblEstado = tk.Label(self.frameDatosLibro, text=f"Estado: {libro[2]}", background="#4c061d", foreground="white")
    lblEstado.pack()
    self.frameDatosLibro.pack()
  
  def advertir(self, message: str): messagebox.showwarning("Advertencia", message)
    
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
      
  def cancelar(self):
    self.gestor.resetCamposTransaccion()
    self.ventana.destroy()
    self.gestor.desbloquearPantalla()
    
  def aceptar(self):
    self.gestor.nuevoExtravio()
    self.cancelar()
    
  def crearLblPregunta(self):
      self.frameLblPregunta = tk.Frame(self.ventana, background="#4c061d")
      lblPregunta = tk.Label(self.frameLblPregunta, text="Registrar Prestamo:", background="#4c061d", foreground="white")
      lblPregunta.pack(padx=10, pady=10)
      return self.frameLblPregunta  
  
  def crearEntryLibro(self):
    self.frameLibro = tk.Frame(self.ventana, background="#4c061d")
    self.frameEntryLibro = tk.Frame(self.frameLibro, background="#4c061d")
    lblLibro = tk.Label(self.frameEntryLibro, text="Id de Libro:", background="#4c061d", foreground="white")
    lblLibro.grid(row=0, column=0, padx=10, pady=10)
    self.varLibro = tk.StringVar()
    self.varLibro.trace_add("write", self.validateInputLibro)
    self.campoLibro = tk.Entry(self.frameEntryLibro, textvariable=self.varLibro)
    self.campoLibro.grid(row=0, column=1, padx=10, pady=10)
    self.btnValidarLibro = ttk.Button(self.frameEntryLibro, text="Aceptar", command=self.validarLibro, 
                              image=self.imgSearch, compound="left", style="Back.TButton")
    self.btnValidarLibro.grid(row=0, column=2, padx=10, pady=10)
    self.frameEntryLibro.pack()
    self.frameDatosLibro = tk.Frame(self.frameLibro, background="#4c061d")
    return self.frameLibro
    
  def validateInputLibro(self, *args):
    entrada_actual = self.varLibro.get()
    if entrada_actual.isdigit(): return True
    self.varLibro.set(self.varLibro.get()[:-1])
    return False
  
  def setEstiloBotones(self):
      self.estilo.configure("Botones.TButton", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
      self.estilo.map('Back', background=[('active','#B0B0B0')])
  
  def crearVentana(self):
    self.ventana.title("Registrar Préstamo")
    self.ventana.protocol("WM_DELETE_WINDOW", self.cancelar)
    self.ventana.resizable(False, False)
    
  def disableLibro(self):
    self.campoLibro.configure(state="disabled")
    self.btnValidarLibro.configure(state="disabled")