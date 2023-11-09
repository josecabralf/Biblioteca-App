from boundaries.PantallaSecundaria import PantallaSecundaria

class PantallaLibros(PantallaSecundaria):
    def __init__(self, volver_a_principal):
      super().__init__(volver_a_principal)
      self.ventana.title("Libros")