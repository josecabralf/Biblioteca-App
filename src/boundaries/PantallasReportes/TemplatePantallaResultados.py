from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk, PhotoImage, messagebox
from config import png_aceptar, png_csv


class TemplatePantallaResultados(ABC):
  def __init__(self, gestor, **kwargs) -> None:
    self.ventana = tk.Toplevel()
    self.gestor = gestor
    self.ventana.configure(bg = "#4c061d")
    self.estilo = ttk.Style()
    self.estilo.theme_use('xpnative')
    self.setEstiloBotones()
    self.widgets = []
    self.crearVentana()
    self.asignarValores(kwargs)
    self.crearWidgets()
    self.ventana.mainloop()
  
  @abstractmethod
  def asignarValores(self, kwargs): ...
  
  def setEstiloBotones(self):
    self.estilo.configure("Botones.TButton", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
    self.estilo.map('Back', background=[('active','#B0B0B0')])   
     
  def crearVentana(self):
    self.ventana.protocol("WM_DELETE_WINDOW", self.aceptar)
    self.ventana.resizable(False, False)
    
  def crearWidgets(self):
    self.widgets.append(self.crearTitulo())
    self.widgets.append(self.crearResultados())
    self.widgets.append(self.crearBotonera())
    self.mostrarWidgets()
    
  def mostrarWidgets(self):
        for i in range(len(self.widgets)): 
          self.widgets[i].grid(row=i, column=0, padx=10, pady=10, sticky="nsew")
    
  @abstractmethod  
  def crearTitulo(self): ...
    
  @abstractmethod
  def crearResultados(self): ...
    
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
  
  @abstractmethod
  def imprimir(self): ...
  
  def showInfo(self, msg): messagebox.showinfo(message=msg)