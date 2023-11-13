import tkinter as tk
from persistence.dtos.LibroDTO import LibroDTO
from tkinter import ttk, PhotoImage, messagebox
from config import png_aceptar, png_cancelar

class PantallaCamposLibro:
    campos = ["Titulo", "Precio"]
    estados = {
            "Disponible": 1,
            "Prestado": 2,
            "Extraviado": 3
            }
    def __init__(self, gestor, libro: tuple, operacion: str) -> None:
        self.ventana = tk.Toplevel()
        self.gestor = gestor
        self.ventana.configure(bg = "#4c061d")
        self.estilo = ttk.Style()
        self.estilo.theme_use('xpnative')
        self.setEstiloBotones()
        self.widgets = []
        self.entries = []
        self.permiso = operacion
        self.crearVentana()
        self.crearWidgets(libro)
        self.ventana.mainloop()

    def setEstiloBotones(self):
        self.estilo.configure("Botones.TButton", padding=10, width=10, foreground="black", bordercolor="black", borderwidth=5)
        self.estilo.map('Back', background=[('active','#B0B0B0')])

    def crearVentana(self):
        self.ventana.title("Libro")
        self.ventana.protocol("WM_DELETE_WINDOW", self.cancelar)
        self.ventana.resizable(False, False)

    def crearWidgets(self, libro: tuple = None):
        self.widgets.append(self.crearEntries(libro))
        self.widgets.append(self.crearBotonera())
        self.mostrarWidgets()

    def crearEntries(self, libro: tuple = None):
        self.entriesFrame = tk.Frame(self.ventana, background="#4c061d")
        for i in range(len(self.campos)):
            label = tk.Label(self.entriesFrame, text=self.campos[i], background="#4c061d", foreground="white")
            label.grid(row=i, column=0, padx=10, pady=10)
            campo = tk.Entry(self.entriesFrame)
            campo.insert(0, libro[i] if libro else "")
            campo.grid(row=i, column=1, padx=10, pady=10)
            self.entries.append(campo)
            if self.permiso == "R" or self.permiso == "D": campo.config(state=tk.DISABLED)
        self.crearCmbEstado(None if not libro else libro[2])
        validate_cmd = (self.ventana.register(self.validar_flotante), '%P')
        self.entries[1].config(validate='key', validatecommand=validate_cmd)
        
        return self.entriesFrame

    def crearBotonera(self):
        self.frameBotonera = tk.Frame(self.ventana, background="#4c061d")
        self.imgAceptar = PhotoImage(file=png_aceptar).subsample(25)
        self.imgCancelar = PhotoImage(file=png_cancelar).subsample(25)
        btnAceptar = ttk.Button(self.frameBotonera, text="Aceptar", command=self.aceptar, 
                                image=self.imgAceptar, compound="left", style="Back.TButton")
        btnCancelar = ttk.Button(self.frameBotonera, text="Cancelar", command=self.cancelar, 
                                 image=self.imgCancelar, compound="left", style="Back.TButton",
                                 state=tk.DISABLED if self.permiso == "R" else tk.NORMAL)
        btnAceptar.pack(side=tk.LEFT, padx=10)
        btnCancelar.pack(side=tk.LEFT, padx=10)
        return self.frameBotonera
        
    def crearBoton(self, nombre: str, comando: callable):
        boton = tk.Button(self.ventana, text=nombre, command=comando)
        return boton

    def crearCmbEstado(self, estado: str = None):
        lblEstado = tk.Label(self.entriesFrame, text="Estado", background="#4c061d", foreground="white")
        lblEstado.grid(row=len(self.campos), column=0, padx=10, pady=10)
        self.cmbEstado = ttk.Combobox(self.entriesFrame, values=list(self.estados.keys()))
        self.cmbEstado.set(list(self.estados.keys())[0])
        
        if estado is not None and estado in self.estados.keys(): self.cmbEstado.set(estado)
        else: self.cmbEstado.set(list(self.estados.keys())[0])
        self.cmbValue = self.estados[self.cmbEstado.get()]
            
        self.cmbEstado.grid(row=len(self.campos), column=1, padx=10, pady=10)
        self.cmbEstado.bind("<<ComboboxSelected>>", self.seleccionar_opcion)
        self.cmbEstado.config(state=tk.DISABLED) 
        # En todo caso se bloquea para evitar estado inconsistente en la BD: 
        # Ej. Libro prestado pero disponible en la pantalla o viceversa

    def mostrarWidgets(self):
        for widget in self.widgets: widget.pack()

    def seleccionar_opcion(self, event):
        seleccionado = self.cmbEstado.get()
        self.cmbValue = self.estados.get(seleccionado, "Valor no encontrado")
    
    def validarContenidoEntries(self):
        for entry in self.entries:
            if entry.get() == "": return False
        return True

    def validar_flotante(self, nuevo_valor):
            try:
                if nuevo_valor == "" or float(nuevo_valor):return True
                else: return False
            except ValueError: return False

    def getValues(self): return LibroDTO(0, self.entries[0].get(), self.entries[1].get(), self.cmbValue)

    def aceptar(self):
        if not self.validarContenidoEntries(): 
            messagebox.showerror("Error", "Debe completar todos los campos")
            return
        if self.permiso == "C": self.gestor.create(self.getValues())
        elif self.permiso == "U": self.gestor.update(self.getValues())
        elif self.permiso == "D": self.gestor.delete()
        self.cancelar()

    def cancelar(self):
        self.ventana.destroy()
        self.gestor.desbloquearPantalla()
