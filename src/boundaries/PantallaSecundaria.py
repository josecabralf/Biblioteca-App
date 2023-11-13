from boundaries.Pantalla import Pantalla
from tkinter import ttk, Frame
from tkinter import PhotoImage
from config import png_return

class PantallaSecundaria(Pantalla):
    def __init__(self, gestor, volver_a_principal):
      super().__init__()
      self.gestor = gestor
      self.volver_a_principal = volver_a_principal
      self.widgets = []
      self.createWidgets()

    def createWidgets(self):
      self.widgets.append(self.createBtnVolver())
      
    def createBtnVolver(self):
      self.frameBtnVolver = Frame(self.ventana, bg="#4c061d")
      self.frameBtnVolver.grid(row=0, column=0, padx=10, pady=10, sticky='ew')
      
      estilo = ttk.Style()
      estilo.configure("Volver.TButton", width=10, background="#4c061d", foreground="white")
      self.img_volver = PhotoImage(file=png_return).subsample(40)
      volver_btn = ttk.Button(self.frameBtnVolver, image= self.img_volver, style="Volver.TButton",
                              compound= "center", command=self.gestor.volver)
      volver_btn.grid(row=0, column=0)
      return self.frameBtnVolver
    
    def getGestor(self): return self.gestor
    
    def volver(self): self.volver_a_principal()