from entities.fabricacionPura.Singleton import Singleton
from tkinter import ttk

class Pantalla(Singleton):
  def __init__(self) -> None:
    self.estilo = ttk.Style()
    self.estilo.theme_use('xpnative')
    self.setEstiloBotones()
    
  def setEstiloBotones(self):
    self.estilo.configure("Botones.TButton", font=("Helvetica", 14, "bold"), padding=10, width=20, foreground="black", bordercolor="black", borderwidth=5)
    self.estilo.map('TButton', background=[('active','#B0B0B0')])
    self.estilo.configure("Botones.Back", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
    self.estilo.map('Back', background=[('active','#B0B0B0')])
    
  def ocultarWidgets(self): ...
      
  def mostrarWidgets(self): ...
    
  def destruir(self):
    for widget in self.widgets: widget.destroy()
    
  def getVentana(self): return self.ventana