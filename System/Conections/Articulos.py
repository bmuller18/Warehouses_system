import tkinter as tk



# Función para hacer clic en el botón de Articulos
def hacer_clic_articulos():
    ventana = tk.Tk()
    ventana.geometry("800x600")
    ventana.title("Articulos")

    mensaje_label = tk.Label(ventana, text="¡Se hizo clic en Articulos!", bg="#73708E")
    mensaje_label.pack()

    ventana.mainloop()


class Articulo:
    def __init__(self, id, nombre, descripcion, cantidad):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad

