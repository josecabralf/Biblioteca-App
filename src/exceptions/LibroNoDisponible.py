class LibroNoDisponible(Exception):
    def __init__(self, mensaje = "El libro no esta disponible."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)