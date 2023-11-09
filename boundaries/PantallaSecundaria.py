from boundaries.Pantalla import Pantalla
from tkinter import ttk
from tkinter import PhotoImage
from config import png_return

class PantallaSecundaria(Pantalla):
    def __init__(self, volver_a_principal):
      super().__init__()
      self.volver_a_principal = volver_a_principal
      self.widgets = []
      self.createWidgets()

    def createWidgets(self):
      self.widgets.append(self.createBtnVolver())
      
    def createBtnVolver(self):
      self.img_volver = PhotoImage(file=png_return).subsample(40)
      volver_btn = ttk.Button(self.ventana, image= self.img_volver,
                              compound= "center", command=lambda: self.volver_a_principal(self))
      volver_btn.grid(row=1, column=0)
      return volver_btn