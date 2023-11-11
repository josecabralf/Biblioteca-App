from tkinter import ttk
from tkinter import PhotoImage

from config import png_reportes, png_extravios, png_libros, png_prestamos, png_socios, png_salir

from use_cases.admin_socios.SociosController import SociosController
from boundaries.PantallasLibros.PantallaLibros import PantallaLibros
from boundaries.PantallasPrestamos.PantallaPrestamos import PantallaPrestamos
from boundaries.PantallasExtravios.PantallaExtravios import PantallaExtravios
from boundaries.PantallasReportes.PantallaReportes import PantallaReportes
from boundaries.Pantalla import Pantalla

class PantallaPrincipal(Pantalla):
    def __init__(self):
        super().__init__()
        self.ventana.title("Sistema de Biblioteca")
        self.createWidgets()
        self.setGrid()
        self.ventana.mainloop()

    def setGrid(self):
        for i in range(3): self.ventana.grid_columnconfigure(i, weight=1)
        for i in range(2): self.ventana.grid_rowconfigure(i, weight=1)
    
    def createWidgets(self):
        self.widgets = []
        self.widgets.append(self.createBtnSocios())
        self.widgets.append(self.createBtnLibros())
        self.widgets.append(self.createBtnPrestamos())
        self.widgets.append(self.createBtnExtravios())
        self.widgets.append(self.createBtnReportes())
        self.widgets.append(self.createBtnSalir())
        self.mostrarWidgets()

    def mostrarWidgets(self):
        for i in range(0, len(self.widgets), 3):
            for j in range(3):
                self.widgets[i + j].grid(row=i // 3, column=j, padx=20, pady=10, sticky="nsew")

    def ocultarWidgets(self):
        [widget.grid_forget() for widget in self.widgets]

    def backToMain(self):
        self.ventana.title("Sistema de Biblioteca")
        self.mostrarWidgets()

    def socios(self):
        self.ocultarWidgets()
        SociosController(self.backToMain)

    def libros(self):
        self.ocultarWidgets()
        self.pantallaLibro = PantallaLibros(self.backToMain)

    def prestamos(self):
        self.ocultarWidgets()
        self.pantallaPrestamo = PantallaPrestamos(self.backToMain)

    def extravios(self):
        self.ocultarWidgets()
        self.pantallaPrestamo = PantallaExtravios(self.backToMain)

    def reportes(self):
        self.ocultarWidgets()
        self.pantallaPrestamo = PantallaReportes(self.backToMain)

    def salir(self):
        self.ventana.destroy()

    # CREACION DE WIDGETS
    def createBtnSocios(self):
        self.img_socios = PhotoImage(file=png_socios).subsample(4)
        return ttk.Button(
            self.ventana,
            text="Socios",
            style="Botones.TButton",
            image=self.img_socios,
            compound="top",
            command=self.socios
        )

    def createBtnLibros(self):
        self.img_libros = PhotoImage(file=png_libros).subsample(4)
        return ttk.Button(
            self.ventana,
            text="Libros",
            style="Botones.TButton",
            image=self.img_libros,
            compound="top",
            command=self.libros
        )

    def createBtnPrestamos(self):
        self.img_prestamos = PhotoImage(file=png_prestamos).subsample(4)
        return ttk.Button(
            self.ventana,
            text="Préstamos",
            style="Botones.TButton",
            image=self.img_prestamos,
            compound="top",
            command=self.prestamos
        )

    def createBtnExtravios(self):
        self.img_extraviados = PhotoImage(file=png_extravios).subsample(4)
        return ttk.Button(
            self.ventana,
            text="Extravios",
            style="Botones.TButton",
            image=self.img_extraviados,
            compound="top",
            command=self.extravios
        )

    def createBtnReportes(self):
        self.img_reportes = PhotoImage(file=png_reportes).subsample(4)
        return ttk.Button(
            self.ventana,
            text="Reportes",
            style="Botones.TButton",
            image=self.img_reportes,
            compound="top",
            command=self.reportes
        )

    def createBtnSalir(self):
        self.img_salir = PhotoImage(file=png_salir).subsample(4)
        return ttk.Button(
            self.ventana,
            text="Salir",
            style="Botones.TButton",
            image=self.img_salir,
            compound="top",
            command=self.salir
        )
