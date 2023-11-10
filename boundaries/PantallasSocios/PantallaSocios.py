from boundaries.PantallaSecundaria import PantallaSecundaria
from tkinter import Frame, Label, Entry, Scrollbar
from tkinter import ttk
from tkinter import StringVar, PhotoImage
from tkinter import messagebox
from tkinter import LEFT, RIGHT, TOP, X, Y, BOTH, CENTER
from tkinter.ttk import Treeview
from config import png_search, png_refresh

class PantallaSocios(PantallaSecundaria):
    def __init__(self, gestor, backToMain):
        super().__init__(backToMain)
        self.gestor = gestor
        self.ventana.title("Socios")
        self.socios = []  # Lista para almacenar los socios cargados
        self.createWidgets()

    def createWidgets(self):
      super().createWidgets()
      self.widgets.append(self.createBarraBusqueda())
      self.widgets.append(self.createLblSociosRegistrados())
      self.widgets.append(self.createGrillaSocios())

    def validateInput(self, *args):
      entrada_actual = self.varBusqueda.get()
      if entrada_actual.isdigit(): return True
      self.varBusqueda.set(self.varBusqueda.get()[:-1])
      return False
      
    def search(self):
      id = self.varBusqueda.get() if self.varBusqueda.get() != "" else -1
      self.gestor.search(id)
      
    def refresh(self):
      self.varBusqueda.set("")
      self.gestor.search(-1)
    
    def setSocios(self, socios):
      self.socios = socios
      self.loadTable()
    
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
        
        return self.frameBusqueda

    def createLblSociosRegistrados(self):
        lblSociosRegistrados = Label(self.ventana, text="Socios Registrados", font=("Helvetica", 16, "bold"), bg="#4c061d", fg="white")
        lblSociosRegistrados.grid(row=2, column=0, pady=10)
        return lblSociosRegistrados

    def createGrillaSocios(self):
        self.frame_grilla = Frame(self.ventana, bg="#4c061d")
        self.frame_grilla.grid(row=3, column=0, padx=10, pady=(0, 10), sticky='nsew')
        columns = ("ID", "Nombre", "Apellido", "Teléfono", "Email")
        self.treeview = Treeview(self.frame_grilla, columns=columns, show="headings", selectmode="browse")

        column_widths = {"ID": 50, "Nombre": 150, "Apellido": 150, "Teléfono": 150, "Email": 250}

        for col in columns:
            self.treeview.heading(col, text=col)
            width = column_widths.get(col, 100)
            self.treeview.column(col, width=width, anchor=CENTER)

        scrollbar = Scrollbar(self.frame_grilla, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.treeview.config(yscrollcommand=scrollbar.set)
        self.treeview.pack(fill=BOTH, expand=True)

        self.treeview.bind("<ButtonRelease-1>", self.seleccionar_fila)
        return self.frame_grilla

    def create_botones_accion(self):
        frame_botones = Frame(self.ventana, bg="#4c061d")
        frame_botones.grid(row=3, column=1, pady=(0, 10))

        btn_crear = ttk.Button(frame_botones, text="Crear", command=self.crear_socio, style="Botones.TButton")
        btn_modificar = ttk.Button(frame_botones, text="Modificar", command=self.modificar_socio, style="Botones.TButton")
        btn_consultar = ttk.Button(frame_botones, text="Consultar", command=self.consultar_socio, style="Botones.TButton")
        btn_borrar = ttk.Button(frame_botones, text="Borrar", command=self.borrar_socio, style="Botones.TButton")

        btn_crear.pack(side=LEFT, padx=5)
        btn_modificar.pack(side=LEFT, padx=5)
        btn_consultar.pack(side=LEFT, padx=5)
        btn_borrar.pack(side=LEFT, padx=5)

    def loadTable(self):
        self.treeview.delete(*self.treeview.get_children())  # Limpiar la grilla
        for socio in self.socios:
            self.treeview.insert("", "end", 
                                 values=(socio.id, socio.nombre, socio.apellido, socio.telefono, socio.email))

    def seleccionar_fila(self, event):
        seleccion = self.treeview.selection()
        if seleccion:
            pass

    def crear_socio(self):
        pass

    def modificar_socio(self):
        pass

    def consultar_socio(self):
        pass

    def borrar_socio(self):
        pass