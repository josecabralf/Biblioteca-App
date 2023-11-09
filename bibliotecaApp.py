from boundaries.PantallaPrincipal import PantallaPrincipal
import tkinter as tk

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.configure(bg = "#4c061d")
    app = PantallaPrincipal(ventana=ventana)
    ventana.mainloop()