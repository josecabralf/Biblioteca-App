from entities.fabricacionPura.Singleton import Singleton
from tkinter import ttk

class Pantalla(Singleton):
  def __init__(self) -> None:
    self.widgets_olvidados = []
    self.estilo = ttk.Style()
    self.setEstiloBotones()
    
  def setEstiloBotones(self):
    self.estilo.theme_use('xpnative')
    self.estilo.configure("Botones.TButton", font=("Helvetica", 14, "bold"), padding=10, width=20, foreground="black", bordercolor="black", borderwidth=5)
    self.estilo.map('TButton', background=[('active','#B0B0B0')])
    
  def ocultarWidgets(self):
    for widget in self.ventana.winfo_children(): 
      widget.grid_forget()
      self.widgets_olvidados.append(widget)
      
  def mostrarWidgets(self):
    for widget in self.widgets_olvidados: widget.grid()
    self.widgets_olvidados = []
    
  def destruir(self):
    for widget in self.ventana.winfo_children(): widget.destroy()
    
  def getVentana(self): return self.ventana