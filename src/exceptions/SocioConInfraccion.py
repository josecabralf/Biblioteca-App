class PrestamoConDemora(Exception):
    def __init__(self, mensaje = "El socio tiene un prestamo con demora."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
        

class MasDeTresPrestamos(Exception):
    def __init__(self, mensaje = "El socio tiene mas de tres prestamos."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)