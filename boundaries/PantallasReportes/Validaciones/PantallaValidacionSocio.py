import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from config import png_aceptar, png_cancelar, png_search


class PantallaValidacionSocio:
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
    self.widgets.append(self.crearLblTitulo())
    self.widgets.append(self.crearEntrySocio())
    self.widgets.append(self.crearBotonera())
    self.mostrarWidgets()
  
  def enableAceptar(self): self.btnAceptar.config(state=tk.NORMAL)
  
  def mostrarWidgets(self):
    for widget in self.widgets: widget.pack()  
  
  def validarSocio(self):
    if self.campoSocio.get() == "":
      self.mostrarError("Debe ingresar un id de socio")
      return
    try: self.socio : tuple = self.gestor.validarSocio(int(self.campoSocio.get()))
    except Exception as e: 
      self.mostrarError(str(e))
      return
    self.disableSocio()
    self.crearDatosSocio()
    self.enableAceptar()
    
  def crearDatosSocio(self):
    lblDatosSocio = tk.Label(self.frameDatosSocio, text="Datos del Socio:", background="#4c061d", foreground="white")
    lblDatosSocio.pack(padx=10, pady=10)
    lblNombre = tk.Label(self.frameDatosSocio, text=f"Nombre: {self.socio[1]}", background="#4c061d", foreground="white")
    lblNombre.pack()
    lblApellido = tk.Label(self.frameDatosSocio, text=f"Apellido: {self.socio[2]}", background="#4c061d", foreground="white")
    lblApellido.pack()
    lblTelefono = tk.Label(self.frameDatosSocio, text=f"Telefono: {self.socio[3]}", background="#4c061d", foreground="white")
    lblTelefono.pack()
    lblEmail = tk.Label(self.frameDatosSocio, text=f"Email: {self.socio[4]}", background="#4c061d", foreground="white")
    lblEmail.pack()
    self.frameDatosSocio.pack()
    
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
    self.gestor.reportarPrestamoSocio(self.socio[0:3])
    
  def crearLblTitulo(self):
      self.frameLblPregunta = tk.Frame(self.ventana, background="#4c061d")
      lblPregunta = tk.Label(self.frameLblPregunta, text="Prestamos de Socio:", background="#4c061d", foreground="white")
      lblPregunta.pack(padx=10, pady=10)
      return self.frameLblPregunta  
    
  def crearEntrySocio(self):
    self.frameSocio = tk.Frame(self.ventana, background="#4c061d")
    self.frameEntrySocio = tk.Frame(self.frameSocio, background="#4c061d")
    lblSocio = tk.Label(self.frameEntrySocio, text="Id de Socio:", background="#4c061d", foreground="white")
    lblSocio.grid(row=0, column=0, padx=10, pady=10)
    self.varSocio = tk.StringVar()
    self.varSocio.trace_add("write", self.validateInputSocio)
    self.campoSocio = tk.Entry(self.frameEntrySocio, textvariable=self.varSocio)
    self.campoSocio.grid(row=0, column=1, padx=10, pady=10)
    self.btnValidarSocio = ttk.Button(self.frameEntrySocio, text="Aceptar", command=self.validarSocio, 
                              image=self.imgSearch, compound="left", style="Back.TButton")
    self.btnValidarSocio.grid(row=0, column=2, padx=10, pady=10)
    self.frameEntrySocio.pack()
    self.frameDatosSocio = tk.Frame(self.frameSocio, background="#4c061d")
    return self.frameSocio
  
  def validateInputSocio(self, *args):
    entrada_actual = self.varSocio.get()
    if entrada_actual.isdigit(): return True
    self.varSocio.set(self.varSocio.get()[:-1])
    return False
  
  def setEstiloBotones(self):
      self.estilo.configure("Botones.TButton", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
      self.estilo.map('Back', background=[('active','#B0B0B0')])
  
  def crearVentana(self):
    self.ventana.title("Validar ID de Socio")
    self.ventana.protocol("WM_DELETE_WINDOW", self.cancelar)
    self.ventana.resizable(False, False)
  
  def disableSocio(self):
    self.campoSocio.configure(state="disabled")
    self.btnValidarSocio.configure(state="disabled")