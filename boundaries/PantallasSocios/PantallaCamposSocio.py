import tkinter as tk
from entities.Socio import Socio

class PantallaCamposSocio:
    def __init__(self, socio: Socio, operacion: str) -> None:
        self.ventana = tk.Tk()
        self.widgets = []
        self.permiso = operacion
        self.crearVentana()
        self.crearWidgets(socio)
        self.ventana.mainloop()

    def crearVentana(self):
        self.ventana.title("Socio")
        self.ventana.geometry("500x500")
        self.ventana.resizable(False, False)

    def crearWidgets(self, socio: Socio = None):
        """Crea los widgets necesarios para ver todos los campos de un socio"""
        self.widgets.append(self.crearCampo("Nombre", socio.getNombre() if socio else None))
        self.widgets.append(self.crearCampo("Apellido", socio.getApellido() if socio else None))
        self.widgets.append(self.crearCampo("Email", socio.getEmail() if socio else None))
        self.widgets.append(self.crearCampo("Telefono", socio.getTelefono() if socio else None))
        self.widgets.append(self.crearBoton("Aceptar", self.aceptar))
        self.widgets.append(self.crearBoton("Cancelar", self.cancelar))
        self.mostrarWidgets()

    def crearCampo(self, nombre: str, valor: str = None):
        """Crea un campo de texto con un nombre y un valor"""
        frame = tk.Frame(self.ventana)
        label = tk.Label(frame, text=nombre)
        label.pack(side=tk.LEFT)
        campo = tk.Entry(frame)
        campo.insert(0, valor if valor else "")
        campo.pack(side=tk.RIGHT)
        if self.permiso == "C": campo.config(state=tk.DISABLED)
        frame.pack()
        return campo

    def crearBoton(self, nombre: str, comando: callable):
        """Crea un boton con un nombre y un comando"""
        boton = tk.Button(self.ventana, text=nombre, command=comando)
        return boton

    def mostrarWidgets(self):
        """Muestra todos los widgets creados"""
        for widget in self.widgets:
            widget.pack()

    def ocultarWidgets(self):
        """Oculta todos los widgets creados"""
        for widget in self.widgets:
            widget.pack_forget()

    def aceptar(self):
        """Acepta los cambios realizados"""
        pass

    def cancelar(self):
        """Cancela los cambios realizados"""
        self.ventana.destroy()
