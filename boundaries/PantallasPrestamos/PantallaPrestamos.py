from boundaries.PantallaSecundaria import PantallaSecundaria
from tkinter import Frame, Label, Entry, Scrollbar, Checkbutton
from tkinter import ttk
from tkinter import StringVar, PhotoImage
from tkinter import messagebox
from tkinter import LEFT, RIGHT, X, Y, BOTH, CENTER
from tkinter.ttk import Treeview
from config import png_search, png_refresh, png_create, png_devolucion
from entities.fabricacionPura.Observer import IObserver

class PantallaPrestamos(PantallaSecundaria, IObserver):
    def __init__(self, gestor, volver_a_principal):
      super().__init__(gestor, volver_a_principal)
      self.ventana.title("Prestamos")
      self.vigentes = False
      self.prestamos = []
      self.fila_seleccionada = None
      self.createWidgets()
      
    def createWidgets(self):
      super().createWidgets()
      self.widgets.append(self.createBarraBusqueda())
      self.widgets.append(self.createLblPrestamosRegistrados())
      self.widgets.append(self.createGrillaPrestamos())
      self.widgets.append(self.createBotonesAccion())
    
    def bloquear(self):
        for c in self.frameBotones.winfo_children(): c.config(state="disabled")
        for c in self.frameBtnVolver.winfo_children(): c.config(state="disabled")
        
    def desbloquear(self):
        for c in self.frameBotones.winfo_children(): c.config(state="normal")
        for c in self.frameBtnVolver.winfo_children(): c.config(state="normal")
    
    def create(self): self.gestor.openPrestamoWindow()
    
    def devolver(self):
      if self.validarFilaSeleccionada():
            self.gestor.openDevolucionWindow(self.fila_seleccionada)
    
    def validarFilaSeleccionada(self):
        if self.fila_seleccionada == None:
            messagebox.showwarning("Advertencia", "Debe seleccionar un prestamo")
            return False
        if self.fila_seleccionada[-1] != "":
            messagebox.showwarning("Advertencia", "El prestamo ya fue devuelto")
            return False
        return True
    
    def setPrestamos(self, prestamos):
      self.prestamos = prestamos
      self.loadTable()
      
    def loadTable(self):
      self.treeview.delete(*self.treeview.get_children())  # Limpiar la grilla
      for prestamo in self.prestamos:
          self.treeview.insert("", "end", values=prestamo)
    
    def marcarVigentes(self): 
      self.vigentes = not self.vigentes
      self.search()
      
    def validateInput(self, *args):
      entrada_actual = self.varBusqueda.get()
      if entrada_actual.isdigit(): return True
      self.varBusqueda.set(self.varBusqueda.get()[:-1])
      return False
    
    def refresh(self):
      self.varBusqueda.set("")
      self.vigentes = False
      self.checkBoxVigentes.deselect()
      self.gestor.search(-1, self.vigentes)
    
    def search(self):
        id = self.varBusqueda.get() if self.varBusqueda.get() != "" else -1
        self.gestor.search(id, self.vigentes)
      
    def getRowValues(self, event):
      seleccion = self.treeview.selection()
      if seleccion: self.fila_seleccionada = self.treeview.item(seleccion[0], "values")      
        
    def createLblPrestamosRegistrados(self):
      lblPrestamosRegistrados = Label(self.ventana, text="Prestamos Registrados", font=("Helvetica", 16, "bold"), bg="#4c061d", fg="white")
      lblPrestamosRegistrados.grid(row=2, column=0, pady=10)
      return lblPrestamosRegistrados
      
    def createBarraBusqueda(self):
      self.frameBusqueda = Frame(self.ventana, bg="#4c061d")
      self.frameBusqueda.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
      
      lblBuscar = Label(self.frameBusqueda, text="Buscar por ID:", font=("Helvetica", 12), bg="#4c061d", fg="white")
      lblBuscar.pack(side=LEFT, padx=5)
      
      frameBarraBoton = Frame(self.frameBusqueda, bg="#4c061d")
      frameBarraBoton.pack(side=LEFT, fill=X, expand=True)
      
      self.varBusqueda = StringVar()
      self.varBusqueda.trace_add("write", self.validateInput)
      entryBusqueda = Entry(frameBarraBoton, textvariable=self.varBusqueda, font=("Helvetica", 12))
      entryBusqueda.pack(side=LEFT, fill=X, expand=True)
      
      estilo_nuevo = ttk.Style()
      estilo_nuevo.configure("Busqueda.TButton", width=10)
      
      self.imgSearch = PhotoImage(file=png_search).subsample(30)
      btnBuscar = ttk.Button(frameBarraBoton, command=self.search, image=self.imgSearch, compound="left", style="Busqueda.TButton")
      btnBuscar.pack(side=LEFT, padx=5)
      
      self.imgRefresh = PhotoImage(file=png_refresh).subsample(120)
      btnBuscar = ttk.Button(frameBarraBoton, command=self.refresh, image=self.imgRefresh, compound="left", style="Busqueda.TButton")
      btnBuscar.pack(side=LEFT, padx=5)
      
      frameVigentes = Frame(self.frameBusqueda, bg="#4c061d")
      lblVigentes = Label(frameVigentes, text="Vigentes:", font=("Helvetica", 12), bg="#4c061d", fg="white")
      lblVigentes.pack(side=LEFT, padx=5)
      self.checkBoxVigentes = Checkbutton(frameVigentes, command=self.marcarVigentes, background="#4c061d", activebackground="#4c061d")
      self.checkBoxVigentes.pack(side=LEFT, padx=5)
      frameVigentes.pack(side=LEFT, padx=5)
      
      return self.frameBusqueda
    
    def createGrillaPrestamos(self):
      self.frame_grilla = Frame(self.ventana, bg="#4c061d")
      self.frame_grilla.grid(row=3, column=0, padx=10, pady=(0, 10), sticky='nsew')
      columns = ("ID", "Libro", "Socio", "Fecha Inicio", "Días", "Fecha Fin")
      self.treeview = Treeview(self.frame_grilla, columns=columns, show="headings", selectmode="browse")

      column_widths = {"ID": 50, "Libro": 300, "Socio": 300, 
                       "Fecha Inicio": 150, "Días": 50, "Fecha Fin": 150}

      for col in columns:
          self.treeview.heading(col, text=col)
          width = column_widths.get(col, 100)
          self.treeview.column(col, width=width, anchor=CENTER)

      scrollbar = Scrollbar(self.frame_grilla, orient="vertical", command=self.treeview.yview)
      scrollbar.pack(side=RIGHT, fill=Y)
      self.treeview.config(yscrollcommand=scrollbar.set)
      self.treeview.pack(fill=BOTH, expand=True)
      self.treeview.bind("<ButtonRelease-1>", self.getRowValues)
      return self.frame_grilla

    def createBotonesAccion(self):
      self.frameBotones = Frame(self.ventana, bg="#4c061d")
      self.frameBotones.grid(row=4, column=0, pady=(0, 10))
      
      self.imgCreate = PhotoImage(file=png_create).subsample(15)
      self.imgUpdate = PhotoImage(file=png_devolucion).subsample(15)
      
      btnCrear = ttk.Button(self.frameBotones, text="Nuevo Prestamo", command=self.create, 
                            style="Botones.TButton", image=self.imgCreate, compound="left")
      btnDevolver = ttk.Button(self.frameBotones, text="Devolución", command=self.devolver, 
                                style="Botones.TButton", image=self.imgUpdate, compound="left")

      btnCrear.pack(side=LEFT, padx=5)
      btnDevolver.pack(side=LEFT, padx=5)
      return self.frameBotones