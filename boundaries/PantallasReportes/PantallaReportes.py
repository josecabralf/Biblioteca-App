from boundaries.PantallaSecundaria import PantallaSecundaria
from tkinter import Frame, Label, PhotoImage, ttk
from config import png_demorado, png_restock, png_solicitantes, png_solicitudes, png_state

class PantallaReportes(PantallaSecundaria):
    def __init__(self, gestor, volver_a_principal):
      super().__init__(gestor, volver_a_principal)
      self.ventana.title("Reportes")
      self.createWidgets()
      
    def createWidgets(self):
      super().createWidgets()
      self.widgets.append(self.createLblReportes())
      self.widgets.append(self.createBotonesAccion())
    
    def reportarLibrosEstado(self): self.gestor.reportarLibrosEstado()
      
    def reportarRestock(self): self.gestor.reportarRestock()
      
    def reportarSolicitantesLibro(self): self.gestor.reportarSolicitantesLibro()
      
    def reportarPrestamoSocio(self): self.gestor.reportarPrestamoSocio()
      
    def reportarDemorados(self): self.gestor.reportarDemorados()
    
    def createLblReportes(self):
      self.frameLblReportes = Frame(self.ventana)
      lblReportes = Label(self.frameLblReportes, text="Reportes")
      lblReportes.pack()
      return self.frameLblReportes
      
    def createBotonesAccion(self):
        self.frameBotones = Frame(self.ventana, bg="#4c061d")
        self.frameBotones.grid(row=1, column=0, columnspan=3, sticky="nsew", padx=20, pady=10)
        
        self.imgState = PhotoImage(file=png_state).subsample(15)
        self.imgRestock = PhotoImage(file=png_restock).subsample(15)
        self.imgSolicitantes = PhotoImage(file=png_solicitantes).subsample(5)
        self.imgSolicitudes = PhotoImage(file=png_solicitudes).subsample(15)
        self.imgDemorado = PhotoImage(file=png_demorado).subsample(15)
        
        btnState = ttk.Button(self.frameBotones, text="Libros por Estado", command=self.reportarLibrosEstado, 
                                  style="Botones.TButton", image=self.imgState, compound="left")
        btnRestock = ttk.Button(self.frameBotones, text="Reposicion Extraviados", 
                                command=self.reportarRestock, style="Botones.TButton", 
                                image=self.imgRestock, compound="left")
        btnSolicitantes = ttk.Button(self.frameBotones, text="Solicitantes por Libro", 
                                     command=self.reportarSolicitantesLibro, style="Botones.TButton", 
                                     image=self.imgSolicitantes, compound="left")
        btnSolicitudes = ttk.Button(self.frameBotones, text="Prestamos por Socio", command=self.reportarPrestamoSocio, 
                                  style="Botones.TButton", image=self.imgSolicitudes, compound="left")
        btnDemorado = ttk.Button(self.frameBotones, text="Prestamos Demorados", command=self.reportarDemorados, 
                              style="Botones.TButton", image=self.imgDemorado, compound="left")
        
        btnState.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        btnRestock.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        btnSolicitantes.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        btnSolicitudes.grid(row=3, column=0, padx=5, pady=5, sticky="nsew")
        btnDemorado.grid(row=4, column=0, padx=5, pady=5, sticky="nsew")
        
        self.frameBotones.columnconfigure(0, weight=1)
        for i in range(5): self.frameBotones.rowconfigure(i, weight=1)
        return self.frameBotones
      
    def bloquear(self):
        for c in self.frameBotones.winfo_children(): c.config(state="disabled")
        for c in self.frameBtnVolver.winfo_children(): c.config(state="disabled")
        
    def desbloquear(self):
        for c in self.frameBotones.winfo_children(): c.config(state="normal")
        for c in self.frameBtnVolver.winfo_children(): c.config(state="normal")