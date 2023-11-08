import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from config import png_reportes, png_extravios, png_libros, png_prestamos, png_socios, png_salir

class PantallaPrincipal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Biblioteca")
        
        # Crear un estilo para los botones
        self.estilo = ttk.Style()
        self.estilo.configure("Botones.TButton", font=("Helvetica", 14, "bold"), padding=10, width=20, background="#1f271b", foreground="black")
        
        self.create_btn_imgs()
        self.create_btn_widgets()
        self.posicionar_btn_widgets()

    def create_btn_imgs(self):
      self.img_socios = PhotoImage(file=png_socios).subsample(4)
      self.img_libros = PhotoImage(file=png_libros).subsample(4)
      self.img_prestamos = PhotoImage(file=png_prestamos).subsample(4)
      self.img_extraviados = PhotoImage(file=png_extravios).subsample(4)
      self.img_reportes = PhotoImage(file=png_reportes).subsample(4)
      self.img_salir = PhotoImage(file=png_salir).subsample(4)
        
    def create_btn_widgets(self):
      self.btn_admin_socios = ttk.Button(self.ventana, text="Socios", style="Botones.TButton", image=self.img_socios, compound="top", command=self.admin_socios)
      self.btn_admin_libros = ttk.Button(self.ventana, text="Libros", style="Botones.TButton", image=self.img_libros, compound="top", command=self.admin_libros)
      self.btn_registrar_prestamos = ttk.Button(self.ventana, text="Préstamos", style="Botones.TButton", image=self.img_prestamos, compound="top", command=self.registrar_prestamos_devoluciones)
      self.btn_registrar_extraviados = ttk.Button(self.ventana, text="Extraviados", style="Botones.TButton", image=self.img_extraviados, compound="top", command=self.registrar_libros_extraviados)
      self.btn_generar_reportes = ttk.Button(self.ventana, text="Reportes", style="Botones.TButton", image=self.img_reportes, compound="top", command=self.generar_reportes)
      self.btn_salir = ttk.Button(self.ventana, text="Salir", style="Botones.TButton", image=self.img_salir, compound="top", command=self.salir)
        
    def posicionar_btn_widgets(self):
      self.btn_admin_socios.grid(row=0, column=0, padx=20, pady=10)
      self.btn_admin_libros.grid(row=0, column=1, padx=20, pady=10)
      self.btn_registrar_prestamos.grid(row=1, column=0, padx=20, pady=10)
      self.btn_registrar_extraviados.grid(row=1, column=1, padx=20, pady=10)
      self.btn_generar_reportes.grid(row=2, column=0, padx=20, pady=10)
      self.btn_salir.grid(row=2, column=1, padx=20, pady=10)  
    
    def admin_socios(self):
        # Lógica para la administración de socios
        pass

    def admin_libros(self):
        # Lógica para la administración de libros
        pass

    def registrar_prestamos_devoluciones(self):
        # Lógica para la registración de préstamos y devoluciones
        pass

    def registrar_libros_extraviados(self):
        # Lógica para la registración de libros extraviados
        pass

    def generar_reportes(self):
        # Lógica para generar reportes
        pass
      
    def salir(self):
        # Lógica para salir
        pass
