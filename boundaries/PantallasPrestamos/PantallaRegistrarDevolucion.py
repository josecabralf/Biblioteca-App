import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from config import png_aceptar, png_cancelar

class PantallaRegistrarDevolucion:
  campos = ["Libro", "Socio", "Fecha de Prestamo", "Días Solicitado"]
  def __init__(self, gestor, prestamo: tuple) -> None:
    self.ventana = tk.Toplevel()
    self.gestor = gestor
    self.ventana.configure(bg = "#4c061d")
    self.estilo = ttk.Style()
    self.estilo.theme_use('xpnative')
    self.setEstiloBotones()
    self.widgets = []
    self.crearVentana()
    self.crearWidgets(prestamo)
    self.ventana.mainloop()
    
  def setEstiloBotones(self):
      self.estilo.configure("Botones.TButton", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
      self.estilo.map('Back', background=[('active','#B0B0B0')])
  
  def crearVentana(self):
    self.ventana.title("Devolver Libro")
    self.ventana.protocol("WM_DELETE_WINDOW", self.cancelar)
    self.ventana.resizable(False, False)
    
  def crearWidgets(self, prestamo: tuple = None):
    self.widgets.append(self.crearLblPregunta())
    self.widgets.append(self.crearDatosPrestamo(prestamo))
    self.widgets.append(self.crearBotonera())
    self.mostrarWidgets()
    
  def mostrarWidgets(self):
        for widget in self.widgets: widget.pack()
        
  def crearLblPregunta(self):
    self.frameLblPregunta = tk.Frame(self.ventana, background="#4c061d")
    lblPregunta = tk.Label(self.frameLblPregunta, text="¿Registrar devolución de libro?", background="#4c061d", foreground="white")
    lblPregunta.pack(padx=10, pady=10)
    return self.frameLblPregunta
  
  def crearDatosPrestamo(self, prestamo: tuple = None):
    self.frameDatosPrestamo = tk.Frame(self.ventana, background="#4c061d")
    for i in range(len(self.campos)):
      label = tk.Label(self.frameDatosPrestamo, text=self.campos[i], background="#4c061d", foreground="white")
      label.grid(row=i, column=0, padx=10, pady=10)
      campo = tk.Entry(self.frameDatosPrestamo)
      campo.insert(0, prestamo[i] if prestamo else "")
      campo.grid(row=i, column=1, padx=10, pady=10)
      campo.config(state=tk.DISABLED)
    return self.frameDatosPrestamo
  
  def crearBotonera(self):
    self.frameBotonera = tk.Frame(self.ventana, background="#4c061d")
    self.imgAceptar = PhotoImage(file=png_aceptar).subsample(25)
    self.imgCancelar = PhotoImage(file=png_cancelar).subsample(25)
    btnAceptar = ttk.Button(self.frameBotonera, text="Aceptar", command=self.aceptar, 
                            image=self.imgAceptar, compound="left", style="Back.TButton")
    btnCancelar = ttk.Button(self.frameBotonera, text="Cancelar", command=self.cancelar, 
                              image=self.imgCancelar, compound="left", style="Back.TButton")
    btnAceptar.pack(side=tk.LEFT, padx=10)
    btnCancelar.pack(side=tk.LEFT, padx=10)
    return self.frameBotonera
    
  def aceptar(self):
    self.gestor.devolver()
    self.cancelar()
    
  def cancelar(self):
    self.ventana.destroy()
    self.gestor.desbloquearPantalla()