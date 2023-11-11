class RegistroNoEncontradoError(Exception):
    def __init__(self, mensaje="El registro no fue encontrado."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)