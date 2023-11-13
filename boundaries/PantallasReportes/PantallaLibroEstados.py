import tkinter as tk
from boundaries.PantallasReportes.TemplatePantallaResultados import TemplatePantallaResultados

class PantallaLibroEstados(TemplatePantallaResultados):  
  def asignarValores(self, kwargs):
    self.dictFrecuenciaEstado = kwargs["dictFrecuenciaEstado"]
     
  def crearVentana(self):
    super().crearVentana()
    self.ventana.title("Reporte Libros Por Estado")
    
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
  
  def imprimir(self): self.gestor.imprimir(self, 0, self.dictFrecuenciaEstado)
  