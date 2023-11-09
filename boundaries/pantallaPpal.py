from tkinter import ttk
from tkinter import PhotoImage
from config import png_reportes, png_extravios, png_libros, png_prestamos, png_socios, png_salir
from boundaries.pantallasSocio.PantallaSocio import PantallaSocio
from boundaries.Pantalla import Pantalla

class PantallaPrincipal(Pantalla):
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Biblioteca")
        
        # Crear un estilo para los botones
        self.estilo = ttk.Style()
        self.estilo.theme_use('xpnative')
        self.estilo.configure("Botones.TButton", font=("Helvetica", 14, "bold"), padding=10, width=20, foreground="black", bordercolor="black", borderwidth=5)
        self.create_btn_widgets()
        self.estilo.map('TButton', background=[('active','#B0B0B0')])

    def create_btn_imgs(self):
      self.img_socios = PhotoImage(file=png_socios).subsample(4)
      self.img_libros = PhotoImage(file=png_libros).subsample(4)
      self.img_prestamos = PhotoImage(file=png_prestamos).subsample(4)
      self.img_extraviados = PhotoImage(file=png_extravios).subsample(4)
      self.img_reportes = PhotoImage(file=png_reportes).subsample(4)
      self.img_salir = PhotoImage(file=png_salir).subsample(4)
        
    def create_btn_widgets(self):
      self.create_btn_imgs()
      self._buttons = []
      self._buttons.append(ttk.Button(self.ventana, text="Socios", style="Botones.TButton", image=self.img_socios, compound="top", command=self.socios))
      self._buttons.append(ttk.Button(self.ventana, text="Libros", style="Botones.TButton", image=self.img_libros, compound="top", command=self.libros))
      self._buttons.append(ttk.Button(self.ventana, text="Préstamos", style="Botones.TButton", image=self.img_prestamos, compound="top", command=self.prestamos))
      self._buttons.append(ttk.Button(self.ventana, text="Extravios", style="Botones.TButton", image=self.img_extraviados, compound="top", command=self.extravios))
      self._buttons.append(ttk.Button(self.ventana, text="Reportes", style="Botones.TButton", image=self.img_reportes, compound="top", command=self.reportes))
      self._buttons.append(ttk.Button(self.ventana, text="Salir", style="Botones.TButton", image=self.img_salir, compound="top", command=self.salir))
      self.posicionar_btn_widgets()
        
    def posicionar_btn_widgets(self):
      for i in range(0, len(self._buttons), 3):
        for j in range(3): self._buttons[i+j].grid(row=i, column=j, padx=20, pady=10)
    
    def socios(self):
        self.ocultarWidgets()
        self.pantalla_socio = PantallaSocio(self.ventana, self.volver_a_principal)

    def volver_a_principal(self, pantalla):
        pantalla.destruir()
        self.create_btn_widgets()
        self.posicionar_btn_widgets()

    def libros(self): 
      self.ocultarWidgets()

    def prestamos(self):
      self.ocultarWidgets()

    def extravios(self): 
      self.ocultarWidgets()

    def reportes(self):
      self.ocultarWidgets()
      
    def salir(self): self.ventana.destroy()