from entities.fabricacionPura.Singleton import Singleton

class Pantalla(Singleton):
  def ocultarWidgets(self):
    for widget in self.ventana.winfo_children(): widget.grid_forget()
    
  def destruir(self):
    for widget in self.ventana.winfo_children(): widget.destroy()