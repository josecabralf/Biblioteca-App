from boundaries.Pantalla import Pantalla
import tkinter as ttk

class PantallaSocio(Pantalla):
    def __init__(self, ventana, volver_a_principal):
      super().__init__()
      self.ventana = ventana
      self.volver_a_principal = volver_a_principal
      self.create_widgets()

    def create_widgets(self):
        volver_btn = ttk.Button(self.ventana, text="Volver a Principal", command=lambda: self.volver_a_principal(self))
        volver_btn.grid(row=1, column=0, pady=10)